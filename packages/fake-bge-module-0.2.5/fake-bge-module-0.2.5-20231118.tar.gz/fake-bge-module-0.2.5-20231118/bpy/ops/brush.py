import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def active_index_set(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Union[str, typing.Any] = "",
        index: typing.Optional[typing.Any] = 0):
    ''' Set active sculpt/paint brush from it's number

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode, Paint mode to set brush for
    :type mode: typing.Union[str, typing.Any]
    :param index: Number, Brush number
    :type index: typing.Optional[typing.Any]
    '''

    pass


def add(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Add brush by mode type

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def curve_preset(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        shape: typing.Optional[typing.Any] = 'SMOOTH'):
    ''' Set brush shape

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param shape: Mode
    :type shape: typing.Optional[typing.Any]
    '''

    pass


def reset(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
          execution_context: typing.Optional[typing.Union[str, int]] = None,
          undo: typing.Optional[bool] = None):
    ''' Return brush to defaults based on current tool

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def scale_size(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        scalar: typing.Optional[typing.Any] = 1.0):
    ''' Change brush size by a scalar

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param scalar: Scalar, Factor to scale brush size by
    :type scalar: typing.Optional[typing.Any]
    '''

    pass


def stencil_control(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'TRANSLATION',
        texmode: typing.Optional[typing.Any] = 'PRIMARY'):
    ''' Control the stencil brush

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Tool
    :type mode: typing.Optional[typing.Any]
    :param texmode: Tool
    :type texmode: typing.Optional[typing.Any]
    '''

    pass


def stencil_fit_image_aspect(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_repeat: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_scale: typing.Optional[typing.Union[bool, typing.Any]] = True,
        mask: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' When using an image texture, adjust the stencil size to fit the image aspect ratio

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param use_repeat: Use Repeat, Use repeat mapping values
    :type use_repeat: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_scale: Use Scale, Use texture scale values
    :type use_scale: typing.Optional[typing.Union[bool, typing.Any]]
    :param mask: Modify Mask Stencil, Modify either the primary or mask stencil
    :type mask: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def stencil_reset_transform(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mask: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Reset the stencil transformation to the default

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mask: Modify Mask Stencil, Modify either the primary or mask stencil
    :type mask: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def uv_sculpt_tool_set(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        tool: typing.Optional[typing.Any] = 'PINCH'):
    ''' Set the UV sculpt tool

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param tool: Tool * ``PINCH`` Pinch, Pinch UVs. * ``RELAX`` Relax, Relax UVs. * ``GRAB`` Grab, Grab UVs.
    :type tool: typing.Optional[typing.Any]
    '''

    pass
