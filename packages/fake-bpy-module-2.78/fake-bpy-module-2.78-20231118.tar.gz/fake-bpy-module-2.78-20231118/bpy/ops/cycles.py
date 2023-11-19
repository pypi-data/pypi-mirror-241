import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def use_shading_nodes(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Enable nodes on a material, world or lamp :file: `addons/cycles/ui.py <https://developer.blender.org/diffusion/BA//addons/cycles/ui.py>`_:813

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass
