import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def fbx(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        check_existing: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_glob: typing.Union[str, typing.Any] = "*.fbx",
        use_selection: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_active_collection: typing.Optional[typing.Union[bool, typing.
                                                            Any]] = False,
        global_scale: typing.Optional[typing.Any] = 1.0,
        apply_unit_scale: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = True,
        apply_scale_options: typing.Optional[typing.Any] = 'FBX_SCALE_NONE',
        bake_space_transform: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = False,
        object_types: typing.Optional[typing.Any] = {
            'ARMATURE', 'CAMERA', 'EMPTY', 'LIGHT', 'MESH', 'OTHER'
        },
        use_mesh_modifiers: typing.Optional[typing.Union[bool, typing.
                                                         Any]] = True,
        use_mesh_modifiers_render: typing.Optional[typing.Union[bool, typing.
                                                                Any]] = True,
        mesh_smooth_type: typing.Optional[typing.Any] = 'OFF',
        use_subsurf: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_mesh_edges: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        use_tspace: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_custom_props: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = False,
        add_leaf_bones: typing.Optional[typing.Union[bool, typing.Any]] = True,
        primary_bone_axis: typing.Optional[typing.Any] = 'Y',
        secondary_bone_axis: typing.Optional[typing.Any] = 'X',
        use_armature_deform_only: typing.Optional[typing.Union[bool, typing.
                                                               Any]] = False,
        armature_nodetype: typing.Optional[typing.Any] = 'NULL',
        bake_anim: typing.Optional[typing.Union[bool, typing.Any]] = True,
        bake_anim_use_all_bones: typing.Optional[typing.Union[bool, typing.
                                                              Any]] = True,
        bake_anim_use_nla_strips: typing.Optional[typing.Union[bool, typing.
                                                               Any]] = True,
        bake_anim_use_all_actions: typing.Optional[typing.Union[bool, typing.
                                                                Any]] = True,
        bake_anim_force_startend_keying: typing.Optional[
            typing.Union[bool, typing.Any]] = True,
        bake_anim_step: typing.Optional[typing.Any] = 1.0,
        bake_anim_simplify_factor: typing.Optional[typing.Any] = 1.0,
        path_mode: typing.Optional[typing.Any] = 'AUTO',
        embed_textures: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        batch_mode: typing.Optional[typing.Any] = 'OFF',
        use_batch_own_dir: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = True,
        use_metadata: typing.Optional[typing.Union[bool, typing.Any]] = True,
        axis_forward: typing.Optional[typing.Any] = '-Z',
        axis_up: typing.Optional[typing.Any] = 'Y'):
    ''' Write a FBX file

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Filepath used for exporting the file
    :type filepath: typing.Union[str, typing.Any]
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_glob: filter_glob
    :type filter_glob: typing.Union[str, typing.Any]
    :param use_selection: Selected Objects, Export selected and visible objects only
    :type use_selection: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_active_collection: Active Collection, Export only objects from the active collection (and its children)
    :type use_active_collection: typing.Optional[typing.Union[bool, typing.Any]]
    :param global_scale: Scale, Scale all data (Some importers do not support scaled armatures!)
    :type global_scale: typing.Optional[typing.Any]
    :param apply_unit_scale: Apply Unit, Take into account current Blender units settings (if unset, raw Blender Units values are used as-is)
    :type apply_unit_scale: typing.Optional[typing.Union[bool, typing.Any]]
    :param apply_scale_options: Apply Scalings, How to apply custom and units scalings in generated FBX file (Blender uses FBX scale to detect units on import, but many other applications do not handle the same way) * ``FBX_SCALE_NONE`` All Local, Apply custom scaling and units scaling to each object transformation, FBX scale remains at 1.0. * ``FBX_SCALE_UNITS`` FBX Units Scale, Apply custom scaling to each object transformation, and units scaling to FBX scale. * ``FBX_SCALE_CUSTOM`` FBX Custom Scale, Apply custom scaling to FBX scale, and units scaling to each object transformation. * ``FBX_SCALE_ALL`` FBX All, Apply custom scaling and units scaling to FBX scale.
    :type apply_scale_options: typing.Optional[typing.Any]
    :param bake_space_transform: Apply Transform, Bake space transform into object data, avoids getting unwanted rotations to objects when target space is not aligned with Blender's space (WARNING! experimental option, use at own risks, known broken with armatures/animations)
    :type bake_space_transform: typing.Optional[typing.Union[bool, typing.Any]]
    :param object_types: Object Types, Which kind of object to export * ``EMPTY`` Empty. * ``CAMERA`` Camera. * ``LIGHT`` Lamp. * ``ARMATURE`` Armature, WARNING: not supported in dupli/group instances. * ``MESH`` Mesh. * ``OTHER`` Other, Other geometry types, like curve, metaball, etc. (converted to meshes).
    :type object_types: typing.Optional[typing.Any]
    :param use_mesh_modifiers: Apply Modifiers, Apply modifiers to mesh objects (except Armature ones) - WARNING: prevents exporting shape keys
    :type use_mesh_modifiers: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_mesh_modifiers_render: Use Modifiers Render Setting, Use render settings when applying modifiers to mesh objects (DISABLED in Blender 2.8)
    :type use_mesh_modifiers_render: typing.Optional[typing.Union[bool, typing.Any]]
    :param mesh_smooth_type: Smoothing, Export smoothing information (prefer 'Normals Only' option if your target importer understand split normals) * ``OFF`` Normals Only, Export only normals instead of writing edge or face smoothing data. * ``FACE`` Face, Write face smoothing. * ``EDGE`` Edge, Write edge smoothing.
    :type mesh_smooth_type: typing.Optional[typing.Any]
    :param use_subsurf: Export Subdivision Surface, Export the last Catmull-Rom subdivision modifier as FBX subdivision (does not apply the modifier even if 'Apply Modifiers' is enabled)
    :type use_subsurf: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_mesh_edges: Loose Edges, Export loose edges (as two-vertices polygons)
    :type use_mesh_edges: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_tspace: Tangent Space, Add binormal and tangent vectors, together with normal they form the tangent space (will only work correctly with tris/quads only meshes!)
    :type use_tspace: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_custom_props: Custom Properties, Export custom properties
    :type use_custom_props: typing.Optional[typing.Union[bool, typing.Any]]
    :param add_leaf_bones: Add Leaf Bones, Append a final bone to the end of each chain to specify last bone length (use this when you intend to edit the armature from exported data)
    :type add_leaf_bones: typing.Optional[typing.Union[bool, typing.Any]]
    :param primary_bone_axis: Primary Bone Axis
    :type primary_bone_axis: typing.Optional[typing.Any]
    :param secondary_bone_axis: Secondary Bone Axis
    :type secondary_bone_axis: typing.Optional[typing.Any]
    :param use_armature_deform_only: Only Deform Bones, Only write deforming bones (and non-deforming ones when they have deforming children)
    :type use_armature_deform_only: typing.Optional[typing.Union[bool, typing.Any]]
    :param armature_nodetype: Armature FBXNode Type, FBX type of node (object) used to represent Blender's armatures (use Null one unless you experience issues with other app, other choices may no import back perfectly in Blender...) * ``NULL`` Null, 'Null' FBX node, similar to Blender's Empty (default). * ``ROOT`` Root, 'Root' FBX node, supposed to be the root of chains of bones.... * ``LIMBNODE`` LimbNode, 'LimbNode' FBX node, a regular joint between two bones....
    :type armature_nodetype: typing.Optional[typing.Any]
    :param bake_anim: Baked Animation, Export baked keyframe animation
    :type bake_anim: typing.Optional[typing.Union[bool, typing.Any]]
    :param bake_anim_use_all_bones: Key All Bones, Force exporting at least one key of animation for all bones (needed with some target applications, like UE4)
    :type bake_anim_use_all_bones: typing.Optional[typing.Union[bool, typing.Any]]
    :param bake_anim_use_nla_strips: NLA Strips, Export each non-muted NLA strip as a separated FBX's AnimStack, if any, instead of global scene animation
    :type bake_anim_use_nla_strips: typing.Optional[typing.Union[bool, typing.Any]]
    :param bake_anim_use_all_actions: All Actions, Export each action as a separated FBX's AnimStack, instead of global scene animation (note that animated objects will get all actions compatible with them, others will get no animation at all)
    :type bake_anim_use_all_actions: typing.Optional[typing.Union[bool, typing.Any]]
    :param bake_anim_force_startend_keying: Force Start/End Keying, Always add a keyframe at start and end of actions for animated channels
    :type bake_anim_force_startend_keying: typing.Optional[typing.Union[bool, typing.Any]]
    :param bake_anim_step: Sampling Rate, How often to evaluate animated values (in frames)
    :type bake_anim_step: typing.Optional[typing.Any]
    :param bake_anim_simplify_factor: Simplify, How much to simplify baked values (0.0 to disable, the higher the more simplified)
    :type bake_anim_simplify_factor: typing.Optional[typing.Any]
    :param path_mode: Path Mode, Method used to reference paths * ``AUTO`` Auto, Use Relative paths with subdirectories only. * ``ABSOLUTE`` Absolute, Always write absolute paths. * ``RELATIVE`` Relative, Always write relative paths (where possible). * ``MATCH`` Match, Match Absolute/Relative setting with input path. * ``STRIP`` Strip Path, Filename only. * ``COPY`` Copy, Copy the file to the destination path (or subdirectory).
    :type path_mode: typing.Optional[typing.Any]
    :param embed_textures: Embed Textures, Embed textures in FBX binary file (only for "Copy" path mode!)
    :type embed_textures: typing.Optional[typing.Union[bool, typing.Any]]
    :param batch_mode: Batch Mode * ``OFF`` Off, Active scene to file. * ``SCENE`` Scene, Each scene as a file. * ``COLLECTION`` Collection, Each collection (data-block ones) as a file, does not include content of children collections. * ``SCENE_COLLECTION`` Scene Collections, Each collection (including master, non-data-block ones) of each scene as a file, including content from children collections. * ``ACTIVE_SCENE_COLLECTION`` Active Scene Collections, Each collection (including master, non-data-block one) of the active scene as a file, including content from children collections.
    :type batch_mode: typing.Optional[typing.Any]
    :param use_batch_own_dir: Batch Own Dir, Create a dir for each exported file
    :type use_batch_own_dir: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_metadata: Use Metadata
    :type use_metadata: typing.Optional[typing.Union[bool, typing.Any]]
    :param axis_forward: Forward
    :type axis_forward: typing.Optional[typing.Any]
    :param axis_up: Up
    :type axis_up: typing.Optional[typing.Any]
    '''

    pass


