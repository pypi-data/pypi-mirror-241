import sys
import typing

GenericType = typing.TypeVar("GenericType")


def code_from_builtin(shader_name: str) -> typing.Dict:
    ''' Exposes the internal shader code for query.

    :param shader_name: { '2D_UNIFORM_COLOR', '2D_FLAT_COLOR', '2D_SMOOTH_COLOR', '2D_IMAGE', '3D_UNIFORM_COLOR', '3D_FLAT_COLOR', '3D_SMOOTH_COLOR'}
    :type shader_name: str
    :rtype: typing.Dict
    :return: Vertex, fragment and geometry shader codes.
    '''

    pass


def from_builtin(shader_name: str) -> typing.Any:
    ''' Shaders that are embedded in the blender internal code. They all read the uniform 'mat4 ModelViewProjectionMatrix', which can be edited by the 'gpu.matrix' module. For more details, you can check the shader code with the function 'gpu.shader.code_from_builtin';

    :param shader_name: { '2D_UNIFORM_COLOR', '2D_FLAT_COLOR', '2D_SMOOTH_COLOR', '2D_IMAGE', '3D_UNIFORM_COLOR', '3D_FLAT_COLOR', '3D_SMOOTH_COLOR'}
    :type shader_name: str
    :rtype: typing.Any
    :return: Shader object corresponding to the given name.
    '''

    pass


def unbind():
    ''' Unbind the bound shader object.

    '''

    pass
