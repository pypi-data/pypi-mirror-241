import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def BoolProperty(
        name: typing.Optional[str] = "",
        description: typing.Optional[str] = "",
        default=False,
        options: typing.Optional[typing.Set] = {'ANIMATABLE'},
        tags: typing.Optional[typing.Set] = {},
        subtype: typing.Optional[str] = 'NONE',
        update: typing.Optional[typing.Any] = None,
        get: typing.Optional[typing.Any] = None,
        set: typing.Optional[typing.Any] = None) -> 'bpy.types.BoolProperty':
    ''' Returns a new boolean property definition.

    :param name: Name used in the user interface.
    :type name: typing.Optional[str]
    :param description: Text used for the tooltip and api documentation.
    :type description: typing.Optional[str]
    :param options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
    :type options: typing.Optional[typing.Set]
    :param tags: Enumerator of tags that are defined by parent class.
    :type tags: typing.Optional[typing.Set]
    :param subtype: Enumerator in ['PIXEL', 'UNSIGNED', 'PERCENTAGE', 'FACTOR', 'ANGLE', 'TIME', 'DISTANCE', 'NONE'].
    :type subtype: typing.Optional[str]
    :param update: Function to be called when this value is modified, This function must take 2 values (self, context) and return None. *Warning* there are no safety checks to avoid infinite recursion.
    :type update: typing.Optional[typing.Any]
    :param get: Function to be called when this value is 'read', This function must take 1 value (self) and return the value of the property.
    :type get: typing.Optional[typing.Any]
    :param set: Function to be called when this value is 'written', This function must take 2 values (self, value) and return None.
    :type set: typing.Optional[typing.Any]
    :rtype: 'bpy.types.BoolProperty'
    '''

    pass


def BoolVectorProperty(
        name: typing.Optional[str] = "",
        description: typing.Optional[str] = "",
        default: typing.Optional[typing.Sequence] = (False, False, False),
        options: typing.Optional[typing.Set] = {'ANIMATABLE'},
        tags: typing.Optional[typing.Set] = {},
        subtype: typing.Optional[str] = 'NONE',
        size: typing.Optional[int] = 3,
        update: typing.Optional[typing.Any] = None,
        get: typing.Optional[typing.Any] = None,
        set: typing.Optional[typing.Any] = None
) -> typing.Union[typing.List, 'bpy.types.BoolProperty']:
    ''' Returns a new vector boolean property definition.

    :param name: Name used in the user interface.
    :type name: typing.Optional[str]
    :param description: Text used for the tooltip and api documentation.
    :type description: typing.Optional[str]
    :param default: sequence of booleans the length of *size*.
    :type default: typing.Optional[typing.Sequence]
    :param options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
    :type options: typing.Optional[typing.Set]
    :param tags: Enumerator of tags that are defined by parent class.
    :type tags: typing.Optional[typing.Set]
    :param subtype: Enumerator in ['COLOR', 'TRANSLATION', 'DIRECTION', 'VELOCITY', 'ACCELERATION', 'MATRIX', 'EULER', 'QUATERNION', 'AXISANGLE', 'XYZ', 'COLOR_GAMMA', 'LAYER', 'LAYER_MEMBER', 'NONE'].
    :type subtype: typing.Optional[str]
    :param size: Vector dimensions in [1, 32].
    :type size: typing.Optional[int]
    :param update: Function to be called when this value is modified, This function must take 2 values (self, context) and return None. *Warning* there are no safety checks to avoid infinite recursion.
    :type update: typing.Optional[typing.Any]
    :param get: Function to be called when this value is 'read', This function must take 1 value (self) and return the value of the property.
    :type get: typing.Optional[typing.Any]
    :param set: Function to be called when this value is 'written', This function must take 2 values (self, value) and return None.
    :type set: typing.Optional[typing.Any]
    :rtype: typing.Union[typing.List, 'bpy.types.BoolProperty']
    '''

    pass


def CollectionProperty(type: typing.Optional[typing.Any] = None,
                       name: typing.Optional[str] = "",
                       description: typing.Optional[str] = "",
                       options: typing.Optional[typing.Set] = {'ANIMATABLE'},
                       tags: typing.Optional[typing.Set] = {}
                       ) -> 'bpy.types.CollectionProperty':
    ''' Returns a new collection property definition.

    :param type: `bpy.types.ID`.
    :type type: typing.Optional[typing.Any]
    :param name: Name used in the user interface.
    :type name: typing.Optional[str]
    :param description: Text used for the tooltip and api documentation.
    :type description: typing.Optional[str]
    :param options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
    :type options: typing.Optional[typing.Set]
    :param tags: Enumerator of tags that are defined by parent class.
    :type tags: typing.Optional[typing.Set]
    :rtype: 'bpy.types.CollectionProperty'
    '''

    pass