def gltf(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        export_format: typing.Optional[typing.Any] = 'GLB',
        ui_tab: typing.Optional[typing.Any] = 'GENERAL',
        export_copyright: typing.Union[str, typing.Any] = "",
        export_image_format: typing.Optional[typing.Any] = 'AUTO',
        export_texture_dir: typing.Union[str, typing.Any] = "",
        export_texcoords: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = True,
        export_normals: typing.Optional[typing.Union[bool, typing.Any]] = True,
        export_draco_mesh_compression_enable: typing.Optional[
            typing.Union[bool, typing.Any]] = False,
        export_draco_mesh_compression_level: typing.Optional[typing.Any] = 6,
        export_draco_position_quantization: typing.Optional[typing.Any] = 14,
        export_draco_normal_quantization: typing.Optional[typing.Any] = 10,
        export_draco_texcoord_quantization: typing.Optional[typing.Any] = 12,
        export_draco_generic_quantization: typing.Optional[typing.Any] = 12,
        export_tangents: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False,
        export_materials: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = True,
        export_colors: typing.Optional[typing.Union[bool, typing.Any]] = True,
        export_cameras: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        export_selected: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False,
        use_selection: typing.Optional[typing.Union[bool, typing.Any]] = False,
        export_extras: typing.Optional[typing.Union[bool, typing.Any]] = False,
        export_yup: typing.Optional[typing.Union[bool, typing.Any]] = True,
        export_apply: typing.Optional[typing.Union[bool, typing.Any]] = False,
        export_animations: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = True,
        export_frame_range: typing.Optional[typing.Union[bool, typing.
                                                         Any]] = True,
        export_frame_step: typing.Optional[typing.Any] = 1,
        export_force_sampling: typing.Optional[typing.Union[bool, typing.
                                                            Any]] = True,
        export_nla_strips: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = True,
        export_def_bones: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = False,
        export_current_frame: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = False,
        export_skins: typing.Optional[typing.Union[bool, typing.Any]] = True,
        export_all_influences: typing.Optional[typing.Union[bool, typing.
                                                            Any]] = False,
        export_morph: typing.Optional[typing.Union[bool, typing.Any]] = True,
        export_morph_normal: typing.Optional[typing.Union[bool, typing.
                                                          Any]] = True,
        export_morph_tangent: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = False,
        export_lights: typing.Optional[typing.Union[bool, typing.Any]] = False,
        export_displacement: typing.Optional[typing.Union[bool, typing.
                                                          Any]] = False,
        will_save_settings: typing.Optional[typing.Union[bool, typing.
                                                         Any]] = False,
        filepath: typing.Union[str, typing.Any] = "",
        check_existing: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_glob: typing.Union[str, typing.Any] = "*.glb;*.gltf"):
    ''' Export scene as glTF 2.0 file

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param export_format: Format, Output format and embedding options. Binary is most efficient, but JSON (embedded or separate) may be easier to edit later * ``GLB`` glTF Binary (.glb), Exports a single file, with all data packed in binary form. Most efficient and portable, but more difficult to edit later. * ``GLTF_EMBEDDED`` glTF Embedded (.gltf), Exports a single file, with all data packed in JSON. Less efficient than binary, but easier to edit later. * ``GLTF_SEPARATE`` glTF Separate (.gltf + .bin + textures), Exports multiple files, with separate JSON, binary and texture data. Easiest to edit later.
    :type export_format: typing.Optional[typing.Any]
    :param ui_tab: ui_tab, Export setting categories * ``GENERAL`` General, General settings. * ``MESHES`` Meshes, Mesh settings. * ``OBJECTS`` Objects, Object settings. * ``ANIMATION`` Animation, Animation settings.
    :type ui_tab: typing.Optional[typing.Any]
    :param export_copyright: Copyright, Legal rights and conditions for the model
    :type export_copyright: typing.Union[str, typing.Any]
    :param export_image_format: Images, Output format for images. PNG is lossless and generally preferred, but JPEG might be preferable for web applications due to the smaller file size * ``AUTO`` Automatic, Save PNGs as PNGs and JPEGs as JPEGs. If neither one, use PNG. * ``JPEG`` JPEG Format (.jpg), Save images as JPEGs. (Images that need alpha are saved as PNGs though.) Be aware of a possible loss in quality.
    :type export_image_format: typing.Optional[typing.Any]
    :param export_texture_dir: Textures, Folder to place texture files in. Relative to the .gltf file
    :type export_texture_dir: typing.Union[str, typing.Any]
    :param export_texcoords: UVs, Export UVs (texture coordinates) with meshes
    :type export_texcoords: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_normals: Normals, Export vertex normals with meshes
    :type export_normals: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_draco_mesh_compression_enable: Draco mesh compression, Compress mesh using Draco
    :type export_draco_mesh_compression_enable: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_draco_mesh_compression_level: Compression level, Compression level (0 = most speed, 6 = most compression, higher values currently not supported)
    :type export_draco_mesh_compression_level: typing.Optional[typing.Any]
    :param export_draco_position_quantization: Position quantization bits, Quantization bits for position values (0 = no quantization)
    :type export_draco_position_quantization: typing.Optional[typing.Any]
    :param export_draco_normal_quantization: Normal quantization bits, Quantization bits for normal values (0 = no quantization)
    :type export_draco_normal_quantization: typing.Optional[typing.Any]
    :param export_draco_texcoord_quantization: Texcoord quantization bits, Quantization bits for texture coordinate values (0 = no quantization)
    :type export_draco_texcoord_quantization: typing.Optional[typing.Any]
    :param export_draco_generic_quantization: Generic quantization bits, Quantization bits for generic coordinate values like weights or joints (0 = no quantization)
    :type export_draco_generic_quantization: typing.Optional[typing.Any]
    :param export_tangents: Tangents, Export vertex tangents with meshes
    :type export_tangents: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_materials: Materials, Export materials
    :type export_materials: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_colors: Vertex Colors, Export vertex colors with meshes
    :type export_colors: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_cameras: Cameras, Export cameras
    :type export_cameras: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_selected: Selected Objects, Export selected objects only
    :type export_selected: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_selection: Selected Objects, Export selected objects only
    :type use_selection: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_extras: Custom Properties, Export custom properties as glTF extras
    :type export_extras: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_yup: +Y Up, Export using glTF convention, +Y up
    :type export_yup: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_apply: Apply Modifiers, Apply modifiers (excluding Armatures) to mesh objects -WARNING: prevents exporting shape keys
    :type export_apply: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_animations: Animations, Exports active actions and NLA tracks as glTF animations
    :type export_animations: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_frame_range: Limit to Playback Range, Clips animations to selected playback range
    :type export_frame_range: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_frame_step: Sampling Rate, How often to evaluate animated values (in frames)
    :type export_frame_step: typing.Optional[typing.Any]
    :param export_force_sampling: Always Sample Animations, Apply sampling to all animations
    :type export_force_sampling: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_nla_strips: Group by NLA Track, When on, multiple actions become part of the same glTF animation if they're pushed onto NLA tracks with the same name. When off, all the currently assigned actions become one glTF animation
    :type export_nla_strips: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_def_bones: Export Deformation Bones Only, Export Deformation bones only (and needed bones for hierarchy)
    :type export_def_bones: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_current_frame: Use Current Frame, Export the scene in the current animation frame
    :type export_current_frame: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_skins: Skinning, Export skinning (armature) data
    :type export_skins: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_all_influences: Include All Bone Influences, Allow >4 joint vertex influences. Models may appear incorrectly in many viewers
    :type export_all_influences: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_morph: Shape Keys, Export shape keys (morph targets)
    :type export_morph: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_morph_normal: Shape Key Normals, Export vertex normals with shape keys (morph targets)
    :type export_morph_normal: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_morph_tangent: Shape Key Tangents, Export vertex tangents with shape keys (morph targets)
    :type export_morph_tangent: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_lights: Punctual Lights, Export directional, point, and spot lights. Uses "KHR_lights_punctual" glTF extension
    :type export_lights: typing.Optional[typing.Union[bool, typing.Any]]
    :param export_displacement: Displacement Textures (EXPERIMENTAL), EXPERIMENTAL: Export displacement textures. Uses incomplete "KHR_materials_displacement" glTF extension
    :type export_displacement: typing.Optional[typing.Union[bool, typing.Any]]
    :param will_save_settings: Remember Export Settings, Store glTF export settings in the Blender project
    :type will_save_settings: typing.Optional[typing.Union[bool, typing.Any]]
    :param filepath: File Path, Filepath used for exporting the file
    :type filepath: typing.Union[str, typing.Any]
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_glob: filter_glob
    :type filter_glob: typing.Union[str, typing.Any]
    '''

    pass


