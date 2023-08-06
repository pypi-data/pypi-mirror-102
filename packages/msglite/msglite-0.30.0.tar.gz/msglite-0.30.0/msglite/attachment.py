import logging

from msglite import constants
from msglite.properties import Properties
from msglite.utils import join_path

log = logging.getLogger(__name__)


class Attachment(object):
    """
    Stores the attachment data of a Message instance.
    Should the attachment be an embeded message, the
    class used to create it will be the same as the
    Message class used to create the attachment.
    """

    def __init__(self, msg, dir_):
        """
        :param msg: the Message instance that the attachment belongs to.
        :param dir_: the directory inside the msg file where the attachment is
            located.
        """
        self.msg = msg
        self.dir = dir_
        stream = self._getStream("__properties_version1.0")
        self.props = Properties(stream, constants.TYPE_ATTACHMENT)

        # Get display name
        self.title = self._getStringStream("__substg1.0_3001")

        # Get extension
        self.extension = self._getStringStream("__substg1.0_3703")

        # Get long filename
        self.long_filename = self._getStringStream("__substg1.0_3707")

        # Get short filename
        self.short_filename = self._getStringStream("__substg1.0_3704")

        # Get Content-ID
        self.cid = self._getStringStream("__substg1.0_3712")

        # Get MIME type
        self.content_type = self._getStringStream("__substg1.0_370E")

        # Get attachment data
        self.data = None

        # MS-OXPROPS 2.601, MS-OXCMSG 2.2.2.9:
        self.method = self.props.get("37050003")
        if self.method is not None:
            self.method = self.method.value & 0x7

        self.type = "data"
        # cf. MS-OXCMSG 2.2.2.9 PidTagAttachMethod Property
        # TODO Handling for special attachment types (like 7)
        if self.method == 0x5:
            prefix = join_path(msg.prefix, dir_, "__substg1.0_3701000D")
            self.type = "msg"
            self.data = msg.__class__(
                self.msg.path,
                prefix=prefix,
                ole=msg.ole,
                filename=self.get_filename(),
                encoding=self.msg.encoding,
            )
        else:
            self.data = self._getStream("__substg1.0_37010102")
            if self.data is None:
                path = join_path("__substg1.0_3701000D", "CONTENTS")
                self.data = self._getStream(path)

        if self.data is None:
            log.warning("Empty attachment: %r", self)
            self.type = None

    def _getStream(self, filename):
        return self.msg._getStream(join_path(self.dir, filename))

    def _getStringStream(self, filename):
        """Gets a string representation of the requested filename."""
        return self.msg._getStringStream(join_path(self.dir, filename))

    def exists(self, filename):
        """Checks if stream exists inside the attachment folder."""
        return self.msg.exists(join_path(self.dir, filename))

    def get_filename(self):
        # If filename is None at this point, use long filename as first
        # preference:
        if self.long_filename:
            return self.long_filename
        # Otherwise use the short filename
        if self.short_filename:
            return self.short_filename
        # Use the title
        if self.title:
            title = self.title
            if self.extension and not title.endswith(self.extension):
                title = title + self.extension
            return title
        # Otherwise just make something up!
        extension = ".bin" if self.extension is None else self.extension
        return "%s%s" % (self.dir, extension)

    def __repr__(self):
        return "<Attachment(%s, %s, %s)>" % (self.dir, self.method, self.get_filename())