def EnumProperty(
        items: typing.Optional[typing.Union[typing.Iterable[
            typing.Iterable[str]], typing.Callable]],
        name: typing.Optional[str] = "",
        description: typing.Optional[str] = "",
        default: typing.Optional[typing.Union[str, typing.Set]] = None,
        options: typing.Optional[typing.Set] = {'ANIMATABLE'},
        tags: typing.Optional[typing.Set] = {},
        update: typing.Optional[typing.Any] = None,
        get: typing.Optional[typing.Any] = None,
        set: typing.Optional[typing.Any] = None) -> 'bpy.types.EnumProperty':
    ''' Returns a new enumerator property definition.

    :param items: ``[(identifier, name, description, icon, number), ...]``. The first three elements of the tuples are mandatory. :identifier: The identifier is used for Python access. :name: Name for the interace. :description: Used for documentation and tooltips. :icon: An icon string identifier or integer icon value (e.g. returned by `bpy.types.UILayout.icon`) :number: Unique value used as the identifier for this item (stored in file data). Use when the identifier may need to change. If the *ENUM_FLAG* option is used, the values are bitmasks and should be powers of two. When an item only contains 4 items they define ``(identifier, name, description, number)``. For dynamic values a callback can be passed which returns a list in the same format as the static list. This function must take 2 arguments ``(self, context)``, **context may be None**. .. warning:: There is a known bug with using a callback, Python must keep a reference to the strings returned or Blender will misbehave or even crash.
    :type items: typing.Optional[typing.Union[typing.Iterable[typing.Iterable[str]], typing.Callable]]
    :param name: Name used in the user interface.
    :type name: typing.Optional[str]
    :param description: Text used for the tooltip and api documentation.
    :type description: typing.Optional[str]
    :param default: The default value for this enum, a string from the identifiers used in *items*. If the *ENUM_FLAG* option is used this must be a set of such string identifiers instead. WARNING: It shall not be specified (or specified to its default *None* value) for dynamic enums (i.e. if a callback function is given as *items* parameter).
    :type default: typing.Optional[typing.Union[str, typing.Set]]
    :param options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'ENUM_FLAG', 'LIBRARY_EDITABLE'].
    :type options: typing.Optional[typing.Set]
    :param tags: Enumerator of tags that are defined by parent class.
    :type tags: typing.Optional[typing.Set]
    :param update: Function to be called when this value is modified, This function must take 2 values (self, context) and return None. *Warning* there are no safety checks to avoid infinite recursion.
    :type update: typing.Optional[typing.Any]
    :param get: Function to be called when this value is 'read', This function must take 1 value (self) and return the value of the property.
    :type get: typing.Optional[typing.Any]
    :param set: Function to be called when this value is 'written', This function must take 2 values (self, value) and return None.
    :type set: typing.Optional[typing.Any]
    :rtype: 'bpy.types.EnumProperty'
    '''

    pass


def FloatProperty(
        name: typing.Optional[str] = "",
        description: typing.Optional[str] = "",
        default=0.0,
        min: typing.Optional[float] = 'sys.float_info.min',
        max: typing.Optional[float] = 'sys.float_info.max',
        soft_min: typing.Optional[float] = 'sys.float_info.min',
        soft_max: typing.Optional[float] = 'sys.float_info.max',
        step: typing.Optional[int] = 3,
        precision: typing.Optional[int] = 2,
        options: typing.Optional[typing.Set] = {'ANIMATABLE'},
        tags: typing.Optional[typing.Set] = {},
        subtype: typing.Optional[str] = 'NONE',
        unit: typing.Optional[str] = 'NONE',
        update: typing.Optional[typing.Any] = None,
        get: typing.Optional[typing.Any] = None,
        set: typing.Optional[typing.Any] = None) -> 'bpy.types.FloatProperty':
    ''' Returns a new float property definition.

    :param name: Name used in the user interface.
    :type name: typing.Optional[str]
    :param description: Text used for the tooltip and api documentation.
    :type description: typing.Optional[str]
    :param min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
    :type min: typing.Optional[float]
    :param max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
    :type max: typing.Optional[float]
    :param soft_min: Soft minimum (>= *min*), user won't be able to drag the widget below this value in the UI.
    :type soft_min: typing.Optional[float]
    :param soft_max: Soft maximum (<= *max*), user won't be able to drag the widget above this value in the UI.
    :type soft_max: typing.Optional[float]
    :param step: actual value is /100).
    :type step: typing.Optional[int]
    :param precision: Maximum number of decimal digits to display, in [0, 6].
    :type precision: typing.Optional[int]
    :param options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
    :type options: typing.Optional[typing.Set]
    :param tags: Enumerator of tags that are defined by parent class.
    :type tags: typing.Optional[typing.Set]
    :param subtype: Enumerator in ['PIXEL', 'UNSIGNED', 'PERCENTAGE', 'FACTOR', 'ANGLE', 'TIME', 'DISTANCE', 'NONE'].
    :type subtype: typing.Optional[str]
    :param unit: Enumerator in ['NONE', 'LENGTH', 'AREA', 'VOLUME', 'ROTATION', 'TIME', 'VELOCITY', 'ACCELERATION', 'MASS', 'CAMERA'].
    :type unit: typing.Optional[str]
    :param update: Function to be called when this value is modified, This function must take 2 values (self, context) and return None. *Warning* there are no safety checks to avoid infinite recursion.
    :type update: typing.Optional[typing.Any]
    :param get: Function to be called when this value is 'read', This function must take 1 value (self) and return the value of the property.
    :type get: typing.Optional[typing.Any]
    :param set: Function to be called when this value is 'written', This function must take 2 values (self, value) and return None.
    :type set: typing.Optional[typing.Any]
    :rtype: 'bpy.types.FloatProperty'
    '''

    pass


def FloatVectorProperty(
        name: typing.Optional[str] = "",
        description: typing.Optional[str] = "",
        default: typing.Optional[typing.Sequence] = (0.0, 0.0, 0.0),
        min: typing.Optional[float] = 'sys.float_info.min',
        max: typing.Optional[float] = 'sys.float_info.max',
        soft_min: typing.Optional[float] = 'sys.float_info.min',
        soft_max: typing.Optional[float] = 'sys.float_info.max',
        step: typing.Optional[int] = 3,
        precision: typing.Optional[int] = 2,
        options: typing.Optional[typing.Set] = {'ANIMATABLE'},
        tags: typing.Optional[typing.Set] = {},
        subtype: typing.Optional[str] = 'NONE',
        unit: typing.Optional[str] = 'NONE',
        size: typing.Optional[int] = 3,
        update: typing.Optional[typing.Any] = None,
        get: typing.Optional[typing.Any] = None,
        set: typing.Optional[typing.Any] = None
) -> typing.Union[typing.List, 'bpy.types.FloatProperty']:
    ''' Returns a new vector float property definition.

    :param name: Name used in the user interface.
    :type name: typing.Optional[str]
    :param description: Text used for the tooltip and api documentation.
    :type description: typing.Optional[str]
    :param default: sequence of floats the length of *size*.
    :type default: typing.Optional[typing.Sequence]
    :param min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
    :type min: typing.Optional[float]
    :param max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
    :type max: typing.Optional[float]
    :param soft_min: Soft minimum (>= *min*), user won't be able to drag the widget below this value in the UI.
    :type soft_min: typing.Optional[float]
    :param soft_max: Soft maximum (<= *max*), user won't be able to drag the widget above this value in the UI.
    :type soft_max: typing.Optional[float]
    :param options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
    :type options: typing.Optional[typing.Set]
    :param tags: Enumerator of tags that are defined by parent class.
    :type tags: typing.Optional[typing.Set]
    :param step: actual value is /100).
    :type step: typing.Optional[int]
    :param precision: Maximum number of decimal digits to display, in [0, 6].
    :type precision: typing.Optional[int]
    :param subtype: Enumerator in ['COLOR', 'TRANSLATION', 'DIRECTION', 'VELOCITY', 'ACCELERATION', 'MATRIX', 'EULER', 'QUATERNION', 'AXISANGLE', 'XYZ', 'COLOR_GAMMA', 'LAYER', 'LAYER_MEMBER', 'NONE'].
    :type subtype: typing.Optional[str]
    :param unit: Enumerator in ['NONE', 'LENGTH', 'AREA', 'VOLUME', 'ROTATION', 'TIME', 'VELOCITY', 'ACCELERATION', 'MASS', 'CAMERA'].
    :type unit: typing.Optional[str]
    :param size: Vector dimensions in [1, 32].
    :type size: typing.Optional[int]
    :param update: Function to be called when this value is modified, This function must take 2 values (self, context) and return None. *Warning* there are no safety checks to avoid infinite recursion.
    :type update: typing.Optional[typing.Any]
    :param get: Function to be called when this value is 'read', This function must take 1 value (self) and return the value of the property.
    :type get: typing.Optional[typing.Any]
    :param set: Function to be called when this value is 'written', This function must take 2 values (self, value) and return None.
    :type set: typing.Optional[typing.Any]
    :rtype: typing.Union[typing.List, 'bpy.types.FloatProperty']
    '''

    pass


def IntProperty(
        name: typing.Optional[str] = "",
        description: typing.Optional[str] = "",
        default=0,
        min: typing.Optional[int] = -2**31,
        max: typing.Optional[int] = 2**31 - 1,
        soft_min: typing.Optional[int] = -2**31,
        soft_max: typing.Optional[int] = 2**31 - 1,
        step: typing.Optional[int] = 1,
        options: typing.Optional[typing.Set] = {'ANIMATABLE'},
        tags: typing.Optional[typing.Set] = {},
        subtype: typing.Optional[str] = 'NONE',
        update: typing.Optional[typing.Any] = None,
        get: typing.Optional[typing.Any] = None,
        set: typing.Optional[typing.Any] = None) -> 'bpy.types.IntProperty':
    ''' Returns a new int property definition.

    :param name: Name used in the user interface.
    :type name: typing.Optional[str]
    :param description: Text used for the tooltip and api documentation.
    :type description: typing.Optional[str]
    :param min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
    :type min: typing.Optional[int]
    :param max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
    :type max: typing.Optional[int]
    :param soft_min: Soft minimum (>= *min*), user won't be able to drag the widget below this value in the UI.
    :type soft_min: typing.Optional[int]
    :param soft_max: Soft maximum (<= *max*), user won't be able to drag the widget above this value in the UI.
    :type soft_max: typing.Optional[int]
    :param step: unused currently!).
    :type step: typing.Optional[int]
    :param options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
    :type options: typing.Optional[typing.Set]
    :param tags: Enumerator of tags that are defined by parent class.
    :type tags: typing.Optional[typing.Set]
    :param subtype: Enumerator in ['PIXEL', 'UNSIGNED', 'PERCENTAGE', 'FACTOR', 'ANGLE', 'TIME', 'DISTANCE', 'NONE'].
    :type subtype: typing.Optional[str]
    :param update: Function to be called when this value is modified, This function must take 2 values (self, context) and return None. *Warning* there are no safety checks to avoid infinite recursion.
    :type update: typing.Optional[typing.Any]
    :param get: Function to be called when this value is 'read', This function must take 1 value (self) and return the value of the property.
    :type get: typing.Optional[typing.Any]
    :param set: Function to be called when this value is 'written', This function must take 2 values (self, value) and return None.
    :type set: typing.Optional[typing.Any]
    :rtype: 'bpy.types.IntProperty'
    '''

    pass


def IntVectorProperty(name: typing.Optional[str] = "",
                      description: typing.Optional[str] = "",
                      default: typing.Optional[typing.Sequence] = (0, 0, 0),
                      min: typing.Optional[int] = -2**31,
                      max: typing.Optional[int] = 2**31 - 1,
                      soft_min: typing.Optional[int] = -2**31,
                      soft_max: typing.Optional[int] = 2**31 - 1,
                      step: typing.Optional[int] = 1,
                      options: typing.Optional[typing.Set] = {'ANIMATABLE'},
                      tags: typing.Optional[typing.Set] = {},
                      subtype: typing.Optional[str] = 'NONE',
                      size: typing.Optional[int] = 3,
                      update: typing.Optional[typing.Any] = None,
                      get: typing.Optional[typing.Any] = None,
                      set: typing.Optional[typing.Any] = None
                      ) -> typing.Union[typing.List, 'bpy.types.IntProperty']:
    ''' Returns a new vector int property definition.

    :param name: Name used in the user interface.
    :type name: typing.Optional[str]
    :param description: Text used for the tooltip and api documentation.
    :type description: typing.Optional[str]
    :param default: sequence of ints the length of *size*.
    :type default: typing.Optional[typing.Sequence]
    :param min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
    :type min: typing.Optional[int]
    :param max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
    :type max: typing.Optional[int]
    :param soft_min: Soft minimum (>= *min*), user won't be able to drag the widget below this value in the UI.
    :type soft_min: typing.Optional[int]
    :param soft_max: Soft maximum (<= *max*), user won't be able to drag the widget above this value in the UI.
    :type soft_max: typing.Optional[int]
    :param step: unused currently!).
    :type step: typing.Optional[int]
    :param options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
    :type options: typing.Optional[typing.Set]
    :param tags: Enumerator of tags that are defined by parent class.
    :type tags: typing.Optional[typing.Set]
    :param subtype: Enumerator in ['COLOR', 'TRANSLATION', 'DIRECTION', 'VELOCITY', 'ACCELERATION', 'MATRIX', 'EULER', 'QUATERNION', 'AXISANGLE', 'XYZ', 'COLOR_GAMMA', 'LAYER', 'LAYER_MEMBER', 'NONE'].
    :type subtype: typing.Optional[str]
    :param size: Vector dimensions in [1, 32].
    :type size: typing.Optional[int]
    :param update: Function to be called when this value is modified, This function must take 2 values (self, context) and return None. *Warning* there are no safety checks to avoid infinite recursion.
    :type update: typing.Optional[typing.Any]
    :param get: Function to be called when this value is 'read', This function must take 1 value (self) and return the value of the property.
    :type get: typing.Optional[typing.Any]
    :param set: Function to be called when this value is 'written', This function must take 2 values (self, value) and return None.
    :type set: typing.Optional[typing.Any]
    :rtype: typing.Union[typing.List, 'bpy.types.IntProperty']
    '''

    pass