def obj(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        check_existing: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_glob: typing.Union[str, typing.Any] = "*.obj;*.mtl",
        use_selection: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_animation: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_mesh_modifiers: typing.Optional[typing.Union[bool, typing.
                                                         Any]] = True,
        use_edges: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_smooth_groups: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = False,
        use_smooth_groups_bitflags: typing.Optional[typing.Union[bool, typing.
                                                                 Any]] = False,
        use_normals: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_uvs: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_materials: typing.Optional[typing.Union[bool, typing.Any]] = True,
        use_triangles: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_nurbs: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_vertex_groups: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = False,
        use_blen_objects: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = True,
        group_by_object: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False,
        group_by_material: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = False,
        keep_vertex_order: typing.Optional[typing.Union[bool, typing.
                                                        Any]] = False,
        global_scale: typing.Optional[typing.Any] = 1.0,
        path_mode: typing.Optional[typing.Any] = 'AUTO',
        axis_forward: typing.Optional[typing.Any] = '-Z',
        axis_up: typing.Optional[typing.Any] = 'Y'):
    ''' Save a Wavefront OBJ File

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Filepath used for exporting the file
    :type filepath: typing.Union[str, typing.Any]
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_glob: filter_glob
    :type filter_glob: typing.Union[str, typing.Any]
    :param use_selection: Selection Only, Export selected objects only
    :type use_selection: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_animation: Animation, Write out an OBJ for each frame
    :type use_animation: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_mesh_modifiers: Apply Modifiers, Apply modifiers
    :type use_mesh_modifiers: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_edges: Include Edges
    :type use_edges: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_smooth_groups: Smooth Groups, Write sharp edges as smooth groups
    :type use_smooth_groups: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_smooth_groups_bitflags: Bitflag Smooth Groups, Same as 'Smooth Groups', but generate smooth groups IDs as bitflags (produces at most 32 different smooth groups, usually much less)
    :type use_smooth_groups_bitflags: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_normals: Write Normals, Export one normal per vertex and per face, to represent flat faces and sharp edges
    :type use_normals: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_uvs: Include UVs, Write out the active UV coordinates
    :type use_uvs: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_materials: Write Materials, Write out the MTL file
    :type use_materials: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_triangles: Triangulate Faces, Convert all faces to triangles
    :type use_triangles: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_nurbs: Write Nurbs, Write nurbs curves as OBJ nurbs rather than converting to geometry
    :type use_nurbs: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_vertex_groups: Polygroups
    :type use_vertex_groups: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_blen_objects: OBJ Objects, Export Blender objects as OBJ objects
    :type use_blen_objects: typing.Optional[typing.Union[bool, typing.Any]]
    :param group_by_object: OBJ Groups, Export Blender objects as OBJ groups
    :type group_by_object: typing.Optional[typing.Union[bool, typing.Any]]
    :param group_by_material: Material Groups, Generate an OBJ group for each part of a geometry using a different material
    :type group_by_material: typing.Optional[typing.Union[bool, typing.Any]]
    :param keep_vertex_order: Keep Vertex Order
    :type keep_vertex_order: typing.Optional[typing.Union[bool, typing.Any]]
    :param global_scale: Scale
    :type global_scale: typing.Optional[typing.Any]
    :param path_mode: Path Mode, Method used to reference paths * ``AUTO`` Auto, Use Relative paths with subdirectories only. * ``ABSOLUTE`` Absolute, Always write absolute paths. * ``RELATIVE`` Relative, Always write relative paths (where possible). * ``MATCH`` Match, Match Absolute/Relative setting with input path. * ``STRIP`` Strip Path, Filename only. * ``COPY`` Copy, Copy the file to the destination path (or subdirectory).
    :type path_mode: typing.Optional[typing.Any]
    :param axis_forward: Forward
    :type axis_forward: typing.Optional[typing.Any]
    :param axis_up: Up
    :type axis_up: typing.Optional[typing.Any]
    '''

    pass


def x3d(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        check_existing: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_glob: typing.Union[str, typing.Any] = "*.x3d",
        use_selection: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_mesh_modifiers: typing.Optional[typing.Union[bool, typing.
                                                         Any]] = True,
        use_triangulate: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = False,
        use_normals: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_compress: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_hierarchy: typing.Optional[typing.Union[bool, typing.Any]] = True,
        name_decorations: typing.Optional[typing.Union[bool, typing.
                                                       Any]] = True,
        use_h3d: typing.Optional[typing.Union[bool, typing.Any]] = False,
        global_scale: typing.Optional[typing.Any] = 1.0,
        path_mode: typing.Optional[typing.Any] = 'AUTO',
        axis_forward: typing.Optional[typing.Any] = 'Z',
        axis_up: typing.Optional[typing.Any] = 'Y'):
    ''' Export selection to Extensible 3D file (.x3d)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Filepath used for exporting the file
    :type filepath: typing.Union[str, typing.Any]
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_glob: filter_glob
    :type filter_glob: typing.Union[str, typing.Any]
    :param use_selection: Selection Only, Export selected objects only
    :type use_selection: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_mesh_modifiers: Apply Modifiers, Use transformed mesh data from each object
    :type use_mesh_modifiers: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_triangulate: Triangulate, Write quads into 'IndexedTriangleSet'
    :type use_triangulate: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_normals: Normals, Write normals with geometry
    :type use_normals: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_compress: Compress, Compress the exported file
    :type use_compress: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_hierarchy: Hierarchy, Export parent child relationships
    :type use_hierarchy: typing.Optional[typing.Union[bool, typing.Any]]
    :param name_decorations: Name decorations, Add prefixes to the names of exported nodes to indicate their type
    :type name_decorations: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_h3d: H3D Extensions, Export shaders for H3D
    :type use_h3d: typing.Optional[typing.Union[bool, typing.Any]]
    :param global_scale: Scale
    :type global_scale: typing.Optional[typing.Any]
    :param path_mode: Path Mode, Method used to reference paths * ``AUTO`` Auto, Use Relative paths with subdirectories only. * ``ABSOLUTE`` Absolute, Always write absolute paths. * ``RELATIVE`` Relative, Always write relative paths (where possible). * ``MATCH`` Match, Match Absolute/Relative setting with input path. * ``STRIP`` Strip Path, Filename only. * ``COPY`` Copy, Copy the file to the destination path (or subdirectory).
    :type path_mode: typing.Optional[typing.Any]
    :param axis_forward: Forward
    :type axis_forward: typing.Optional[typing.Any]
    :param axis_up: Up
    :type axis_up: typing.Optional[typing.Any]
    '''

    pass
