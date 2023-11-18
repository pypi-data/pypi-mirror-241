
from typing import List
from typing import NewType
from typing import Optional
from typing import Union
from typing import TYPE_CHECKING

from logging import Logger
from logging import getLogger

# noinspection PyPackageRequirements
from deprecated import deprecated

from pyutmodel.PyutObject import PyutObject
from pyutmodel.PyutLinkType import PyutLinkType

if TYPE_CHECKING:
    from pyutmodel.PyutClass import PyutClass
    from pyutmodel.PyutNote import PyutNote
    from pyutmodel.PyutLinkedObject import PyutLinkedObject



class PyutLink(PyutObject):
    """
    A standard link between a Class or Note.

    A PyutLink represents a UML link between a Class or a Note in Pyut.

    Example:
    ```python

        myLink  = PyutLink("linkName", OglLinkType.OGL_INHERITANCE, "0", "*")
    ```
    """

    # noinspection PyUnresolvedReferences
    def __init__(self, name="", linkType: PyutLinkType = PyutLinkType.INHERITANCE,
                 cardSrc:      str = "",
                 cardDest:     str = "",
                 bidir:        bool = False,
                 source:       Optional['PyutClass']                    = None,
                 destination:  Optional[Union['PyutClass', 'PyutNote']] = None):
        """

        Args:
            name:        The link name
            linkType:    The enum representing the link type
            cardSrc:     The source cardinality
            cardDest:    The destination cardinality
            bidir:      `True` if the link is bidirectional, else `False`
            source:      The source of the link
            destination: The destination of the link
        """
        super().__init__(name)
        self.logger: Logger       = getLogger(__name__)
        self._type:  PyutLinkType = linkType

        self._sourceCardinality:      str  = cardSrc
        self._destinationCardinality: str  = cardDest
        self._bidirectional:          bool = bidir

        self._src:  Optional['PyutLinkedObject'] = source
        self._dest: Optional['PyutLinkedObject'] = destination

    @property
    def sourceCardinality(self) -> str:
        """
        Return a string representing source's cardinality

        Returns: string source cardinality
        """
        return self._sourceCardinality

    @sourceCardinality.setter
    def sourceCardinality(self, cardSrc: str):
        """
        Update the source cardinality.

        Args:
            cardSrc:

        """
        self._sourceCardinality = cardSrc

    @property
    def destinationCardinality(self) -> str:
        """
        Return a string representing cardinality destination.

        Returns: string destination cardinality
        """
        return self._destinationCardinality

    @destinationCardinality.setter
    def destinationCardinality(self, cardDest: str):
        """
        Updating destination cardinality.

        Args:
            cardDest
        """
        self._destinationCardinality = cardDest

    def getSource(self):
        """
        Return the source object of the link

        Returns: object Class or Note
        """
        return self._src

    def setSource(self, source):
        """
        Set the source object of this link.
        Args:
            source  PyutClass or PyutNote
        """
        self._src = source

    def getDestination(self):
        """
        Return an object destination who is linked to this link.

        Returns: object PyutClass or PyutNote
        """
        return self._dest

    def setDestination(self, destination):
        """
        Update the link destination.

        Args:
             destination -- PyutClass or PyutNote
        """
        self._dest = destination

    def getBidir(self) -> bool:
        """
        Get the link is bidirectional value

        Returns: `True` if the link is bidirectional else `False`
        """
        return self._bidirectional

    def setBidir(self, bidirectional: bool):
        """
        Update the bidirectional value

        Args:
             bidirectional
        """
        self._bidirectional = bidirectional

    @deprecated(reason='Use linkType')
    def setType(self, linkType: PyutLinkType):
        """
        Update the link type

        Args:
              linkType : Type of the link
        """
        if isinstance(linkType, int):
            try:
                self._type = PyutLinkType(linkType)
            except (ValueError, Exception) as e:
                self.logger.info(f'setType: {e}')
                self._type = PyutLinkType.INHERITANCE
        else:
            self._type = linkType

    @deprecated(reason='Use linkType')
    def getType(self) -> PyutLinkType:
        """
        Get the link type.

        Returns:
            The type of the link
        """
        return self._type

    @property
    def linkType(self) -> PyutLinkType:
        return self._type

    @linkType.setter
    def linkType(self, theType: PyutLinkType):
        self._type = theType

    def __str__(self):
        """
        String representation.

        Returns:
             string representing link
        """
        return f'("{self.name}") links from {self._src} to {self._dest}'


PyutLinks      = NewType('PyutLinks', List[PyutLink])