def PointerProperty(type: typing.Optional[typing.Any] = None,
                    name: typing.Optional[str] = "",
                    description: typing.Optional[str] = "",
                    options: typing.Optional[typing.Set] = {'ANIMATABLE'},
                    tags: typing.Optional[typing.Set] = {},
                    poll: typing.Optional[typing.Any] = None,
                    update: typing.Optional[typing.Any] = None
                    ) -> 'bpy.types.PointerProperty':
    ''' Returns a new pointer property definition.

    :param type: `bpy.types.ID`.
    :type type: typing.Optional[typing.Any]
    :param name: Name used in the user interface.
    :type name: typing.Optional[str]
    :param description: Text used for the tooltip and api documentation.
    :type description: typing.Optional[str]
    :param options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
    :type options: typing.Optional[typing.Set]
    :param tags: Enumerator of tags that are defined by parent class.
    :type tags: typing.Optional[typing.Set]
    :param poll: function to be called to determine whether an item is valid for this property. The function must take 2 values (self, object) and return Bool.
    :type poll: typing.Optional[typing.Any]
    :param update: Function to be called when this value is modified, This function must take 2 values (self, context) and return None. *Warning* there are no safety checks to avoid infinite recursion.
    :type update: typing.Optional[typing.Any]
    :rtype: 'bpy.types.PointerProperty'
    '''

    pass


def RemoveProperty(cls: typing.Optional[typing.Any],
                   attr: typing.Optional[str]):
    ''' Removes a dynamically defined property.

    :param cls: The class containing the property (must be a positional argument).
    :type cls: typing.Optional[typing.Any]
    :param attr: Property name (must be passed as a keyword).
    :type attr: typing.Optional[str]
    '''

    pass


def StringProperty(
        name: typing.Optional[str] = "",
        description: typing.Optional[str] = "",
        default: typing.Optional[str] = "",
        maxlen: typing.Optional[int] = 0,
        options: typing.Optional[typing.Set] = {'ANIMATABLE'},
        tags: typing.Optional[typing.Set] = {},
        subtype: typing.Optional[str] = 'NONE',
        update: typing.Optional[typing.Any] = None,
        get: typing.Optional[typing.Any] = None,
        set: typing.Optional[typing.Any] = None) -> 'bpy.types.StringProperty':
    ''' Returns a new string property definition.

    :param name: Name used in the user interface.
    :type name: typing.Optional[str]
    :param description: Text used for the tooltip and api documentation.
    :type description: typing.Optional[str]
    :param default: initializer string.
    :type default: typing.Optional[str]
    :param maxlen: maximum length of the string.
    :type maxlen: typing.Optional[int]
    :param options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
    :type options: typing.Optional[typing.Set]
    :param tags: Enumerator of tags that are defined by parent class.
    :type tags: typing.Optional[typing.Set]
    :param subtype: Enumerator in ['FILE_PATH', 'DIR_PATH', 'FILE_NAME', 'BYTE_STRING', 'PASSWORD', 'NONE'].
    :type subtype: typing.Optional[str]
    :param update: Function to be called when this value is modified, This function must take 2 values (self, context) and return None. *Warning* there are no safety checks to avoid infinite recursion.
    :type update: typing.Optional[typing.Any]
    :param get: Function to be called when this value is 'read', This function must take 1 value (self) and return the value of the property.
    :type get: typing.Optional[typing.Any]
    :param set: Function to be called when this value is 'written', This function must take 2 values (self, value) and return None.
    :type set: typing.Optional[typing.Any]
    :rtype: 'bpy.types.StringProperty'
    '''

    pass
