from enum import Enum


class PyutStereotype(Enum):
    """
    Stereotype Enumeration
    https://www.ibm.com/docs/en/rational-soft-arch/9.5?topic=elements-uml-model-element-stereotypes
    """
    AUXILIARY            = 'auxiliary'
    BOUNDARY             = 'boundary'
    BUILD_COMPONENT      = 'buildComponent'
    CONTROL              = 'control'
    DOCUMENT             = 'document'
    ENTITY               = 'entity'
    EXECUTABLE           = 'executable'
    FILE                 = 'file'
    FOCUS                = 'focus'
    IMPLEMENT            = 'implement'
    IMPLEMENTATION_CLASS = 'implementationClass'
    INTERFACE            = 'interface'
    LIBRARY              = 'library'
    METACLASS            = 'metaclass'
    NODE_TYPE            = 'node type'
    POWER_TYPE           = 'powertype'
    REALIZATION          = 'realization'
    SCRIPT               = 'script'
    SERVICE              = 'service'
    SOURCE               = 'source'
    SPECIFICATION        = 'specification'
    SUBSYSTEM            = 'subsystem'
    THREAD               = 'thread'
    TYPE                 = 'type'
    UTILITY              = 'utility'
    NO_STEREOTYPE        = 'noStereotype'

    @classmethod
    def toEnum(cls, strValue: str) -> 'PyutStereotype':
        """
        Converts the input string to the appropriate stereotype

        Args:
            strValue:   A string value

        Returns:  The stereotype enumeration;  Empty strings, multi-spaces strings, & None
        values return PyutStereotype.NO_STEREOTYPE
        """
        stereotype:   PyutStereotype = PyutStereotype.NO_STEREOTYPE
        if strValue is None:
            canonicalStr: str = ''  # Force None
        else:
            canonicalStr = strValue.strip(' ')  # I want exact match

        match canonicalStr:
            case PyutStereotype.AUXILIARY.value:
                stereotype = PyutStereotype.AUXILIARY
            case PyutStereotype.FOCUS.value:
                stereotype = PyutStereotype.FOCUS
            case PyutStereotype.IMPLEMENTATION_CLASS.value:
                stereotype = PyutStereotype.IMPLEMENTATION_CLASS
            case PyutStereotype.METACLASS.value:
                stereotype = PyutStereotype.METACLASS
            case PyutStereotype.TYPE.value:
                stereotype = PyutStereotype.TYPE
            case PyutStereotype.UTILITY.value:
                stereotype = PyutStereotype.UTILITY
            case PyutStereotype.NO_STEREOTYPE.value:
                stereotype = PyutStereotype.NO_STEREOTYPE
            case '':
                pass    # No stereotype
            case _:
                print(f'Warning: did not recognize this  stereotype string: `{canonicalStr}`')

        return stereotype
