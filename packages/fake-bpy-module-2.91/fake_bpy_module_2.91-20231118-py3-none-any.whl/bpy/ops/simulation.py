import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def new(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Create a new simulation data block and edit it in the opened simulation editor :file: `startup/bl_operators/simulation.py\:33 <https://developer.blender.org/diffusion/B/browse/master/release/scripts/startup/bl_operators/simulation.py$33>`_

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass
