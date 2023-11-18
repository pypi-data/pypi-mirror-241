

from deprecated import deprecated

from pyutmodel.PyutClassCommon import PyutClassCommon
from pyutmodel.PyutDisplayParameters import PyutDisplayParameters
from pyutmodel.PyutInterface import PyutInterface
from pyutmodel.PyutInterface import PyutInterfaces
from pyutmodel.PyutLinkedObject import PyutLinkedObject
from pyutmodel.PyutStereotype import PyutStereotype


class PyutClass(PyutClassCommon, PyutLinkedObject):
    """
    A standard class representation.

    A PyutClass represents a UML class in Pyut. It manages its:
        - object data fields (`PyutField`)
        - methods (`PyutMethod`)
        - parents (`PyutClass`)(classes from which this one inherits)
        - stereotype (`PyutStereotype`)
        - a description (`string`)

    Example:
        myClass = PyutClass("Foo") # this will create a `Foo` class
        myClass.description = "Example class"

        fields = myClass.fields # this is the original fields []
        fields.append(PyutField("bar", "int"))

    """
    def __init__(self, name=""):
        """

        Args:
            name: class name
        """
        PyutLinkedObject.__init__(self, name)
        PyutClassCommon.__init__(self)

        self._stereotype: PyutStereotype = PyutStereotype.NO_STEREOTYPE

        # Display properties
        self._displayStereotype: bool                  = True
        self._displayParameters: PyutDisplayParameters = PyutDisplayParameters.UNSPECIFIED
        self._interfaces:        PyutInterfaces        = PyutInterfaces([])

    @property
    def displayParameters(self) -> PyutDisplayParameters:
        return self._displayParameters

    @displayParameters.setter
    def displayParameters(self, newValue: PyutDisplayParameters):
        self._displayParameters = newValue

    @property
    def interfaces(self) -> PyutInterfaces:
        return self._interfaces

    @interfaces.setter
    def interfaces(self, theNewInterfaces: PyutInterfaces):
        self._interfaces = theNewInterfaces

    def addInterface(self, pyutInterface: PyutInterface):
        self._interfaces.append(pyutInterface)

    @property
    def stereotype(self) -> PyutStereotype:
        """
        Return the stereotype associated with this class

        Returns:  None if there's no stereotype.
        """
        return self._stereotype

    @stereotype.setter
    def stereotype(self, newValue: PyutStereotype):
        self._stereotype = newValue

    @property
    def displayStereoType(self) -> bool:
        """
                Returns:   True if the UI should display the stereotype
        """
        return self._displayStereotype

    @displayStereoType.setter
    def displayStereoType(self, newValue: bool):
        """
        Indicate whether the UI should display the stereotype
        Args:
            newValue:  'True' do display on the UI, else 'False'
        """
        self._displayStereotype = newValue

    @deprecated(version='1.0.3', reason='Use properties they are better')
    def getStereotype(self):
        """
        Return the stereotype used, or None if there's no stereotype.
        """
        return self._stereotype

    @deprecated(version='1.0.3', reason='Use properties they are better')
    def setStereotype(self, stereotype):
        """
        Replace the actual stereotype by the one given.

        """
        # Python 3 update
        # if type(stereotype) == StringType or type(stereotype) == UnicodeType:
        if type(stereotype) is str:
            stereotype = PyutStereotype(stereotype)
        self._stereotype = stereotype

    @deprecated(version='1.0.3', reason='Use displayStereoType property it is better')
    def getShowStereotype(self):
        """
        Return True if we must display the stereotype

        @return boolean indicating if we must display the stereotype
        """
        return self._displayStereotype

    @deprecated(version='1.0.3', reason='Use displayStereoType property it is better')
    def setShowStereotype(self, theNewValue: bool):
        """
        Define the showStereotype property

        @param theNewValue : boolean indicating if we must display the stereotype

        """
        self._displayStereotype = theNewValue

    def __getstate__(self):
        """
        For deepcopy operations, specifies which fields to avoid copying.
        Deepcopy must not copy the links to other classes, or it would result
        in copying the entire diagram.
        """
        aDict = self.__dict__.copy()
        aDict["_parents"]    = []
        return aDict

    def __str__(self):
        """
        String representation.
        """
        return f"Class : {self.name}"

    def __repr__(self):
        return self.__str__()
