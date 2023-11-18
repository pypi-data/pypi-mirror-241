
from deprecated import deprecated

from logging import Logger
from logging import getLogger

from pyutmodel.PyutObject import PyutObject
from pyutmodel.PyutType import PyutType


class PyutParameter(PyutObject):
    """
    """

    DEFAULT_PARAMETER_NAME: str = 'param'

    def __init__(self, name: str = DEFAULT_PARAMETER_NAME, parameterType: PyutType = PyutType(""), defaultValue: str = ''):
        """

        Args:
            name: init name with the name
            parameterType: the param type

        """
        super().__init__(name)

        self.logger: Logger = getLogger(__name__)

        self._type:         PyutType = parameterType
        self._defaultValue: str      = defaultValue

    @deprecated(reason='Use the properties')
    def getType(self) -> PyutType:
        return self._type

    @deprecated(reason='Use the properties')
    def setType(self, theType: PyutType):
        """
        Set parameter type

        Args:
            theType:
        """
        if isinstance(theType, str):
            self.logger.warning(f'Setting return type as string is deprecated.  use PyutType')
            theType = PyutType(theType)

        self.logger.debug(f'theType: `{theType}`')
        self._type = theType

    @deprecated(reason='Use the properties')
    def getDefaultValue(self) -> str:
        return self._defaultValue

    @deprecated(reason='Use the properties')
    def setDefaultValue(self, defaultValue: str):
        self._defaultValue = defaultValue

    @property
    def type(self) -> PyutType:
        return self._type

    @type.setter
    def type(self, theType: PyutType):
        if isinstance(theType, str):
            self.logger.warning(f'Setting return type as string is deprecated.  use PyutType')
            theType = PyutType(theType)

        self.logger.debug(f'theType: `{theType}`')
        self._type = theType

    @property
    def defaultValue(self) -> str:
        return self._defaultValue

    @defaultValue.setter
    def defaultValue(self, newValue: str):
        self._defaultValue = newValue

    def __str__(self) -> str:
        """

        Returns:  String version of a PyutParm
        """
        s = self.name

        if str(self._type.value) != "":
            s = f'{s}: {self._type.value}'

        if self._defaultValue != '':
            s = f'{s} = {self._defaultValue}'

        return s

    def __repr__(self) -> str:
        return self.__str__()