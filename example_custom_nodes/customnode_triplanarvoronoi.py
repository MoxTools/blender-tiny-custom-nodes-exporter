bl_info = {
    "name": "Custom Node - TriplanarVoronoi",
    "author": "MoxTools Generator",
    "version": (1, 0, 0),
    "blender": (4, 0, 0),
    "location": "Shader Editor > Shift+A > Custom Nodes",
    "description": "Automatically exported standalone custom node",
    "category": "Node",
}

import bpy
from bpy.types import ShaderNodeCustomGroup

class Generated_TriplanarVoronoi_Node(ShaderNodeCustomGroup):
    bl_idname = 'ShaderNode_TriplanarVoronoi_Generated'
    bl_label = 'TriplanarVoronoi'
    bl_icon = 'NONE'

    image_pointer: bpy.props.PointerProperty(type=bpy.types.Image, name="Texture", update=lambda self, context: self.update_image(context))

    def update_image(self, context):
        if hasattr(self, "image_pointer") and self.node_tree:
            # Safety check: does the assigned image still exist in Blender?
            img = self.image_pointer if (self.image_pointer and self.image_pointer.name in bpy.data.images) else None
            for node in self.node_tree.nodes:
                if node.type == 'TEX_IMAGE':
                    node.image = img
            if context and hasattr(context, "area") and context.area:
                context.area.tag_redraw()

    def init(self, context):
        # Generate a unique tree name for this instance
        tree_name = f'.internal_TriplanarVoronoi_' + str(id(self))
        group = bpy.data.node_groups.new(name=tree_name, type='ShaderNodeTree')

        sock = group.interface.new_socket(name='Color', in_out='OUTPUT', socket_type='NodeSocketColor')
        try: sock.default_value = bpy.data.node_groups['TriplanarVoronoi'].interface.items_tree[0].default_value
        except: pass
        sock = group.interface.new_socket(name='TextureScale', in_out='INPUT', socket_type='NodeSocketFloat')
        try: sock.default_value = 10.0
        except: pass
        try: sock.min_value = 1.0
        except: pass
        try: sock.max_value = 1000.0
        except: pass
        sock = group.interface.new_socket(name='VoronoiScale', in_out='INPUT', socket_type='NodeSocketFloat')
        try: sock.default_value = 10.0
        except: pass
        try: sock.min_value = 0.0
        except: pass
        try: sock.max_value = 1000.0
        except: pass
        sock = group.interface.new_socket(name='VoronoiBlend', in_out='INPUT', socket_type='NodeSocketFloat')
        try: sock.default_value = 90.0
        except: pass
        try: sock.min_value = 0.0
        except: pass
        try: sock.max_value = 100.0
        except: pass
        sock = group.interface.new_socket(name='TriplanarBlendY', in_out='INPUT', socket_type='NodeSocketFloat')
        try: sock.default_value = 80.0
        except: pass
        try: sock.min_value = 0.0
        except: pass
        try: sock.max_value = 200.0
        except: pass
        sock = group.interface.new_socket(name='TriplanarBlendZ', in_out='INPUT', socket_type='NodeSocketFloat')
        try: sock.default_value = 80.0
        except: pass
        try: sock.min_value = 0.0
        except: pass
        try: sock.max_value = 200.0
        except: pass

        # Dictionary for exact node mapping
        created_nodes = {}

        group_input = group.nodes.new('NodeGroupInput')
        created_nodes['Group Input'] = group_input

        group_output = group.nodes.new('NodeGroupOutput')
        created_nodes['Group Output'] = group_output

        group_input.location_absolute = (-2689.5849609375, 808.1829833984375)
        group_output.location_absolute = (1978.4549560546875, 62.2730712890625)
        node_Texture_Coordinate_002 = group.nodes.new('ShaderNodeTexCoord')
        node_Texture_Coordinate_002.location_absolute = (-501.75665283203125, 557.2987060546875)
        try: node_Texture_Coordinate_002.location_absolute = Vector((-501.75665283203125, 557.2987060546875))
        except: pass
        try: node_Texture_Coordinate_002.warning_propagation = 'ALL'
        except: pass
        try: node_Texture_Coordinate_002.mute = False
        except: pass
        try: node_Texture_Coordinate_002.bl_label = 'Texture Coordinate'
        except: pass
        try: node_Texture_Coordinate_002.bl_description = 'Retrieve multiple types of texture coordinates.\nTypically used as inputs for texture nodes'
        except: pass
        try: node_Texture_Coordinate_002.bl_icon = 'NONE'
        except: pass
        try: node_Texture_Coordinate_002.bl_width_default = 140.0
        except: pass
        try: node_Texture_Coordinate_002.bl_width_min = 100.0
        except: pass
        try: node_Texture_Coordinate_002.bl_width_max = 700.0
        except: pass
        try: node_Texture_Coordinate_002.bl_height_default = 100.0
        except: pass
        try: node_Texture_Coordinate_002.bl_height_min = 30.0
        except: pass
        try: node_Texture_Coordinate_002.bl_height_max = 30.0
        except: pass
        try: node_Texture_Coordinate_002.object = None
        except: pass
        try: node_Texture_Coordinate_002.from_instancer = False
        except: pass
        created_nodes['Texture Coordinate.002'] = node_Texture_Coordinate_002
        node_Mapping_001 = group.nodes.new('ShaderNodeMapping')
        node_Mapping_001.location_absolute = (-4.708367824554443, -285.2556457519531)
        try: node_Mapping_001.location_absolute = Vector((-4.708367824554443, -285.2556457519531))
        except: pass
        try: node_Mapping_001.warning_propagation = 'ALL'
        except: pass
        try: node_Mapping_001.mute = False
        except: pass
        try: node_Mapping_001.bl_label = 'Mapping'
        except: pass
        try: node_Mapping_001.bl_description = 'Transform the input vector by applying translation, rotation, and scale'
        except: pass
        try: node_Mapping_001.bl_icon = 'NONE'
        except: pass
        try: node_Mapping_001.bl_width_default = 140.0
        except: pass
        try: node_Mapping_001.bl_width_min = 100.0
        except: pass
        try: node_Mapping_001.bl_width_max = 700.0
        except: pass
        try: node_Mapping_001.bl_height_default = 100.0
        except: pass
        try: node_Mapping_001.bl_height_min = 30.0
        except: pass
        try: node_Mapping_001.bl_height_max = 30.0
        except: pass
        try: node_Mapping_001.vector_type = 'POINT'
        except: pass
        created_nodes['Mapping.001'] = node_Mapping_001
        node_Mix = group.nodes.new('ShaderNodeMix')
        node_Mix.location_absolute = (939.8900756835938, -291.6180114746094)
        try: node_Mix.location_absolute = Vector((939.8900756835938, -291.6180114746094))
        except: pass
        try: node_Mix.warning_propagation = 'ALL'
        except: pass
        try: node_Mix.mute = False
        except: pass
        try: node_Mix.bl_label = 'Mix'
        except: pass
        try: node_Mix.bl_description = 'Mix values by a factor'
        except: pass
        try: node_Mix.bl_icon = 'NONE'
        except: pass
        try: node_Mix.bl_width_default = 140.0
        except: pass
        try: node_Mix.bl_width_min = 100.0
        except: pass
        try: node_Mix.bl_width_max = 700.0
        except: pass
        try: node_Mix.bl_height_default = 100.0
        except: pass
        try: node_Mix.bl_height_min = 30.0
        except: pass
        try: node_Mix.bl_height_max = 30.0
        except: pass
        try: node_Mix.data_type = 'RGBA'
        except: pass
        try: node_Mix.factor_mode = 'UNIFORM'
        except: pass
        try: node_Mix.blend_type = 'MIX'
        except: pass
        try: node_Mix.clamp_factor = True
        except: pass
        try: node_Mix.clamp_result = False
        except: pass
        try: node_Mix.inputs[1].default_value = [0.5,0.5,0.5]
        except: pass
        try: node_Mix.inputs[2].default_value = 0.0
        except: pass
        try: node_Mix.inputs[3].default_value = 0.0
        except: pass
        try: node_Mix.inputs[4].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Mix.inputs[5].default_value = [0.0,0.0,0.0]
        except: pass
        created_nodes['Mix'] = node_Mix
        node_Mix_001 = group.nodes.new('ShaderNodeMix')
        node_Mix_001.location_absolute = (1110.4471435546875, -730.7175903320312)
        try: node_Mix_001.location_absolute = Vector((1110.4471435546875, -730.7175903320312))
        except: pass
        try: node_Mix_001.warning_propagation = 'ALL'
        except: pass
        try: node_Mix_001.mute = False
        except: pass
        try: node_Mix_001.bl_label = 'Mix'
        except: pass
        try: node_Mix_001.bl_description = 'Mix values by a factor'
        except: pass
        try: node_Mix_001.bl_icon = 'NONE'
        except: pass
        try: node_Mix_001.bl_width_default = 140.0
        except: pass
        try: node_Mix_001.bl_width_min = 100.0
        except: pass
        try: node_Mix_001.bl_width_max = 700.0
        except: pass
        try: node_Mix_001.bl_height_default = 100.0
        except: pass
        try: node_Mix_001.bl_height_min = 30.0
        except: pass
        try: node_Mix_001.bl_height_max = 30.0
        except: pass
        try: node_Mix_001.data_type = 'RGBA'
        except: pass
        try: node_Mix_001.factor_mode = 'UNIFORM'
        except: pass
        try: node_Mix_001.blend_type = 'MIX'
        except: pass
        try: node_Mix_001.clamp_factor = True
        except: pass
        try: node_Mix_001.clamp_result = False
        except: pass
        try: node_Mix_001.inputs[1].default_value = [0.5,0.5,0.5]
        except: pass
        try: node_Mix_001.inputs[2].default_value = 0.0
        except: pass
        try: node_Mix_001.inputs[3].default_value = 0.0
        except: pass
        try: node_Mix_001.inputs[4].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Mix_001.inputs[5].default_value = [0.0,0.0,0.0]
        except: pass
        created_nodes['Mix.001'] = node_Mix_001
        node_Vector_Math_002 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_002.location_absolute = (-41.9268913269043, 245.3990936279297)
        try: node_Vector_Math_002.location_absolute = Vector((-41.9268913269043, 245.3990936279297))
        except: pass
        try: node_Vector_Math_002.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_002.mute = False
        except: pass
        try: node_Vector_Math_002.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_002.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_002.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_002.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_002.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_002.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_002.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_002.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_002.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_002.operation = 'POWER'
        except: pass
        try: node_Vector_Math_002.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_002.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.002'] = node_Vector_Math_002
        node_Vector_Math_003 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_003.location_absolute = (135.183349609375, 224.53640747070312)
        try: node_Vector_Math_003.location_absolute = Vector((135.183349609375, 224.53640747070312))
        except: pass
        try: node_Vector_Math_003.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_003.mute = False
        except: pass
        try: node_Vector_Math_003.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_003.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_003.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_003.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_003.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_003.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_003.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_003.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_003.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_003.operation = 'NORMALIZE'
        except: pass
        try: node_Vector_Math_003.inputs[1].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_003.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_003.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.003'] = node_Vector_Math_003
        node_Vector_Math_001 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_001.location_absolute = (-190.15805053710938, 123.3564224243164)
        try: node_Vector_Math_001.location_absolute = Vector((-190.15805053710938, 123.3564224243164))
        except: pass
        try: node_Vector_Math_001.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_001.mute = False
        except: pass
        try: node_Vector_Math_001.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_001.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_001.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_001.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_001.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_001.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_001.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_001.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_001.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_001.operation = 'ABSOLUTE'
        except: pass
        try: node_Vector_Math_001.inputs[1].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_001.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_001.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.001'] = node_Vector_Math_001
        node_Vector_Math_004 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_004.location_absolute = (-319.45928955078125, 123.77845764160156)
        try: node_Vector_Math_004.location_absolute = Vector((-319.45928955078125, 123.77845764160156))
        except: pass
        try: node_Vector_Math_004.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_004.mute = False
        except: pass
        try: node_Vector_Math_004.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_004.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_004.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_004.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_004.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_004.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_004.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_004.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_004.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_004.operation = 'NORMALIZE'
        except: pass
        try: node_Vector_Math_004.inputs[1].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_004.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_004.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.004'] = node_Vector_Math_004
        node_Vector_Rotate = group.nodes.new('ShaderNodeVectorRotate')
        node_Vector_Rotate.location_absolute = (-187.44168090820312, -283.4295654296875)
        try: node_Vector_Rotate.location_absolute = Vector((-187.44168090820312, -283.4295654296875))
        except: pass
        try: node_Vector_Rotate.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Rotate.mute = False
        except: pass
        try: node_Vector_Rotate.bl_label = 'Vector Rotate'
        except: pass
        try: node_Vector_Rotate.bl_description = 'Rotate a vector around a pivot point (center)'
        except: pass
        try: node_Vector_Rotate.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Rotate.bl_width_default = 140.0
        except: pass
        try: node_Vector_Rotate.bl_width_min = 100.0
        except: pass
        try: node_Vector_Rotate.bl_width_max = 700.0
        except: pass
        try: node_Vector_Rotate.bl_height_default = 100.0
        except: pass
        try: node_Vector_Rotate.bl_height_min = 30.0
        except: pass
        try: node_Vector_Rotate.bl_height_max = 30.0
        except: pass
        try: node_Vector_Rotate.rotation_type = 'EULER_XYZ'
        except: pass
        try: node_Vector_Rotate.invert = False
        except: pass
        try: node_Vector_Rotate.inputs[1].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Rotate.inputs[2].default_value = [0.0,0.0,0.7000000476837158]
        except: pass
        try: node_Vector_Rotate.inputs[3].default_value = 7.084291458129883
        except: pass
        created_nodes['Vector Rotate'] = node_Vector_Rotate
        node_Combine_XYZ = group.nodes.new('ShaderNodeCombineXYZ')
        node_Combine_XYZ.location_absolute = (-382.5724792480469, -489.41241455078125)
        try: node_Combine_XYZ.location_absolute = Vector((-382.5724792480469, -489.41241455078125))
        except: pass
        try: node_Combine_XYZ.warning_propagation = 'ALL'
        except: pass
        try: node_Combine_XYZ.mute = False
        except: pass
        try: node_Combine_XYZ.bl_label = 'Combine XYZ'
        except: pass
        try: node_Combine_XYZ.bl_description = 'Create a vector from X, Y, and Z components'
        except: pass
        try: node_Combine_XYZ.bl_icon = 'NONE'
        except: pass
        try: node_Combine_XYZ.bl_width_default = 140.0
        except: pass
        try: node_Combine_XYZ.bl_width_min = 100.0
        except: pass
        try: node_Combine_XYZ.bl_width_max = 700.0
        except: pass
        try: node_Combine_XYZ.bl_height_default = 100.0
        except: pass
        try: node_Combine_XYZ.bl_height_min = 30.0
        except: pass
        try: node_Combine_XYZ.bl_height_max = 30.0
        except: pass
        try: node_Combine_XYZ.inputs[0].default_value = 0.0
        except: pass
        try: node_Combine_XYZ.inputs[1].default_value = 0.0
        except: pass
        created_nodes['Combine XYZ'] = node_Combine_XYZ
        node_Voronoi_Texture_001 = group.nodes.new('ShaderNodeTexVoronoi')
        node_Voronoi_Texture_001.location_absolute = (57.61560821533203, 580.592529296875)
        try: node_Voronoi_Texture_001.location_absolute = Vector((57.61560821533203, 580.592529296875))
        except: pass
        try: node_Voronoi_Texture_001.warning_propagation = 'ALL'
        except: pass
        try: node_Voronoi_Texture_001.mute = False
        except: pass
        try: node_Voronoi_Texture_001.bl_label = 'Voronoi Texture'
        except: pass
        try: node_Voronoi_Texture_001.bl_description = 'Generate Worley noise based on the distance to random points. Typically used to generate textures such as stones, water, or biological cells'
        except: pass
        try: node_Voronoi_Texture_001.bl_icon = 'NONE'
        except: pass
        try: node_Voronoi_Texture_001.bl_width_default = 155.0
        except: pass
        try: node_Voronoi_Texture_001.bl_width_min = 140.0
        except: pass
        try: node_Voronoi_Texture_001.bl_width_max = 700.0
        except: pass
        try: node_Voronoi_Texture_001.bl_height_default = 100.0
        except: pass
        try: node_Voronoi_Texture_001.bl_height_min = 30.0
        except: pass
        try: node_Voronoi_Texture_001.bl_height_max = 30.0
        except: pass
        try: node_Voronoi_Texture_001.voronoi_dimensions = '2D'
        except: pass
        try: node_Voronoi_Texture_001.distance = 'EUCLIDEAN'
        except: pass
        try: node_Voronoi_Texture_001.feature = 'DISTANCE_TO_EDGE'
        except: pass
        try: node_Voronoi_Texture_001.normalize = False
        except: pass
        try: node_Voronoi_Texture_001.inputs[1].default_value = 0.0
        except: pass
        try: node_Voronoi_Texture_001.inputs[3].default_value = 0.0
        except: pass
        try: node_Voronoi_Texture_001.inputs[4].default_value = 1.0
        except: pass
        try: node_Voronoi_Texture_001.inputs[5].default_value = 2.100001335144043
        except: pass
        try: node_Voronoi_Texture_001.inputs[6].default_value = 0.363095223903656
        except: pass
        try: node_Voronoi_Texture_001.inputs[7].default_value = 0.5
        except: pass
        try: node_Voronoi_Texture_001.inputs[8].default_value = 1.0
        except: pass
        created_nodes['Voronoi Texture.001'] = node_Voronoi_Texture_001
        node_Mix_002 = group.nodes.new('ShaderNodeMix')
        node_Mix_002.location_absolute = (1639.16796875, 220.1870574951172)
        try: node_Mix_002.location_absolute = Vector((1639.16796875, 220.1870574951172))
        except: pass
        try: node_Mix_002.warning_propagation = 'ALL'
        except: pass
        try: node_Mix_002.mute = False
        except: pass
        try: node_Mix_002.bl_label = 'Mix'
        except: pass
        try: node_Mix_002.bl_description = 'Mix values by a factor'
        except: pass
        try: node_Mix_002.bl_icon = 'NONE'
        except: pass
        try: node_Mix_002.bl_width_default = 140.0
        except: pass
        try: node_Mix_002.bl_width_min = 100.0
        except: pass
        try: node_Mix_002.bl_width_max = 700.0
        except: pass
        try: node_Mix_002.bl_height_default = 100.0
        except: pass
        try: node_Mix_002.bl_height_min = 30.0
        except: pass
        try: node_Mix_002.bl_height_max = 30.0
        except: pass
        try: node_Mix_002.data_type = 'RGBA'
        except: pass
        try: node_Mix_002.factor_mode = 'UNIFORM'
        except: pass
        try: node_Mix_002.blend_type = 'MIX'
        except: pass
        try: node_Mix_002.clamp_factor = True
        except: pass
        try: node_Mix_002.clamp_result = False
        except: pass
        try: node_Mix_002.inputs[1].default_value = [0.5,0.5,0.5]
        except: pass
        try: node_Mix_002.inputs[2].default_value = 0.0
        except: pass
        try: node_Mix_002.inputs[3].default_value = 0.0
        except: pass
        try: node_Mix_002.inputs[4].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Mix_002.inputs[5].default_value = [0.0,0.0,0.0]
        except: pass
        created_nodes['Mix.002'] = node_Mix_002
        node_Map_Range = group.nodes.new('ShaderNodeMapRange')
        node_Map_Range.location_absolute = (318.0509948730469, 580.432373046875)
        try: node_Map_Range.location_absolute = Vector((318.0509948730469, 580.432373046875))
        except: pass
        try: node_Map_Range.warning_propagation = 'ALL'
        except: pass
        try: node_Map_Range.mute = False
        except: pass
        try: node_Map_Range.bl_label = 'Map Range'
        except: pass
        try: node_Map_Range.bl_description = 'Remap a value from a range to a target range'
        except: pass
        try: node_Map_Range.bl_icon = 'NONE'
        except: pass
        try: node_Map_Range.bl_width_default = 140.0
        except: pass
        try: node_Map_Range.bl_width_min = 100.0
        except: pass
        try: node_Map_Range.bl_width_max = 700.0
        except: pass
        try: node_Map_Range.bl_height_default = 100.0
        except: pass
        try: node_Map_Range.bl_height_min = 30.0
        except: pass
        try: node_Map_Range.bl_height_max = 30.0
        except: pass
        try: node_Map_Range.clamp = True
        except: pass
        try: node_Map_Range.interpolation_type = 'LINEAR'
        except: pass
        try: node_Map_Range.data_type = 'FLOAT'
        except: pass
        try: node_Map_Range.inputs[1].default_value = 0.0
        except: pass
        try: node_Map_Range.inputs[3].default_value = 0.0
        except: pass
        try: node_Map_Range.inputs[4].default_value = 1.0
        except: pass
        try: node_Map_Range.inputs[5].default_value = 4.0
        except: pass
        try: node_Map_Range.inputs[6].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Map_Range.inputs[7].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Map_Range.inputs[8].default_value = [1.0,1.0,1.0]
        except: pass
        try: node_Map_Range.inputs[9].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Map_Range.inputs[10].default_value = [1.0,1.0,1.0]
        except: pass
        try: node_Map_Range.inputs[11].default_value = [4.0,4.0,4.0]
        except: pass
        created_nodes['Map Range'] = node_Map_Range
        node_Math_001 = group.nodes.new('ShaderNodeMath')
        node_Math_001.location_absolute = (-1077.610595703125, 796.2484130859375)
        try: node_Math_001.location_absolute = Vector((-1077.610595703125, 796.2484130859375))
        except: pass
        try: node_Math_001.warning_propagation = 'ALL'
        except: pass
        try: node_Math_001.mute = False
        except: pass
        try: node_Math_001.bl_label = 'Math'
        except: pass
        try: node_Math_001.bl_description = 'Perform math operations'
        except: pass
        try: node_Math_001.bl_icon = 'NONE'
        except: pass
        try: node_Math_001.bl_width_default = 140.0
        except: pass
        try: node_Math_001.bl_width_min = 100.0
        except: pass
        try: node_Math_001.bl_width_max = 700.0
        except: pass
        try: node_Math_001.bl_height_default = 100.0
        except: pass
        try: node_Math_001.bl_height_min = 30.0
        except: pass
        try: node_Math_001.bl_height_max = 30.0
        except: pass
        try: node_Math_001.operation = 'DIVIDE'
        except: pass
        try: node_Math_001.use_clamp = False
        except: pass
        try: node_Math_001.inputs[1].default_value = 100.0
        except: pass
        try: node_Math_001.inputs[2].default_value = 0.5
        except: pass
        created_nodes['Math.001'] = node_Math_001
        node_Math_002 = group.nodes.new('ShaderNodeMath')
        node_Math_002.location_absolute = (-773.898193359375, 795.4407958984375)
        try: node_Math_002.location_absolute = Vector((-773.898193359375, 795.4407958984375))
        except: pass
        try: node_Math_002.warning_propagation = 'ALL'
        except: pass
        try: node_Math_002.mute = False
        except: pass
        try: node_Math_002.bl_label = 'Math'
        except: pass
        try: node_Math_002.bl_description = 'Perform math operations'
        except: pass
        try: node_Math_002.bl_icon = 'NONE'
        except: pass
        try: node_Math_002.bl_width_default = 140.0
        except: pass
        try: node_Math_002.bl_width_min = 100.0
        except: pass
        try: node_Math_002.bl_width_max = 700.0
        except: pass
        try: node_Math_002.bl_height_default = 100.0
        except: pass
        try: node_Math_002.bl_height_min = 30.0
        except: pass
        try: node_Math_002.bl_height_max = 30.0
        except: pass
        try: node_Math_002.operation = 'SUBTRACT'
        except: pass
        try: node_Math_002.use_clamp = False
        except: pass
        try: node_Math_002.inputs[0].default_value = 1.0
        except: pass
        try: node_Math_002.inputs[2].default_value = 0.5
        except: pass
        created_nodes['Math.002'] = node_Math_002
        node_Math_004 = group.nodes.new('ShaderNodeMath')
        node_Math_004.location_absolute = (-2066.786376953125, 221.43063354492188)
        try: node_Math_004.location_absolute = Vector((-2066.786376953125, 221.43063354492188))
        except: pass
        try: node_Math_004.warning_propagation = 'ALL'
        except: pass
        try: node_Math_004.mute = False
        except: pass
        try: node_Math_004.bl_label = 'Math'
        except: pass
        try: node_Math_004.bl_description = 'Perform math operations'
        except: pass
        try: node_Math_004.bl_icon = 'NONE'
        except: pass
        try: node_Math_004.bl_width_default = 140.0
        except: pass
        try: node_Math_004.bl_width_min = 100.0
        except: pass
        try: node_Math_004.bl_width_max = 700.0
        except: pass
        try: node_Math_004.bl_height_default = 100.0
        except: pass
        try: node_Math_004.bl_height_min = 30.0
        except: pass
        try: node_Math_004.bl_height_max = 30.0
        except: pass
        try: node_Math_004.operation = 'DIVIDE'
        except: pass
        try: node_Math_004.use_clamp = False
        except: pass
        try: node_Math_004.inputs[1].default_value = 100.0
        except: pass
        try: node_Math_004.inputs[2].default_value = 0.5
        except: pass
        created_nodes['Math.004'] = node_Math_004
        node_Voronoi_Texture_003 = group.nodes.new('ShaderNodeTexVoronoi')
        node_Voronoi_Texture_003.location_absolute = (-1004.2744140625, -424.3075256347656)
        try: node_Voronoi_Texture_003.location_absolute = Vector((-1004.2744140625, -424.3075256347656))
        except: pass
        try: node_Voronoi_Texture_003.warning_propagation = 'ALL'
        except: pass
        try: node_Voronoi_Texture_003.mute = False
        except: pass
        try: node_Voronoi_Texture_003.bl_label = 'Voronoi Texture'
        except: pass
        try: node_Voronoi_Texture_003.bl_description = 'Generate Worley noise based on the distance to random points. Typically used to generate textures such as stones, water, or biological cells'
        except: pass
        try: node_Voronoi_Texture_003.bl_icon = 'NONE'
        except: pass
        try: node_Voronoi_Texture_003.bl_width_default = 155.0
        except: pass
        try: node_Voronoi_Texture_003.bl_width_min = 140.0
        except: pass
        try: node_Voronoi_Texture_003.bl_width_max = 700.0
        except: pass
        try: node_Voronoi_Texture_003.bl_height_default = 100.0
        except: pass
        try: node_Voronoi_Texture_003.bl_height_min = 30.0
        except: pass
        try: node_Voronoi_Texture_003.bl_height_max = 30.0
        except: pass
        try: node_Voronoi_Texture_003.voronoi_dimensions = '2D'
        except: pass
        try: node_Voronoi_Texture_003.distance = 'EUCLIDEAN'
        except: pass
        try: node_Voronoi_Texture_003.feature = 'F1'
        except: pass
        try: node_Voronoi_Texture_003.normalize = False
        except: pass
        try: node_Voronoi_Texture_003.inputs[1].default_value = 0.0
        except: pass
        try: node_Voronoi_Texture_003.inputs[3].default_value = 0.0
        except: pass
        try: node_Voronoi_Texture_003.inputs[4].default_value = 0.6428571343421936
        except: pass
        try: node_Voronoi_Texture_003.inputs[5].default_value = 11.90000057220459
        except: pass
        try: node_Voronoi_Texture_003.inputs[6].default_value = 0.363095223903656
        except: pass
        try: node_Voronoi_Texture_003.inputs[7].default_value = 0.5
        except: pass
        try: node_Voronoi_Texture_003.inputs[8].default_value = 1.0
        except: pass
        created_nodes['Voronoi Texture.003'] = node_Voronoi_Texture_003
        node_Noise_Texture_002 = group.nodes.new('ShaderNodeTexNoise')
        node_Noise_Texture_002.location_absolute = (-773.4857177734375, -477.8623046875)
        try: node_Noise_Texture_002.location_absolute = Vector((-773.4857177734375, -477.8623046875))
        except: pass
        try: node_Noise_Texture_002.warning_propagation = 'ALL'
        except: pass
        try: node_Noise_Texture_002.mute = False
        except: pass
        try: node_Noise_Texture_002.bl_label = 'Noise Texture'
        except: pass
        try: node_Noise_Texture_002.bl_description = 'Generate fractal Perlin noise'
        except: pass
        try: node_Noise_Texture_002.bl_icon = 'NONE'
        except: pass
        try: node_Noise_Texture_002.bl_width_default = 145.0
        except: pass
        try: node_Noise_Texture_002.bl_width_min = 140.0
        except: pass
        try: node_Noise_Texture_002.bl_width_max = 700.0
        except: pass
        try: node_Noise_Texture_002.bl_height_default = 100.0
        except: pass
        try: node_Noise_Texture_002.bl_height_min = 30.0
        except: pass
        try: node_Noise_Texture_002.bl_height_max = 30.0
        except: pass
        try: node_Noise_Texture_002.noise_dimensions = '2D'
        except: pass
        try: node_Noise_Texture_002.noise_type = 'FBM'
        except: pass
        try: node_Noise_Texture_002.normalize = False
        except: pass
        try: node_Noise_Texture_002.inputs[1].default_value = 0.0
        except: pass
        try: node_Noise_Texture_002.inputs[2].default_value = 0.5000004768371582
        except: pass
        try: node_Noise_Texture_002.inputs[3].default_value = 2.0
        except: pass
        try: node_Noise_Texture_002.inputs[4].default_value = 0.5
        except: pass
        try: node_Noise_Texture_002.inputs[5].default_value = 2.0
        except: pass
        try: node_Noise_Texture_002.inputs[6].default_value = 0.0
        except: pass
        try: node_Noise_Texture_002.inputs[7].default_value = 1.0
        except: pass
        try: node_Noise_Texture_002.inputs[8].default_value = 0.0
        except: pass
        created_nodes['Noise Texture.002'] = node_Noise_Texture_002
        node_Vector_Math_006 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_006.location_absolute = (-791.520751953125, -324.26812744140625)
        try: node_Vector_Math_006.location_absolute = Vector((-791.520751953125, -324.26812744140625))
        except: pass
        try: node_Vector_Math_006.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_006.mute = False
        except: pass
        try: node_Vector_Math_006.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_006.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_006.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_006.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_006.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_006.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_006.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_006.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_006.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_006.operation = 'SUBTRACT'
        except: pass
        try: node_Vector_Math_006.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_006.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.006'] = node_Vector_Math_006
        node_Math_006 = group.nodes.new('ShaderNodeMath')
        node_Math_006.location_absolute = (-572.2617797851562, -483.96014404296875)
        try: node_Math_006.location_absolute = Vector((-572.2617797851562, -483.96014404296875))
        except: pass
        try: node_Math_006.warning_propagation = 'ALL'
        except: pass
        try: node_Math_006.mute = False
        except: pass
        try: node_Math_006.bl_label = 'Math'
        except: pass
        try: node_Math_006.bl_description = 'Perform math operations'
        except: pass
        try: node_Math_006.bl_icon = 'NONE'
        except: pass
        try: node_Math_006.bl_width_default = 140.0
        except: pass
        try: node_Math_006.bl_width_min = 100.0
        except: pass
        try: node_Math_006.bl_width_max = 700.0
        except: pass
        try: node_Math_006.bl_height_default = 100.0
        except: pass
        try: node_Math_006.bl_height_min = 30.0
        except: pass
        try: node_Math_006.bl_height_max = 30.0
        except: pass
        try: node_Math_006.operation = 'MULTIPLY'
        except: pass
        try: node_Math_006.use_clamp = False
        except: pass
        try: node_Math_006.inputs[1].default_value = 6.2829999923706055
        except: pass
        try: node_Math_006.inputs[2].default_value = 0.5
        except: pass
        created_nodes['Math.006'] = node_Math_006
        node_Texture_Coordinate_005 = group.nodes.new('ShaderNodeTexCoord')
        node_Texture_Coordinate_005.location_absolute = (-1556.985595703125, -373.0363464355469)
        try: node_Texture_Coordinate_005.location_absolute = Vector((-1556.985595703125, -373.0363464355469))
        except: pass
        try: node_Texture_Coordinate_005.warning_propagation = 'ALL'
        except: pass
        try: node_Texture_Coordinate_005.mute = False
        except: pass
        try: node_Texture_Coordinate_005.bl_label = 'Texture Coordinate'
        except: pass
        try: node_Texture_Coordinate_005.bl_description = 'Retrieve multiple types of texture coordinates.\nTypically used as inputs for texture nodes'
        except: pass
        try: node_Texture_Coordinate_005.bl_icon = 'NONE'
        except: pass
        try: node_Texture_Coordinate_005.bl_width_default = 140.0
        except: pass
        try: node_Texture_Coordinate_005.bl_width_min = 100.0
        except: pass
        try: node_Texture_Coordinate_005.bl_width_max = 700.0
        except: pass
        try: node_Texture_Coordinate_005.bl_height_default = 100.0
        except: pass
        try: node_Texture_Coordinate_005.bl_height_min = 30.0
        except: pass
        try: node_Texture_Coordinate_005.bl_height_max = 30.0
        except: pass
        try: node_Texture_Coordinate_005.object = None
        except: pass
        try: node_Texture_Coordinate_005.from_instancer = False
        except: pass
        created_nodes['Texture Coordinate.005'] = node_Texture_Coordinate_005
        node_Separate_XYZ = group.nodes.new('ShaderNodeSeparateXYZ')
        node_Separate_XYZ.location_absolute = (-1370.9158935546875, -374.49481201171875)
        try: node_Separate_XYZ.location_absolute = Vector((-1370.9158935546875, -374.49481201171875))
        except: pass
        try: node_Separate_XYZ.warning_propagation = 'ALL'
        except: pass
        try: node_Separate_XYZ.mute = False
        except: pass
        try: node_Separate_XYZ.bl_label = 'Separate XYZ'
        except: pass
        try: node_Separate_XYZ.bl_description = 'Split a vector into its X, Y, and Z components'
        except: pass
        try: node_Separate_XYZ.bl_icon = 'NONE'
        except: pass
        try: node_Separate_XYZ.bl_width_default = 140.0
        except: pass
        try: node_Separate_XYZ.bl_width_min = 100.0
        except: pass
        try: node_Separate_XYZ.bl_width_max = 700.0
        except: pass
        try: node_Separate_XYZ.bl_height_default = 100.0
        except: pass
        try: node_Separate_XYZ.bl_height_min = 30.0
        except: pass
        try: node_Separate_XYZ.bl_height_max = 30.0
        except: pass
        created_nodes['Separate XYZ'] = node_Separate_XYZ
        node_Combine_XYZ_003 = group.nodes.new('ShaderNodeCombineXYZ')
        node_Combine_XYZ_003.location_absolute = (-1193.0172119140625, -374.4947509765625)
        try: node_Combine_XYZ_003.location_absolute = Vector((-1193.0172119140625, -374.4947509765625))
        except: pass
        try: node_Combine_XYZ_003.warning_propagation = 'ALL'
        except: pass
        try: node_Combine_XYZ_003.mute = False
        except: pass
        try: node_Combine_XYZ_003.bl_label = 'Combine XYZ'
        except: pass
        try: node_Combine_XYZ_003.bl_description = 'Create a vector from X, Y, and Z components'
        except: pass
        try: node_Combine_XYZ_003.bl_icon = 'NONE'
        except: pass
        try: node_Combine_XYZ_003.bl_width_default = 140.0
        except: pass
        try: node_Combine_XYZ_003.bl_width_min = 100.0
        except: pass
        try: node_Combine_XYZ_003.bl_width_max = 700.0
        except: pass
        try: node_Combine_XYZ_003.bl_height_default = 100.0
        except: pass
        try: node_Combine_XYZ_003.bl_height_min = 30.0
        except: pass
        try: node_Combine_XYZ_003.bl_height_max = 30.0
        except: pass
        try: node_Combine_XYZ_003.inputs[2].default_value = 0.0
        except: pass
        created_nodes['Combine XYZ.003'] = node_Combine_XYZ_003
        node_Frame = group.nodes.new('NodeFrame')
        node_Frame.location_absolute = (-1586.800048828125, -247.1999969482422)
        node_Frame.label = 'X'
        node_Frame.shrink = True
        try: node_Frame.location_absolute = Vector((-1586.800048828125, -247.1999969482422))
        except: pass
        try: node_Frame.warning_propagation = 'ALL'
        except: pass
        try: node_Frame.mute = False
        except: pass
        try: node_Frame.bl_label = 'Frame'
        except: pass
        try: node_Frame.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame.bl_icon = 'NONE'
        except: pass
        try: node_Frame.bl_width_default = 150.0
        except: pass
        try: node_Frame.bl_width_min = 100.0
        except: pass
        try: node_Frame.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame.bl_height_default = 100.0
        except: pass
        try: node_Frame.bl_height_min = 30.0
        except: pass
        try: node_Frame.bl_height_max = 30.0
        except: pass
        try: node_Frame.text = None
        except: pass
        try: node_Frame.shrink = True
        except: pass
        try: node_Frame.label_size = 20
        except: pass
        created_nodes['Frame'] = node_Frame
        node_Mapping_002 = group.nodes.new('ShaderNodeMapping')
        node_Mapping_002.location_absolute = (-4.650198459625244, -867.5562744140625)
        try: node_Mapping_002.location_absolute = Vector((-4.650198459625244, -867.5562744140625))
        except: pass
        try: node_Mapping_002.warning_propagation = 'ALL'
        except: pass
        try: node_Mapping_002.mute = False
        except: pass
        try: node_Mapping_002.bl_label = 'Mapping'
        except: pass
        try: node_Mapping_002.bl_description = 'Transform the input vector by applying translation, rotation, and scale'
        except: pass
        try: node_Mapping_002.bl_icon = 'NONE'
        except: pass
        try: node_Mapping_002.bl_width_default = 140.0
        except: pass
        try: node_Mapping_002.bl_width_min = 100.0
        except: pass
        try: node_Mapping_002.bl_width_max = 700.0
        except: pass
        try: node_Mapping_002.bl_height_default = 100.0
        except: pass
        try: node_Mapping_002.bl_height_min = 30.0
        except: pass
        try: node_Mapping_002.bl_height_max = 30.0
        except: pass
        try: node_Mapping_002.vector_type = 'POINT'
        except: pass
        created_nodes['Mapping.002'] = node_Mapping_002
        node_Vector_Rotate_001 = group.nodes.new('ShaderNodeVectorRotate')
        node_Vector_Rotate_001.location_absolute = (-187.38351440429688, -865.7301025390625)
        try: node_Vector_Rotate_001.location_absolute = Vector((-187.38351440429688, -865.7301025390625))
        except: pass
        try: node_Vector_Rotate_001.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Rotate_001.mute = False
        except: pass
        try: node_Vector_Rotate_001.bl_label = 'Vector Rotate'
        except: pass
        try: node_Vector_Rotate_001.bl_description = 'Rotate a vector around a pivot point (center)'
        except: pass
        try: node_Vector_Rotate_001.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Rotate_001.bl_width_default = 140.0
        except: pass
        try: node_Vector_Rotate_001.bl_width_min = 100.0
        except: pass
        try: node_Vector_Rotate_001.bl_width_max = 700.0
        except: pass
        try: node_Vector_Rotate_001.bl_height_default = 100.0
        except: pass
        try: node_Vector_Rotate_001.bl_height_min = 30.0
        except: pass
        try: node_Vector_Rotate_001.bl_height_max = 30.0
        except: pass
        try: node_Vector_Rotate_001.rotation_type = 'EULER_XYZ'
        except: pass
        try: node_Vector_Rotate_001.invert = False
        except: pass
        try: node_Vector_Rotate_001.inputs[1].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Rotate_001.inputs[2].default_value = [0.0,0.0,0.7000000476837158]
        except: pass
        try: node_Vector_Rotate_001.inputs[3].default_value = 7.084291458129883
        except: pass
        created_nodes['Vector Rotate.001'] = node_Vector_Rotate_001
        node_Combine_XYZ_001 = group.nodes.new('ShaderNodeCombineXYZ')
        node_Combine_XYZ_001.location_absolute = (-382.5143127441406, -1071.7130126953125)
        try: node_Combine_XYZ_001.location_absolute = Vector((-382.5143127441406, -1071.7130126953125))
        except: pass
        try: node_Combine_XYZ_001.warning_propagation = 'ALL'
        except: pass
        try: node_Combine_XYZ_001.mute = False
        except: pass
        try: node_Combine_XYZ_001.bl_label = 'Combine XYZ'
        except: pass
        try: node_Combine_XYZ_001.bl_description = 'Create a vector from X, Y, and Z components'
        except: pass
        try: node_Combine_XYZ_001.bl_icon = 'NONE'
        except: pass
        try: node_Combine_XYZ_001.bl_width_default = 140.0
        except: pass
        try: node_Combine_XYZ_001.bl_width_min = 100.0
        except: pass
        try: node_Combine_XYZ_001.bl_width_max = 700.0
        except: pass
        try: node_Combine_XYZ_001.bl_height_default = 100.0
        except: pass
        try: node_Combine_XYZ_001.bl_height_min = 30.0
        except: pass
        try: node_Combine_XYZ_001.bl_height_max = 30.0
        except: pass
        try: node_Combine_XYZ_001.inputs[0].default_value = 0.0
        except: pass
        try: node_Combine_XYZ_001.inputs[1].default_value = 0.0
        except: pass
        created_nodes['Combine XYZ.001'] = node_Combine_XYZ_001
        node_Voronoi_Texture_004 = group.nodes.new('ShaderNodeTexVoronoi')
        node_Voronoi_Texture_004.location_absolute = (-1004.2161865234375, -1006.6080932617188)
        try: node_Voronoi_Texture_004.location_absolute = Vector((-1004.2161865234375, -1006.6080932617188))
        except: pass
        try: node_Voronoi_Texture_004.warning_propagation = 'ALL'
        except: pass
        try: node_Voronoi_Texture_004.mute = False
        except: pass
        try: node_Voronoi_Texture_004.bl_label = 'Voronoi Texture'
        except: pass
        try: node_Voronoi_Texture_004.bl_description = 'Generate Worley noise based on the distance to random points. Typically used to generate textures such as stones, water, or biological cells'
        except: pass
        try: node_Voronoi_Texture_004.bl_icon = 'NONE'
        except: pass
        try: node_Voronoi_Texture_004.bl_width_default = 155.0
        except: pass
        try: node_Voronoi_Texture_004.bl_width_min = 140.0
        except: pass
        try: node_Voronoi_Texture_004.bl_width_max = 700.0
        except: pass
        try: node_Voronoi_Texture_004.bl_height_default = 100.0
        except: pass
        try: node_Voronoi_Texture_004.bl_height_min = 30.0
        except: pass
        try: node_Voronoi_Texture_004.bl_height_max = 30.0
        except: pass
        try: node_Voronoi_Texture_004.voronoi_dimensions = '2D'
        except: pass
        try: node_Voronoi_Texture_004.distance = 'EUCLIDEAN'
        except: pass
        try: node_Voronoi_Texture_004.feature = 'F1'
        except: pass
        try: node_Voronoi_Texture_004.normalize = False
        except: pass
        try: node_Voronoi_Texture_004.inputs[1].default_value = 0.0
        except: pass
        try: node_Voronoi_Texture_004.inputs[3].default_value = 0.0
        except: pass
        try: node_Voronoi_Texture_004.inputs[4].default_value = 0.6428571343421936
        except: pass
        try: node_Voronoi_Texture_004.inputs[5].default_value = 11.90000057220459
        except: pass
        try: node_Voronoi_Texture_004.inputs[6].default_value = 0.363095223903656
        except: pass
        try: node_Voronoi_Texture_004.inputs[7].default_value = 0.5
        except: pass
        try: node_Voronoi_Texture_004.inputs[8].default_value = 1.0
        except: pass
        created_nodes['Voronoi Texture.004'] = node_Voronoi_Texture_004
        node_Noise_Texture_003 = group.nodes.new('ShaderNodeTexNoise')
        node_Noise_Texture_003.location_absolute = (-773.4273681640625, -1060.162841796875)
        try: node_Noise_Texture_003.location_absolute = Vector((-773.4273681640625, -1060.162841796875))
        except: pass
        try: node_Noise_Texture_003.warning_propagation = 'ALL'
        except: pass
        try: node_Noise_Texture_003.mute = False
        except: pass
        try: node_Noise_Texture_003.bl_label = 'Noise Texture'
        except: pass
        try: node_Noise_Texture_003.bl_description = 'Generate fractal Perlin noise'
        except: pass
        try: node_Noise_Texture_003.bl_icon = 'NONE'
        except: pass
        try: node_Noise_Texture_003.bl_width_default = 145.0
        except: pass
        try: node_Noise_Texture_003.bl_width_min = 140.0
        except: pass
        try: node_Noise_Texture_003.bl_width_max = 700.0
        except: pass
        try: node_Noise_Texture_003.bl_height_default = 100.0
        except: pass
        try: node_Noise_Texture_003.bl_height_min = 30.0
        except: pass
        try: node_Noise_Texture_003.bl_height_max = 30.0
        except: pass
        try: node_Noise_Texture_003.noise_dimensions = '2D'
        except: pass
        try: node_Noise_Texture_003.noise_type = 'FBM'
        except: pass
        try: node_Noise_Texture_003.normalize = False
        except: pass
        try: node_Noise_Texture_003.inputs[1].default_value = 0.0
        except: pass
        try: node_Noise_Texture_003.inputs[2].default_value = 0.5000004768371582
        except: pass
        try: node_Noise_Texture_003.inputs[3].default_value = 2.0
        except: pass
        try: node_Noise_Texture_003.inputs[4].default_value = 0.5
        except: pass
        try: node_Noise_Texture_003.inputs[5].default_value = 2.0
        except: pass
        try: node_Noise_Texture_003.inputs[6].default_value = 0.0
        except: pass
        try: node_Noise_Texture_003.inputs[7].default_value = 1.0
        except: pass
        try: node_Noise_Texture_003.inputs[8].default_value = 0.0
        except: pass
        created_nodes['Noise Texture.003'] = node_Noise_Texture_003
        node_Vector_Math_007 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_007.location_absolute = (-791.4625244140625, -906.5687255859375)
        try: node_Vector_Math_007.location_absolute = Vector((-791.4625244140625, -906.5687255859375))
        except: pass
        try: node_Vector_Math_007.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_007.mute = False
        except: pass
        try: node_Vector_Math_007.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_007.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_007.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_007.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_007.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_007.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_007.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_007.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_007.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_007.operation = 'SUBTRACT'
        except: pass
        try: node_Vector_Math_007.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_007.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.007'] = node_Vector_Math_007
        node_Math_007 = group.nodes.new('ShaderNodeMath')
        node_Math_007.location_absolute = (-572.20361328125, -1066.2607421875)
        try: node_Math_007.location_absolute = Vector((-572.20361328125, -1066.2607421875))
        except: pass
        try: node_Math_007.warning_propagation = 'ALL'
        except: pass
        try: node_Math_007.mute = False
        except: pass
        try: node_Math_007.bl_label = 'Math'
        except: pass
        try: node_Math_007.bl_description = 'Perform math operations'
        except: pass
        try: node_Math_007.bl_icon = 'NONE'
        except: pass
        try: node_Math_007.bl_width_default = 140.0
        except: pass
        try: node_Math_007.bl_width_min = 100.0
        except: pass
        try: node_Math_007.bl_width_max = 700.0
        except: pass
        try: node_Math_007.bl_height_default = 100.0
        except: pass
        try: node_Math_007.bl_height_min = 30.0
        except: pass
        try: node_Math_007.bl_height_max = 30.0
        except: pass
        try: node_Math_007.operation = 'MULTIPLY'
        except: pass
        try: node_Math_007.use_clamp = False
        except: pass
        try: node_Math_007.inputs[1].default_value = 6.2829999923706055
        except: pass
        try: node_Math_007.inputs[2].default_value = 0.5
        except: pass
        created_nodes['Math.007'] = node_Math_007
        node_Texture_Coordinate_006 = group.nodes.new('ShaderNodeTexCoord')
        node_Texture_Coordinate_006.location_absolute = (-1556.9273681640625, -955.3369140625)
        try: node_Texture_Coordinate_006.location_absolute = Vector((-1556.9273681640625, -955.3369140625))
        except: pass
        try: node_Texture_Coordinate_006.warning_propagation = 'ALL'
        except: pass
        try: node_Texture_Coordinate_006.mute = False
        except: pass
        try: node_Texture_Coordinate_006.bl_label = 'Texture Coordinate'
        except: pass
        try: node_Texture_Coordinate_006.bl_description = 'Retrieve multiple types of texture coordinates.\nTypically used as inputs for texture nodes'
        except: pass
        try: node_Texture_Coordinate_006.bl_icon = 'NONE'
        except: pass
        try: node_Texture_Coordinate_006.bl_width_default = 140.0
        except: pass
        try: node_Texture_Coordinate_006.bl_width_min = 100.0
        except: pass
        try: node_Texture_Coordinate_006.bl_width_max = 700.0
        except: pass
        try: node_Texture_Coordinate_006.bl_height_default = 100.0
        except: pass
        try: node_Texture_Coordinate_006.bl_height_min = 30.0
        except: pass
        try: node_Texture_Coordinate_006.bl_height_max = 30.0
        except: pass
        try: node_Texture_Coordinate_006.object = None
        except: pass
        try: node_Texture_Coordinate_006.from_instancer = False
        except: pass
        created_nodes['Texture Coordinate.006'] = node_Texture_Coordinate_006
        node_Separate_XYZ_001 = group.nodes.new('ShaderNodeSeparateXYZ')
        node_Separate_XYZ_001.location_absolute = (-1370.857666015625, -956.7952880859375)
        try: node_Separate_XYZ_001.location_absolute = Vector((-1370.857666015625, -956.7952880859375))
        except: pass
        try: node_Separate_XYZ_001.warning_propagation = 'ALL'
        except: pass
        try: node_Separate_XYZ_001.mute = False
        except: pass
        try: node_Separate_XYZ_001.bl_label = 'Separate XYZ'
        except: pass
        try: node_Separate_XYZ_001.bl_description = 'Split a vector into its X, Y, and Z components'
        except: pass
        try: node_Separate_XYZ_001.bl_icon = 'NONE'
        except: pass
        try: node_Separate_XYZ_001.bl_width_default = 140.0
        except: pass
        try: node_Separate_XYZ_001.bl_width_min = 100.0
        except: pass
        try: node_Separate_XYZ_001.bl_width_max = 700.0
        except: pass
        try: node_Separate_XYZ_001.bl_height_default = 100.0
        except: pass
        try: node_Separate_XYZ_001.bl_height_min = 30.0
        except: pass
        try: node_Separate_XYZ_001.bl_height_max = 30.0
        except: pass
        created_nodes['Separate XYZ.001'] = node_Separate_XYZ_001
        node_Combine_XYZ_004 = group.nodes.new('ShaderNodeCombineXYZ')
        node_Combine_XYZ_004.location_absolute = (-1192.958740234375, -956.7952880859375)
        try: node_Combine_XYZ_004.location_absolute = Vector((-1192.958740234375, -956.7952880859375))
        except: pass
        try: node_Combine_XYZ_004.warning_propagation = 'ALL'
        except: pass
        try: node_Combine_XYZ_004.mute = False
        except: pass
        try: node_Combine_XYZ_004.bl_label = 'Combine XYZ'
        except: pass
        try: node_Combine_XYZ_004.bl_description = 'Create a vector from X, Y, and Z components'
        except: pass
        try: node_Combine_XYZ_004.bl_icon = 'NONE'
        except: pass
        try: node_Combine_XYZ_004.bl_width_default = 140.0
        except: pass
        try: node_Combine_XYZ_004.bl_width_min = 100.0
        except: pass
        try: node_Combine_XYZ_004.bl_width_max = 700.0
        except: pass
        try: node_Combine_XYZ_004.bl_height_default = 100.0
        except: pass
        try: node_Combine_XYZ_004.bl_height_min = 30.0
        except: pass
        try: node_Combine_XYZ_004.bl_height_max = 30.0
        except: pass
        try: node_Combine_XYZ_004.inputs[2].default_value = 0.0
        except: pass
        created_nodes['Combine XYZ.004'] = node_Combine_XYZ_004
        node_Frame_001 = group.nodes.new('NodeFrame')
        node_Frame_001.location_absolute = (-1586.800048828125, -829.5999755859375)
        node_Frame_001.label = 'Y'
        node_Frame_001.shrink = True
        try: node_Frame_001.location_absolute = Vector((-1586.800048828125, -829.5999755859375))
        except: pass
        try: node_Frame_001.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_001.mute = False
        except: pass
        try: node_Frame_001.bl_label = 'Frame'
        except: pass
        try: node_Frame_001.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_001.bl_icon = 'NONE'
        except: pass
        try: node_Frame_001.bl_width_default = 150.0
        except: pass
        try: node_Frame_001.bl_width_min = 100.0
        except: pass
        try: node_Frame_001.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_001.bl_height_default = 100.0
        except: pass
        try: node_Frame_001.bl_height_min = 30.0
        except: pass
        try: node_Frame_001.bl_height_max = 30.0
        except: pass
        try: node_Frame_001.text = None
        except: pass
        try: node_Frame_001.shrink = True
        except: pass
        try: node_Frame_001.label_size = 20
        except: pass
        created_nodes['Frame.001'] = node_Frame_001
        node_Mapping_003 = group.nodes.new('ShaderNodeMapping')
        node_Mapping_003.location_absolute = (4.057916164398193, -1476.433349609375)
        try: node_Mapping_003.location_absolute = Vector((4.057916164398193, -1476.433349609375))
        except: pass
        try: node_Mapping_003.warning_propagation = 'ALL'
        except: pass
        try: node_Mapping_003.mute = False
        except: pass
        try: node_Mapping_003.bl_label = 'Mapping'
        except: pass
        try: node_Mapping_003.bl_description = 'Transform the input vector by applying translation, rotation, and scale'
        except: pass
        try: node_Mapping_003.bl_icon = 'NONE'
        except: pass
        try: node_Mapping_003.bl_width_default = 140.0
        except: pass
        try: node_Mapping_003.bl_width_min = 100.0
        except: pass
        try: node_Mapping_003.bl_width_max = 700.0
        except: pass
        try: node_Mapping_003.bl_height_default = 100.0
        except: pass
        try: node_Mapping_003.bl_height_min = 30.0
        except: pass
        try: node_Mapping_003.bl_height_max = 30.0
        except: pass
        try: node_Mapping_003.vector_type = 'POINT'
        except: pass
        created_nodes['Mapping.003'] = node_Mapping_003
        node_Vector_Rotate_002 = group.nodes.new('ShaderNodeVectorRotate')
        node_Vector_Rotate_002.location_absolute = (-178.67538452148438, -1474.607177734375)
        try: node_Vector_Rotate_002.location_absolute = Vector((-178.67538452148438, -1474.607177734375))
        except: pass
        try: node_Vector_Rotate_002.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Rotate_002.mute = False
        except: pass
        try: node_Vector_Rotate_002.bl_label = 'Vector Rotate'
        except: pass
        try: node_Vector_Rotate_002.bl_description = 'Rotate a vector around a pivot point (center)'
        except: pass
        try: node_Vector_Rotate_002.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Rotate_002.bl_width_default = 140.0
        except: pass
        try: node_Vector_Rotate_002.bl_width_min = 100.0
        except: pass
        try: node_Vector_Rotate_002.bl_width_max = 700.0
        except: pass
        try: node_Vector_Rotate_002.bl_height_default = 100.0
        except: pass
        try: node_Vector_Rotate_002.bl_height_min = 30.0
        except: pass
        try: node_Vector_Rotate_002.bl_height_max = 30.0
        except: pass
        try: node_Vector_Rotate_002.rotation_type = 'EULER_XYZ'
        except: pass
        try: node_Vector_Rotate_002.invert = False
        except: pass
        try: node_Vector_Rotate_002.inputs[1].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Rotate_002.inputs[2].default_value = [0.0,0.0,0.7000000476837158]
        except: pass
        try: node_Vector_Rotate_002.inputs[3].default_value = 7.084291458129883
        except: pass
        created_nodes['Vector Rotate.002'] = node_Vector_Rotate_002
        node_Combine_XYZ_002 = group.nodes.new('ShaderNodeCombineXYZ')
        node_Combine_XYZ_002.location_absolute = (-373.8061218261719, -1680.590087890625)
        try: node_Combine_XYZ_002.location_absolute = Vector((-373.8061218261719, -1680.590087890625))
        except: pass
        try: node_Combine_XYZ_002.warning_propagation = 'ALL'
        except: pass
        try: node_Combine_XYZ_002.mute = False
        except: pass
        try: node_Combine_XYZ_002.bl_label = 'Combine XYZ'
        except: pass
        try: node_Combine_XYZ_002.bl_description = 'Create a vector from X, Y, and Z components'
        except: pass
        try: node_Combine_XYZ_002.bl_icon = 'NONE'
        except: pass
        try: node_Combine_XYZ_002.bl_width_default = 140.0
        except: pass
        try: node_Combine_XYZ_002.bl_width_min = 100.0
        except: pass
        try: node_Combine_XYZ_002.bl_width_max = 700.0
        except: pass
        try: node_Combine_XYZ_002.bl_height_default = 100.0
        except: pass
        try: node_Combine_XYZ_002.bl_height_min = 30.0
        except: pass
        try: node_Combine_XYZ_002.bl_height_max = 30.0
        except: pass
        try: node_Combine_XYZ_002.inputs[0].default_value = 0.0
        except: pass
        try: node_Combine_XYZ_002.inputs[1].default_value = 0.0
        except: pass
        created_nodes['Combine XYZ.002'] = node_Combine_XYZ_002
        node_Voronoi_Texture_005 = group.nodes.new('ShaderNodeTexVoronoi')
        node_Voronoi_Texture_005.location_absolute = (-995.5081787109375, -1615.485107421875)
        try: node_Voronoi_Texture_005.location_absolute = Vector((-995.5081787109375, -1615.485107421875))
        except: pass
        try: node_Voronoi_Texture_005.warning_propagation = 'ALL'
        except: pass
        try: node_Voronoi_Texture_005.mute = False
        except: pass
        try: node_Voronoi_Texture_005.bl_label = 'Voronoi Texture'
        except: pass
        try: node_Voronoi_Texture_005.bl_description = 'Generate Worley noise based on the distance to random points. Typically used to generate textures such as stones, water, or biological cells'
        except: pass
        try: node_Voronoi_Texture_005.bl_icon = 'NONE'
        except: pass
        try: node_Voronoi_Texture_005.bl_width_default = 155.0
        except: pass
        try: node_Voronoi_Texture_005.bl_width_min = 140.0
        except: pass
        try: node_Voronoi_Texture_005.bl_width_max = 700.0
        except: pass
        try: node_Voronoi_Texture_005.bl_height_default = 100.0
        except: pass
        try: node_Voronoi_Texture_005.bl_height_min = 30.0
        except: pass
        try: node_Voronoi_Texture_005.bl_height_max = 30.0
        except: pass
        try: node_Voronoi_Texture_005.voronoi_dimensions = '2D'
        except: pass
        try: node_Voronoi_Texture_005.distance = 'EUCLIDEAN'
        except: pass
        try: node_Voronoi_Texture_005.feature = 'F1'
        except: pass
        try: node_Voronoi_Texture_005.normalize = False
        except: pass
        try: node_Voronoi_Texture_005.inputs[1].default_value = 0.0
        except: pass
        try: node_Voronoi_Texture_005.inputs[3].default_value = 0.0
        except: pass
        try: node_Voronoi_Texture_005.inputs[4].default_value = 0.6428571343421936
        except: pass
        try: node_Voronoi_Texture_005.inputs[5].default_value = 11.90000057220459
        except: pass
        try: node_Voronoi_Texture_005.inputs[6].default_value = 0.363095223903656
        except: pass
        try: node_Voronoi_Texture_005.inputs[7].default_value = 0.5
        except: pass
        try: node_Voronoi_Texture_005.inputs[8].default_value = 1.0
        except: pass
        created_nodes['Voronoi Texture.005'] = node_Voronoi_Texture_005
        node_Noise_Texture_004 = group.nodes.new('ShaderNodeTexNoise')
        node_Noise_Texture_004.location_absolute = (-764.7193603515625, -1669.040283203125)
        try: node_Noise_Texture_004.location_absolute = Vector((-764.7193603515625, -1669.040283203125))
        except: pass
        try: node_Noise_Texture_004.warning_propagation = 'ALL'
        except: pass
        try: node_Noise_Texture_004.mute = False
        except: pass
        try: node_Noise_Texture_004.bl_label = 'Noise Texture'
        except: pass
        try: node_Noise_Texture_004.bl_description = 'Generate fractal Perlin noise'
        except: pass
        try: node_Noise_Texture_004.bl_icon = 'NONE'
        except: pass
        try: node_Noise_Texture_004.bl_width_default = 145.0
        except: pass
        try: node_Noise_Texture_004.bl_width_min = 140.0
        except: pass
        try: node_Noise_Texture_004.bl_width_max = 700.0
        except: pass
        try: node_Noise_Texture_004.bl_height_default = 100.0
        except: pass
        try: node_Noise_Texture_004.bl_height_min = 30.0
        except: pass
        try: node_Noise_Texture_004.bl_height_max = 30.0
        except: pass
        try: node_Noise_Texture_004.noise_dimensions = '2D'
        except: pass
        try: node_Noise_Texture_004.noise_type = 'FBM'
        except: pass
        try: node_Noise_Texture_004.normalize = False
        except: pass
        try: node_Noise_Texture_004.inputs[1].default_value = 0.0
        except: pass
        try: node_Noise_Texture_004.inputs[2].default_value = 0.5000004768371582
        except: pass
        try: node_Noise_Texture_004.inputs[3].default_value = 2.0
        except: pass
        try: node_Noise_Texture_004.inputs[4].default_value = 0.5
        except: pass
        try: node_Noise_Texture_004.inputs[5].default_value = 2.0
        except: pass
        try: node_Noise_Texture_004.inputs[6].default_value = 0.0
        except: pass
        try: node_Noise_Texture_004.inputs[7].default_value = 1.0
        except: pass
        try: node_Noise_Texture_004.inputs[8].default_value = 0.0
        except: pass
        created_nodes['Noise Texture.004'] = node_Noise_Texture_004
        node_Vector_Math_008 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_008.location_absolute = (-782.7543334960938, -1515.4456787109375)
        try: node_Vector_Math_008.location_absolute = Vector((-782.7543334960938, -1515.4456787109375))
        except: pass
        try: node_Vector_Math_008.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_008.mute = False
        except: pass
        try: node_Vector_Math_008.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_008.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_008.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_008.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_008.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_008.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_008.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_008.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_008.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_008.operation = 'SUBTRACT'
        except: pass
        try: node_Vector_Math_008.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_008.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.008'] = node_Vector_Math_008
        node_Math_008 = group.nodes.new('ShaderNodeMath')
        node_Math_008.location_absolute = (-563.4954833984375, -1675.137939453125)
        try: node_Math_008.location_absolute = Vector((-563.4954833984375, -1675.137939453125))
        except: pass
        try: node_Math_008.warning_propagation = 'ALL'
        except: pass
        try: node_Math_008.mute = False
        except: pass
        try: node_Math_008.bl_label = 'Math'
        except: pass
        try: node_Math_008.bl_description = 'Perform math operations'
        except: pass
        try: node_Math_008.bl_icon = 'NONE'
        except: pass
        try: node_Math_008.bl_width_default = 140.0
        except: pass
        try: node_Math_008.bl_width_min = 100.0
        except: pass
        try: node_Math_008.bl_width_max = 700.0
        except: pass
        try: node_Math_008.bl_height_default = 100.0
        except: pass
        try: node_Math_008.bl_height_min = 30.0
        except: pass
        try: node_Math_008.bl_height_max = 30.0
        except: pass
        try: node_Math_008.operation = 'MULTIPLY'
        except: pass
        try: node_Math_008.use_clamp = False
        except: pass
        try: node_Math_008.inputs[1].default_value = 6.2829999923706055
        except: pass
        try: node_Math_008.inputs[2].default_value = 0.5
        except: pass
        created_nodes['Math.008'] = node_Math_008
        node_Texture_Coordinate_007 = group.nodes.new('ShaderNodeTexCoord')
        node_Texture_Coordinate_007.location_absolute = (-1548.218994140625, -1564.2139892578125)
        try: node_Texture_Coordinate_007.location_absolute = Vector((-1548.218994140625, -1564.2139892578125))
        except: pass
        try: node_Texture_Coordinate_007.warning_propagation = 'ALL'
        except: pass
        try: node_Texture_Coordinate_007.mute = False
        except: pass
        try: node_Texture_Coordinate_007.bl_label = 'Texture Coordinate'
        except: pass
        try: node_Texture_Coordinate_007.bl_description = 'Retrieve multiple types of texture coordinates.\nTypically used as inputs for texture nodes'
        except: pass
        try: node_Texture_Coordinate_007.bl_icon = 'NONE'
        except: pass
        try: node_Texture_Coordinate_007.bl_width_default = 140.0
        except: pass
        try: node_Texture_Coordinate_007.bl_width_min = 100.0
        except: pass
        try: node_Texture_Coordinate_007.bl_width_max = 700.0
        except: pass
        try: node_Texture_Coordinate_007.bl_height_default = 100.0
        except: pass
        try: node_Texture_Coordinate_007.bl_height_min = 30.0
        except: pass
        try: node_Texture_Coordinate_007.bl_height_max = 30.0
        except: pass
        try: node_Texture_Coordinate_007.object = None
        except: pass
        try: node_Texture_Coordinate_007.from_instancer = False
        except: pass
        created_nodes['Texture Coordinate.007'] = node_Texture_Coordinate_007
        node_Separate_XYZ_003 = group.nodes.new('ShaderNodeSeparateXYZ')
        node_Separate_XYZ_003.location_absolute = (-1362.149658203125, -1565.67236328125)
        try: node_Separate_XYZ_003.location_absolute = Vector((-1362.149658203125, -1565.67236328125))
        except: pass
        try: node_Separate_XYZ_003.warning_propagation = 'ALL'
        except: pass
        try: node_Separate_XYZ_003.mute = False
        except: pass
        try: node_Separate_XYZ_003.bl_label = 'Separate XYZ'
        except: pass
        try: node_Separate_XYZ_003.bl_description = 'Split a vector into its X, Y, and Z components'
        except: pass
        try: node_Separate_XYZ_003.bl_icon = 'NONE'
        except: pass
        try: node_Separate_XYZ_003.bl_width_default = 140.0
        except: pass
        try: node_Separate_XYZ_003.bl_width_min = 100.0
        except: pass
        try: node_Separate_XYZ_003.bl_width_max = 700.0
        except: pass
        try: node_Separate_XYZ_003.bl_height_default = 100.0
        except: pass
        try: node_Separate_XYZ_003.bl_height_min = 30.0
        except: pass
        try: node_Separate_XYZ_003.bl_height_max = 30.0
        except: pass
        created_nodes['Separate XYZ.003'] = node_Separate_XYZ_003
        node_Combine_XYZ_005 = group.nodes.new('ShaderNodeCombineXYZ')
        node_Combine_XYZ_005.location_absolute = (-1184.2509765625, -1565.67236328125)
        try: node_Combine_XYZ_005.location_absolute = Vector((-1184.2509765625, -1565.67236328125))
        except: pass
        try: node_Combine_XYZ_005.warning_propagation = 'ALL'
        except: pass
        try: node_Combine_XYZ_005.mute = False
        except: pass
        try: node_Combine_XYZ_005.bl_label = 'Combine XYZ'
        except: pass
        try: node_Combine_XYZ_005.bl_description = 'Create a vector from X, Y, and Z components'
        except: pass
        try: node_Combine_XYZ_005.bl_icon = 'NONE'
        except: pass
        try: node_Combine_XYZ_005.bl_width_default = 140.0
        except: pass
        try: node_Combine_XYZ_005.bl_width_min = 100.0
        except: pass
        try: node_Combine_XYZ_005.bl_width_max = 700.0
        except: pass
        try: node_Combine_XYZ_005.bl_height_default = 100.0
        except: pass
        try: node_Combine_XYZ_005.bl_height_min = 30.0
        except: pass
        try: node_Combine_XYZ_005.bl_height_max = 30.0
        except: pass
        try: node_Combine_XYZ_005.inputs[2].default_value = 0.0
        except: pass
        created_nodes['Combine XYZ.005'] = node_Combine_XYZ_005
        node_Frame_002 = group.nodes.new('NodeFrame')
        node_Frame_002.location_absolute = (-1578.0, -1432.0)
        node_Frame_002.label = 'Z'
        node_Frame_002.shrink = True
        try: node_Frame_002.location_absolute = Vector((-1578.0, -1432.0))
        except: pass
        try: node_Frame_002.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_002.mute = False
        except: pass
        try: node_Frame_002.bl_label = 'Frame'
        except: pass
        try: node_Frame_002.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_002.bl_icon = 'NONE'
        except: pass
        try: node_Frame_002.bl_width_default = 150.0
        except: pass
        try: node_Frame_002.bl_width_min = 100.0
        except: pass
        try: node_Frame_002.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_002.bl_height_default = 100.0
        except: pass
        try: node_Frame_002.bl_height_min = 30.0
        except: pass
        try: node_Frame_002.bl_height_max = 30.0
        except: pass
        try: node_Frame_002.text = None
        except: pass
        try: node_Frame_002.shrink = True
        except: pass
        try: node_Frame_002.label_size = 20
        except: pass
        created_nodes['Frame.002'] = node_Frame_002
        node_Texture_Coordinate_003 = group.nodes.new('ShaderNodeTexCoord')
        node_Texture_Coordinate_003.location_absolute = (-474.2916564941406, 171.8564453125)
        try: node_Texture_Coordinate_003.location_absolute = Vector((-474.2916564941406, 171.8564453125))
        except: pass
        try: node_Texture_Coordinate_003.warning_propagation = 'ALL'
        except: pass
        try: node_Texture_Coordinate_003.mute = False
        except: pass
        try: node_Texture_Coordinate_003.bl_label = 'Texture Coordinate'
        except: pass
        try: node_Texture_Coordinate_003.bl_description = 'Retrieve multiple types of texture coordinates.\nTypically used as inputs for texture nodes'
        except: pass
        try: node_Texture_Coordinate_003.bl_icon = 'NONE'
        except: pass
        try: node_Texture_Coordinate_003.bl_width_default = 140.0
        except: pass
        try: node_Texture_Coordinate_003.bl_width_min = 100.0
        except: pass
        try: node_Texture_Coordinate_003.bl_width_max = 700.0
        except: pass
        try: node_Texture_Coordinate_003.bl_height_default = 100.0
        except: pass
        try: node_Texture_Coordinate_003.bl_height_min = 30.0
        except: pass
        try: node_Texture_Coordinate_003.bl_height_max = 30.0
        except: pass
        try: node_Texture_Coordinate_003.object = None
        except: pass
        try: node_Texture_Coordinate_003.from_instancer = False
        except: pass
        created_nodes['Texture Coordinate.003'] = node_Texture_Coordinate_003
        node_Frame_003 = group.nodes.new('NodeFrame')
        node_Frame_003.location_absolute = (-504.3999938964844, 299.6000061035156)
        node_Frame_003.shrink = True
        try: node_Frame_003.location_absolute = Vector((-504.3999938964844, 299.6000061035156))
        except: pass
        try: node_Frame_003.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_003.mute = False
        except: pass
        try: node_Frame_003.bl_label = 'Frame'
        except: pass
        try: node_Frame_003.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_003.bl_icon = 'NONE'
        except: pass
        try: node_Frame_003.bl_width_default = 150.0
        except: pass
        try: node_Frame_003.bl_width_min = 100.0
        except: pass
        try: node_Frame_003.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_003.bl_height_default = 100.0
        except: pass
        try: node_Frame_003.bl_height_min = 30.0
        except: pass
        try: node_Frame_003.bl_height_max = 30.0
        except: pass
        try: node_Frame_003.text = None
        except: pass
        try: node_Frame_003.shrink = True
        except: pass
        try: node_Frame_003.label_size = 20
        except: pass
        created_nodes['Frame.003'] = node_Frame_003
        node_Combine_XYZ_006 = group.nodes.new('ShaderNodeCombineXYZ')
        node_Combine_XYZ_006.location_absolute = (-126.9717788696289, 532.7435302734375)
        try: node_Combine_XYZ_006.location_absolute = Vector((-126.9717788696289, 532.7435302734375))
        except: pass
        try: node_Combine_XYZ_006.warning_propagation = 'ALL'
        except: pass
        try: node_Combine_XYZ_006.mute = False
        except: pass
        try: node_Combine_XYZ_006.bl_label = 'Combine XYZ'
        except: pass
        try: node_Combine_XYZ_006.bl_description = 'Create a vector from X, Y, and Z components'
        except: pass
        try: node_Combine_XYZ_006.bl_icon = 'NONE'
        except: pass
        try: node_Combine_XYZ_006.bl_width_default = 140.0
        except: pass
        try: node_Combine_XYZ_006.bl_width_min = 100.0
        except: pass
        try: node_Combine_XYZ_006.bl_width_max = 700.0
        except: pass
        try: node_Combine_XYZ_006.bl_height_default = 100.0
        except: pass
        try: node_Combine_XYZ_006.bl_height_min = 30.0
        except: pass
        try: node_Combine_XYZ_006.bl_height_max = 30.0
        except: pass
        try: node_Combine_XYZ_006.inputs[2].default_value = 0.0
        except: pass
        created_nodes['Combine XYZ.006'] = node_Combine_XYZ_006
        node_Separate_XYZ_004 = group.nodes.new('ShaderNodeSeparateXYZ')
        node_Separate_XYZ_004.location_absolute = (-319.1066589355469, 531.8524169921875)
        try: node_Separate_XYZ_004.location_absolute = Vector((-319.1066589355469, 531.8524169921875))
        except: pass
        try: node_Separate_XYZ_004.warning_propagation = 'ALL'
        except: pass
        try: node_Separate_XYZ_004.mute = False
        except: pass
        try: node_Separate_XYZ_004.bl_label = 'Separate XYZ'
        except: pass
        try: node_Separate_XYZ_004.bl_description = 'Split a vector into its X, Y, and Z components'
        except: pass
        try: node_Separate_XYZ_004.bl_icon = 'NONE'
        except: pass
        try: node_Separate_XYZ_004.bl_width_default = 140.0
        except: pass
        try: node_Separate_XYZ_004.bl_width_min = 100.0
        except: pass
        try: node_Separate_XYZ_004.bl_width_max = 700.0
        except: pass
        try: node_Separate_XYZ_004.bl_height_default = 100.0
        except: pass
        try: node_Separate_XYZ_004.bl_height_min = 30.0
        except: pass
        try: node_Separate_XYZ_004.bl_height_max = 30.0
        except: pass
        created_nodes['Separate XYZ.004'] = node_Separate_XYZ_004
        node_Frame_004 = group.nodes.new('NodeFrame')
        node_Frame_004.location_absolute = (-1616.800048828125, -217.1999969482422)
        node_Frame_004.shrink = True
        try: node_Frame_004.location_absolute = Vector((-1616.800048828125, -217.1999969482422))
        except: pass
        try: node_Frame_004.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_004.mute = False
        except: pass
        try: node_Frame_004.bl_label = 'Frame'
        except: pass
        try: node_Frame_004.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_004.bl_icon = 'NONE'
        except: pass
        try: node_Frame_004.bl_width_default = 150.0
        except: pass
        try: node_Frame_004.bl_width_min = 100.0
        except: pass
        try: node_Frame_004.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_004.bl_height_default = 100.0
        except: pass
        try: node_Frame_004.bl_height_min = 30.0
        except: pass
        try: node_Frame_004.bl_height_max = 30.0
        except: pass
        try: node_Frame_004.text = None
        except: pass
        try: node_Frame_004.shrink = True
        except: pass
        try: node_Frame_004.label_size = 20
        except: pass
        created_nodes['Frame.004'] = node_Frame_004
        node_Frame_005 = group.nodes.new('NodeFrame')
        node_Frame_005.location_absolute = (-531.5999755859375, 616.7999877929688)
        node_Frame_005.label = 'Z'
        node_Frame_005.shrink = True
        try: node_Frame_005.location_absolute = Vector((-531.5999755859375, 616.7999877929688))
        except: pass
        try: node_Frame_005.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_005.mute = False
        except: pass
        try: node_Frame_005.bl_label = 'Frame'
        except: pass
        try: node_Frame_005.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_005.bl_icon = 'NONE'
        except: pass
        try: node_Frame_005.bl_width_default = 150.0
        except: pass
        try: node_Frame_005.bl_width_min = 100.0
        except: pass
        try: node_Frame_005.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_005.bl_height_default = 100.0
        except: pass
        try: node_Frame_005.bl_height_min = 30.0
        except: pass
        try: node_Frame_005.bl_height_max = 30.0
        except: pass
        try: node_Frame_005.text = None
        except: pass
        try: node_Frame_005.shrink = True
        except: pass
        try: node_Frame_005.label_size = 20
        except: pass
        created_nodes['Frame.005'] = node_Frame_005
        node_Texture_Coordinate_004 = group.nodes.new('ShaderNodeTexCoord')
        node_Texture_Coordinate_004.location_absolute = (-515.59033203125, 912.5919799804688)
        try: node_Texture_Coordinate_004.location_absolute = Vector((-515.59033203125, 912.5919799804688))
        except: pass
        try: node_Texture_Coordinate_004.warning_propagation = 'ALL'
        except: pass
        try: node_Texture_Coordinate_004.mute = False
        except: pass
        try: node_Texture_Coordinate_004.bl_label = 'Texture Coordinate'
        except: pass
        try: node_Texture_Coordinate_004.bl_description = 'Retrieve multiple types of texture coordinates.\nTypically used as inputs for texture nodes'
        except: pass
        try: node_Texture_Coordinate_004.bl_icon = 'NONE'
        except: pass
        try: node_Texture_Coordinate_004.bl_width_default = 140.0
        except: pass
        try: node_Texture_Coordinate_004.bl_width_min = 100.0
        except: pass
        try: node_Texture_Coordinate_004.bl_width_max = 700.0
        except: pass
        try: node_Texture_Coordinate_004.bl_height_default = 100.0
        except: pass
        try: node_Texture_Coordinate_004.bl_height_min = 30.0
        except: pass
        try: node_Texture_Coordinate_004.bl_height_max = 30.0
        except: pass
        try: node_Texture_Coordinate_004.object = None
        except: pass
        try: node_Texture_Coordinate_004.from_instancer = False
        except: pass
        created_nodes['Texture Coordinate.004'] = node_Texture_Coordinate_004
        node_Voronoi_Texture_002 = group.nodes.new('ShaderNodeTexVoronoi')
        node_Voronoi_Texture_002.location_absolute = (43.781951904296875, 935.8857421875)
        try: node_Voronoi_Texture_002.location_absolute = Vector((43.781951904296875, 935.8857421875))
        except: pass
        try: node_Voronoi_Texture_002.warning_propagation = 'ALL'
        except: pass
        try: node_Voronoi_Texture_002.mute = False
        except: pass
        try: node_Voronoi_Texture_002.bl_label = 'Voronoi Texture'
        except: pass
        try: node_Voronoi_Texture_002.bl_description = 'Generate Worley noise based on the distance to random points. Typically used to generate textures such as stones, water, or biological cells'
        except: pass
        try: node_Voronoi_Texture_002.bl_icon = 'NONE'
        except: pass
        try: node_Voronoi_Texture_002.bl_width_default = 155.0
        except: pass
        try: node_Voronoi_Texture_002.bl_width_min = 140.0
        except: pass
        try: node_Voronoi_Texture_002.bl_width_max = 700.0
        except: pass
        try: node_Voronoi_Texture_002.bl_height_default = 100.0
        except: pass
        try: node_Voronoi_Texture_002.bl_height_min = 30.0
        except: pass
        try: node_Voronoi_Texture_002.bl_height_max = 30.0
        except: pass
        try: node_Voronoi_Texture_002.voronoi_dimensions = '2D'
        except: pass
        try: node_Voronoi_Texture_002.distance = 'EUCLIDEAN'
        except: pass
        try: node_Voronoi_Texture_002.feature = 'DISTANCE_TO_EDGE'
        except: pass
        try: node_Voronoi_Texture_002.normalize = False
        except: pass
        try: node_Voronoi_Texture_002.inputs[1].default_value = 0.0
        except: pass
        try: node_Voronoi_Texture_002.inputs[3].default_value = 0.0
        except: pass
        try: node_Voronoi_Texture_002.inputs[4].default_value = 1.0
        except: pass
        try: node_Voronoi_Texture_002.inputs[5].default_value = 2.100001335144043
        except: pass
        try: node_Voronoi_Texture_002.inputs[6].default_value = 0.363095223903656
        except: pass
        try: node_Voronoi_Texture_002.inputs[7].default_value = 0.5
        except: pass
        try: node_Voronoi_Texture_002.inputs[8].default_value = 1.0
        except: pass
        created_nodes['Voronoi Texture.002'] = node_Voronoi_Texture_002
        node_Map_Range_001 = group.nodes.new('ShaderNodeMapRange')
        node_Map_Range_001.location_absolute = (304.21734619140625, 935.7255859375)
        try: node_Map_Range_001.location_absolute = Vector((304.21734619140625, 935.7255859375))
        except: pass
        try: node_Map_Range_001.warning_propagation = 'ALL'
        except: pass
        try: node_Map_Range_001.mute = False
        except: pass
        try: node_Map_Range_001.bl_label = 'Map Range'
        except: pass
        try: node_Map_Range_001.bl_description = 'Remap a value from a range to a target range'
        except: pass
        try: node_Map_Range_001.bl_icon = 'NONE'
        except: pass
        try: node_Map_Range_001.bl_width_default = 140.0
        except: pass
        try: node_Map_Range_001.bl_width_min = 100.0
        except: pass
        try: node_Map_Range_001.bl_width_max = 700.0
        except: pass
        try: node_Map_Range_001.bl_height_default = 100.0
        except: pass
        try: node_Map_Range_001.bl_height_min = 30.0
        except: pass
        try: node_Map_Range_001.bl_height_max = 30.0
        except: pass
        try: node_Map_Range_001.clamp = True
        except: pass
        try: node_Map_Range_001.interpolation_type = 'LINEAR'
        except: pass
        try: node_Map_Range_001.data_type = 'FLOAT'
        except: pass
        try: node_Map_Range_001.inputs[1].default_value = 0.0
        except: pass
        try: node_Map_Range_001.inputs[3].default_value = 0.0
        except: pass
        try: node_Map_Range_001.inputs[4].default_value = 1.0
        except: pass
        try: node_Map_Range_001.inputs[5].default_value = 4.0
        except: pass
        try: node_Map_Range_001.inputs[6].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Map_Range_001.inputs[7].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Map_Range_001.inputs[8].default_value = [1.0,1.0,1.0]
        except: pass
        try: node_Map_Range_001.inputs[9].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Map_Range_001.inputs[10].default_value = [1.0,1.0,1.0]
        except: pass
        try: node_Map_Range_001.inputs[11].default_value = [4.0,4.0,4.0]
        except: pass
        created_nodes['Map Range.001'] = node_Map_Range_001
        node_Combine_XYZ_007 = group.nodes.new('ShaderNodeCombineXYZ')
        node_Combine_XYZ_007.location_absolute = (-140.80545043945312, 888.0368041992188)
        try: node_Combine_XYZ_007.location_absolute = Vector((-140.80545043945312, 888.0368041992188))
        except: pass
        try: node_Combine_XYZ_007.warning_propagation = 'ALL'
        except: pass
        try: node_Combine_XYZ_007.mute = False
        except: pass
        try: node_Combine_XYZ_007.bl_label = 'Combine XYZ'
        except: pass
        try: node_Combine_XYZ_007.bl_description = 'Create a vector from X, Y, and Z components'
        except: pass
        try: node_Combine_XYZ_007.bl_icon = 'NONE'
        except: pass
        try: node_Combine_XYZ_007.bl_width_default = 140.0
        except: pass
        try: node_Combine_XYZ_007.bl_width_min = 100.0
        except: pass
        try: node_Combine_XYZ_007.bl_width_max = 700.0
        except: pass
        try: node_Combine_XYZ_007.bl_height_default = 100.0
        except: pass
        try: node_Combine_XYZ_007.bl_height_min = 30.0
        except: pass
        try: node_Combine_XYZ_007.bl_height_max = 30.0
        except: pass
        try: node_Combine_XYZ_007.inputs[2].default_value = 0.0
        except: pass
        created_nodes['Combine XYZ.007'] = node_Combine_XYZ_007
        node_Separate_XYZ_005 = group.nodes.new('ShaderNodeSeparateXYZ')
        node_Separate_XYZ_005.location_absolute = (-332.9403381347656, 887.1456909179688)
        try: node_Separate_XYZ_005.location_absolute = Vector((-332.9403381347656, 887.1456909179688))
        except: pass
        try: node_Separate_XYZ_005.warning_propagation = 'ALL'
        except: pass
        try: node_Separate_XYZ_005.mute = False
        except: pass
        try: node_Separate_XYZ_005.bl_label = 'Separate XYZ'
        except: pass
        try: node_Separate_XYZ_005.bl_description = 'Split a vector into its X, Y, and Z components'
        except: pass
        try: node_Separate_XYZ_005.bl_icon = 'NONE'
        except: pass
        try: node_Separate_XYZ_005.bl_width_default = 140.0
        except: pass
        try: node_Separate_XYZ_005.bl_width_min = 100.0
        except: pass
        try: node_Separate_XYZ_005.bl_width_max = 700.0
        except: pass
        try: node_Separate_XYZ_005.bl_height_default = 100.0
        except: pass
        try: node_Separate_XYZ_005.bl_height_min = 30.0
        except: pass
        try: node_Separate_XYZ_005.bl_height_max = 30.0
        except: pass
        created_nodes['Separate XYZ.005'] = node_Separate_XYZ_005
        node_Frame_006 = group.nodes.new('NodeFrame')
        node_Frame_006.location_absolute = (-545.2000122070312, 972.0)
        node_Frame_006.label = 'Y'
        node_Frame_006.shrink = True
        try: node_Frame_006.location_absolute = Vector((-545.2000122070312, 972.0))
        except: pass
        try: node_Frame_006.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_006.mute = False
        except: pass
        try: node_Frame_006.bl_label = 'Frame'
        except: pass
        try: node_Frame_006.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_006.bl_icon = 'NONE'
        except: pass
        try: node_Frame_006.bl_width_default = 150.0
        except: pass
        try: node_Frame_006.bl_width_min = 100.0
        except: pass
        try: node_Frame_006.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_006.bl_height_default = 100.0
        except: pass
        try: node_Frame_006.bl_height_min = 30.0
        except: pass
        try: node_Frame_006.bl_height_max = 30.0
        except: pass
        try: node_Frame_006.text = None
        except: pass
        try: node_Frame_006.shrink = True
        except: pass
        try: node_Frame_006.label_size = 20
        except: pass
        created_nodes['Frame.006'] = node_Frame_006
        node_Texture_Coordinate_008 = group.nodes.new('ShaderNodeTexCoord')
        node_Texture_Coordinate_008.location_absolute = (-528.3582763671875, 1278.149169921875)
        try: node_Texture_Coordinate_008.location_absolute = Vector((-528.3582763671875, 1278.149169921875))
        except: pass
        try: node_Texture_Coordinate_008.warning_propagation = 'ALL'
        except: pass
        try: node_Texture_Coordinate_008.mute = False
        except: pass
        try: node_Texture_Coordinate_008.bl_label = 'Texture Coordinate'
        except: pass
        try: node_Texture_Coordinate_008.bl_description = 'Retrieve multiple types of texture coordinates.\nTypically used as inputs for texture nodes'
        except: pass
        try: node_Texture_Coordinate_008.bl_icon = 'NONE'
        except: pass
        try: node_Texture_Coordinate_008.bl_width_default = 140.0
        except: pass
        try: node_Texture_Coordinate_008.bl_width_min = 100.0
        except: pass
        try: node_Texture_Coordinate_008.bl_width_max = 700.0
        except: pass
        try: node_Texture_Coordinate_008.bl_height_default = 100.0
        except: pass
        try: node_Texture_Coordinate_008.bl_height_min = 30.0
        except: pass
        try: node_Texture_Coordinate_008.bl_height_max = 30.0
        except: pass
        try: node_Texture_Coordinate_008.object = None
        except: pass
        try: node_Texture_Coordinate_008.from_instancer = False
        except: pass
        created_nodes['Texture Coordinate.008'] = node_Texture_Coordinate_008
        node_Voronoi_Texture_006 = group.nodes.new('ShaderNodeTexVoronoi')
        node_Voronoi_Texture_006.location_absolute = (31.0139217376709, 1301.443115234375)
        try: node_Voronoi_Texture_006.location_absolute = Vector((31.0139217376709, 1301.443115234375))
        except: pass
        try: node_Voronoi_Texture_006.warning_propagation = 'ALL'
        except: pass
        try: node_Voronoi_Texture_006.mute = False
        except: pass
        try: node_Voronoi_Texture_006.bl_label = 'Voronoi Texture'
        except: pass
        try: node_Voronoi_Texture_006.bl_description = 'Generate Worley noise based on the distance to random points. Typically used to generate textures such as stones, water, or biological cells'
        except: pass
        try: node_Voronoi_Texture_006.bl_icon = 'NONE'
        except: pass
        try: node_Voronoi_Texture_006.bl_width_default = 155.0
        except: pass
        try: node_Voronoi_Texture_006.bl_width_min = 140.0
        except: pass
        try: node_Voronoi_Texture_006.bl_width_max = 700.0
        except: pass
        try: node_Voronoi_Texture_006.bl_height_default = 100.0
        except: pass
        try: node_Voronoi_Texture_006.bl_height_min = 30.0
        except: pass
        try: node_Voronoi_Texture_006.bl_height_max = 30.0
        except: pass
        try: node_Voronoi_Texture_006.voronoi_dimensions = '2D'
        except: pass
        try: node_Voronoi_Texture_006.distance = 'EUCLIDEAN'
        except: pass
        try: node_Voronoi_Texture_006.feature = 'DISTANCE_TO_EDGE'
        except: pass
        try: node_Voronoi_Texture_006.normalize = False
        except: pass
        try: node_Voronoi_Texture_006.inputs[1].default_value = 0.0
        except: pass
        try: node_Voronoi_Texture_006.inputs[3].default_value = 0.0
        except: pass
        try: node_Voronoi_Texture_006.inputs[4].default_value = 1.0
        except: pass
        try: node_Voronoi_Texture_006.inputs[5].default_value = 2.100001335144043
        except: pass
        try: node_Voronoi_Texture_006.inputs[6].default_value = 0.363095223903656
        except: pass
        try: node_Voronoi_Texture_006.inputs[7].default_value = 0.5
        except: pass
        try: node_Voronoi_Texture_006.inputs[8].default_value = 1.0
        except: pass
        created_nodes['Voronoi Texture.006'] = node_Voronoi_Texture_006
        node_Map_Range_002 = group.nodes.new('ShaderNodeMapRange')
        node_Map_Range_002.location_absolute = (291.44927978515625, 1301.282958984375)
        try: node_Map_Range_002.location_absolute = Vector((291.44927978515625, 1301.282958984375))
        except: pass
        try: node_Map_Range_002.warning_propagation = 'ALL'
        except: pass
        try: node_Map_Range_002.mute = False
        except: pass
        try: node_Map_Range_002.bl_label = 'Map Range'
        except: pass
        try: node_Map_Range_002.bl_description = 'Remap a value from a range to a target range'
        except: pass
        try: node_Map_Range_002.bl_icon = 'NONE'
        except: pass
        try: node_Map_Range_002.bl_width_default = 140.0
        except: pass
        try: node_Map_Range_002.bl_width_min = 100.0
        except: pass
        try: node_Map_Range_002.bl_width_max = 700.0
        except: pass
        try: node_Map_Range_002.bl_height_default = 100.0
        except: pass
        try: node_Map_Range_002.bl_height_min = 30.0
        except: pass
        try: node_Map_Range_002.bl_height_max = 30.0
        except: pass
        try: node_Map_Range_002.clamp = True
        except: pass
        try: node_Map_Range_002.interpolation_type = 'LINEAR'
        except: pass
        try: node_Map_Range_002.data_type = 'FLOAT'
        except: pass
        try: node_Map_Range_002.inputs[1].default_value = 0.0
        except: pass
        try: node_Map_Range_002.inputs[3].default_value = 0.0
        except: pass
        try: node_Map_Range_002.inputs[4].default_value = 1.0
        except: pass
        try: node_Map_Range_002.inputs[5].default_value = 4.0
        except: pass
        try: node_Map_Range_002.inputs[6].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Map_Range_002.inputs[7].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Map_Range_002.inputs[8].default_value = [1.0,1.0,1.0]
        except: pass
        try: node_Map_Range_002.inputs[9].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Map_Range_002.inputs[10].default_value = [1.0,1.0,1.0]
        except: pass
        try: node_Map_Range_002.inputs[11].default_value = [4.0,4.0,4.0]
        except: pass
        created_nodes['Map Range.002'] = node_Map_Range_002
        node_Combine_XYZ_008 = group.nodes.new('ShaderNodeCombineXYZ')
        node_Combine_XYZ_008.location_absolute = (-153.573486328125, 1253.5941162109375)
        try: node_Combine_XYZ_008.location_absolute = Vector((-153.573486328125, 1253.5941162109375))
        except: pass
        try: node_Combine_XYZ_008.warning_propagation = 'ALL'
        except: pass
        try: node_Combine_XYZ_008.mute = False
        except: pass
        try: node_Combine_XYZ_008.bl_label = 'Combine XYZ'
        except: pass
        try: node_Combine_XYZ_008.bl_description = 'Create a vector from X, Y, and Z components'
        except: pass
        try: node_Combine_XYZ_008.bl_icon = 'NONE'
        except: pass
        try: node_Combine_XYZ_008.bl_width_default = 140.0
        except: pass
        try: node_Combine_XYZ_008.bl_width_min = 100.0
        except: pass
        try: node_Combine_XYZ_008.bl_width_max = 700.0
        except: pass
        try: node_Combine_XYZ_008.bl_height_default = 100.0
        except: pass
        try: node_Combine_XYZ_008.bl_height_min = 30.0
        except: pass
        try: node_Combine_XYZ_008.bl_height_max = 30.0
        except: pass
        try: node_Combine_XYZ_008.inputs[2].default_value = 0.0
        except: pass
        created_nodes['Combine XYZ.008'] = node_Combine_XYZ_008
        node_Separate_XYZ_006 = group.nodes.new('ShaderNodeSeparateXYZ')
        node_Separate_XYZ_006.location_absolute = (-345.7083435058594, 1252.702880859375)
        try: node_Separate_XYZ_006.location_absolute = Vector((-345.7083435058594, 1252.702880859375))
        except: pass
        try: node_Separate_XYZ_006.warning_propagation = 'ALL'
        except: pass
        try: node_Separate_XYZ_006.mute = False
        except: pass
        try: node_Separate_XYZ_006.bl_label = 'Separate XYZ'
        except: pass
        try: node_Separate_XYZ_006.bl_description = 'Split a vector into its X, Y, and Z components'
        except: pass
        try: node_Separate_XYZ_006.bl_icon = 'NONE'
        except: pass
        try: node_Separate_XYZ_006.bl_width_default = 140.0
        except: pass
        try: node_Separate_XYZ_006.bl_width_min = 100.0
        except: pass
        try: node_Separate_XYZ_006.bl_width_max = 700.0
        except: pass
        try: node_Separate_XYZ_006.bl_height_default = 100.0
        except: pass
        try: node_Separate_XYZ_006.bl_height_min = 30.0
        except: pass
        try: node_Separate_XYZ_006.bl_height_max = 30.0
        except: pass
        created_nodes['Separate XYZ.006'] = node_Separate_XYZ_006
        node_Frame_007 = group.nodes.new('NodeFrame')
        node_Frame_007.location_absolute = (-558.0, 1337.5999755859375)
        node_Frame_007.label = 'X'
        node_Frame_007.shrink = True
        try: node_Frame_007.location_absolute = Vector((-558.0, 1337.5999755859375))
        except: pass
        try: node_Frame_007.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_007.mute = False
        except: pass
        try: node_Frame_007.bl_label = 'Frame'
        except: pass
        try: node_Frame_007.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_007.bl_icon = 'NONE'
        except: pass
        try: node_Frame_007.bl_width_default = 150.0
        except: pass
        try: node_Frame_007.bl_width_min = 100.0
        except: pass
        try: node_Frame_007.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_007.bl_height_default = 100.0
        except: pass
        try: node_Frame_007.bl_height_min = 30.0
        except: pass
        try: node_Frame_007.bl_height_max = 30.0
        except: pass
        try: node_Frame_007.text = None
        except: pass
        try: node_Frame_007.shrink = True
        except: pass
        try: node_Frame_007.label_size = 20
        except: pass
        created_nodes['Frame.007'] = node_Frame_007
        node_Mix_003 = group.nodes.new('ShaderNodeMix')
        node_Mix_003.location_absolute = (970.3733520507812, 1110.913330078125)
        try: node_Mix_003.location_absolute = Vector((970.3733520507812, 1110.913330078125))
        except: pass
        try: node_Mix_003.warning_propagation = 'ALL'
        except: pass
        try: node_Mix_003.mute = False
        except: pass
        try: node_Mix_003.bl_label = 'Mix'
        except: pass
        try: node_Mix_003.bl_description = 'Mix values by a factor'
        except: pass
        try: node_Mix_003.bl_icon = 'NONE'
        except: pass
        try: node_Mix_003.bl_width_default = 140.0
        except: pass
        try: node_Mix_003.bl_width_min = 100.0
        except: pass
        try: node_Mix_003.bl_width_max = 700.0
        except: pass
        try: node_Mix_003.bl_height_default = 100.0
        except: pass
        try: node_Mix_003.bl_height_min = 30.0
        except: pass
        try: node_Mix_003.bl_height_max = 30.0
        except: pass
        try: node_Mix_003.data_type = 'RGBA'
        except: pass
        try: node_Mix_003.factor_mode = 'UNIFORM'
        except: pass
        try: node_Mix_003.blend_type = 'MIX'
        except: pass
        try: node_Mix_003.clamp_factor = True
        except: pass
        try: node_Mix_003.clamp_result = False
        except: pass
        try: node_Mix_003.inputs[1].default_value = [0.5,0.5,0.5]
        except: pass
        try: node_Mix_003.inputs[2].default_value = 0.0
        except: pass
        try: node_Mix_003.inputs[3].default_value = 0.0
        except: pass
        try: node_Mix_003.inputs[4].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Mix_003.inputs[5].default_value = [0.0,0.0,0.0]
        except: pass
        created_nodes['Mix.003'] = node_Mix_003
        node_Mix_004 = group.nodes.new('ShaderNodeMix')
        node_Mix_004.location_absolute = (1142.1153564453125, 565.9999389648438)
        try: node_Mix_004.location_absolute = Vector((1142.1153564453125, 565.9999389648438))
        except: pass
        try: node_Mix_004.warning_propagation = 'ALL'
        except: pass
        try: node_Mix_004.mute = False
        except: pass
        try: node_Mix_004.bl_label = 'Mix'
        except: pass
        try: node_Mix_004.bl_description = 'Mix values by a factor'
        except: pass
        try: node_Mix_004.bl_icon = 'NONE'
        except: pass
        try: node_Mix_004.bl_width_default = 140.0
        except: pass
        try: node_Mix_004.bl_width_min = 100.0
        except: pass
        try: node_Mix_004.bl_width_max = 700.0
        except: pass
        try: node_Mix_004.bl_height_default = 100.0
        except: pass
        try: node_Mix_004.bl_height_min = 30.0
        except: pass
        try: node_Mix_004.bl_height_max = 30.0
        except: pass
        try: node_Mix_004.data_type = 'RGBA'
        except: pass
        try: node_Mix_004.factor_mode = 'UNIFORM'
        except: pass
        try: node_Mix_004.blend_type = 'MIX'
        except: pass
        try: node_Mix_004.clamp_factor = True
        except: pass
        try: node_Mix_004.clamp_result = False
        except: pass
        try: node_Mix_004.inputs[1].default_value = [0.5,0.5,0.5]
        except: pass
        try: node_Mix_004.inputs[2].default_value = 0.0
        except: pass
        try: node_Mix_004.inputs[3].default_value = 0.0
        except: pass
        try: node_Mix_004.inputs[4].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Mix_004.inputs[5].default_value = [0.0,0.0,0.0]
        except: pass
        created_nodes['Mix.004'] = node_Mix_004
        node_Frame_008 = group.nodes.new('NodeFrame')
        node_Frame_008.location_absolute = (-588.0, 1367.5999755859375)
        node_Frame_008.shrink = True
        try: node_Frame_008.location_absolute = Vector((-588.0, 1367.5999755859375))
        except: pass
        try: node_Frame_008.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_008.mute = False
        except: pass
        try: node_Frame_008.bl_label = 'Frame'
        except: pass
        try: node_Frame_008.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_008.bl_icon = 'NONE'
        except: pass
        try: node_Frame_008.bl_width_default = 150.0
        except: pass
        try: node_Frame_008.bl_width_min = 100.0
        except: pass
        try: node_Frame_008.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_008.bl_height_default = 100.0
        except: pass
        try: node_Frame_008.bl_height_min = 30.0
        except: pass
        try: node_Frame_008.bl_height_max = 30.0
        except: pass
        try: node_Frame_008.text = None
        except: pass
        try: node_Frame_008.shrink = True
        except: pass
        try: node_Frame_008.label_size = 20
        except: pass
        created_nodes['Frame.008'] = node_Frame_008
        node_Texture_Coordinate_009 = group.nodes.new('ShaderNodeTexCoord')
        node_Texture_Coordinate_009.location_absolute = (-505.7488708496094, 1811.3873291015625)
        try: node_Texture_Coordinate_009.location_absolute = Vector((-505.7488708496094, 1811.3873291015625))
        except: pass
        try: node_Texture_Coordinate_009.warning_propagation = 'ALL'
        except: pass
        try: node_Texture_Coordinate_009.mute = False
        except: pass
        try: node_Texture_Coordinate_009.bl_label = 'Texture Coordinate'
        except: pass
        try: node_Texture_Coordinate_009.bl_description = 'Retrieve multiple types of texture coordinates.\nTypically used as inputs for texture nodes'
        except: pass
        try: node_Texture_Coordinate_009.bl_icon = 'NONE'
        except: pass
        try: node_Texture_Coordinate_009.bl_width_default = 140.0
        except: pass
        try: node_Texture_Coordinate_009.bl_width_min = 100.0
        except: pass
        try: node_Texture_Coordinate_009.bl_width_max = 700.0
        except: pass
        try: node_Texture_Coordinate_009.bl_height_default = 100.0
        except: pass
        try: node_Texture_Coordinate_009.bl_height_min = 30.0
        except: pass
        try: node_Texture_Coordinate_009.bl_height_max = 30.0
        except: pass
        try: node_Texture_Coordinate_009.object = None
        except: pass
        try: node_Texture_Coordinate_009.from_instancer = False
        except: pass
        created_nodes['Texture Coordinate.009'] = node_Texture_Coordinate_009
        node_Combine_XYZ_009 = group.nodes.new('ShaderNodeCombineXYZ')
        node_Combine_XYZ_009.location_absolute = (-130.9640350341797, 1786.832275390625)
        try: node_Combine_XYZ_009.location_absolute = Vector((-130.9640350341797, 1786.832275390625))
        except: pass
        try: node_Combine_XYZ_009.warning_propagation = 'ALL'
        except: pass
        try: node_Combine_XYZ_009.mute = False
        except: pass
        try: node_Combine_XYZ_009.bl_label = 'Combine XYZ'
        except: pass
        try: node_Combine_XYZ_009.bl_description = 'Create a vector from X, Y, and Z components'
        except: pass
        try: node_Combine_XYZ_009.bl_icon = 'NONE'
        except: pass
        try: node_Combine_XYZ_009.bl_width_default = 140.0
        except: pass
        try: node_Combine_XYZ_009.bl_width_min = 100.0
        except: pass
        try: node_Combine_XYZ_009.bl_width_max = 700.0
        except: pass
        try: node_Combine_XYZ_009.bl_height_default = 100.0
        except: pass
        try: node_Combine_XYZ_009.bl_height_min = 30.0
        except: pass
        try: node_Combine_XYZ_009.bl_height_max = 30.0
        except: pass
        try: node_Combine_XYZ_009.inputs[2].default_value = 0.0
        except: pass
        created_nodes['Combine XYZ.009'] = node_Combine_XYZ_009
        node_Separate_XYZ_007 = group.nodes.new('ShaderNodeSeparateXYZ')
        node_Separate_XYZ_007.location_absolute = (-323.0988464355469, 1785.9410400390625)
        try: node_Separate_XYZ_007.location_absolute = Vector((-323.0988464355469, 1785.9410400390625))
        except: pass
        try: node_Separate_XYZ_007.warning_propagation = 'ALL'
        except: pass
        try: node_Separate_XYZ_007.mute = False
        except: pass
        try: node_Separate_XYZ_007.bl_label = 'Separate XYZ'
        except: pass
        try: node_Separate_XYZ_007.bl_description = 'Split a vector into its X, Y, and Z components'
        except: pass
        try: node_Separate_XYZ_007.bl_icon = 'NONE'
        except: pass
        try: node_Separate_XYZ_007.bl_width_default = 140.0
        except: pass
        try: node_Separate_XYZ_007.bl_width_min = 100.0
        except: pass
        try: node_Separate_XYZ_007.bl_width_max = 700.0
        except: pass
        try: node_Separate_XYZ_007.bl_height_default = 100.0
        except: pass
        try: node_Separate_XYZ_007.bl_height_min = 30.0
        except: pass
        try: node_Separate_XYZ_007.bl_height_max = 30.0
        except: pass
        created_nodes['Separate XYZ.007'] = node_Separate_XYZ_007
        node_Frame_009 = group.nodes.new('NodeFrame')
        node_Frame_009.location_absolute = (-535.5999755859375, 1847.199951171875)
        node_Frame_009.label = 'Z'
        node_Frame_009.shrink = True
        try: node_Frame_009.location_absolute = Vector((-535.5999755859375, 1847.199951171875))
        except: pass
        try: node_Frame_009.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_009.mute = False
        except: pass
        try: node_Frame_009.bl_label = 'Frame'
        except: pass
        try: node_Frame_009.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_009.bl_icon = 'NONE'
        except: pass
        try: node_Frame_009.bl_width_default = 150.0
        except: pass
        try: node_Frame_009.bl_width_min = 100.0
        except: pass
        try: node_Frame_009.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_009.bl_height_default = 100.0
        except: pass
        try: node_Frame_009.bl_height_min = 30.0
        except: pass
        try: node_Frame_009.bl_height_max = 30.0
        except: pass
        try: node_Frame_009.text = None
        except: pass
        try: node_Frame_009.shrink = True
        except: pass
        try: node_Frame_009.label_size = 20
        except: pass
        created_nodes['Frame.009'] = node_Frame_009
        node_Texture_Coordinate_010 = group.nodes.new('ShaderNodeTexCoord')
        node_Texture_Coordinate_010.location_absolute = (-508.27520751953125, 2240.36083984375)
        try: node_Texture_Coordinate_010.location_absolute = Vector((-508.27520751953125, 2240.36083984375))
        except: pass
        try: node_Texture_Coordinate_010.warning_propagation = 'ALL'
        except: pass
        try: node_Texture_Coordinate_010.mute = False
        except: pass
        try: node_Texture_Coordinate_010.bl_label = 'Texture Coordinate'
        except: pass
        try: node_Texture_Coordinate_010.bl_description = 'Retrieve multiple types of texture coordinates.\nTypically used as inputs for texture nodes'
        except: pass
        try: node_Texture_Coordinate_010.bl_icon = 'NONE'
        except: pass
        try: node_Texture_Coordinate_010.bl_width_default = 140.0
        except: pass
        try: node_Texture_Coordinate_010.bl_width_min = 100.0
        except: pass
        try: node_Texture_Coordinate_010.bl_width_max = 700.0
        except: pass
        try: node_Texture_Coordinate_010.bl_height_default = 100.0
        except: pass
        try: node_Texture_Coordinate_010.bl_height_min = 30.0
        except: pass
        try: node_Texture_Coordinate_010.bl_height_max = 30.0
        except: pass
        try: node_Texture_Coordinate_010.object = None
        except: pass
        try: node_Texture_Coordinate_010.from_instancer = False
        except: pass
        created_nodes['Texture Coordinate.010'] = node_Texture_Coordinate_010
        node_Combine_XYZ_010 = group.nodes.new('ShaderNodeCombineXYZ')
        node_Combine_XYZ_010.location_absolute = (-133.49032592773438, 2215.805908203125)
        try: node_Combine_XYZ_010.location_absolute = Vector((-133.49032592773438, 2215.805908203125))
        except: pass
        try: node_Combine_XYZ_010.warning_propagation = 'ALL'
        except: pass
        try: node_Combine_XYZ_010.mute = False
        except: pass
        try: node_Combine_XYZ_010.bl_label = 'Combine XYZ'
        except: pass
        try: node_Combine_XYZ_010.bl_description = 'Create a vector from X, Y, and Z components'
        except: pass
        try: node_Combine_XYZ_010.bl_icon = 'NONE'
        except: pass
        try: node_Combine_XYZ_010.bl_width_default = 140.0
        except: pass
        try: node_Combine_XYZ_010.bl_width_min = 100.0
        except: pass
        try: node_Combine_XYZ_010.bl_width_max = 700.0
        except: pass
        try: node_Combine_XYZ_010.bl_height_default = 100.0
        except: pass
        try: node_Combine_XYZ_010.bl_height_min = 30.0
        except: pass
        try: node_Combine_XYZ_010.bl_height_max = 30.0
        except: pass
        try: node_Combine_XYZ_010.inputs[2].default_value = 0.0
        except: pass
        created_nodes['Combine XYZ.010'] = node_Combine_XYZ_010
        node_Separate_XYZ_008 = group.nodes.new('ShaderNodeSeparateXYZ')
        node_Separate_XYZ_008.location_absolute = (-325.6252136230469, 2214.914794921875)
        try: node_Separate_XYZ_008.location_absolute = Vector((-325.6252136230469, 2214.914794921875))
        except: pass
        try: node_Separate_XYZ_008.warning_propagation = 'ALL'
        except: pass
        try: node_Separate_XYZ_008.mute = False
        except: pass
        try: node_Separate_XYZ_008.bl_label = 'Separate XYZ'
        except: pass
        try: node_Separate_XYZ_008.bl_description = 'Split a vector into its X, Y, and Z components'
        except: pass
        try: node_Separate_XYZ_008.bl_icon = 'NONE'
        except: pass
        try: node_Separate_XYZ_008.bl_width_default = 140.0
        except: pass
        try: node_Separate_XYZ_008.bl_width_min = 100.0
        except: pass
        try: node_Separate_XYZ_008.bl_width_max = 700.0
        except: pass
        try: node_Separate_XYZ_008.bl_height_default = 100.0
        except: pass
        try: node_Separate_XYZ_008.bl_height_min = 30.0
        except: pass
        try: node_Separate_XYZ_008.bl_height_max = 30.0
        except: pass
        created_nodes['Separate XYZ.008'] = node_Separate_XYZ_008
        node_Frame_010 = group.nodes.new('NodeFrame')
        node_Frame_010.location_absolute = (-538.0, 2279.199951171875)
        node_Frame_010.label = 'Y'
        node_Frame_010.shrink = True
        try: node_Frame_010.location_absolute = Vector((-538.0, 2279.199951171875))
        except: pass
        try: node_Frame_010.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_010.mute = False
        except: pass
        try: node_Frame_010.bl_label = 'Frame'
        except: pass
        try: node_Frame_010.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_010.bl_icon = 'NONE'
        except: pass
        try: node_Frame_010.bl_width_default = 150.0
        except: pass
        try: node_Frame_010.bl_width_min = 100.0
        except: pass
        try: node_Frame_010.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_010.bl_height_default = 100.0
        except: pass
        try: node_Frame_010.bl_height_min = 30.0
        except: pass
        try: node_Frame_010.bl_height_max = 30.0
        except: pass
        try: node_Frame_010.text = None
        except: pass
        try: node_Frame_010.shrink = True
        except: pass
        try: node_Frame_010.label_size = 20
        except: pass
        created_nodes['Frame.010'] = node_Frame_010
        node_Texture_Coordinate_011 = group.nodes.new('ShaderNodeTexCoord')
        node_Texture_Coordinate_011.location_absolute = (-505.637939453125, 2623.814208984375)
        try: node_Texture_Coordinate_011.location_absolute = Vector((-505.637939453125, 2623.814208984375))
        except: pass
        try: node_Texture_Coordinate_011.warning_propagation = 'ALL'
        except: pass
        try: node_Texture_Coordinate_011.mute = False
        except: pass
        try: node_Texture_Coordinate_011.bl_label = 'Texture Coordinate'
        except: pass
        try: node_Texture_Coordinate_011.bl_description = 'Retrieve multiple types of texture coordinates.\nTypically used as inputs for texture nodes'
        except: pass
        try: node_Texture_Coordinate_011.bl_icon = 'NONE'
        except: pass
        try: node_Texture_Coordinate_011.bl_width_default = 140.0
        except: pass
        try: node_Texture_Coordinate_011.bl_width_min = 100.0
        except: pass
        try: node_Texture_Coordinate_011.bl_width_max = 700.0
        except: pass
        try: node_Texture_Coordinate_011.bl_height_default = 100.0
        except: pass
        try: node_Texture_Coordinate_011.bl_height_min = 30.0
        except: pass
        try: node_Texture_Coordinate_011.bl_height_max = 30.0
        except: pass
        try: node_Texture_Coordinate_011.object = None
        except: pass
        try: node_Texture_Coordinate_011.from_instancer = False
        except: pass
        created_nodes['Texture Coordinate.011'] = node_Texture_Coordinate_011
        node_Combine_XYZ_011 = group.nodes.new('ShaderNodeCombineXYZ')
        node_Combine_XYZ_011.location_absolute = (-130.85317993164062, 2599.25927734375)
        try: node_Combine_XYZ_011.location_absolute = Vector((-130.85317993164062, 2599.25927734375))
        except: pass
        try: node_Combine_XYZ_011.warning_propagation = 'ALL'
        except: pass
        try: node_Combine_XYZ_011.mute = False
        except: pass
        try: node_Combine_XYZ_011.bl_label = 'Combine XYZ'
        except: pass
        try: node_Combine_XYZ_011.bl_description = 'Create a vector from X, Y, and Z components'
        except: pass
        try: node_Combine_XYZ_011.bl_icon = 'NONE'
        except: pass
        try: node_Combine_XYZ_011.bl_width_default = 140.0
        except: pass
        try: node_Combine_XYZ_011.bl_width_min = 100.0
        except: pass
        try: node_Combine_XYZ_011.bl_width_max = 700.0
        except: pass
        try: node_Combine_XYZ_011.bl_height_default = 100.0
        except: pass
        try: node_Combine_XYZ_011.bl_height_min = 30.0
        except: pass
        try: node_Combine_XYZ_011.bl_height_max = 30.0
        except: pass
        try: node_Combine_XYZ_011.inputs[2].default_value = 0.0
        except: pass
        created_nodes['Combine XYZ.011'] = node_Combine_XYZ_011
        node_Separate_XYZ_009 = group.nodes.new('ShaderNodeSeparateXYZ')
        node_Separate_XYZ_009.location_absolute = (-322.988037109375, 2598.368408203125)
        try: node_Separate_XYZ_009.location_absolute = Vector((-322.988037109375, 2598.368408203125))
        except: pass
        try: node_Separate_XYZ_009.warning_propagation = 'ALL'
        except: pass
        try: node_Separate_XYZ_009.mute = False
        except: pass
        try: node_Separate_XYZ_009.bl_label = 'Separate XYZ'
        except: pass
        try: node_Separate_XYZ_009.bl_description = 'Split a vector into its X, Y, and Z components'
        except: pass
        try: node_Separate_XYZ_009.bl_icon = 'NONE'
        except: pass
        try: node_Separate_XYZ_009.bl_width_default = 140.0
        except: pass
        try: node_Separate_XYZ_009.bl_width_min = 100.0
        except: pass
        try: node_Separate_XYZ_009.bl_width_max = 700.0
        except: pass
        try: node_Separate_XYZ_009.bl_height_default = 100.0
        except: pass
        try: node_Separate_XYZ_009.bl_height_min = 30.0
        except: pass
        try: node_Separate_XYZ_009.bl_height_max = 30.0
        except: pass
        created_nodes['Separate XYZ.009'] = node_Separate_XYZ_009
        node_Frame_011 = group.nodes.new('NodeFrame')
        node_Frame_011.location_absolute = (-535.5999755859375, 2713.60009765625)
        node_Frame_011.label = 'X'
        node_Frame_011.shrink = True
        try: node_Frame_011.location_absolute = Vector((-535.5999755859375, 2713.60009765625))
        except: pass
        try: node_Frame_011.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_011.mute = False
        except: pass
        try: node_Frame_011.bl_label = 'Frame'
        except: pass
        try: node_Frame_011.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_011.bl_icon = 'NONE'
        except: pass
        try: node_Frame_011.bl_width_default = 150.0
        except: pass
        try: node_Frame_011.bl_width_min = 100.0
        except: pass
        try: node_Frame_011.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_011.bl_height_default = 100.0
        except: pass
        try: node_Frame_011.bl_height_min = 30.0
        except: pass
        try: node_Frame_011.bl_height_max = 30.0
        except: pass
        try: node_Frame_011.text = None
        except: pass
        try: node_Frame_011.shrink = True
        except: pass
        try: node_Frame_011.label_size = 20
        except: pass
        created_nodes['Frame.011'] = node_Frame_011
        node_Mix_005 = group.nodes.new('ShaderNodeMix')
        node_Mix_005.location_absolute = (905.85888671875, 2311.48193359375)
        try: node_Mix_005.location_absolute = Vector((905.85888671875, 2311.48193359375))
        except: pass
        try: node_Mix_005.warning_propagation = 'ALL'
        except: pass
        try: node_Mix_005.mute = False
        except: pass
        try: node_Mix_005.bl_label = 'Mix'
        except: pass
        try: node_Mix_005.bl_description = 'Mix values by a factor'
        except: pass
        try: node_Mix_005.bl_icon = 'NONE'
        except: pass
        try: node_Mix_005.bl_width_default = 140.0
        except: pass
        try: node_Mix_005.bl_width_min = 100.0
        except: pass
        try: node_Mix_005.bl_width_max = 700.0
        except: pass
        try: node_Mix_005.bl_height_default = 100.0
        except: pass
        try: node_Mix_005.bl_height_min = 30.0
        except: pass
        try: node_Mix_005.bl_height_max = 30.0
        except: pass
        try: node_Mix_005.data_type = 'RGBA'
        except: pass
        try: node_Mix_005.factor_mode = 'UNIFORM'
        except: pass
        try: node_Mix_005.blend_type = 'MIX'
        except: pass
        try: node_Mix_005.clamp_factor = True
        except: pass
        try: node_Mix_005.clamp_result = False
        except: pass
        try: node_Mix_005.inputs[1].default_value = [0.5,0.5,0.5]
        except: pass
        try: node_Mix_005.inputs[2].default_value = 0.0
        except: pass
        try: node_Mix_005.inputs[3].default_value = 0.0
        except: pass
        try: node_Mix_005.inputs[4].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Mix_005.inputs[5].default_value = [0.0,0.0,0.0]
        except: pass
        created_nodes['Mix.005'] = node_Mix_005
        node_Mix_006 = group.nodes.new('ShaderNodeMix')
        node_Mix_006.location_absolute = (1187.20068359375, 1766.568359375)
        try: node_Mix_006.location_absolute = Vector((1187.20068359375, 1766.568359375))
        except: pass
        try: node_Mix_006.warning_propagation = 'ALL'
        except: pass
        try: node_Mix_006.mute = False
        except: pass
        try: node_Mix_006.bl_label = 'Mix'
        except: pass
        try: node_Mix_006.bl_description = 'Mix values by a factor'
        except: pass
        try: node_Mix_006.bl_icon = 'NONE'
        except: pass
        try: node_Mix_006.bl_width_default = 140.0
        except: pass
        try: node_Mix_006.bl_width_min = 100.0
        except: pass
        try: node_Mix_006.bl_width_max = 700.0
        except: pass
        try: node_Mix_006.bl_height_default = 100.0
        except: pass
        try: node_Mix_006.bl_height_min = 30.0
        except: pass
        try: node_Mix_006.bl_height_max = 30.0
        except: pass
        try: node_Mix_006.data_type = 'RGBA'
        except: pass
        try: node_Mix_006.factor_mode = 'UNIFORM'
        except: pass
        try: node_Mix_006.blend_type = 'MIX'
        except: pass
        try: node_Mix_006.clamp_factor = True
        except: pass
        try: node_Mix_006.clamp_result = False
        except: pass
        try: node_Mix_006.inputs[1].default_value = [0.5,0.5,0.5]
        except: pass
        try: node_Mix_006.inputs[2].default_value = 0.0
        except: pass
        try: node_Mix_006.inputs[3].default_value = 0.0
        except: pass
        try: node_Mix_006.inputs[4].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Mix_006.inputs[5].default_value = [0.0,0.0,0.0]
        except: pass
        created_nodes['Mix.006'] = node_Mix_006
        node_Frame_012 = group.nodes.new('NodeFrame')
        node_Frame_012.location_absolute = (-568.0, 2743.60009765625)
        node_Frame_012.shrink = True
        try: node_Frame_012.location_absolute = Vector((-568.0, 2743.60009765625))
        except: pass
        try: node_Frame_012.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_012.mute = False
        except: pass
        try: node_Frame_012.bl_label = 'Frame'
        except: pass
        try: node_Frame_012.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_012.bl_icon = 'NONE'
        except: pass
        try: node_Frame_012.bl_width_default = 150.0
        except: pass
        try: node_Frame_012.bl_width_min = 100.0
        except: pass
        try: node_Frame_012.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_012.bl_height_default = 100.0
        except: pass
        try: node_Frame_012.bl_height_min = 30.0
        except: pass
        try: node_Frame_012.bl_height_max = 30.0
        except: pass
        try: node_Frame_012.text = None
        except: pass
        try: node_Frame_012.shrink = True
        except: pass
        try: node_Frame_012.label_size = 20
        except: pass
        created_nodes['Frame.012'] = node_Frame_012
        node_Mapping = group.nodes.new('ShaderNodeMapping')
        node_Mapping.location_absolute = (52.42578125, 2677.714599609375)
        try: node_Mapping.location_absolute = Vector((52.42578125, 2677.714599609375))
        except: pass
        try: node_Mapping.warning_propagation = 'ALL'
        except: pass
        try: node_Mapping.mute = False
        except: pass
        try: node_Mapping.bl_label = 'Mapping'
        except: pass
        try: node_Mapping.bl_description = 'Transform the input vector by applying translation, rotation, and scale'
        except: pass
        try: node_Mapping.bl_icon = 'NONE'
        except: pass
        try: node_Mapping.bl_width_default = 140.0
        except: pass
        try: node_Mapping.bl_width_min = 100.0
        except: pass
        try: node_Mapping.bl_width_max = 700.0
        except: pass
        try: node_Mapping.bl_height_default = 100.0
        except: pass
        try: node_Mapping.bl_height_min = 30.0
        except: pass
        try: node_Mapping.bl_height_max = 30.0
        except: pass
        try: node_Mapping.vector_type = 'POINT'
        except: pass
        created_nodes['Mapping'] = node_Mapping
        node_Mapping_004 = group.nodes.new('ShaderNodeMapping')
        node_Mapping_004.location_absolute = (46.85051727294922, 2242.95458984375)
        try: node_Mapping_004.location_absolute = Vector((46.85051727294922, 2242.95458984375))
        except: pass
        try: node_Mapping_004.warning_propagation = 'ALL'
        except: pass
        try: node_Mapping_004.mute = False
        except: pass
        try: node_Mapping_004.bl_label = 'Mapping'
        except: pass
        try: node_Mapping_004.bl_description = 'Transform the input vector by applying translation, rotation, and scale'
        except: pass
        try: node_Mapping_004.bl_icon = 'NONE'
        except: pass
        try: node_Mapping_004.bl_width_default = 140.0
        except: pass
        try: node_Mapping_004.bl_width_min = 100.0
        except: pass
        try: node_Mapping_004.bl_width_max = 700.0
        except: pass
        try: node_Mapping_004.bl_height_default = 100.0
        except: pass
        try: node_Mapping_004.bl_height_min = 30.0
        except: pass
        try: node_Mapping_004.bl_height_max = 30.0
        except: pass
        try: node_Mapping_004.vector_type = 'POINT'
        except: pass
        created_nodes['Mapping.004'] = node_Mapping_004
        node_Mapping_005 = group.nodes.new('ShaderNodeMapping')
        node_Mapping_005.location_absolute = (45.32073211669922, 1793.103759765625)
        try: node_Mapping_005.location_absolute = Vector((45.32073211669922, 1793.103759765625))
        except: pass
        try: node_Mapping_005.warning_propagation = 'ALL'
        except: pass
        try: node_Mapping_005.mute = False
        except: pass
        try: node_Mapping_005.bl_label = 'Mapping'
        except: pass
        try: node_Mapping_005.bl_description = 'Transform the input vector by applying translation, rotation, and scale'
        except: pass
        try: node_Mapping_005.bl_icon = 'NONE'
        except: pass
        try: node_Mapping_005.bl_width_default = 140.0
        except: pass
        try: node_Mapping_005.bl_width_min = 100.0
        except: pass
        try: node_Mapping_005.bl_width_max = 700.0
        except: pass
        try: node_Mapping_005.bl_height_default = 100.0
        except: pass
        try: node_Mapping_005.bl_height_min = 30.0
        except: pass
        try: node_Mapping_005.bl_height_max = 30.0
        except: pass
        try: node_Mapping_005.vector_type = 'POINT'
        except: pass
        created_nodes['Mapping.005'] = node_Mapping_005
        node_Math = group.nodes.new('ShaderNodeMath')
        node_Math.location_absolute = (-2067.764404296875, 418.872314453125)
        try: node_Math.location_absolute = Vector((-2067.764404296875, 418.872314453125))
        except: pass
        try: node_Math.warning_propagation = 'ALL'
        except: pass
        try: node_Math.mute = False
        except: pass
        try: node_Math.bl_label = 'Math'
        except: pass
        try: node_Math.bl_description = 'Perform math operations'
        except: pass
        try: node_Math.bl_icon = 'NONE'
        except: pass
        try: node_Math.bl_width_default = 140.0
        except: pass
        try: node_Math.bl_width_min = 100.0
        except: pass
        try: node_Math.bl_width_max = 700.0
        except: pass
        try: node_Math.bl_height_default = 100.0
        except: pass
        try: node_Math.bl_height_min = 30.0
        except: pass
        try: node_Math.bl_height_max = 30.0
        except: pass
        try: node_Math.operation = 'DIVIDE'
        except: pass
        try: node_Math.use_clamp = False
        except: pass
        try: node_Math.inputs[1].default_value = 100.0
        except: pass
        try: node_Math.inputs[2].default_value = 0.5
        except: pass
        created_nodes['Math'] = node_Math
        node_Vector_Math_005 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_005.location_absolute = (-43.66376876831055, 87.82987976074219)
        try: node_Vector_Math_005.location_absolute = Vector((-43.66376876831055, 87.82987976074219))
        except: pass
        try: node_Vector_Math_005.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_005.mute = False
        except: pass
        try: node_Vector_Math_005.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_005.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_005.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_005.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_005.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_005.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_005.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_005.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_005.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_005.operation = 'POWER'
        except: pass
        try: node_Vector_Math_005.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_005.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.005'] = node_Vector_Math_005
        node_Vector_Math_009 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_009.location_absolute = (127.31639099121094, 58.1043815612793)
        try: node_Vector_Math_009.location_absolute = Vector((127.31639099121094, 58.1043815612793))
        except: pass
        try: node_Vector_Math_009.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_009.mute = False
        except: pass
        try: node_Vector_Math_009.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_009.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_009.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_009.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_009.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_009.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_009.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_009.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_009.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_009.operation = 'NORMALIZE'
        except: pass
        try: node_Vector_Math_009.inputs[1].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_009.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_009.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.009'] = node_Vector_Math_009
        node_Separate_XYZ_002 = group.nodes.new('ShaderNodeSeparateXYZ')
        node_Separate_XYZ_002.location_absolute = (354.42144775390625, 97.5800552368164)
        try: node_Separate_XYZ_002.location_absolute = Vector((354.42144775390625, 97.5800552368164))
        except: pass
        try: node_Separate_XYZ_002.warning_propagation = 'ALL'
        except: pass
        try: node_Separate_XYZ_002.mute = False
        except: pass
        try: node_Separate_XYZ_002.bl_label = 'Separate XYZ'
        except: pass
        try: node_Separate_XYZ_002.bl_description = 'Split a vector into its X, Y, and Z components'
        except: pass
        try: node_Separate_XYZ_002.bl_icon = 'NONE'
        except: pass
        try: node_Separate_XYZ_002.bl_width_default = 140.0
        except: pass
        try: node_Separate_XYZ_002.bl_width_min = 100.0
        except: pass
        try: node_Separate_XYZ_002.bl_width_max = 700.0
        except: pass
        try: node_Separate_XYZ_002.bl_height_default = 100.0
        except: pass
        try: node_Separate_XYZ_002.bl_height_min = 30.0
        except: pass
        try: node_Separate_XYZ_002.bl_height_max = 30.0
        except: pass
        created_nodes['Separate XYZ.002'] = node_Separate_XYZ_002
        node_Separate_XYZ_010 = group.nodes.new('ShaderNodeSeparateXYZ')
        node_Separate_XYZ_010.location_absolute = (348.97052001953125, 269.2652282714844)
        try: node_Separate_XYZ_010.location_absolute = Vector((348.97052001953125, 269.2652282714844))
        except: pass
        try: node_Separate_XYZ_010.warning_propagation = 'ALL'
        except: pass
        try: node_Separate_XYZ_010.mute = False
        except: pass
        try: node_Separate_XYZ_010.bl_label = 'Separate XYZ'
        except: pass
        try: node_Separate_XYZ_010.bl_description = 'Split a vector into its X, Y, and Z components'
        except: pass
        try: node_Separate_XYZ_010.bl_icon = 'NONE'
        except: pass
        try: node_Separate_XYZ_010.bl_width_default = 140.0
        except: pass
        try: node_Separate_XYZ_010.bl_width_min = 100.0
        except: pass
        try: node_Separate_XYZ_010.bl_width_max = 700.0
        except: pass
        try: node_Separate_XYZ_010.bl_height_default = 100.0
        except: pass
        try: node_Separate_XYZ_010.bl_height_min = 30.0
        except: pass
        try: node_Separate_XYZ_010.bl_height_max = 30.0
        except: pass
        created_nodes['Separate XYZ.010'] = node_Separate_XYZ_010
        node_Image_Texture = group.nodes.new('ShaderNodeTexImage')
        node_Image_Texture.location_absolute = (175.19998168945312, -293.00531005859375)
        try: node_Image_Texture.location_absolute = Vector((175.19998168945312, -293.00531005859375))
        except: pass
        try: node_Image_Texture.warning_propagation = 'ALL'
        except: pass
        try: node_Image_Texture.mute = False
        except: pass
        try: node_Image_Texture.bl_label = 'Image Texture'
        except: pass
        try: node_Image_Texture.bl_description = 'Sample an image file as a texture'
        except: pass
        try: node_Image_Texture.bl_icon = 'NONE'
        except: pass
        try: node_Image_Texture.bl_width_default = 240.0
        except: pass
        try: node_Image_Texture.bl_width_min = 140.0
        except: pass
        try: node_Image_Texture.bl_width_max = 700.0
        except: pass
        try: node_Image_Texture.bl_height_default = 100.0
        except: pass
        try: node_Image_Texture.bl_height_min = 30.0
        except: pass
        try: node_Image_Texture.bl_height_max = 30.0
        except: pass
        try: node_Image_Texture.image = bpy.data.images['Image']
        except: pass
        try: node_Image_Texture.projection = 'FLAT'
        except: pass
        try: node_Image_Texture.interpolation = 'Linear'
        except: pass
        try: node_Image_Texture.projection_blend = 0.0
        except: pass
        try: node_Image_Texture.extension = 'REPEAT'
        except: pass
        created_nodes['Image Texture'] = node_Image_Texture
        node_Image_Texture_001 = group.nodes.new('ShaderNodeTexImage')
        node_Image_Texture_001.location_absolute = (175.19998168945312, -913.9451904296875)
        try: node_Image_Texture_001.location_absolute = Vector((175.19998168945312, -913.9451904296875))
        except: pass
        try: node_Image_Texture_001.warning_propagation = 'ALL'
        except: pass
        try: node_Image_Texture_001.mute = False
        except: pass
        try: node_Image_Texture_001.bl_label = 'Image Texture'
        except: pass
        try: node_Image_Texture_001.bl_description = 'Sample an image file as a texture'
        except: pass
        try: node_Image_Texture_001.bl_icon = 'NONE'
        except: pass
        try: node_Image_Texture_001.bl_width_default = 240.0
        except: pass
        try: node_Image_Texture_001.bl_width_min = 140.0
        except: pass
        try: node_Image_Texture_001.bl_width_max = 700.0
        except: pass
        try: node_Image_Texture_001.bl_height_default = 100.0
        except: pass
        try: node_Image_Texture_001.bl_height_min = 30.0
        except: pass
        try: node_Image_Texture_001.bl_height_max = 30.0
        except: pass
        try: node_Image_Texture_001.image = bpy.data.images['Image']
        except: pass
        try: node_Image_Texture_001.projection = 'FLAT'
        except: pass
        try: node_Image_Texture_001.interpolation = 'Linear'
        except: pass
        try: node_Image_Texture_001.projection_blend = 0.0
        except: pass
        try: node_Image_Texture_001.extension = 'REPEAT'
        except: pass
        created_nodes['Image Texture.001'] = node_Image_Texture_001
        node_Image_Texture_004 = group.nodes.new('ShaderNodeTexImage')
        node_Image_Texture_004.location_absolute = (213.84375, -1467.7381591796875)
        try: node_Image_Texture_004.location_absolute = Vector((213.84375, -1467.7381591796875))
        except: pass
        try: node_Image_Texture_004.warning_propagation = 'ALL'
        except: pass
        try: node_Image_Texture_004.mute = False
        except: pass
        try: node_Image_Texture_004.bl_label = 'Image Texture'
        except: pass
        try: node_Image_Texture_004.bl_description = 'Sample an image file as a texture'
        except: pass
        try: node_Image_Texture_004.bl_icon = 'NONE'
        except: pass
        try: node_Image_Texture_004.bl_width_default = 240.0
        except: pass
        try: node_Image_Texture_004.bl_width_min = 140.0
        except: pass
        try: node_Image_Texture_004.bl_width_max = 700.0
        except: pass
        try: node_Image_Texture_004.bl_height_default = 100.0
        except: pass
        try: node_Image_Texture_004.bl_height_min = 30.0
        except: pass
        try: node_Image_Texture_004.bl_height_max = 30.0
        except: pass
        try: node_Image_Texture_004.image = bpy.data.images['Image']
        except: pass
        try: node_Image_Texture_004.projection = 'FLAT'
        except: pass
        try: node_Image_Texture_004.interpolation = 'Linear'
        except: pass
        try: node_Image_Texture_004.projection_blend = 0.0
        except: pass
        try: node_Image_Texture_004.extension = 'REPEAT'
        except: pass
        created_nodes['Image Texture.004'] = node_Image_Texture_004
        node_Image_Texture_002 = group.nodes.new('ShaderNodeTexImage')
        node_Image_Texture_002.location_absolute = (269.22857666015625, 1792.1605224609375)
        try: node_Image_Texture_002.location_absolute = Vector((269.22857666015625, 1792.1605224609375))
        except: pass
        try: node_Image_Texture_002.warning_propagation = 'ALL'
        except: pass
        try: node_Image_Texture_002.mute = False
        except: pass
        try: node_Image_Texture_002.bl_label = 'Image Texture'
        except: pass
        try: node_Image_Texture_002.bl_description = 'Sample an image file as a texture'
        except: pass
        try: node_Image_Texture_002.bl_icon = 'NONE'
        except: pass
        try: node_Image_Texture_002.bl_width_default = 240.0
        except: pass
        try: node_Image_Texture_002.bl_width_min = 140.0
        except: pass
        try: node_Image_Texture_002.bl_width_max = 700.0
        except: pass
        try: node_Image_Texture_002.bl_height_default = 100.0
        except: pass
        try: node_Image_Texture_002.bl_height_min = 30.0
        except: pass
        try: node_Image_Texture_002.bl_height_max = 30.0
        except: pass
        try: node_Image_Texture_002.image = bpy.data.images['Image']
        except: pass
        try: node_Image_Texture_002.projection = 'FLAT'
        except: pass
        try: node_Image_Texture_002.interpolation = 'Linear'
        except: pass
        try: node_Image_Texture_002.projection_blend = 0.0
        except: pass
        try: node_Image_Texture_002.extension = 'REPEAT'
        except: pass
        created_nodes['Image Texture.002'] = node_Image_Texture_002
        node_Image_Texture_006 = group.nodes.new('ShaderNodeTexImage')
        node_Image_Texture_006.location_absolute = (259.27984619140625, 2229.54931640625)
        try: node_Image_Texture_006.location_absolute = Vector((259.27984619140625, 2229.54931640625))
        except: pass
        try: node_Image_Texture_006.warning_propagation = 'ALL'
        except: pass
        try: node_Image_Texture_006.mute = False
        except: pass
        try: node_Image_Texture_006.bl_label = 'Image Texture'
        except: pass
        try: node_Image_Texture_006.bl_description = 'Sample an image file as a texture'
        except: pass
        try: node_Image_Texture_006.bl_icon = 'NONE'
        except: pass
        try: node_Image_Texture_006.bl_width_default = 240.0
        except: pass
        try: node_Image_Texture_006.bl_width_min = 140.0
        except: pass
        try: node_Image_Texture_006.bl_width_max = 700.0
        except: pass
        try: node_Image_Texture_006.bl_height_default = 100.0
        except: pass
        try: node_Image_Texture_006.bl_height_min = 30.0
        except: pass
        try: node_Image_Texture_006.bl_height_max = 30.0
        except: pass
        try: node_Image_Texture_006.image = bpy.data.images['Image']
        except: pass
        try: node_Image_Texture_006.projection = 'FLAT'
        except: pass
        try: node_Image_Texture_006.interpolation = 'Linear'
        except: pass
        try: node_Image_Texture_006.projection_blend = 0.0
        except: pass
        try: node_Image_Texture_006.extension = 'REPEAT'
        except: pass
        created_nodes['Image Texture.006'] = node_Image_Texture_006
        node_Image_Texture_005 = group.nodes.new('ShaderNodeTexImage')
        node_Image_Texture_005.location_absolute = (268.3586730957031, 2666.984375)
        try: node_Image_Texture_005.location_absolute = Vector((268.3586730957031, 2666.984375))
        except: pass
        try: node_Image_Texture_005.warning_propagation = 'ALL'
        except: pass
        try: node_Image_Texture_005.mute = False
        except: pass
        try: node_Image_Texture_005.bl_label = 'Image Texture'
        except: pass
        try: node_Image_Texture_005.bl_description = 'Sample an image file as a texture'
        except: pass
        try: node_Image_Texture_005.bl_icon = 'NONE'
        except: pass
        try: node_Image_Texture_005.bl_width_default = 240.0
        except: pass
        try: node_Image_Texture_005.bl_width_min = 140.0
        except: pass
        try: node_Image_Texture_005.bl_width_max = 700.0
        except: pass
        try: node_Image_Texture_005.bl_height_default = 100.0
        except: pass
        try: node_Image_Texture_005.bl_height_min = 30.0
        except: pass
        try: node_Image_Texture_005.bl_height_max = 30.0
        except: pass
        try: node_Image_Texture_005.image = bpy.data.images['Image']
        except: pass
        try: node_Image_Texture_005.projection = 'FLAT'
        except: pass
        try: node_Image_Texture_005.interpolation = 'Linear'
        except: pass
        try: node_Image_Texture_005.projection_blend = 0.0
        except: pass
        try: node_Image_Texture_005.extension = 'REPEAT'
        except: pass
        created_nodes['Image Texture.005'] = node_Image_Texture_005

        # --- PACK NODES INTO FRAMES ---
        if 'Texture Coordinate.002' in created_nodes and 'Frame.005' in created_nodes:
            created_nodes['Texture Coordinate.002'].parent = created_nodes['Frame.005']
        if 'Mapping.001' in created_nodes and 'Frame' in created_nodes:
            created_nodes['Mapping.001'].parent = created_nodes['Frame']
        if 'Vector Math.002' in created_nodes and 'Frame.003' in created_nodes:
            created_nodes['Vector Math.002'].parent = created_nodes['Frame.003']
        if 'Vector Math.003' in created_nodes and 'Frame.003' in created_nodes:
            created_nodes['Vector Math.003'].parent = created_nodes['Frame.003']
        if 'Vector Math.001' in created_nodes and 'Frame.003' in created_nodes:
            created_nodes['Vector Math.001'].parent = created_nodes['Frame.003']
        if 'Vector Math.004' in created_nodes and 'Frame.003' in created_nodes:
            created_nodes['Vector Math.004'].parent = created_nodes['Frame.003']
        if 'Vector Rotate' in created_nodes and 'Frame' in created_nodes:
            created_nodes['Vector Rotate'].parent = created_nodes['Frame']
        if 'Combine XYZ' in created_nodes and 'Frame' in created_nodes:
            created_nodes['Combine XYZ'].parent = created_nodes['Frame']
        if 'Voronoi Texture.001' in created_nodes and 'Frame.005' in created_nodes:
            created_nodes['Voronoi Texture.001'].parent = created_nodes['Frame.005']
        if 'Map Range' in created_nodes and 'Frame.005' in created_nodes:
            created_nodes['Map Range'].parent = created_nodes['Frame.005']
        if 'Voronoi Texture.003' in created_nodes and 'Frame' in created_nodes:
            created_nodes['Voronoi Texture.003'].parent = created_nodes['Frame']
        if 'Noise Texture.002' in created_nodes and 'Frame' in created_nodes:
            created_nodes['Noise Texture.002'].parent = created_nodes['Frame']
        if 'Vector Math.006' in created_nodes and 'Frame' in created_nodes:
            created_nodes['Vector Math.006'].parent = created_nodes['Frame']
        if 'Math.006' in created_nodes and 'Frame' in created_nodes:
            created_nodes['Math.006'].parent = created_nodes['Frame']
        if 'Texture Coordinate.005' in created_nodes and 'Frame' in created_nodes:
            created_nodes['Texture Coordinate.005'].parent = created_nodes['Frame']
        if 'Separate XYZ' in created_nodes and 'Frame' in created_nodes:
            created_nodes['Separate XYZ'].parent = created_nodes['Frame']
        if 'Combine XYZ.003' in created_nodes and 'Frame' in created_nodes:
            created_nodes['Combine XYZ.003'].parent = created_nodes['Frame']
        if 'Frame' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Frame'].parent = created_nodes['Frame.004']
        if 'Mapping.002' in created_nodes and 'Frame.001' in created_nodes:
            created_nodes['Mapping.002'].parent = created_nodes['Frame.001']
        if 'Vector Rotate.001' in created_nodes and 'Frame.001' in created_nodes:
            created_nodes['Vector Rotate.001'].parent = created_nodes['Frame.001']
        if 'Combine XYZ.001' in created_nodes and 'Frame.001' in created_nodes:
            created_nodes['Combine XYZ.001'].parent = created_nodes['Frame.001']
        if 'Voronoi Texture.004' in created_nodes and 'Frame.001' in created_nodes:
            created_nodes['Voronoi Texture.004'].parent = created_nodes['Frame.001']
        if 'Noise Texture.003' in created_nodes and 'Frame.001' in created_nodes:
            created_nodes['Noise Texture.003'].parent = created_nodes['Frame.001']
        if 'Vector Math.007' in created_nodes and 'Frame.001' in created_nodes:
            created_nodes['Vector Math.007'].parent = created_nodes['Frame.001']
        if 'Math.007' in created_nodes and 'Frame.001' in created_nodes:
            created_nodes['Math.007'].parent = created_nodes['Frame.001']
        if 'Texture Coordinate.006' in created_nodes and 'Frame.001' in created_nodes:
            created_nodes['Texture Coordinate.006'].parent = created_nodes['Frame.001']
        if 'Separate XYZ.001' in created_nodes and 'Frame.001' in created_nodes:
            created_nodes['Separate XYZ.001'].parent = created_nodes['Frame.001']
        if 'Combine XYZ.004' in created_nodes and 'Frame.001' in created_nodes:
            created_nodes['Combine XYZ.004'].parent = created_nodes['Frame.001']
        if 'Frame.001' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Frame.001'].parent = created_nodes['Frame.004']
        if 'Mapping.003' in created_nodes and 'Frame.002' in created_nodes:
            created_nodes['Mapping.003'].parent = created_nodes['Frame.002']
        if 'Vector Rotate.002' in created_nodes and 'Frame.002' in created_nodes:
            created_nodes['Vector Rotate.002'].parent = created_nodes['Frame.002']
        if 'Combine XYZ.002' in created_nodes and 'Frame.002' in created_nodes:
            created_nodes['Combine XYZ.002'].parent = created_nodes['Frame.002']
        if 'Voronoi Texture.005' in created_nodes and 'Frame.002' in created_nodes:
            created_nodes['Voronoi Texture.005'].parent = created_nodes['Frame.002']
        if 'Noise Texture.004' in created_nodes and 'Frame.002' in created_nodes:
            created_nodes['Noise Texture.004'].parent = created_nodes['Frame.002']
        if 'Vector Math.008' in created_nodes and 'Frame.002' in created_nodes:
            created_nodes['Vector Math.008'].parent = created_nodes['Frame.002']
        if 'Math.008' in created_nodes and 'Frame.002' in created_nodes:
            created_nodes['Math.008'].parent = created_nodes['Frame.002']
        if 'Texture Coordinate.007' in created_nodes and 'Frame.002' in created_nodes:
            created_nodes['Texture Coordinate.007'].parent = created_nodes['Frame.002']
        if 'Separate XYZ.003' in created_nodes and 'Frame.002' in created_nodes:
            created_nodes['Separate XYZ.003'].parent = created_nodes['Frame.002']
        if 'Combine XYZ.005' in created_nodes and 'Frame.002' in created_nodes:
            created_nodes['Combine XYZ.005'].parent = created_nodes['Frame.002']
        if 'Frame.002' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Frame.002'].parent = created_nodes['Frame.004']
        if 'Texture Coordinate.003' in created_nodes and 'Frame.003' in created_nodes:
            created_nodes['Texture Coordinate.003'].parent = created_nodes['Frame.003']
        if 'Combine XYZ.006' in created_nodes and 'Frame.005' in created_nodes:
            created_nodes['Combine XYZ.006'].parent = created_nodes['Frame.005']
        if 'Separate XYZ.004' in created_nodes and 'Frame.005' in created_nodes:
            created_nodes['Separate XYZ.004'].parent = created_nodes['Frame.005']
        if 'Frame.005' in created_nodes and 'Frame.008' in created_nodes:
            created_nodes['Frame.005'].parent = created_nodes['Frame.008']
        if 'Texture Coordinate.004' in created_nodes and 'Frame.006' in created_nodes:
            created_nodes['Texture Coordinate.004'].parent = created_nodes['Frame.006']
        if 'Voronoi Texture.002' in created_nodes and 'Frame.006' in created_nodes:
            created_nodes['Voronoi Texture.002'].parent = created_nodes['Frame.006']
        if 'Map Range.001' in created_nodes and 'Frame.006' in created_nodes:
            created_nodes['Map Range.001'].parent = created_nodes['Frame.006']
        if 'Combine XYZ.007' in created_nodes and 'Frame.006' in created_nodes:
            created_nodes['Combine XYZ.007'].parent = created_nodes['Frame.006']
        if 'Separate XYZ.005' in created_nodes and 'Frame.006' in created_nodes:
            created_nodes['Separate XYZ.005'].parent = created_nodes['Frame.006']
        if 'Frame.006' in created_nodes and 'Frame.008' in created_nodes:
            created_nodes['Frame.006'].parent = created_nodes['Frame.008']
        if 'Texture Coordinate.008' in created_nodes and 'Frame.007' in created_nodes:
            created_nodes['Texture Coordinate.008'].parent = created_nodes['Frame.007']
        if 'Voronoi Texture.006' in created_nodes and 'Frame.007' in created_nodes:
            created_nodes['Voronoi Texture.006'].parent = created_nodes['Frame.007']
        if 'Map Range.002' in created_nodes and 'Frame.007' in created_nodes:
            created_nodes['Map Range.002'].parent = created_nodes['Frame.007']
        if 'Combine XYZ.008' in created_nodes and 'Frame.007' in created_nodes:
            created_nodes['Combine XYZ.008'].parent = created_nodes['Frame.007']
        if 'Separate XYZ.006' in created_nodes and 'Frame.007' in created_nodes:
            created_nodes['Separate XYZ.006'].parent = created_nodes['Frame.007']
        if 'Frame.007' in created_nodes and 'Frame.008' in created_nodes:
            created_nodes['Frame.007'].parent = created_nodes['Frame.008']
        if 'Texture Coordinate.009' in created_nodes and 'Frame.009' in created_nodes:
            created_nodes['Texture Coordinate.009'].parent = created_nodes['Frame.009']
        if 'Combine XYZ.009' in created_nodes and 'Frame.009' in created_nodes:
            created_nodes['Combine XYZ.009'].parent = created_nodes['Frame.009']
        if 'Separate XYZ.007' in created_nodes and 'Frame.009' in created_nodes:
            created_nodes['Separate XYZ.007'].parent = created_nodes['Frame.009']
        if 'Frame.009' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Frame.009'].parent = created_nodes['Frame.012']
        if 'Texture Coordinate.010' in created_nodes and 'Frame.010' in created_nodes:
            created_nodes['Texture Coordinate.010'].parent = created_nodes['Frame.010']
        if 'Combine XYZ.010' in created_nodes and 'Frame.010' in created_nodes:
            created_nodes['Combine XYZ.010'].parent = created_nodes['Frame.010']
        if 'Separate XYZ.008' in created_nodes and 'Frame.010' in created_nodes:
            created_nodes['Separate XYZ.008'].parent = created_nodes['Frame.010']
        if 'Frame.010' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Frame.010'].parent = created_nodes['Frame.012']
        if 'Texture Coordinate.011' in created_nodes and 'Frame.011' in created_nodes:
            created_nodes['Texture Coordinate.011'].parent = created_nodes['Frame.011']
        if 'Combine XYZ.011' in created_nodes and 'Frame.011' in created_nodes:
            created_nodes['Combine XYZ.011'].parent = created_nodes['Frame.011']
        if 'Separate XYZ.009' in created_nodes and 'Frame.011' in created_nodes:
            created_nodes['Separate XYZ.009'].parent = created_nodes['Frame.011']
        if 'Frame.011' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Frame.011'].parent = created_nodes['Frame.012']
        if 'Mapping' in created_nodes and 'Frame.011' in created_nodes:
            created_nodes['Mapping'].parent = created_nodes['Frame.011']
        if 'Mapping.004' in created_nodes and 'Frame.010' in created_nodes:
            created_nodes['Mapping.004'].parent = created_nodes['Frame.010']
        if 'Mapping.005' in created_nodes and 'Frame.009' in created_nodes:
            created_nodes['Mapping.005'].parent = created_nodes['Frame.009']
        if 'Vector Math.005' in created_nodes and 'Frame.003' in created_nodes:
            created_nodes['Vector Math.005'].parent = created_nodes['Frame.003']
        if 'Vector Math.009' in created_nodes and 'Frame.003' in created_nodes:
            created_nodes['Vector Math.009'].parent = created_nodes['Frame.003']
        if 'Separate XYZ.002' in created_nodes and 'Frame.003' in created_nodes:
            created_nodes['Separate XYZ.002'].parent = created_nodes['Frame.003']
        if 'Separate XYZ.010' in created_nodes and 'Frame.003' in created_nodes:
            created_nodes['Separate XYZ.010'].parent = created_nodes['Frame.003']
        if 'Image Texture' in created_nodes and 'Frame' in created_nodes:
            created_nodes['Image Texture'].parent = created_nodes['Frame']
        if 'Image Texture.001' in created_nodes and 'Frame.001' in created_nodes:
            created_nodes['Image Texture.001'].parent = created_nodes['Frame.001']
        if 'Image Texture.004' in created_nodes and 'Frame.002' in created_nodes:
            created_nodes['Image Texture.004'].parent = created_nodes['Frame.002']
        if 'Image Texture.002' in created_nodes and 'Frame.009' in created_nodes:
            created_nodes['Image Texture.002'].parent = created_nodes['Frame.009']
        if 'Image Texture.006' in created_nodes and 'Frame.010' in created_nodes:
            created_nodes['Image Texture.006'].parent = created_nodes['Frame.010']
        if 'Image Texture.005' in created_nodes and 'Frame.011' in created_nodes:
            created_nodes['Image Texture.005'].parent = created_nodes['Frame.011']

        # --- CONNECT LINKS ---
        try: group.links.new(created_nodes['Mix'].outputs[2], created_nodes['Mix.001'].inputs[6])
        except: pass
        try: group.links.new(created_nodes['Vector Math.002'].outputs[0], created_nodes['Vector Math.003'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.004'].outputs[0], created_nodes['Vector Math.001'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Combine XYZ'].outputs[0], created_nodes['Vector Rotate'].inputs[4])
        except: pass
        try: group.links.new(created_nodes['Vector Rotate'].outputs[0], created_nodes['Mapping.001'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Mix.001'].outputs[2], created_nodes['Mix.002'].inputs[7])
        except: pass
        try: group.links.new(created_nodes['Voronoi Texture.001'].outputs[0], created_nodes['Map Range'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Group Input'].outputs[2], created_nodes['Math.001'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Math.001'].outputs[0], created_nodes['Math.002'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Group Input'].outputs[1], created_nodes['Math.004'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Voronoi Texture.003'].outputs[2], created_nodes['Vector Math.006'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Noise Texture.002'].outputs[0], created_nodes['Math.006'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.006'].outputs[0], created_nodes['Vector Rotate'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Texture Coordinate.005'].outputs[3], created_nodes['Separate XYZ'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Combine XYZ.003'].outputs[0], created_nodes['Vector Math.006'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Combine XYZ.003'].outputs[0], created_nodes['Voronoi Texture.003'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ'].outputs[2], created_nodes['Combine XYZ.003'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ'].outputs[1], created_nodes['Combine XYZ.003'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Math.006'].outputs[0], created_nodes['Combine XYZ'].inputs[2])
        except: pass
        try: group.links.new(created_nodes['Combine XYZ.001'].outputs[0], created_nodes['Vector Rotate.001'].inputs[4])
        except: pass
        try: group.links.new(created_nodes['Vector Rotate.001'].outputs[0], created_nodes['Mapping.002'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Voronoi Texture.004'].outputs[2], created_nodes['Vector Math.007'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Noise Texture.003'].outputs[0], created_nodes['Math.007'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.007'].outputs[0], created_nodes['Vector Rotate.001'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Texture Coordinate.006'].outputs[3], created_nodes['Separate XYZ.001'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Combine XYZ.004'].outputs[0], created_nodes['Vector Math.007'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Combine XYZ.004'].outputs[0], created_nodes['Voronoi Texture.004'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.001'].outputs[2], created_nodes['Combine XYZ.004'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Math.007'].outputs[0], created_nodes['Combine XYZ.001'].inputs[2])
        except: pass
        try: group.links.new(created_nodes['Combine XYZ.002'].outputs[0], created_nodes['Vector Rotate.002'].inputs[4])
        except: pass
        try: group.links.new(created_nodes['Vector Rotate.002'].outputs[0], created_nodes['Mapping.003'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Voronoi Texture.005'].outputs[2], created_nodes['Vector Math.008'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Noise Texture.004'].outputs[0], created_nodes['Math.008'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.008'].outputs[0], created_nodes['Vector Rotate.002'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Texture Coordinate.007'].outputs[3], created_nodes['Separate XYZ.003'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Combine XYZ.005'].outputs[0], created_nodes['Vector Math.008'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Combine XYZ.005'].outputs[0], created_nodes['Voronoi Texture.005'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Math.008'].outputs[0], created_nodes['Combine XYZ.002'].inputs[2])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.001'].outputs[0], created_nodes['Combine XYZ.004'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.003'].outputs[0], created_nodes['Combine XYZ.005'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.003'].outputs[1], created_nodes['Combine XYZ.005'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Texture Coordinate.003'].outputs[1], created_nodes['Vector Math.004'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Combine XYZ.006'].outputs[0], created_nodes['Voronoi Texture.001'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.004'].outputs[0], created_nodes['Combine XYZ.006'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.004'].outputs[1], created_nodes['Combine XYZ.006'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Texture Coordinate.002'].outputs[3], created_nodes['Separate XYZ.004'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Voronoi Texture.002'].outputs[0], created_nodes['Map Range.001'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Combine XYZ.007'].outputs[0], created_nodes['Voronoi Texture.002'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.005'].outputs[0], created_nodes['Combine XYZ.007'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Texture Coordinate.004'].outputs[3], created_nodes['Separate XYZ.005'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Voronoi Texture.006'].outputs[0], created_nodes['Map Range.002'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Combine XYZ.008'].outputs[0], created_nodes['Voronoi Texture.006'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Texture Coordinate.008'].outputs[3], created_nodes['Separate XYZ.006'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.006'].outputs[1], created_nodes['Combine XYZ.008'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.006'].outputs[2], created_nodes['Combine XYZ.008'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.005'].outputs[2], created_nodes['Combine XYZ.007'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Mix.003'].outputs[2], created_nodes['Mix.004'].inputs[6])
        except: pass
        try: group.links.new(created_nodes['Map Range.002'].outputs[0], created_nodes['Mix.003'].inputs[6])
        except: pass
        try: group.links.new(created_nodes['Map Range.001'].outputs[0], created_nodes['Mix.003'].inputs[7])
        except: pass
        try: group.links.new(created_nodes['Map Range'].outputs[0], created_nodes['Mix.004'].inputs[7])
        except: pass
        try: group.links.new(created_nodes['Mix.004'].outputs[2], created_nodes['Mix.002'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.007'].outputs[0], created_nodes['Combine XYZ.009'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.007'].outputs[1], created_nodes['Combine XYZ.009'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Texture Coordinate.009'].outputs[3], created_nodes['Separate XYZ.007'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.008'].outputs[0], created_nodes['Combine XYZ.010'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Texture Coordinate.010'].outputs[3], created_nodes['Separate XYZ.008'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Texture Coordinate.011'].outputs[3], created_nodes['Separate XYZ.009'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.009'].outputs[1], created_nodes['Combine XYZ.011'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.009'].outputs[2], created_nodes['Combine XYZ.011'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.008'].outputs[2], created_nodes['Combine XYZ.010'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Mix.005'].outputs[2], created_nodes['Mix.006'].inputs[6])
        except: pass
        try: group.links.new(created_nodes['Image Texture.005'].outputs[0], created_nodes['Mix.005'].inputs[6])
        except: pass
        try: group.links.new(created_nodes['Image Texture.006'].outputs[0], created_nodes['Mix.005'].inputs[7])
        except: pass
        try: group.links.new(created_nodes['Image Texture.002'].outputs[0], created_nodes['Mix.006'].inputs[7])
        except: pass
        try: group.links.new(created_nodes['Mix.006'].outputs[2], created_nodes['Mix.002'].inputs[6])
        except: pass
        try: group.links.new(created_nodes['Math.002'].outputs[0], created_nodes['Map Range.002'].inputs[2])
        except: pass
        try: group.links.new(created_nodes['Math.002'].outputs[0], created_nodes['Map Range.001'].inputs[2])
        except: pass
        try: group.links.new(created_nodes['Math.002'].outputs[0], created_nodes['Map Range'].inputs[2])
        except: pass
        try: group.links.new(created_nodes['Combine XYZ.011'].outputs[0], created_nodes['Mapping'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Combine XYZ.010'].outputs[0], created_nodes['Mapping.004'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Combine XYZ.009'].outputs[0], created_nodes['Mapping.005'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Math.004'].outputs[0], created_nodes['Voronoi Texture.003'].inputs[2])
        except: pass
        try: group.links.new(created_nodes['Math.004'].outputs[0], created_nodes['Voronoi Texture.004'].inputs[2])
        except: pass
        try: group.links.new(created_nodes['Math.004'].outputs[0], created_nodes['Voronoi Texture.005'].inputs[2])
        except: pass
        try: group.links.new(created_nodes['Math.004'].outputs[0], created_nodes['Voronoi Texture.006'].inputs[2])
        except: pass
        try: group.links.new(created_nodes['Math.004'].outputs[0], created_nodes['Voronoi Texture.002'].inputs[2])
        except: pass
        try: group.links.new(created_nodes['Math.004'].outputs[0], created_nodes['Voronoi Texture.001'].inputs[2])
        except: pass
        try: group.links.new(created_nodes['Group Input'].outputs[0], created_nodes['Math'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Math'].outputs[0], created_nodes['Mapping.002'].inputs[3])
        except: pass
        try: group.links.new(created_nodes['Math'].outputs[0], created_nodes['Mapping.003'].inputs[3])
        except: pass
        try: group.links.new(created_nodes['Math'].outputs[0], created_nodes['Mapping.001'].inputs[3])
        except: pass
        try: group.links.new(created_nodes['Math'].outputs[0], created_nodes['Mapping.005'].inputs[3])
        except: pass
        try: group.links.new(created_nodes['Math'].outputs[0], created_nodes['Mapping.004'].inputs[3])
        except: pass
        try: group.links.new(created_nodes['Math'].outputs[0], created_nodes['Mapping'].inputs[3])
        except: pass
        try: group.links.new(created_nodes['Group Input'].outputs[3], created_nodes['Vector Math.002'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.005'].outputs[0], created_nodes['Vector Math.009'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Group Input'].outputs[4], created_nodes['Vector Math.005'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.001'].outputs[0], created_nodes['Vector Math.002'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.001'].outputs[0], created_nodes['Vector Math.005'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.009'].outputs[0], created_nodes['Separate XYZ.002'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.002'].outputs[2], created_nodes['Mix.001'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.002'].outputs[2], created_nodes['Mix.004'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.002'].outputs[2], created_nodes['Mix.006'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.003'].outputs[0], created_nodes['Separate XYZ.010'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.010'].outputs[1], created_nodes['Mix.003'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.010'].outputs[1], created_nodes['Mix'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.010'].outputs[1], created_nodes['Mix.005'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Mapping.001'].outputs[0], created_nodes['Image Texture'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Mapping.002'].outputs[0], created_nodes['Image Texture.001'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Mapping.003'].outputs[0], created_nodes['Image Texture.004'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Mapping.005'].outputs[0], created_nodes['Image Texture.002'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Mapping.004'].outputs[0], created_nodes['Image Texture.006'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Mapping'].outputs[0], created_nodes['Image Texture.005'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Voronoi Texture.005'].outputs[2], created_nodes['Noise Texture.004'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Voronoi Texture.004'].outputs[2], created_nodes['Noise Texture.003'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Voronoi Texture.003'].outputs[2], created_nodes['Noise Texture.002'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Mix.002'].outputs[2], created_nodes['Group Output'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Image Texture.004'].outputs[0], created_nodes['Mix.001'].inputs[7])
        except: pass
        try: group.links.new(created_nodes['Image Texture.001'].outputs[0], created_nodes['Mix'].inputs[7])
        except: pass
        try: group.links.new(created_nodes['Image Texture'].outputs[0], created_nodes['Mix'].inputs[6])
        except: pass

        self.node_tree = group
        if hasattr(self, "update_image"):
            self.update_image(context)

    def draw_buttons(self, context, layout):
        layout.template_ID(self, "image_pointer", open="image.open")

    def free(self):
        if self.node_tree and self.node_tree.users <= 1:
            try: bpy.data.node_groups.remove(self.node_tree)
            except: pass


# --- COLLISION-FREE SHARED MENU SYSTEM ---
class NODE_MT_custom_nodes_submenu(bpy.types.Menu):
    bl_label = "Custom Nodes"
    bl_idname = "NODE_MT_custom_nodes_submenu"

    def draw(self, context):
        pass

def draw_in_main_menu(self, context):
    if getattr(self, "bl_idname", "") == "NODE_MT_shader_node_add_all":
        layout = self.layout
        layout.separator()
        layout.menu("NODE_MT_custom_nodes_submenu")

def append_to_submenu(self, context):
    self.layout.operator("node.add_node", text="TriplanarVoronoi").type = Generated_TriplanarVoronoi_Node.bl_idname

def register():
    bpy.utils.register_class(Generated_TriplanarVoronoi_Node)
    
    if not hasattr(bpy.types, "NODE_MT_custom_nodes_submenu"):
        bpy.utils.register_class(NODE_MT_custom_nodes_submenu)
        bpy.types.NODE_MT_shader_node_add_all.append(draw_in_main_menu)
        
    bpy.types.NODE_MT_custom_nodes_submenu.append(append_to_submenu)

def unregister():
    try: bpy.types.NODE_MT_custom_nodes_submenu.remove(append_to_submenu)
    except: pass
    
    try:
        if hasattr(bpy.types, "NODE_MT_custom_nodes_submenu"):
            if not getattr(bpy.types.NODE_MT_custom_nodes_submenu, "_draw_funcs", None):
                bpy.types.NODE_MT_shader_node_add_all.remove(draw_in_main_menu)
                bpy.utils.unregister_class(NODE_MT_custom_nodes_submenu)
    except: pass
    
    bpy.utils.unregister_class(Generated_TriplanarVoronoi_Node)

if __name__ == "__main__":
    register()
