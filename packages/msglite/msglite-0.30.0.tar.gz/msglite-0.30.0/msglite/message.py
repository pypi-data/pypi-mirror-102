import logging
from olefile import OleFileIO
from compressed_rtf import decompress
import email.utils
from email.policy import default
from email.parser import Parser as EmailParser

from msglite import constants
from msglite.attachment import Attachment
from msglite.properties import Properties
from msglite.recipient import Recipient
from msglite.encoding import get_encoding
from msglite.utils import format_party, guess_encoding, join_path

log = logging.getLogger(__name__)


class Message(object):
    """Parser for Microsoft Outlook message files."""

    def __init__(
        self,
        path,
        prefix="",
        ole=None,
        filename=None,
        encoding=None,
        lazy=False,
    ):
        """
        :param path: path to the msg file in the system or is the raw msg file.
        :param prefix: used for extracting embeded msg files
            inside the main one. Do not set manually unless
            you know what you are doing.
        :param filename: optional, the filename to be used by default when
            saving.
        :param: extract_attachments: extract data from attachments to message
        :param lazy: continue with extraction even if an attachment fails
        """
        self.path = path
        self.filename = filename
        if ole is None:
            ole = OleFileIO(path)
        self.ole = ole
        self.lazy = lazy

        # Parse the main props
        self.prefix = prefix
        prop_type = constants.TYPE_MESSAGE_EMBED
        if self.prefix == "":
            prop_type = constants.TYPE_MESSAGE
        propdata = self._getStream("__properties_version1.0")
        self.mainProperties = Properties(propdata, prop_type)

        # Determine if the message is unicode-style:
        # PidTagStoreSupportMask
        self.is_unicode = False
        if "340D0003" in self.mainProperties:
            value = self.mainProperties["340D0003"].value
            self.is_unicode = (value & 0x40000) != 0

        self.encoding = encoding
        # if "66C30003" in self.mainProperties:
        #     # PidTagCodePageId
        #     codepage = self.mainProperties["66C30003"].value
        #     self.encoding = get_encoding(codepage, self.encoding)

        if self.encoding is None:
            metadata = ole.get_metadata()
            self.encoding = get_encoding(metadata.codepage)

        if "3FFD0003" in self.mainProperties:
            # PidTagMessageCodepage
            codepage = self.mainProperties["3FFD0003"].value
            self.encoding = get_encoding(codepage, self.encoding)
        if self.encoding is None:
            self.encoding = self.guessEncoding()

        log.debug("Message encoding: %s", self.encoding)
        self.subject = self.getStringField("0037")
        self.date = self.mainProperties.date

    def close(self):
        self.ole.close()

    def guessEncoding(self):
        data = b""
        for field in self.ole.listdir():
            field = field[-1]
            if not field.endswith("001E"):
                continue
            raw = self._getStream(field)
            if raw is not None:
                data += b"\n" + raw
        return guess_encoding(data)

    def exists(self, inp):
        """Checks if :param inp: exists in the msg file."""
        return self.ole.exists(join_path(self.prefix, inp))

    def _getStream(self, filename):
        filename = join_path(self.prefix, filename)
        try:
            with self.ole.openstream(filename) as stream:
                return stream.read()
        except OSError:
            return None

    def _iterEncodings(self, data, type_, encoding):
        if type_ == "001F" and self.is_unicode:
            yield "utf-16-le"
        yield encoding
        if self.encoding != encoding:
            yield self.encoding
        yield guess_encoding(data)
        yield "utf-8"

    def _getStringStream(self, filename, encoding=None):
        """Gets a unicode representation of the requested filename."""
        for type_ in ("001F", "001E", "0102"):
            stream_name = filename + type_
            data = self._getStream(stream_name)
            if data is None:
                continue
            for cand in self._iterEncodings(data, type_, encoding):
                if cand is None:
                    continue
                try:
                    return data.decode(cand)
                except Exception:
                    msg = "Failed to decode %s (%s bytes, %s codec)"
                    log.debug(msg, stream_name, len(data), cand)

    def getStringField(self, name, encoding=None):
        return self._getStringStream("__substg1.0_%s" % name, encoding=encoding)

    def list_paths(self):
        """
        Replacement for OleFileIO.listdir that runs at the current
        prefix directory.
        """
        seen = set()
        for path in self.ole.listdir():
            path = "/".join(path)
            if not path.startswith(self.prefix):
                continue

            path = path[len(self.prefix) :]
            path = path.strip("/")
            path = path.split("/")[0]
            if path not in seen:
                seen.add(path)
                yield path

    @property
    def attachments(self):
        """ Returns a list of all attachments. """
        if not hasattr(self, "_attachments"):
            self._attachments = []
            for path in self.list_paths():
                if path.startswith("__attach"):
                    try:
                        self._attachments.append(Attachment(self, path))
                    except TypeError:
                        msg = "Could not parse attachment %s in %s" % (path, self.path)
                        log.exception(msg)
        return self._attachments

    @property
    def recipients(self):
        """ Returns a list of all recipients. """
        if not hasattr(self, "_recipients"):
            self._recipients = []
            for path in self.list_paths():
                if path.startswith("__recip"):
                    self._recipients.append(Recipient(self, path))
        return self._recipients

    def getRecipientsByType(self, type):
        recipients = []
        for x in self.recipients:
            if x.type & 0x0000000F == type:
                recipients.append(x.formatted)
        return recipients

    @property
    def header(self):
        """ Returns the message header. """
        if not hasattr(self, "_header"):
            headerText = self.getStringField("007D")
            headerText = headerText or ""
            parser = EmailParser(policy=default)
            self._header = parser.parsestr(headerText)
        return self._header

    def getHeader(self, name):
        try:
            return self.header.get_all(name)
        except (TypeError, IndexError, AttributeError, ValueError):
            log.exception("Cannot read header: %s", name)
            return None

    @property
    def parsedDate(self):
        return email.utils.parsedate(self.date)

    @property
    def senders(self):
        """Returns the message sender, if it exists."""
        headerResult = self.getHeader("from")
        if headerResult is not None:
            return headerResult
        senders = self.getRecipientsByType(constants.RECIPIENT_SENDER)
        if len(senders):
            return senders
        text = self.getStringField("0C1A")
        email = self.getStringField("5D01")
        if email is None:
            email = self.getStringField("0C1F")
        return [format_party(email, text)]

    @property
    def sender(self):
        for sender in self.senders:
            return sender

    @property
    def to(self):
        """Returns the 'To' field."""
        headerResult = self.getHeader("to")
        if headerResult is not None:
            return headerResult
        return self.getRecipientsByType(constants.RECIPIENT_TO)

    @property
    def cc(self):
        """Returns the 'CC' field."""
        headerResult = self.getHeader("cc")
        if headerResult is not None:
            return headerResult
        return self.getRecipientsByType(constants.RECIPIENT_CC)

    @property
    def bcc(self):
        """Returns the 'BCC' field."""
        headerResult = self.getHeader("bcc")
        if headerResult is not None:
            return headerResult
        return self.getRecipientsByType(constants.RECIPIENT_BCC)

    @property
    def bodyEncoding(self):
        """Special encoding for the raw or HTML bodies."""
        prop = self.mainProperties.get("3FDE0003")
        if prop is not None:
            # PidTagInternetCodepage
            return get_encoding(prop.value)

    @property
    def body(self):
        """Returns the message body."""
        # PidTagBody
        return self.getStringField("1000", encoding=self.bodyEncoding)

    @property
    def compressedRtf(self):
        """Returns the compressed RTF stream, if it exists."""
        return self._getStream("__substg1.0_10090102")

    @property
    def rtfBody(self):
        return decompress(self.compressedRtf)

    @property
    def htmlBody(self):
        """Returns the html body, if it exists."""
        # PidTagHtml
        return self.getStringField("1013", encoding=self.bodyEncoding)

    @property
    def message_id(self):
        message_id = self.getHeader("message-id")
        if message_id is not None:
            return message_id
        return self.getStringField("1035")

    @property
    def references(self):
        message_id = self.getHeader("references")
        if message_id is not None:
            return message_id
        return self.getStringField("1039")

    @property
    def reply_to(self):
        return self._getStringStream("__substg1.0_1042")

    def dump(self):
        """Prints out a summary of the message."""
        print("Message")
        print("Sender:", self.sender)
        print("To:", self.to)
        print("Cc:", self.cc)
        print("Bcc:", self.bcc)
        print("Message-Id:", self.message_id)
        print("References:", self.references)
        print("Subject:", self.subject)
        print("Encoding:", self.encoding)
        print("Date:", self.date)
        print("Body:")
        print(self.body)
        print("HTML:")
        print(self.htmlBody)
