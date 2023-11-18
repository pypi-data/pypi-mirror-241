
from logging import Logger
from logging import getLogger

from deprecated import deprecated

from pyutmodel.PyutLink import PyutLink


class PyutSDMessage(PyutLink):
    """
    A message between two lifeline of two SDInstances.
    Note : Use getSrcY, getDstY

    """

    # def __init__(self, message="", src=None, srcTime=0, dst=None, dstTime=0, oglObject=None):
    def __init__(self, message="", src=None, srcTime=0, dst=None, dstTime=0):

        """
        TODO:  add timescale zoomer ?! and offset ?
        Args:
            message: for the message
            src:     source of the link
            srcTime: time on the source
            dst:     where the link goes
            dstTime: time on the destination
        """
        self.logger: Logger = getLogger(__name__)

        self.logger.debug(f"PyutSDMessage.__init__ {srcTime}, {dstTime}")
        super().__init__(source=src, destination=dst)
        self._message: str   = message
        self._srcTime: int   = srcTime
        self._dstTime: int   = dstTime
        #
        # TODO: Why oh why oh why?
        # self._oglObject = oglObject

    # def setOglObject(self, obj):
    #     """
    #     TODO: Fix this circular reference with Protocol:
    #     https://pythontest.com/fix-circular-import-python-typing-protocol/
    #     """
    #     self._oglObject = obj

    @property
    def message(self) -> str:
        """
        Returns: The message as a string
        """
        return self._message

    @message.setter
    def message(self, newValue: str):
        self._message = newValue

    @deprecated(reason='Use .message property')
    def getMessage(self):
        return self._message

    @property
    def sourceY(self) -> int:
        """
        Returns:  Y position on source
        """
        return self._srcTime

    @sourceY.setter
    def sourceY(self, newValue: int):
        """
        Returns:  Y position on source
        """
        self._srcTime = newValue

    @property
    def destinationY(self) -> int:
        """
        Returns: Y position on destination
        """
        return self._dstTime

    @destinationY.setter
    def destinationY(self, newValue: int):
        self._dstTime = newValue

    @property
    def sourceId(self) -> int:  # ignore it because the default is None
        return self._src.id     # type: ignore

    def destinationId(self) -> int:
        return self._dest.id      # type: ignore

    @deprecated(reason='Use .sourceY property')
    def getSrcY(self):
        return self._srcTime

    @deprecated(reason='Use .sourceY property')
    def setSrcY(self, newValue: int):
        self._srcTime = newValue

    @deprecated(reason='Use .destinationY property')
    def getDstY(self):
        return self._dstTime

    @deprecated(reason='Use .destinationY property')
    def setDstY(self, newValue: int):
        self._dstTime = newValue

    @deprecated(reason='Use .sourceY property')
    def getSrcTime(self):
        """
        Return time on source
        DON'T use it, or only for saving purpose
        @author C.Dutoit
        """
        return self._srcTime

    @deprecated(reason='Use .destinationY property')
    def getDstTime(self):
        """
        Return time on destination
        DON'T use it, or only for saving purpose
        @author C.Dutoit
        """
        return self._dstTime

    # @deprecated(reason='Use .sourceY property')
    # def setSrcTime(self, value, updateOGLObject=True):
    #     """
    #     Define time on source
    #     DON'T use it, or only for saving purpose
    #     @author C.Dutoit
    #     """
    #     self._srcTime = int(value)
    #     if updateOGLObject and self._oglObject is not None:
    #         self._oglObject.updatePositions()

    # @deprecated(reason='Use .destinationY property')
    # def setDstTime(self, value, updateOGLObject=True):
    #     """
    #     Define time on destination
    #     DON'T use it, or only for saving purpose
    #     @author C.Dutoit
    #     """
    #     self._dstTime = int(value)
    #     if updateOGLObject and self._oglObject is not None:
    #         self._oglObject.updatePositions()

    @deprecated(reason='Use .sourceId')
    def getSrcID(self):
        """
        TODO:  There is a problem;  Not sure this method is valid

        Returns:    Y position on source
        """
        return self._src.getId()        # type: ignore

    @deprecated(reason='Use .destinationId')
    def getDstID(self):
        """
        TODO:  There is a problem;  Not sure this method is valid

        Returns:    Y position on source
        """
        return self._dest.getId()       # type: ignore

    def getSource(self):
        """
        Return Y position on source
        @author C.Dutoit
        """
        return self._src

    def getDest(self):
        """
        Return Y position on source
        @author C.Dutoit
        """
        return self._dest

    @deprecated(reason='Use .message property')
    def setMessage(self, value):
        self._message = value

    def setSource(self, src=None, srcTime=-1):
        """
        Args:
            src:    Source object
            srcTime: ???
        """
        if src is not None:
            super().setSource(src)
        if srcTime != -1:
            self.logger.debug(f"PyutSDMessage - Setting srcTime to: {srcTime}")
            # self.setSrcTime(srcTime)
            self.sourceY = srcTime

    def setDestination(self, dst=None, dstTime=-1):
        """
        Define the destination

        Args:
            dst:        destination object
            dstTime:    Time on the destination
        """
        if dst is not None:
            PyutLink.setDestination(self, dst)
        if dstTime != -1:
            self.logger.debug(f"Setting dstTime to {dstTime}")
            # self.setDstTime(dstTime)
            self.destinationY = dstTime

    def __str__(self):
        """

        Returns:    string representing this object
        """
        # return _("(%s) link to %s") % (self._src, self._dest)
        return f'{self._src} linked to {self._dest}'
