bl_info = {
    "name": "Custom Node - TriplanarVoronoiNormal",
    "author": "MoxTools Generator",
    "version": (1, 0, 0),
    "blender": (4, 0, 0),
    "location": "Shader Editor > Shift+A > Custom Nodes",
    "description": "Automatically exported standalone custom node",
    "category": "Node",
}

import bpy
from bpy.types import ShaderNodeCustomGroup

class Generated_TriplanarVoronoiNormal_Node(ShaderNodeCustomGroup):
    bl_idname = 'ShaderNode_TriplanarVoronoiNormal_Generated'
    bl_label = 'TriplanarVoronoiNormal'
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
        tree_name = f'.internal_TriplanarVoronoiNormal_' + str(id(self))
        group = bpy.data.node_groups.new(name=tree_name, type='ShaderNodeTree')

        sock = group.interface.new_socket(name='Color', in_out='OUTPUT', socket_type='NodeSocketColor')
        try: sock.default_value = bpy.data.node_groups['TriplanarVoronoiNormal'].interface.items_tree[0].default_value
        except: pass
        sock = group.interface.new_socket(name='Invert Green', in_out='INPUT', socket_type='NodeSocketBool')
        try: sock.default_value = False
        except: pass
        sock = group.interface.new_socket(name='NormalStrength', in_out='INPUT', socket_type='NodeSocketFloat')
        try: sock.default_value = 100.0
        except: pass
        try: sock.min_value = 0.0
        except: pass
        try: sock.max_value = 200.0
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

        group_input.location_absolute = (-6558.4267578125, 355.03961181640625)
        group_output.location_absolute = (2439.78173828125, 324.6109619140625)
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
        node_Mapping_001.location_absolute = (-3253.146728515625, -214.394775390625)
        try: node_Mapping_001.location_absolute = Vector((-3253.146728515625, -214.394775390625))
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
        node_Mix.location_absolute = (920.67919921875, -212.11581420898438)
        try: node_Mix.location_absolute = Vector((920.67919921875, -212.11581420898438))
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
        node_Mix_001.location_absolute = (1150.86767578125, -864.54736328125)
        try: node_Mix_001.location_absolute = Vector((1150.86767578125, -864.54736328125))
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
        node_Vector_Rotate.location_absolute = (-3435.88037109375, -212.56875610351562)
        try: node_Vector_Rotate.location_absolute = Vector((-3435.88037109375, -212.56875610351562))
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
        node_Combine_XYZ.location_absolute = (-3631.01123046875, -418.55145263671875)
        try: node_Combine_XYZ.location_absolute = Vector((-3631.01123046875, -418.55145263671875))
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
        node_Mix_002.location_absolute = (2033.6298828125, 591.8543090820312)
        try: node_Mix_002.location_absolute = Vector((2033.6298828125, 591.8543090820312))
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
        node_Math_001.location_absolute = (-1098.7052001953125, 777.2348022460938)
        try: node_Math_001.location_absolute = Vector((-1098.7052001953125, 777.2348022460938))
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
        node_Math_002.location_absolute = (-794.9927978515625, 776.4271850585938)
        try: node_Math_002.location_absolute = Vector((-794.9927978515625, 776.4271850585938))
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
        node_Math_004.location_absolute = (-5741.64697265625, 880.7310791015625)
        try: node_Math_004.location_absolute = Vector((-5741.64697265625, 880.7310791015625))
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
        node_Voronoi_Texture_003.location_absolute = (-4252.7138671875, -353.4466247558594)
        try: node_Voronoi_Texture_003.location_absolute = Vector((-4252.7138671875, -353.4466247558594))
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
        node_Noise_Texture_002.location_absolute = (-4021.925048828125, -407.0015563964844)
        try: node_Noise_Texture_002.location_absolute = Vector((-4021.925048828125, -407.0015563964844))
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
        node_Vector_Math_006.location_absolute = (-4039.960205078125, -253.4073028564453)
        try: node_Vector_Math_006.location_absolute = Vector((-4039.960205078125, -253.4073028564453))
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
        node_Math_006.location_absolute = (-3831.37744140625, -533.3214111328125)
        try: node_Math_006.location_absolute = Vector((-3831.37744140625, -533.3214111328125))
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
        node_Texture_Coordinate_005.location_absolute = (-4805.4248046875, -302.175537109375)
        try: node_Texture_Coordinate_005.location_absolute = Vector((-4805.4248046875, -302.175537109375))
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
        node_Separate_XYZ.location_absolute = (-4619.35546875, -303.6339416503906)
        try: node_Separate_XYZ.location_absolute = Vector((-4619.35546875, -303.6339416503906))
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
        node_Combine_XYZ_003.location_absolute = (-4441.45703125, -303.6339416503906)
        try: node_Combine_XYZ_003.location_absolute = Vector((-4441.45703125, -303.6339416503906))
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
        node_Frame.location_absolute = (-4835.60009765625, -176.8000030517578)
        node_Frame.label = 'X'
        node_Frame.shrink = True
        try: node_Frame.location_absolute = Vector((-4835.60009765625, -176.8000030517578))
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
        node_Mapping_002.location_absolute = (-3244.6396484375, -953.0654296875)
        try: node_Mapping_002.location_absolute = Vector((-3244.6396484375, -953.0654296875))
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
        node_Vector_Rotate_001.location_absolute = (-3427.372314453125, -951.2392578125)
        try: node_Vector_Rotate_001.location_absolute = Vector((-3427.372314453125, -951.2392578125))
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
        node_Combine_XYZ_001.location_absolute = (-3622.503173828125, -1157.2222900390625)
        try: node_Combine_XYZ_001.location_absolute = Vector((-3622.503173828125, -1157.2222900390625))
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
        node_Voronoi_Texture_004.location_absolute = (-4244.205078125, -1092.1175537109375)
        try: node_Voronoi_Texture_004.location_absolute = Vector((-4244.205078125, -1092.1175537109375))
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
        node_Noise_Texture_003.location_absolute = (-4013.41650390625, -1145.6724853515625)
        try: node_Noise_Texture_003.location_absolute = Vector((-4013.41650390625, -1145.6724853515625))
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
        node_Vector_Math_007.location_absolute = (-4031.45166015625, -992.0779418945312)
        try: node_Vector_Math_007.location_absolute = Vector((-4031.45166015625, -992.0779418945312))
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
        node_Math_007.location_absolute = (-3823.98828125, -1277.386962890625)
        try: node_Math_007.location_absolute = Vector((-3823.98828125, -1277.386962890625))
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
        node_Texture_Coordinate_006.location_absolute = (-4796.91650390625, -1040.8463134765625)
        try: node_Texture_Coordinate_006.location_absolute = Vector((-4796.91650390625, -1040.8463134765625))
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
        node_Separate_XYZ_001.location_absolute = (-4610.84619140625, -1042.304443359375)
        try: node_Separate_XYZ_001.location_absolute = Vector((-4610.84619140625, -1042.304443359375))
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
        node_Combine_XYZ_004.location_absolute = (-4432.94775390625, -1042.304443359375)
        try: node_Combine_XYZ_004.location_absolute = Vector((-4432.94775390625, -1042.304443359375))
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
        node_Frame_001.location_absolute = (-4826.7998046875, -915.2000122070312)
        node_Frame_001.label = 'Y'
        node_Frame_001.shrink = True
        try: node_Frame_001.location_absolute = Vector((-4826.7998046875, -915.2000122070312))
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
        node_Mapping_003.location_absolute = (-3256.823974609375, -1746.824462890625)
        try: node_Mapping_003.location_absolute = Vector((-3256.823974609375, -1746.824462890625))
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
        node_Vector_Rotate_002.location_absolute = (-3439.556640625, -1744.998291015625)
        try: node_Vector_Rotate_002.location_absolute = Vector((-3439.556640625, -1744.998291015625))
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
        node_Combine_XYZ_002.location_absolute = (-3634.6875, -1950.980712890625)
        try: node_Combine_XYZ_002.location_absolute = Vector((-3634.6875, -1950.980712890625))
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
        node_Voronoi_Texture_005.location_absolute = (-4256.390625, -1885.875732421875)
        try: node_Voronoi_Texture_005.location_absolute = Vector((-4256.390625, -1885.875732421875))
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
        node_Noise_Texture_004.location_absolute = (-4025.6015625, -1939.4306640625)
        try: node_Noise_Texture_004.location_absolute = Vector((-4025.6015625, -1939.4306640625))
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
        node_Vector_Math_008.location_absolute = (-4043.63671875, -1785.8363037109375)
        try: node_Vector_Math_008.location_absolute = Vector((-4043.63671875, -1785.8363037109375))
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
        node_Math_008.location_absolute = (-3822.263671875, -2059.7099609375)
        try: node_Math_008.location_absolute = Vector((-3822.263671875, -2059.7099609375))
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
        node_Texture_Coordinate_007.location_absolute = (-4809.1005859375, -1834.6044921875)
        try: node_Texture_Coordinate_007.location_absolute = Vector((-4809.1005859375, -1834.6044921875))
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
        node_Separate_XYZ_003.location_absolute = (-4623.0322265625, -1836.063232421875)
        try: node_Separate_XYZ_003.location_absolute = Vector((-4623.0322265625, -1836.063232421875))
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
        node_Combine_XYZ_005.location_absolute = (-4445.1337890625, -1836.063232421875)
        try: node_Combine_XYZ_005.location_absolute = Vector((-4445.1337890625, -1836.063232421875))
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
        node_Frame_002.location_absolute = (-4838.7998046875, -1702.4000244140625)
        node_Frame_002.label = 'Z'
        node_Frame_002.shrink = True
        try: node_Frame_002.location_absolute = Vector((-4838.7998046875, -1702.4000244140625))
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
        node_Frame_004.location_absolute = (-4868.7998046875, -146.8000030517578)
        node_Frame_004.shrink = True
        try: node_Frame_004.location_absolute = Vector((-4868.7998046875, -146.8000030517578))
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
        node_Texture_Coordinate_009.location_absolute = (-3642.389892578125, 2210.8388671875)
        try: node_Texture_Coordinate_009.location_absolute = Vector((-3642.389892578125, 2210.8388671875))
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
        node_Combine_XYZ_009.location_absolute = (-3267.60498046875, 2186.28369140625)
        try: node_Combine_XYZ_009.location_absolute = Vector((-3267.60498046875, 2186.28369140625))
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
        node_Separate_XYZ_007.location_absolute = (-3459.73974609375, 2185.392822265625)
        try: node_Separate_XYZ_007.location_absolute = Vector((-3459.73974609375, 2185.392822265625))
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
        node_Frame_009.location_absolute = (-3672.39990234375, 2247.199951171875)
        node_Frame_009.label = 'Z'
        node_Frame_009.shrink = True
        try: node_Frame_009.location_absolute = Vector((-3672.39990234375, 2247.199951171875))
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
        node_Texture_Coordinate_010.location_absolute = (-3647.331298828125, 2816.911865234375)
        try: node_Texture_Coordinate_010.location_absolute = Vector((-3647.331298828125, 2816.911865234375))
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
        node_Combine_XYZ_010.location_absolute = (-3272.546630859375, 2792.35693359375)
        try: node_Combine_XYZ_010.location_absolute = Vector((-3272.546630859375, 2792.35693359375))
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
        node_Separate_XYZ_008.location_absolute = (-3464.681640625, 2791.4658203125)
        try: node_Separate_XYZ_008.location_absolute = Vector((-3464.681640625, 2791.4658203125))
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
        node_Frame_010.location_absolute = (-3677.199951171875, 2852.800048828125)
        node_Frame_010.label = 'Y'
        node_Frame_010.shrink = True
        try: node_Frame_010.location_absolute = Vector((-3677.199951171875, 2852.800048828125))
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
        node_Texture_Coordinate_011.location_absolute = (-3644.048095703125, 3409.686767578125)
        try: node_Texture_Coordinate_011.location_absolute = Vector((-3644.048095703125, 3409.686767578125))
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
        node_Combine_XYZ_011.location_absolute = (-3269.26318359375, 3385.131591796875)
        try: node_Combine_XYZ_011.location_absolute = Vector((-3269.26318359375, 3385.131591796875))
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
        node_Separate_XYZ_009.location_absolute = (-3461.39794921875, 3384.24072265625)
        try: node_Separate_XYZ_009.location_absolute = Vector((-3461.39794921875, 3384.24072265625))
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
        node_Frame_011.location_absolute = (-3674.0, 3445.60009765625)
        node_Frame_011.label = 'X'
        node_Frame_011.shrink = True
        try: node_Frame_011.location_absolute = Vector((-3674.0, 3445.60009765625))
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
        node_Frame_012.location_absolute = (-3707.199951171875, 3499.60009765625)
        node_Frame_012.shrink = True
        try: node_Frame_012.location_absolute = Vector((-3707.199951171875, 3499.60009765625))
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
        node_Math = group.nodes.new('ShaderNodeMath')
        node_Math.location_absolute = (-5732.74853515625, 1282.1588134765625)
        try: node_Math.location_absolute = Vector((-5732.74853515625, 1282.1588134765625))
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
        node_Vector_Math_005.location_absolute = (-43.66376876831055, 48.11513137817383)
        try: node_Vector_Math_005.location_absolute = Vector((-43.66376876831055, 48.11513137817383))
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
        node_Image_Texture.location_absolute = (-3073.23876953125, -222.14443969726562)
        try: node_Image_Texture.location_absolute = Vector((-3073.23876953125, -222.14443969726562))
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
        try: node_Image_Texture.image = bpy.data.images['bricks2_normal.jpg']
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
        node_Image_Texture_001.location_absolute = (-3065.92236328125, -955.1875)
        try: node_Image_Texture_001.location_absolute = Vector((-3065.92236328125, -955.1875))
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
        try: node_Image_Texture_001.image = bpy.data.images['bricks2_normal.jpg']
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
        node_Image_Texture_004.location_absolute = (-3047.0380859375, -1738.129150390625)
        try: node_Image_Texture_004.location_absolute = Vector((-3047.0380859375, -1738.129150390625))
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
        try: node_Image_Texture_004.image = bpy.data.images['bricks2_normal.jpg']
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
        node_Image_Texture_002.location_absolute = (-2887.82275390625, 2209.90771484375)
        try: node_Image_Texture_002.location_absolute = Vector((-2887.82275390625, 2209.90771484375))
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
        try: node_Image_Texture_002.image = bpy.data.images['bricks2_normal.jpg']
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
        node_Image_Texture_006.location_absolute = (-2871.390625, 2813.02490234375)
        try: node_Image_Texture_006.location_absolute = Vector((-2871.390625, 2813.02490234375))
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
        try: node_Image_Texture_006.image = bpy.data.images['bricks2_normal.jpg']
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
        node_Image_Texture_005.location_absolute = (-2865.805908203125, 3399.88037109375)
        try: node_Image_Texture_005.location_absolute = Vector((-2865.805908203125, 3399.88037109375))
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
        try: node_Image_Texture_005.image = bpy.data.images['bricks2_normal.jpg']
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
        node_Vector_Math_013 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_013.location_absolute = (-2111.37060546875, -960.2312622070312)
        try: node_Vector_Math_013.location_absolute = Vector((-2111.37060546875, -960.2312622070312))
        except: pass
        try: node_Vector_Math_013.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_013.mute = False
        except: pass
        try: node_Vector_Math_013.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_013.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_013.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_013.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_013.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_013.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_013.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_013.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_013.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_013.operation = 'MULTIPLY'
        except: pass
        try: node_Vector_Math_013.inputs[1].default_value = [2.0,2.0,2.0]
        except: pass
        try: node_Vector_Math_013.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_013.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.013'] = node_Vector_Math_013
        node_Vector_Math_014 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_014.location_absolute = (-1933.265869140625, -962.8917846679688)
        try: node_Vector_Math_014.location_absolute = Vector((-1933.265869140625, -962.8917846679688))
        except: pass
        try: node_Vector_Math_014.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_014.mute = False
        except: pass
        try: node_Vector_Math_014.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_014.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_014.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_014.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_014.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_014.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_014.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_014.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_014.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_014.operation = 'SUBTRACT'
        except: pass
        try: node_Vector_Math_014.inputs[1].default_value = [1.0,1.0,1.0]
        except: pass
        try: node_Vector_Math_014.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_014.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.014'] = node_Vector_Math_014
        node_Frame_016 = group.nodes.new('NodeFrame')
        node_Frame_016.location_absolute = (-2141.199951171875, -924.0)
        node_Frame_016.label = 'Unpack'
        node_Frame_016.shrink = True
        try: node_Frame_016.location_absolute = Vector((-2141.199951171875, -924.0))
        except: pass
        try: node_Frame_016.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_016.mute = False
        except: pass
        try: node_Frame_016.bl_label = 'Frame'
        except: pass
        try: node_Frame_016.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_016.bl_icon = 'NONE'
        except: pass
        try: node_Frame_016.bl_width_default = 150.0
        except: pass
        try: node_Frame_016.bl_width_min = 100.0
        except: pass
        try: node_Frame_016.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_016.bl_height_default = 100.0
        except: pass
        try: node_Frame_016.bl_height_min = 30.0
        except: pass
        try: node_Frame_016.bl_height_max = 30.0
        except: pass
        try: node_Frame_016.text = None
        except: pass
        try: node_Frame_016.shrink = True
        except: pass
        try: node_Frame_016.label_size = 20
        except: pass
        created_nodes['Frame.016'] = node_Frame_016
        node_Vector_Transform_003 = group.nodes.new('ShaderNodeVectorTransform')
        node_Vector_Transform_003.location_absolute = (1449.9486083984375, -765.4405517578125)
        try: node_Vector_Transform_003.location_absolute = Vector((1449.9486083984375, -765.4405517578125))
        except: pass
        try: node_Vector_Transform_003.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Transform_003.mute = False
        except: pass
        try: node_Vector_Transform_003.bl_label = 'Vector Transform'
        except: pass
        try: node_Vector_Transform_003.bl_description = 'Convert a vector, point, or normal between world, camera, and object coordinate space'
        except: pass
        try: node_Vector_Transform_003.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Transform_003.bl_width_default = 140.0
        except: pass
        try: node_Vector_Transform_003.bl_width_min = 100.0
        except: pass
        try: node_Vector_Transform_003.bl_width_max = 700.0
        except: pass
        try: node_Vector_Transform_003.bl_height_default = 100.0
        except: pass
        try: node_Vector_Transform_003.bl_height_min = 30.0
        except: pass
        try: node_Vector_Transform_003.bl_height_max = 30.0
        except: pass
        try: node_Vector_Transform_003.vector_type = 'NORMAL'
        except: pass
        try: node_Vector_Transform_003.convert_from = 'OBJECT'
        except: pass
        try: node_Vector_Transform_003.convert_to = 'WORLD'
        except: pass
        created_nodes['Vector Transform.003'] = node_Vector_Transform_003
        node_Texture_Coordinate_023 = group.nodes.new('ShaderNodeTexCoord')
        node_Texture_Coordinate_023.location_absolute = (-1013.8455810546875, -1151.9163818359375)
        try: node_Texture_Coordinate_023.location_absolute = Vector((-1013.8455810546875, -1151.9163818359375))
        except: pass
        try: node_Texture_Coordinate_023.warning_propagation = 'ALL'
        except: pass
        try: node_Texture_Coordinate_023.mute = False
        except: pass
        try: node_Texture_Coordinate_023.bl_label = 'Texture Coordinate'
        except: pass
        try: node_Texture_Coordinate_023.bl_description = 'Retrieve multiple types of texture coordinates.\nTypically used as inputs for texture nodes'
        except: pass
        try: node_Texture_Coordinate_023.bl_icon = 'NONE'
        except: pass
        try: node_Texture_Coordinate_023.bl_width_default = 140.0
        except: pass
        try: node_Texture_Coordinate_023.bl_width_min = 100.0
        except: pass
        try: node_Texture_Coordinate_023.bl_width_max = 700.0
        except: pass
        try: node_Texture_Coordinate_023.bl_height_default = 100.0
        except: pass
        try: node_Texture_Coordinate_023.bl_height_min = 30.0
        except: pass
        try: node_Texture_Coordinate_023.bl_height_max = 30.0
        except: pass
        try: node_Texture_Coordinate_023.object = None
        except: pass
        try: node_Texture_Coordinate_023.from_instancer = False
        except: pass
        created_nodes['Texture Coordinate.023'] = node_Texture_Coordinate_023
        node_Vector_Math_028 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_028.location_absolute = (-751.36962890625, -1287.435791015625)
        try: node_Vector_Math_028.location_absolute = Vector((-751.36962890625, -1287.435791015625))
        except: pass
        try: node_Vector_Math_028.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_028.mute = False
        except: pass
        try: node_Vector_Math_028.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_028.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_028.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_028.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_028.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_028.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_028.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_028.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_028.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_028.operation = 'CROSS_PRODUCT'
        except: pass
        try: node_Vector_Math_028.inputs[1].default_value = [0.0,0.0,1.0]
        except: pass
        try: node_Vector_Math_028.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_028.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.028'] = node_Vector_Math_028
        node_Vector_Math_042 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_042.location_absolute = (-630.5394287109375, -1132.607666015625)
        try: node_Vector_Math_042.location_absolute = Vector((-630.5394287109375, -1132.607666015625))
        except: pass
        try: node_Vector_Math_042.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_042.mute = False
        except: pass
        try: node_Vector_Math_042.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_042.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_042.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_042.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_042.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_042.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_042.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_042.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_042.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_042.operation = 'CROSS_PRODUCT'
        except: pass
        try: node_Vector_Math_042.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_042.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.042'] = node_Vector_Math_042
        node_Vector_Math_015 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_015.location_absolute = (-176.5287322998047, -962.8223876953125)
        try: node_Vector_Math_015.location_absolute = Vector((-176.5287322998047, -962.8223876953125))
        except: pass
        try: node_Vector_Math_015.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_015.mute = False
        except: pass
        try: node_Vector_Math_015.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_015.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_015.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_015.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_015.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_015.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_015.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_015.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_015.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_015.operation = 'MULTIPLY'
        except: pass
        try: node_Vector_Math_015.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_015.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.015'] = node_Vector_Math_015
        node_Vector_Math_016 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_016.location_absolute = (-174.6678924560547, -1122.6134033203125)
        try: node_Vector_Math_016.location_absolute = Vector((-174.6678924560547, -1122.6134033203125))
        except: pass
        try: node_Vector_Math_016.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_016.mute = False
        except: pass
        try: node_Vector_Math_016.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_016.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_016.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_016.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_016.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_016.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_016.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_016.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_016.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_016.operation = 'MULTIPLY'
        except: pass
        try: node_Vector_Math_016.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_016.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.016'] = node_Vector_Math_016
        node_Vector_Math_029 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_029.location_absolute = (-174.6678009033203, -1283.8548583984375)
        try: node_Vector_Math_029.location_absolute = Vector((-174.6678009033203, -1283.8548583984375))
        except: pass
        try: node_Vector_Math_029.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_029.mute = False
        except: pass
        try: node_Vector_Math_029.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_029.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_029.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_029.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_029.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_029.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_029.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_029.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_029.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_029.operation = 'MULTIPLY'
        except: pass
        try: node_Vector_Math_029.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_029.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.029'] = node_Vector_Math_029
        node_Vector_Math_030 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_030.location_absolute = (6.604418754577637, -1019.3624267578125)
        try: node_Vector_Math_030.location_absolute = Vector((6.604418754577637, -1019.3624267578125))
        except: pass
        try: node_Vector_Math_030.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_030.mute = False
        except: pass
        try: node_Vector_Math_030.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_030.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_030.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_030.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_030.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_030.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_030.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_030.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_030.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_030.operation = 'ADD'
        except: pass
        try: node_Vector_Math_030.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_030.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.030'] = node_Vector_Math_030
        node_Vector_Math_031 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_031.location_absolute = (231.2859649658203, -1189.445068359375)
        try: node_Vector_Math_031.location_absolute = Vector((231.2859649658203, -1189.445068359375))
        except: pass
        try: node_Vector_Math_031.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_031.mute = False
        except: pass
        try: node_Vector_Math_031.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_031.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_031.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_031.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_031.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_031.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_031.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_031.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_031.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_031.operation = 'ADD'
        except: pass
        try: node_Vector_Math_031.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_031.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.031'] = node_Vector_Math_031
        node_Vector_Math_032 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_032.location_absolute = (392.9598693847656, -1195.302490234375)
        try: node_Vector_Math_032.location_absolute = Vector((392.9598693847656, -1195.302490234375))
        except: pass
        try: node_Vector_Math_032.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_032.mute = False
        except: pass
        try: node_Vector_Math_032.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_032.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_032.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_032.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_032.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_032.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_032.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_032.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_032.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_032.operation = 'NORMALIZE'
        except: pass
        try: node_Vector_Math_032.inputs[1].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_032.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_032.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.032'] = node_Vector_Math_032
        node_Frame_017 = group.nodes.new('NodeFrame')
        node_Frame_017.location_absolute = (-1043.5999755859375, -1102.800048828125)
        node_Frame_017.shrink = True
        try: node_Frame_017.location_absolute = Vector((-1043.5999755859375, -1102.800048828125))
        except: pass
        try: node_Frame_017.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_017.mute = False
        except: pass
        try: node_Frame_017.bl_label = 'Frame'
        except: pass
        try: node_Frame_017.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_017.bl_icon = 'NONE'
        except: pass
        try: node_Frame_017.bl_width_default = 150.0
        except: pass
        try: node_Frame_017.bl_width_min = 100.0
        except: pass
        try: node_Frame_017.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_017.bl_height_default = 100.0
        except: pass
        try: node_Frame_017.bl_height_min = 30.0
        except: pass
        try: node_Frame_017.bl_height_max = 30.0
        except: pass
        try: node_Frame_017.text = None
        except: pass
        try: node_Frame_017.shrink = True
        except: pass
        try: node_Frame_017.label_size = 20
        except: pass
        created_nodes['Frame.017'] = node_Frame_017
        node_Separate_Color_001 = group.nodes.new('ShaderNodeSeparateColor')
        node_Separate_Color_001.location_absolute = (-2719.593994140625, -969.4207153320312)
        try: node_Separate_Color_001.location_absolute = Vector((-2719.593994140625, -969.4207153320312))
        except: pass
        try: node_Separate_Color_001.warning_propagation = 'ALL'
        except: pass
        try: node_Separate_Color_001.mute = False
        except: pass
        try: node_Separate_Color_001.bl_label = 'Separate Color'
        except: pass
        try: node_Separate_Color_001.bl_description = 'Split a color into its individual components using multiple models'
        except: pass
        try: node_Separate_Color_001.bl_icon = 'NONE'
        except: pass
        try: node_Separate_Color_001.bl_width_default = 140.0
        except: pass
        try: node_Separate_Color_001.bl_width_min = 100.0
        except: pass
        try: node_Separate_Color_001.bl_width_max = 700.0
        except: pass
        try: node_Separate_Color_001.bl_height_default = 100.0
        except: pass
        try: node_Separate_Color_001.bl_height_min = 30.0
        except: pass
        try: node_Separate_Color_001.bl_height_max = 30.0
        except: pass
        try: node_Separate_Color_001.mode = 'RGB'
        except: pass
        created_nodes['Separate Color.001'] = node_Separate_Color_001
        node_Combine_Color_001 = group.nodes.new('ShaderNodeCombineColor')
        node_Combine_Color_001.location_absolute = (-2320.451171875, -959.6806640625)
        try: node_Combine_Color_001.location_absolute = Vector((-2320.451171875, -959.6806640625))
        except: pass
        try: node_Combine_Color_001.warning_propagation = 'ALL'
        except: pass
        try: node_Combine_Color_001.mute = False
        except: pass
        try: node_Combine_Color_001.bl_label = 'Combine Color'
        except: pass
        try: node_Combine_Color_001.bl_description = 'Create a color from individual components using multiple models'
        except: pass
        try: node_Combine_Color_001.bl_icon = 'NONE'
        except: pass
        try: node_Combine_Color_001.bl_width_default = 140.0
        except: pass
        try: node_Combine_Color_001.bl_width_min = 100.0
        except: pass
        try: node_Combine_Color_001.bl_width_max = 700.0
        except: pass
        try: node_Combine_Color_001.bl_height_default = 100.0
        except: pass
        try: node_Combine_Color_001.bl_height_min = 30.0
        except: pass
        try: node_Combine_Color_001.bl_height_max = 30.0
        except: pass
        try: node_Combine_Color_001.mode = 'RGB'
        except: pass
        created_nodes['Combine Color.001'] = node_Combine_Color_001
        node_Frame_018 = group.nodes.new('NodeFrame')
        node_Frame_018.location_absolute = (-2749.199951171875, -924.0)
        node_Frame_018.label = 'Format'
        node_Frame_018.shrink = True
        try: node_Frame_018.location_absolute = Vector((-2749.199951171875, -924.0))
        except: pass
        try: node_Frame_018.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_018.mute = False
        except: pass
        try: node_Frame_018.bl_label = 'Frame'
        except: pass
        try: node_Frame_018.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_018.bl_icon = 'NONE'
        except: pass
        try: node_Frame_018.bl_width_default = 150.0
        except: pass
        try: node_Frame_018.bl_width_min = 100.0
        except: pass
        try: node_Frame_018.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_018.bl_height_default = 100.0
        except: pass
        try: node_Frame_018.bl_height_min = 30.0
        except: pass
        try: node_Frame_018.bl_height_max = 30.0
        except: pass
        try: node_Frame_018.text = None
        except: pass
        try: node_Frame_018.shrink = True
        except: pass
        try: node_Frame_018.label_size = 20
        except: pass
        created_nodes['Frame.018'] = node_Frame_018
        node_Invert_Color_001 = group.nodes.new('ShaderNodeInvert')
        node_Invert_Color_001.location_absolute = (-2519.46630859375, -1024.9482421875)
        try: node_Invert_Color_001.location_absolute = Vector((-2519.46630859375, -1024.9482421875))
        except: pass
        try: node_Invert_Color_001.warning_propagation = 'ALL'
        except: pass
        try: node_Invert_Color_001.mute = False
        except: pass
        try: node_Invert_Color_001.bl_label = 'Invert Color'
        except: pass
        try: node_Invert_Color_001.bl_description = 'Invert a color, producing a negative'
        except: pass
        try: node_Invert_Color_001.bl_icon = 'NONE'
        except: pass
        try: node_Invert_Color_001.bl_width_default = 140.0
        except: pass
        try: node_Invert_Color_001.bl_width_min = 100.0
        except: pass
        try: node_Invert_Color_001.bl_width_max = 700.0
        except: pass
        try: node_Invert_Color_001.bl_height_default = 100.0
        except: pass
        try: node_Invert_Color_001.bl_height_min = 30.0
        except: pass
        try: node_Invert_Color_001.bl_height_max = 30.0
        except: pass
        created_nodes['Invert Color.001'] = node_Invert_Color_001
        node_Vector_Math_025 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_025.location_absolute = (-1223.2828369140625, -938.8116455078125)
        try: node_Vector_Math_025.location_absolute = Vector((-1223.2828369140625, -938.8116455078125))
        except: pass
        try: node_Vector_Math_025.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_025.mute = False
        except: pass
        try: node_Vector_Math_025.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_025.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_025.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_025.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_025.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_025.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_025.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_025.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_025.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_025.operation = 'NORMALIZE'
        except: pass
        try: node_Vector_Math_025.inputs[1].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_025.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_025.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.025'] = node_Vector_Math_025
        node_Vector_Math_026 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_026.location_absolute = (-1404.8966064453125, -938.7874755859375)
        try: node_Vector_Math_026.location_absolute = Vector((-1404.8966064453125, -938.7874755859375))
        except: pass
        try: node_Vector_Math_026.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_026.mute = False
        except: pass
        try: node_Vector_Math_026.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_026.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_026.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_026.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_026.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_026.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_026.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_026.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_026.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_026.operation = 'MULTIPLY'
        except: pass
        try: node_Vector_Math_026.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_026.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.026'] = node_Vector_Math_026
        node_Frame_024 = group.nodes.new('NodeFrame')
        node_Frame_024.location_absolute = (-1434.800048828125, -902.4000244140625)
        node_Frame_024.label = 'Strength'
        node_Frame_024.shrink = True
        try: node_Frame_024.location_absolute = Vector((-1434.800048828125, -902.4000244140625))
        except: pass
        try: node_Frame_024.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_024.mute = False
        except: pass
        try: node_Frame_024.bl_label = 'Frame'
        except: pass
        try: node_Frame_024.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_024.bl_icon = 'NONE'
        except: pass
        try: node_Frame_024.bl_width_default = 150.0
        except: pass
        try: node_Frame_024.bl_width_min = 100.0
        except: pass
        try: node_Frame_024.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_024.bl_height_default = 100.0
        except: pass
        try: node_Frame_024.bl_height_min = 30.0
        except: pass
        try: node_Frame_024.bl_height_max = 30.0
        except: pass
        try: node_Frame_024.text = None
        except: pass
        try: node_Frame_024.shrink = True
        except: pass
        try: node_Frame_024.label_size = 20
        except: pass
        created_nodes['Frame.024'] = node_Frame_024
        node_Separate_XYZ_011 = group.nodes.new('ShaderNodeSeparateXYZ')
        node_Separate_XYZ_011.location_absolute = (-599.59619140625, -954.9700927734375)
        try: node_Separate_XYZ_011.location_absolute = Vector((-599.59619140625, -954.9700927734375))
        except: pass
        try: node_Separate_XYZ_011.warning_propagation = 'ALL'
        except: pass
        try: node_Separate_XYZ_011.mute = False
        except: pass
        try: node_Separate_XYZ_011.bl_label = 'Separate XYZ'
        except: pass
        try: node_Separate_XYZ_011.bl_description = 'Split a vector into its X, Y, and Z components'
        except: pass
        try: node_Separate_XYZ_011.bl_icon = 'NONE'
        except: pass
        try: node_Separate_XYZ_011.bl_width_default = 140.0
        except: pass
        try: node_Separate_XYZ_011.bl_width_min = 100.0
        except: pass
        try: node_Separate_XYZ_011.bl_width_max = 700.0
        except: pass
        try: node_Separate_XYZ_011.bl_height_default = 100.0
        except: pass
        try: node_Separate_XYZ_011.bl_height_min = 30.0
        except: pass
        try: node_Separate_XYZ_011.bl_height_max = 30.0
        except: pass
        created_nodes['Separate XYZ.011'] = node_Separate_XYZ_011
        node_Math_005 = group.nodes.new('ShaderNodeMath')
        node_Math_005.location_absolute = (-410.74444580078125, -923.17431640625)
        try: node_Math_005.location_absolute = Vector((-410.74444580078125, -923.17431640625))
        except: pass
        try: node_Math_005.warning_propagation = 'ALL'
        except: pass
        try: node_Math_005.mute = False
        except: pass
        try: node_Math_005.bl_label = 'Math'
        except: pass
        try: node_Math_005.bl_description = 'Perform math operations'
        except: pass
        try: node_Math_005.bl_icon = 'NONE'
        except: pass
        try: node_Math_005.bl_width_default = 140.0
        except: pass
        try: node_Math_005.bl_width_min = 100.0
        except: pass
        try: node_Math_005.bl_width_max = 700.0
        except: pass
        try: node_Math_005.bl_height_default = 100.0
        except: pass
        try: node_Math_005.bl_height_min = 30.0
        except: pass
        try: node_Math_005.bl_height_max = 30.0
        except: pass
        try: node_Math_005.operation = 'MULTIPLY'
        except: pass
        try: node_Math_005.use_clamp = False
        except: pass
        try: node_Math_005.inputs[1].default_value = -1.0
        except: pass
        try: node_Math_005.inputs[2].default_value = 0.5
        except: pass
        created_nodes['Math.005'] = node_Math_005
        node_Combine_XYZ_012 = group.nodes.new('ShaderNodeCombineXYZ')
        node_Combine_XYZ_012.location_absolute = (-1230.6873779296875, -1091.998291015625)
        try: node_Combine_XYZ_012.location_absolute = Vector((-1230.6873779296875, -1091.998291015625))
        except: pass
        try: node_Combine_XYZ_012.warning_propagation = 'ALL'
        except: pass
        try: node_Combine_XYZ_012.mute = False
        except: pass
        try: node_Combine_XYZ_012.bl_label = 'Combine XYZ'
        except: pass
        try: node_Combine_XYZ_012.bl_description = 'Create a vector from X, Y, and Z components'
        except: pass
        try: node_Combine_XYZ_012.bl_icon = 'NONE'
        except: pass
        try: node_Combine_XYZ_012.bl_width_default = 140.0
        except: pass
        try: node_Combine_XYZ_012.bl_width_min = 100.0
        except: pass
        try: node_Combine_XYZ_012.bl_width_max = 700.0
        except: pass
        try: node_Combine_XYZ_012.bl_height_default = 100.0
        except: pass
        try: node_Combine_XYZ_012.bl_height_min = 30.0
        except: pass
        try: node_Combine_XYZ_012.bl_height_max = 30.0
        except: pass
        try: node_Combine_XYZ_012.inputs[2].default_value = 1.0
        except: pass
        created_nodes['Combine XYZ.012'] = node_Combine_XYZ_012
        node_Vector_Math_021 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_021.location_absolute = (-2141.34326171875, -215.2458038330078)
        try: node_Vector_Math_021.location_absolute = Vector((-2141.34326171875, -215.2458038330078))
        except: pass
        try: node_Vector_Math_021.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_021.mute = False
        except: pass
        try: node_Vector_Math_021.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_021.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_021.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_021.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_021.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_021.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_021.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_021.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_021.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_021.operation = 'MULTIPLY'
        except: pass
        try: node_Vector_Math_021.inputs[1].default_value = [2.0,2.0,2.0]
        except: pass
        try: node_Vector_Math_021.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_021.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.021'] = node_Vector_Math_021
        node_Vector_Math_022 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_022.location_absolute = (-1963.239013671875, -217.90634155273438)
        try: node_Vector_Math_022.location_absolute = Vector((-1963.239013671875, -217.90634155273438))
        except: pass
        try: node_Vector_Math_022.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_022.mute = False
        except: pass
        try: node_Vector_Math_022.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_022.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_022.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_022.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_022.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_022.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_022.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_022.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_022.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_022.operation = 'SUBTRACT'
        except: pass
        try: node_Vector_Math_022.inputs[1].default_value = [1.0,1.0,1.0]
        except: pass
        try: node_Vector_Math_022.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_022.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.022'] = node_Vector_Math_022
        node_Frame_022 = group.nodes.new('NodeFrame')
        node_Frame_022.location_absolute = (-2171.60009765625, -179.1999969482422)
        node_Frame_022.label = 'Unpack'
        node_Frame_022.shrink = True
        try: node_Frame_022.location_absolute = Vector((-2171.60009765625, -179.1999969482422))
        except: pass
        try: node_Frame_022.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_022.mute = False
        except: pass
        try: node_Frame_022.bl_label = 'Frame'
        except: pass
        try: node_Frame_022.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_022.bl_icon = 'NONE'
        except: pass
        try: node_Frame_022.bl_width_default = 150.0
        except: pass
        try: node_Frame_022.bl_width_min = 100.0
        except: pass
        try: node_Frame_022.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_022.bl_height_default = 100.0
        except: pass
        try: node_Frame_022.bl_height_min = 30.0
        except: pass
        try: node_Frame_022.bl_height_max = 30.0
        except: pass
        try: node_Frame_022.text = None
        except: pass
        try: node_Frame_022.shrink = True
        except: pass
        try: node_Frame_022.label_size = 20
        except: pass
        created_nodes['Frame.022'] = node_Frame_022
        node_Texture_Coordinate_024 = group.nodes.new('ShaderNodeTexCoord')
        node_Texture_Coordinate_024.location_absolute = (-1022.5704956054688, -454.59423828125)
        try: node_Texture_Coordinate_024.location_absolute = Vector((-1022.5704956054688, -454.59423828125))
        except: pass
        try: node_Texture_Coordinate_024.warning_propagation = 'ALL'
        except: pass
        try: node_Texture_Coordinate_024.mute = False
        except: pass
        try: node_Texture_Coordinate_024.bl_label = 'Texture Coordinate'
        except: pass
        try: node_Texture_Coordinate_024.bl_description = 'Retrieve multiple types of texture coordinates.\nTypically used as inputs for texture nodes'
        except: pass
        try: node_Texture_Coordinate_024.bl_icon = 'NONE'
        except: pass
        try: node_Texture_Coordinate_024.bl_width_default = 140.0
        except: pass
        try: node_Texture_Coordinate_024.bl_width_min = 100.0
        except: pass
        try: node_Texture_Coordinate_024.bl_width_max = 700.0
        except: pass
        try: node_Texture_Coordinate_024.bl_height_default = 100.0
        except: pass
        try: node_Texture_Coordinate_024.bl_height_min = 30.0
        except: pass
        try: node_Texture_Coordinate_024.bl_height_max = 30.0
        except: pass
        try: node_Texture_Coordinate_024.object = None
        except: pass
        try: node_Texture_Coordinate_024.from_instancer = False
        except: pass
        created_nodes['Texture Coordinate.024'] = node_Texture_Coordinate_024
        node_Vector_Math_033 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_033.location_absolute = (-807.6565551757812, -535.306640625)
        try: node_Vector_Math_033.location_absolute = Vector((-807.6565551757812, -535.306640625))
        except: pass
        try: node_Vector_Math_033.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_033.mute = False
        except: pass
        try: node_Vector_Math_033.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_033.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_033.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_033.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_033.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_033.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_033.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_033.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_033.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_033.operation = 'CROSS_PRODUCT'
        except: pass
        try: node_Vector_Math_033.inputs[1].default_value = [0.0,0.0,1.0]
        except: pass
        try: node_Vector_Math_033.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_033.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.033'] = node_Vector_Math_033
        node_Vector_Math_043 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_043.location_absolute = (-639.2642822265625, -435.28533935546875)
        try: node_Vector_Math_043.location_absolute = Vector((-639.2642822265625, -435.28533935546875))
        except: pass
        try: node_Vector_Math_043.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_043.mute = False
        except: pass
        try: node_Vector_Math_043.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_043.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_043.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_043.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_043.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_043.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_043.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_043.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_043.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_043.operation = 'CROSS_PRODUCT'
        except: pass
        try: node_Vector_Math_043.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_043.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.043'] = node_Vector_Math_043
        node_Vector_Math_023 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_023.location_absolute = (-185.25344848632812, -265.50006103515625)
        try: node_Vector_Math_023.location_absolute = Vector((-185.25344848632812, -265.50006103515625))
        except: pass
        try: node_Vector_Math_023.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_023.mute = False
        except: pass
        try: node_Vector_Math_023.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_023.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_023.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_023.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_023.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_023.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_023.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_023.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_023.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_023.operation = 'MULTIPLY'
        except: pass
        try: node_Vector_Math_023.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_023.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.023'] = node_Vector_Math_023
        node_Vector_Math_024 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_024.location_absolute = (-183.3927001953125, -425.29107666015625)
        try: node_Vector_Math_024.location_absolute = Vector((-183.3927001953125, -425.29107666015625))
        except: pass
        try: node_Vector_Math_024.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_024.mute = False
        except: pass
        try: node_Vector_Math_024.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_024.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_024.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_024.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_024.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_024.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_024.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_024.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_024.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_024.operation = 'MULTIPLY'
        except: pass
        try: node_Vector_Math_024.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_024.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.024'] = node_Vector_Math_024
        node_Vector_Math_034 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_034.location_absolute = (-183.3925018310547, -586.53271484375)
        try: node_Vector_Math_034.location_absolute = Vector((-183.3925018310547, -586.53271484375))
        except: pass
        try: node_Vector_Math_034.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_034.mute = False
        except: pass
        try: node_Vector_Math_034.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_034.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_034.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_034.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_034.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_034.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_034.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_034.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_034.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_034.operation = 'MULTIPLY'
        except: pass
        try: node_Vector_Math_034.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_034.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.034'] = node_Vector_Math_034
        node_Vector_Math_044 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_044.location_absolute = (-2.1202149391174316, -322.04010009765625)
        try: node_Vector_Math_044.location_absolute = Vector((-2.1202149391174316, -322.04010009765625))
        except: pass
        try: node_Vector_Math_044.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_044.mute = False
        except: pass
        try: node_Vector_Math_044.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_044.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_044.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_044.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_044.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_044.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_044.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_044.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_044.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_044.operation = 'ADD'
        except: pass
        try: node_Vector_Math_044.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_044.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.044'] = node_Vector_Math_044
        node_Vector_Math_045 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_045.location_absolute = (222.5612335205078, -492.12274169921875)
        try: node_Vector_Math_045.location_absolute = Vector((222.5612335205078, -492.12274169921875))
        except: pass
        try: node_Vector_Math_045.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_045.mute = False
        except: pass
        try: node_Vector_Math_045.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_045.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_045.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_045.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_045.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_045.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_045.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_045.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_045.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_045.operation = 'ADD'
        except: pass
        try: node_Vector_Math_045.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_045.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.045'] = node_Vector_Math_045
        node_Vector_Math_046 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_046.location_absolute = (384.23516845703125, -497.98016357421875)
        try: node_Vector_Math_046.location_absolute = Vector((384.23516845703125, -497.98016357421875))
        except: pass
        try: node_Vector_Math_046.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_046.mute = False
        except: pass
        try: node_Vector_Math_046.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_046.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_046.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_046.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_046.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_046.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_046.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_046.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_046.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_046.operation = 'NORMALIZE'
        except: pass
        try: node_Vector_Math_046.inputs[1].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_046.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_046.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.046'] = node_Vector_Math_046
        node_Frame_023 = group.nodes.new('NodeFrame')
        node_Frame_023.location_absolute = (-1052.4000244140625, -405.20001220703125)
        node_Frame_023.shrink = True
        try: node_Frame_023.location_absolute = Vector((-1052.4000244140625, -405.20001220703125))
        except: pass
        try: node_Frame_023.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_023.mute = False
        except: pass
        try: node_Frame_023.bl_label = 'Frame'
        except: pass
        try: node_Frame_023.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_023.bl_icon = 'NONE'
        except: pass
        try: node_Frame_023.bl_width_default = 150.0
        except: pass
        try: node_Frame_023.bl_width_min = 100.0
        except: pass
        try: node_Frame_023.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_023.bl_height_default = 100.0
        except: pass
        try: node_Frame_023.bl_height_min = 30.0
        except: pass
        try: node_Frame_023.bl_height_max = 30.0
        except: pass
        try: node_Frame_023.text = None
        except: pass
        try: node_Frame_023.shrink = True
        except: pass
        try: node_Frame_023.label_size = 20
        except: pass
        created_nodes['Frame.023'] = node_Frame_023
        node_Separate_Color_003 = group.nodes.new('ShaderNodeSeparateColor')
        node_Separate_Color_003.location_absolute = (-2749.567138671875, -224.4352569580078)
        try: node_Separate_Color_003.location_absolute = Vector((-2749.567138671875, -224.4352569580078))
        except: pass
        try: node_Separate_Color_003.warning_propagation = 'ALL'
        except: pass
        try: node_Separate_Color_003.mute = False
        except: pass
        try: node_Separate_Color_003.bl_label = 'Separate Color'
        except: pass
        try: node_Separate_Color_003.bl_description = 'Split a color into its individual components using multiple models'
        except: pass
        try: node_Separate_Color_003.bl_icon = 'NONE'
        except: pass
        try: node_Separate_Color_003.bl_width_default = 140.0
        except: pass
        try: node_Separate_Color_003.bl_width_min = 100.0
        except: pass
        try: node_Separate_Color_003.bl_width_max = 700.0
        except: pass
        try: node_Separate_Color_003.bl_height_default = 100.0
        except: pass
        try: node_Separate_Color_003.bl_height_min = 30.0
        except: pass
        try: node_Separate_Color_003.bl_height_max = 30.0
        except: pass
        try: node_Separate_Color_003.mode = 'RGB'
        except: pass
        created_nodes['Separate Color.003'] = node_Separate_Color_003
        node_Combine_Color_002 = group.nodes.new('ShaderNodeCombineColor')
        node_Combine_Color_002.location_absolute = (-2350.424072265625, -214.69515991210938)
        try: node_Combine_Color_002.location_absolute = Vector((-2350.424072265625, -214.69515991210938))
        except: pass
        try: node_Combine_Color_002.warning_propagation = 'ALL'
        except: pass
        try: node_Combine_Color_002.mute = False
        except: pass
        try: node_Combine_Color_002.bl_label = 'Combine Color'
        except: pass
        try: node_Combine_Color_002.bl_description = 'Create a color from individual components using multiple models'
        except: pass
        try: node_Combine_Color_002.bl_icon = 'NONE'
        except: pass
        try: node_Combine_Color_002.bl_width_default = 140.0
        except: pass
        try: node_Combine_Color_002.bl_width_min = 100.0
        except: pass
        try: node_Combine_Color_002.bl_width_max = 700.0
        except: pass
        try: node_Combine_Color_002.bl_height_default = 100.0
        except: pass
        try: node_Combine_Color_002.bl_height_min = 30.0
        except: pass
        try: node_Combine_Color_002.bl_height_max = 30.0
        except: pass
        try: node_Combine_Color_002.mode = 'RGB'
        except: pass
        created_nodes['Combine Color.002'] = node_Combine_Color_002
        node_Frame_025 = group.nodes.new('NodeFrame')
        node_Frame_025.location_absolute = (-2779.60009765625, -178.39999389648438)
        node_Frame_025.label = 'Format'
        node_Frame_025.shrink = True
        try: node_Frame_025.location_absolute = Vector((-2779.60009765625, -178.39999389648438))
        except: pass
        try: node_Frame_025.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_025.mute = False
        except: pass
        try: node_Frame_025.bl_label = 'Frame'
        except: pass
        try: node_Frame_025.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_025.bl_icon = 'NONE'
        except: pass
        try: node_Frame_025.bl_width_default = 150.0
        except: pass
        try: node_Frame_025.bl_width_min = 100.0
        except: pass
        try: node_Frame_025.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_025.bl_height_default = 100.0
        except: pass
        try: node_Frame_025.bl_height_min = 30.0
        except: pass
        try: node_Frame_025.bl_height_max = 30.0
        except: pass
        try: node_Frame_025.text = None
        except: pass
        try: node_Frame_025.shrink = True
        except: pass
        try: node_Frame_025.label_size = 20
        except: pass
        created_nodes['Frame.025'] = node_Frame_025
        node_Invert_Color_003 = group.nodes.new('ShaderNodeInvert')
        node_Invert_Color_003.location_absolute = (-2549.439453125, -279.9627380371094)
        try: node_Invert_Color_003.location_absolute = Vector((-2549.439453125, -279.9627380371094))
        except: pass
        try: node_Invert_Color_003.warning_propagation = 'ALL'
        except: pass
        try: node_Invert_Color_003.mute = False
        except: pass
        try: node_Invert_Color_003.bl_label = 'Invert Color'
        except: pass
        try: node_Invert_Color_003.bl_description = 'Invert a color, producing a negative'
        except: pass
        try: node_Invert_Color_003.bl_icon = 'NONE'
        except: pass
        try: node_Invert_Color_003.bl_width_default = 140.0
        except: pass
        try: node_Invert_Color_003.bl_width_min = 100.0
        except: pass
        try: node_Invert_Color_003.bl_width_max = 700.0
        except: pass
        try: node_Invert_Color_003.bl_height_default = 100.0
        except: pass
        try: node_Invert_Color_003.bl_height_min = 30.0
        except: pass
        try: node_Invert_Color_003.bl_height_max = 30.0
        except: pass
        created_nodes['Invert Color.003'] = node_Invert_Color_003
        node_Vector_Math_027 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_027.location_absolute = (-1232.00732421875, -241.4893035888672)
        try: node_Vector_Math_027.location_absolute = Vector((-1232.00732421875, -241.4893035888672))
        except: pass
        try: node_Vector_Math_027.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_027.mute = False
        except: pass
        try: node_Vector_Math_027.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_027.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_027.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_027.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_027.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_027.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_027.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_027.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_027.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_027.operation = 'NORMALIZE'
        except: pass
        try: node_Vector_Math_027.inputs[1].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_027.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_027.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.027'] = node_Vector_Math_027
        node_Vector_Math_047 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_047.location_absolute = (-1413.6212158203125, -241.46524047851562)
        try: node_Vector_Math_047.location_absolute = Vector((-1413.6212158203125, -241.46524047851562))
        except: pass
        try: node_Vector_Math_047.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_047.mute = False
        except: pass
        try: node_Vector_Math_047.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_047.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_047.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_047.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_047.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_047.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_047.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_047.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_047.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_047.operation = 'MULTIPLY'
        except: pass
        try: node_Vector_Math_047.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_047.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.047'] = node_Vector_Math_047
        node_Frame_026 = group.nodes.new('NodeFrame')
        node_Frame_026.location_absolute = (-1443.5999755859375, -201.60000610351562)
        node_Frame_026.label = 'Strength'
        node_Frame_026.shrink = True
        try: node_Frame_026.location_absolute = Vector((-1443.5999755859375, -201.60000610351562))
        except: pass
        try: node_Frame_026.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_026.mute = False
        except: pass
        try: node_Frame_026.bl_label = 'Frame'
        except: pass
        try: node_Frame_026.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_026.bl_icon = 'NONE'
        except: pass
        try: node_Frame_026.bl_width_default = 150.0
        except: pass
        try: node_Frame_026.bl_width_min = 100.0
        except: pass
        try: node_Frame_026.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_026.bl_height_default = 100.0
        except: pass
        try: node_Frame_026.bl_height_min = 30.0
        except: pass
        try: node_Frame_026.bl_height_max = 30.0
        except: pass
        try: node_Frame_026.text = None
        except: pass
        try: node_Frame_026.shrink = True
        except: pass
        try: node_Frame_026.label_size = 20
        except: pass
        created_nodes['Frame.026'] = node_Frame_026
        node_Separate_XYZ_012 = group.nodes.new('ShaderNodeSeparateXYZ')
        node_Separate_XYZ_012.location_absolute = (-608.3209228515625, -257.64776611328125)
        try: node_Separate_XYZ_012.location_absolute = Vector((-608.3209228515625, -257.64776611328125))
        except: pass
        try: node_Separate_XYZ_012.warning_propagation = 'ALL'
        except: pass
        try: node_Separate_XYZ_012.mute = False
        except: pass
        try: node_Separate_XYZ_012.bl_label = 'Separate XYZ'
        except: pass
        try: node_Separate_XYZ_012.bl_description = 'Split a vector into its X, Y, and Z components'
        except: pass
        try: node_Separate_XYZ_012.bl_icon = 'NONE'
        except: pass
        try: node_Separate_XYZ_012.bl_width_default = 140.0
        except: pass
        try: node_Separate_XYZ_012.bl_width_min = 100.0
        except: pass
        try: node_Separate_XYZ_012.bl_width_max = 700.0
        except: pass
        try: node_Separate_XYZ_012.bl_height_default = 100.0
        except: pass
        try: node_Separate_XYZ_012.bl_height_min = 30.0
        except: pass
        try: node_Separate_XYZ_012.bl_height_max = 30.0
        except: pass
        created_nodes['Separate XYZ.012'] = node_Separate_XYZ_012
        node_Math_011 = group.nodes.new('ShaderNodeMath')
        node_Math_011.location_absolute = (-395.78350830078125, -253.526611328125)
        try: node_Math_011.location_absolute = Vector((-395.78350830078125, -253.526611328125))
        except: pass
        try: node_Math_011.warning_propagation = 'ALL'
        except: pass
        try: node_Math_011.mute = False
        except: pass
        try: node_Math_011.bl_label = 'Math'
        except: pass
        try: node_Math_011.bl_description = 'Perform math operations'
        except: pass
        try: node_Math_011.bl_icon = 'NONE'
        except: pass
        try: node_Math_011.bl_width_default = 140.0
        except: pass
        try: node_Math_011.bl_width_min = 100.0
        except: pass
        try: node_Math_011.bl_width_max = 700.0
        except: pass
        try: node_Math_011.bl_height_default = 100.0
        except: pass
        try: node_Math_011.bl_height_min = 30.0
        except: pass
        try: node_Math_011.bl_height_max = 30.0
        except: pass
        try: node_Math_011.operation = 'MULTIPLY'
        except: pass
        try: node_Math_011.use_clamp = False
        except: pass
        try: node_Math_011.inputs[1].default_value = -1.0
        except: pass
        try: node_Math_011.inputs[2].default_value = 0.5
        except: pass
        created_nodes['Math.011'] = node_Math_011
        node_Combine_XYZ_013 = group.nodes.new('ShaderNodeCombineXYZ')
        node_Combine_XYZ_013.location_absolute = (-1239.412353515625, -394.67596435546875)
        try: node_Combine_XYZ_013.location_absolute = Vector((-1239.412353515625, -394.67596435546875))
        except: pass
        try: node_Combine_XYZ_013.warning_propagation = 'ALL'
        except: pass
        try: node_Combine_XYZ_013.mute = False
        except: pass
        try: node_Combine_XYZ_013.bl_label = 'Combine XYZ'
        except: pass
        try: node_Combine_XYZ_013.bl_description = 'Create a vector from X, Y, and Z components'
        except: pass
        try: node_Combine_XYZ_013.bl_icon = 'NONE'
        except: pass
        try: node_Combine_XYZ_013.bl_width_default = 140.0
        except: pass
        try: node_Combine_XYZ_013.bl_width_min = 100.0
        except: pass
        try: node_Combine_XYZ_013.bl_width_max = 700.0
        except: pass
        try: node_Combine_XYZ_013.bl_height_default = 100.0
        except: pass
        try: node_Combine_XYZ_013.bl_height_min = 30.0
        except: pass
        try: node_Combine_XYZ_013.bl_height_max = 30.0
        except: pass
        try: node_Combine_XYZ_013.inputs[2].default_value = 1.0
        except: pass
        created_nodes['Combine XYZ.013'] = node_Combine_XYZ_013
        node_Vector_Math_017 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_017.location_absolute = (-2106.8896484375, -1741.8421630859375)
        try: node_Vector_Math_017.location_absolute = Vector((-2106.8896484375, -1741.8421630859375))
        except: pass
        try: node_Vector_Math_017.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_017.mute = False
        except: pass
        try: node_Vector_Math_017.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_017.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_017.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_017.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_017.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_017.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_017.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_017.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_017.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_017.operation = 'MULTIPLY'
        except: pass
        try: node_Vector_Math_017.inputs[1].default_value = [2.0,2.0,2.0]
        except: pass
        try: node_Vector_Math_017.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_017.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.017'] = node_Vector_Math_017
        node_Vector_Math_018 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_018.location_absolute = (-1928.784912109375, -1744.502685546875)
        try: node_Vector_Math_018.location_absolute = Vector((-1928.784912109375, -1744.502685546875))
        except: pass
        try: node_Vector_Math_018.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_018.mute = False
        except: pass
        try: node_Vector_Math_018.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_018.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_018.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_018.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_018.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_018.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_018.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_018.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_018.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_018.operation = 'SUBTRACT'
        except: pass
        try: node_Vector_Math_018.inputs[1].default_value = [1.0,1.0,1.0]
        except: pass
        try: node_Vector_Math_018.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_018.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.018'] = node_Vector_Math_018
        node_Frame_019 = group.nodes.new('NodeFrame')
        node_Frame_019.location_absolute = (-2137.199951171875, -1705.5999755859375)
        node_Frame_019.label = 'Unpack'
        node_Frame_019.shrink = True
        try: node_Frame_019.location_absolute = Vector((-2137.199951171875, -1705.5999755859375))
        except: pass
        try: node_Frame_019.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_019.mute = False
        except: pass
        try: node_Frame_019.bl_label = 'Frame'
        except: pass
        try: node_Frame_019.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_019.bl_icon = 'NONE'
        except: pass
        try: node_Frame_019.bl_width_default = 150.0
        except: pass
        try: node_Frame_019.bl_width_min = 100.0
        except: pass
        try: node_Frame_019.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_019.bl_height_default = 100.0
        except: pass
        try: node_Frame_019.bl_height_min = 30.0
        except: pass
        try: node_Frame_019.bl_height_max = 30.0
        except: pass
        try: node_Frame_019.text = None
        except: pass
        try: node_Frame_019.shrink = True
        except: pass
        try: node_Frame_019.label_size = 20
        except: pass
        created_nodes['Frame.019'] = node_Frame_019
        node_Texture_Coordinate_025 = group.nodes.new('ShaderNodeTexCoord')
        node_Texture_Coordinate_025.location_absolute = (-970.3307495117188, -1921.787353515625)
        try: node_Texture_Coordinate_025.location_absolute = Vector((-970.3307495117188, -1921.787353515625))
        except: pass
        try: node_Texture_Coordinate_025.warning_propagation = 'ALL'
        except: pass
        try: node_Texture_Coordinate_025.mute = False
        except: pass
        try: node_Texture_Coordinate_025.bl_label = 'Texture Coordinate'
        except: pass
        try: node_Texture_Coordinate_025.bl_description = 'Retrieve multiple types of texture coordinates.\nTypically used as inputs for texture nodes'
        except: pass
        try: node_Texture_Coordinate_025.bl_icon = 'NONE'
        except: pass
        try: node_Texture_Coordinate_025.bl_width_default = 140.0
        except: pass
        try: node_Texture_Coordinate_025.bl_width_min = 100.0
        except: pass
        try: node_Texture_Coordinate_025.bl_width_max = 700.0
        except: pass
        try: node_Texture_Coordinate_025.bl_height_default = 100.0
        except: pass
        try: node_Texture_Coordinate_025.bl_height_min = 30.0
        except: pass
        try: node_Texture_Coordinate_025.bl_height_max = 30.0
        except: pass
        try: node_Texture_Coordinate_025.object = None
        except: pass
        try: node_Texture_Coordinate_025.from_instancer = False
        except: pass
        created_nodes['Texture Coordinate.025'] = node_Texture_Coordinate_025
        node_Vector_Math_035 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_035.location_absolute = (-786.1222534179688, -2006.943115234375)
        try: node_Vector_Math_035.location_absolute = Vector((-786.1222534179688, -2006.943115234375))
        except: pass
        try: node_Vector_Math_035.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_035.mute = False
        except: pass
        try: node_Vector_Math_035.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_035.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_035.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_035.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_035.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_035.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_035.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_035.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_035.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_035.operation = 'CROSS_PRODUCT'
        except: pass
        try: node_Vector_Math_035.inputs[1].default_value = [1.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_035.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_035.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.035'] = node_Vector_Math_035
        node_Vector_Math_048 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_048.location_absolute = (-617.7296752929688, -1906.921630859375)
        try: node_Vector_Math_048.location_absolute = Vector((-617.7296752929688, -1906.921630859375))
        except: pass
        try: node_Vector_Math_048.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_048.mute = False
        except: pass
        try: node_Vector_Math_048.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_048.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_048.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_048.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_048.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_048.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_048.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_048.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_048.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_048.operation = 'CROSS_PRODUCT'
        except: pass
        try: node_Vector_Math_048.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_048.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.048'] = node_Vector_Math_048
        node_Vector_Math_019 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_019.location_absolute = (-178.0778045654297, -1721.8623046875)
        try: node_Vector_Math_019.location_absolute = Vector((-178.0778045654297, -1721.8623046875))
        except: pass
        try: node_Vector_Math_019.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_019.mute = False
        except: pass
        try: node_Vector_Math_019.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_019.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_019.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_019.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_019.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_019.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_019.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_019.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_019.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_019.operation = 'MULTIPLY'
        except: pass
        try: node_Vector_Math_019.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_019.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.019'] = node_Vector_Math_019
        node_Vector_Math_020 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_020.location_absolute = (-176.21707153320312, -1881.6533203125)
        try: node_Vector_Math_020.location_absolute = Vector((-176.21707153320312, -1881.6533203125))
        except: pass
        try: node_Vector_Math_020.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_020.mute = False
        except: pass
        try: node_Vector_Math_020.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_020.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_020.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_020.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_020.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_020.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_020.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_020.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_020.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_020.operation = 'MULTIPLY'
        except: pass
        try: node_Vector_Math_020.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_020.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.020'] = node_Vector_Math_020
        node_Vector_Math_036 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_036.location_absolute = (-176.2166748046875, -2042.8948974609375)
        try: node_Vector_Math_036.location_absolute = Vector((-176.2166748046875, -2042.8948974609375))
        except: pass
        try: node_Vector_Math_036.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_036.mute = False
        except: pass
        try: node_Vector_Math_036.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_036.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_036.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_036.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_036.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_036.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_036.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_036.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_036.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_036.operation = 'MULTIPLY'
        except: pass
        try: node_Vector_Math_036.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_036.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.036'] = node_Vector_Math_036
        node_Vector_Math_037 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_037.location_absolute = (5.055395603179932, -1778.40234375)
        try: node_Vector_Math_037.location_absolute = Vector((5.055395603179932, -1778.40234375))
        except: pass
        try: node_Vector_Math_037.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_037.mute = False
        except: pass
        try: node_Vector_Math_037.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_037.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_037.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_037.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_037.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_037.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_037.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_037.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_037.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_037.operation = 'ADD'
        except: pass
        try: node_Vector_Math_037.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_037.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.037'] = node_Vector_Math_037
        node_Vector_Math_038 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_038.location_absolute = (229.73684692382812, -1948.4849853515625)
        try: node_Vector_Math_038.location_absolute = Vector((229.73684692382812, -1948.4849853515625))
        except: pass
        try: node_Vector_Math_038.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_038.mute = False
        except: pass
        try: node_Vector_Math_038.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_038.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_038.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_038.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_038.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_038.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_038.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_038.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_038.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_038.operation = 'ADD'
        except: pass
        try: node_Vector_Math_038.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_038.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.038'] = node_Vector_Math_038
        node_Vector_Math_039 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_039.location_absolute = (391.4107666015625, -1954.3424072265625)
        try: node_Vector_Math_039.location_absolute = Vector((391.4107666015625, -1954.3424072265625))
        except: pass
        try: node_Vector_Math_039.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_039.mute = False
        except: pass
        try: node_Vector_Math_039.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_039.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_039.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_039.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_039.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_039.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_039.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_039.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_039.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_039.operation = 'NORMALIZE'
        except: pass
        try: node_Vector_Math_039.inputs[1].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_039.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_039.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.039'] = node_Vector_Math_039
        node_Frame_020 = group.nodes.new('NodeFrame')
        node_Frame_020.location_absolute = (-1000.4000244140625, -1877.199951171875)
        node_Frame_020.shrink = True
        try: node_Frame_020.location_absolute = Vector((-1000.4000244140625, -1877.199951171875))
        except: pass
        try: node_Frame_020.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_020.mute = False
        except: pass
        try: node_Frame_020.bl_label = 'Frame'
        except: pass
        try: node_Frame_020.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_020.bl_icon = 'NONE'
        except: pass
        try: node_Frame_020.bl_width_default = 150.0
        except: pass
        try: node_Frame_020.bl_width_min = 100.0
        except: pass
        try: node_Frame_020.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_020.bl_height_default = 100.0
        except: pass
        try: node_Frame_020.bl_height_min = 30.0
        except: pass
        try: node_Frame_020.bl_height_max = 30.0
        except: pass
        try: node_Frame_020.text = None
        except: pass
        try: node_Frame_020.shrink = True
        except: pass
        try: node_Frame_020.label_size = 20
        except: pass
        created_nodes['Frame.020'] = node_Frame_020
        node_Separate_Color_002 = group.nodes.new('ShaderNodeSeparateColor')
        node_Separate_Color_002.location_absolute = (-2715.113037109375, -1751.0316162109375)
        try: node_Separate_Color_002.location_absolute = Vector((-2715.113037109375, -1751.0316162109375))
        except: pass
        try: node_Separate_Color_002.warning_propagation = 'ALL'
        except: pass
        try: node_Separate_Color_002.mute = False
        except: pass
        try: node_Separate_Color_002.bl_label = 'Separate Color'
        except: pass
        try: node_Separate_Color_002.bl_description = 'Split a color into its individual components using multiple models'
        except: pass
        try: node_Separate_Color_002.bl_icon = 'NONE'
        except: pass
        try: node_Separate_Color_002.bl_width_default = 140.0
        except: pass
        try: node_Separate_Color_002.bl_width_min = 100.0
        except: pass
        try: node_Separate_Color_002.bl_width_max = 700.0
        except: pass
        try: node_Separate_Color_002.bl_height_default = 100.0
        except: pass
        try: node_Separate_Color_002.bl_height_min = 30.0
        except: pass
        try: node_Separate_Color_002.bl_height_max = 30.0
        except: pass
        try: node_Separate_Color_002.mode = 'RGB'
        except: pass
        created_nodes['Separate Color.002'] = node_Separate_Color_002
        node_Combine_Color_003 = group.nodes.new('ShaderNodeCombineColor')
        node_Combine_Color_003.location_absolute = (-2315.97021484375, -1741.2916259765625)
        try: node_Combine_Color_003.location_absolute = Vector((-2315.97021484375, -1741.2916259765625))
        except: pass
        try: node_Combine_Color_003.warning_propagation = 'ALL'
        except: pass
        try: node_Combine_Color_003.mute = False
        except: pass
        try: node_Combine_Color_003.bl_label = 'Combine Color'
        except: pass
        try: node_Combine_Color_003.bl_description = 'Create a color from individual components using multiple models'
        except: pass
        try: node_Combine_Color_003.bl_icon = 'NONE'
        except: pass
        try: node_Combine_Color_003.bl_width_default = 140.0
        except: pass
        try: node_Combine_Color_003.bl_width_min = 100.0
        except: pass
        try: node_Combine_Color_003.bl_width_max = 700.0
        except: pass
        try: node_Combine_Color_003.bl_height_default = 100.0
        except: pass
        try: node_Combine_Color_003.bl_height_min = 30.0
        except: pass
        try: node_Combine_Color_003.bl_height_max = 30.0
        except: pass
        try: node_Combine_Color_003.mode = 'RGB'
        except: pass
        created_nodes['Combine Color.003'] = node_Combine_Color_003
        node_Frame_021 = group.nodes.new('NodeFrame')
        node_Frame_021.location_absolute = (-2745.199951171875, -1705.5999755859375)
        node_Frame_021.label = 'Format'
        node_Frame_021.shrink = True
        try: node_Frame_021.location_absolute = Vector((-2745.199951171875, -1705.5999755859375))
        except: pass
        try: node_Frame_021.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_021.mute = False
        except: pass
        try: node_Frame_021.bl_label = 'Frame'
        except: pass
        try: node_Frame_021.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_021.bl_icon = 'NONE'
        except: pass
        try: node_Frame_021.bl_width_default = 150.0
        except: pass
        try: node_Frame_021.bl_width_min = 100.0
        except: pass
        try: node_Frame_021.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_021.bl_height_default = 100.0
        except: pass
        try: node_Frame_021.bl_height_min = 30.0
        except: pass
        try: node_Frame_021.bl_height_max = 30.0
        except: pass
        try: node_Frame_021.text = None
        except: pass
        try: node_Frame_021.shrink = True
        except: pass
        try: node_Frame_021.label_size = 20
        except: pass
        created_nodes['Frame.021'] = node_Frame_021
        node_Invert_Color_002 = group.nodes.new('ShaderNodeInvert')
        node_Invert_Color_002.location_absolute = (-2514.9853515625, -1806.5592041015625)
        try: node_Invert_Color_002.location_absolute = Vector((-2514.9853515625, -1806.5592041015625))
        except: pass
        try: node_Invert_Color_002.warning_propagation = 'ALL'
        except: pass
        try: node_Invert_Color_002.mute = False
        except: pass
        try: node_Invert_Color_002.bl_label = 'Invert Color'
        except: pass
        try: node_Invert_Color_002.bl_description = 'Invert a color, producing a negative'
        except: pass
        try: node_Invert_Color_002.bl_icon = 'NONE'
        except: pass
        try: node_Invert_Color_002.bl_width_default = 140.0
        except: pass
        try: node_Invert_Color_002.bl_width_min = 100.0
        except: pass
        try: node_Invert_Color_002.bl_width_max = 700.0
        except: pass
        try: node_Invert_Color_002.bl_height_default = 100.0
        except: pass
        try: node_Invert_Color_002.bl_height_min = 30.0
        except: pass
        try: node_Invert_Color_002.bl_height_max = 30.0
        except: pass
        created_nodes['Invert Color.002'] = node_Invert_Color_002
        node_Vector_Math_040 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_040.location_absolute = (-1219.567138671875, -1740.791748046875)
        try: node_Vector_Math_040.location_absolute = Vector((-1219.567138671875, -1740.791748046875))
        except: pass
        try: node_Vector_Math_040.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_040.mute = False
        except: pass
        try: node_Vector_Math_040.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_040.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_040.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_040.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_040.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_040.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_040.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_040.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_040.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_040.operation = 'NORMALIZE'
        except: pass
        try: node_Vector_Math_040.inputs[1].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_040.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_040.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.040'] = node_Vector_Math_040
        node_Vector_Math_041 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_041.location_absolute = (-1401.1807861328125, -1740.767822265625)
        try: node_Vector_Math_041.location_absolute = Vector((-1401.1807861328125, -1740.767822265625))
        except: pass
        try: node_Vector_Math_041.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_041.mute = False
        except: pass
        try: node_Vector_Math_041.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_041.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_041.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_041.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_041.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_041.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_041.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_041.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_041.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_041.operation = 'MULTIPLY'
        except: pass
        try: node_Vector_Math_041.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_041.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.041'] = node_Vector_Math_041
        node_Frame_027 = group.nodes.new('NodeFrame')
        node_Frame_027.location_absolute = (-1430.800048828125, -1704.800048828125)
        node_Frame_027.label = 'Strength'
        node_Frame_027.shrink = True
        try: node_Frame_027.location_absolute = Vector((-1430.800048828125, -1704.800048828125))
        except: pass
        try: node_Frame_027.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_027.mute = False
        except: pass
        try: node_Frame_027.bl_label = 'Frame'
        except: pass
        try: node_Frame_027.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_027.bl_icon = 'NONE'
        except: pass
        try: node_Frame_027.bl_width_default = 150.0
        except: pass
        try: node_Frame_027.bl_width_min = 100.0
        except: pass
        try: node_Frame_027.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_027.bl_height_default = 100.0
        except: pass
        try: node_Frame_027.bl_height_min = 30.0
        except: pass
        try: node_Frame_027.bl_height_max = 30.0
        except: pass
        try: node_Frame_027.text = None
        except: pass
        try: node_Frame_027.shrink = True
        except: pass
        try: node_Frame_027.label_size = 20
        except: pass
        created_nodes['Frame.027'] = node_Frame_027
        node_Separate_XYZ_013 = group.nodes.new('ShaderNodeSeparateXYZ')
        node_Separate_XYZ_013.location_absolute = (-601.14501953125, -1714.010009765625)
        try: node_Separate_XYZ_013.location_absolute = Vector((-601.14501953125, -1714.010009765625))
        except: pass
        try: node_Separate_XYZ_013.warning_propagation = 'ALL'
        except: pass
        try: node_Separate_XYZ_013.mute = False
        except: pass
        try: node_Separate_XYZ_013.bl_label = 'Separate XYZ'
        except: pass
        try: node_Separate_XYZ_013.bl_description = 'Split a vector into its X, Y, and Z components'
        except: pass
        try: node_Separate_XYZ_013.bl_icon = 'NONE'
        except: pass
        try: node_Separate_XYZ_013.bl_width_default = 140.0
        except: pass
        try: node_Separate_XYZ_013.bl_width_min = 100.0
        except: pass
        try: node_Separate_XYZ_013.bl_width_max = 700.0
        except: pass
        try: node_Separate_XYZ_013.bl_height_default = 100.0
        except: pass
        try: node_Separate_XYZ_013.bl_height_min = 30.0
        except: pass
        try: node_Separate_XYZ_013.bl_height_max = 30.0
        except: pass
        created_nodes['Separate XYZ.013'] = node_Separate_XYZ_013
        node_Math_009 = group.nodes.new('ShaderNodeMath')
        node_Math_009.location_absolute = (-412.29345703125, -1682.2142333984375)
        try: node_Math_009.location_absolute = Vector((-412.29345703125, -1682.2142333984375))
        except: pass
        try: node_Math_009.warning_propagation = 'ALL'
        except: pass
        try: node_Math_009.mute = False
        except: pass
        try: node_Math_009.bl_label = 'Math'
        except: pass
        try: node_Math_009.bl_description = 'Perform math operations'
        except: pass
        try: node_Math_009.bl_icon = 'NONE'
        except: pass
        try: node_Math_009.bl_width_default = 140.0
        except: pass
        try: node_Math_009.bl_width_min = 100.0
        except: pass
        try: node_Math_009.bl_width_max = 700.0
        except: pass
        try: node_Math_009.bl_height_default = 100.0
        except: pass
        try: node_Math_009.bl_height_min = 30.0
        except: pass
        try: node_Math_009.bl_height_max = 30.0
        except: pass
        try: node_Math_009.operation = 'MULTIPLY'
        except: pass
        try: node_Math_009.use_clamp = False
        except: pass
        try: node_Math_009.inputs[1].default_value = -1.0
        except: pass
        try: node_Math_009.inputs[2].default_value = 0.5
        except: pass
        created_nodes['Math.009'] = node_Math_009
        node_Combine_XYZ_014 = group.nodes.new('ShaderNodeCombineXYZ')
        node_Combine_XYZ_014.location_absolute = (-1226.9718017578125, -1893.978271484375)
        try: node_Combine_XYZ_014.location_absolute = Vector((-1226.9718017578125, -1893.978271484375))
        except: pass
        try: node_Combine_XYZ_014.warning_propagation = 'ALL'
        except: pass
        try: node_Combine_XYZ_014.mute = False
        except: pass
        try: node_Combine_XYZ_014.bl_label = 'Combine XYZ'
        except: pass
        try: node_Combine_XYZ_014.bl_description = 'Create a vector from X, Y, and Z components'
        except: pass
        try: node_Combine_XYZ_014.bl_icon = 'NONE'
        except: pass
        try: node_Combine_XYZ_014.bl_width_default = 140.0
        except: pass
        try: node_Combine_XYZ_014.bl_width_min = 100.0
        except: pass
        try: node_Combine_XYZ_014.bl_width_max = 700.0
        except: pass
        try: node_Combine_XYZ_014.bl_height_default = 100.0
        except: pass
        try: node_Combine_XYZ_014.bl_height_min = 30.0
        except: pass
        try: node_Combine_XYZ_014.bl_height_max = 30.0
        except: pass
        try: node_Combine_XYZ_014.inputs[2].default_value = 1.0
        except: pass
        created_nodes['Combine XYZ.014'] = node_Combine_XYZ_014
        node_Vector_Rotate_003 = group.nodes.new('ShaderNodeVectorRotate')
        node_Vector_Rotate_003.location_absolute = (-1673.7275390625, -1806.0911865234375)
        try: node_Vector_Rotate_003.location_absolute = Vector((-1673.7275390625, -1806.0911865234375))
        except: pass
        try: node_Vector_Rotate_003.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Rotate_003.mute = False
        except: pass
        try: node_Vector_Rotate_003.bl_label = 'Vector Rotate'
        except: pass
        try: node_Vector_Rotate_003.bl_description = 'Rotate a vector around a pivot point (center)'
        except: pass
        try: node_Vector_Rotate_003.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Rotate_003.bl_width_default = 140.0
        except: pass
        try: node_Vector_Rotate_003.bl_width_min = 100.0
        except: pass
        try: node_Vector_Rotate_003.bl_width_max = 700.0
        except: pass
        try: node_Vector_Rotate_003.bl_height_default = 100.0
        except: pass
        try: node_Vector_Rotate_003.bl_height_min = 30.0
        except: pass
        try: node_Vector_Rotate_003.bl_height_max = 30.0
        except: pass
        try: node_Vector_Rotate_003.rotation_type = 'Z_AXIS'
        except: pass
        try: node_Vector_Rotate_003.invert = False
        except: pass
        try: node_Vector_Rotate_003.inputs[1].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Rotate_003.inputs[2].default_value = [0.0,0.0,1.0]
        except: pass
        created_nodes['Vector Rotate.003'] = node_Vector_Rotate_003
        node_Vector_Rotate_004 = group.nodes.new('ShaderNodeVectorRotate')
        node_Vector_Rotate_004.location_absolute = (-1706.5941162109375, -257.99139404296875)
        try: node_Vector_Rotate_004.location_absolute = Vector((-1706.5941162109375, -257.99139404296875))
        except: pass
        try: node_Vector_Rotate_004.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Rotate_004.mute = False
        except: pass
        try: node_Vector_Rotate_004.bl_label = 'Vector Rotate'
        except: pass
        try: node_Vector_Rotate_004.bl_description = 'Rotate a vector around a pivot point (center)'
        except: pass
        try: node_Vector_Rotate_004.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Rotate_004.bl_width_default = 140.0
        except: pass
        try: node_Vector_Rotate_004.bl_width_min = 100.0
        except: pass
        try: node_Vector_Rotate_004.bl_width_max = 700.0
        except: pass
        try: node_Vector_Rotate_004.bl_height_default = 100.0
        except: pass
        try: node_Vector_Rotate_004.bl_height_min = 30.0
        except: pass
        try: node_Vector_Rotate_004.bl_height_max = 30.0
        except: pass
        try: node_Vector_Rotate_004.rotation_type = 'Z_AXIS'
        except: pass
        try: node_Vector_Rotate_004.invert = False
        except: pass
        try: node_Vector_Rotate_004.inputs[1].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Rotate_004.inputs[2].default_value = [0.0,0.0,1.0]
        except: pass
        created_nodes['Vector Rotate.004'] = node_Vector_Rotate_004
        node_Vector_Rotate_005 = group.nodes.new('ShaderNodeVectorRotate')
        node_Vector_Rotate_005.location_absolute = (-1695.5198974609375, -1024.2130126953125)
        try: node_Vector_Rotate_005.location_absolute = Vector((-1695.5198974609375, -1024.2130126953125))
        except: pass
        try: node_Vector_Rotate_005.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Rotate_005.mute = False
        except: pass
        try: node_Vector_Rotate_005.bl_label = 'Vector Rotate'
        except: pass
        try: node_Vector_Rotate_005.bl_description = 'Rotate a vector around a pivot point (center)'
        except: pass
        try: node_Vector_Rotate_005.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Rotate_005.bl_width_default = 140.0
        except: pass
        try: node_Vector_Rotate_005.bl_width_min = 100.0
        except: pass
        try: node_Vector_Rotate_005.bl_width_max = 700.0
        except: pass
        try: node_Vector_Rotate_005.bl_height_default = 100.0
        except: pass
        try: node_Vector_Rotate_005.bl_height_min = 30.0
        except: pass
        try: node_Vector_Rotate_005.bl_height_max = 30.0
        except: pass
        try: node_Vector_Rotate_005.rotation_type = 'Z_AXIS'
        except: pass
        try: node_Vector_Rotate_005.invert = False
        except: pass
        try: node_Vector_Rotate_005.inputs[1].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Rotate_005.inputs[2].default_value = [0.0,0.0,1.0]
        except: pass
        created_nodes['Vector Rotate.005'] = node_Vector_Rotate_005
        node_Vector_Math_049 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_049.location_absolute = (-1934.5257568359375, 2810.3671875)
        try: node_Vector_Math_049.location_absolute = Vector((-1934.5257568359375, 2810.3671875))
        except: pass
        try: node_Vector_Math_049.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_049.mute = False
        except: pass
        try: node_Vector_Math_049.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_049.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_049.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_049.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_049.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_049.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_049.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_049.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_049.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_049.operation = 'MULTIPLY'
        except: pass
        try: node_Vector_Math_049.inputs[1].default_value = [2.0,2.0,2.0]
        except: pass
        try: node_Vector_Math_049.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_049.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.049'] = node_Vector_Math_049
        node_Vector_Math_050 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_050.location_absolute = (-1756.421142578125, 2807.70654296875)
        try: node_Vector_Math_050.location_absolute = Vector((-1756.421142578125, 2807.70654296875))
        except: pass
        try: node_Vector_Math_050.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_050.mute = False
        except: pass
        try: node_Vector_Math_050.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_050.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_050.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_050.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_050.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_050.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_050.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_050.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_050.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_050.operation = 'SUBTRACT'
        except: pass
        try: node_Vector_Math_050.inputs[1].default_value = [1.0,1.0,1.0]
        except: pass
        try: node_Vector_Math_050.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_050.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.050'] = node_Vector_Math_050
        node_Frame_028 = group.nodes.new('NodeFrame')
        node_Frame_028.location_absolute = (-1964.4000244140625, 2846.39990234375)
        node_Frame_028.label = 'Unpack'
        node_Frame_028.shrink = True
        try: node_Frame_028.location_absolute = Vector((-1964.4000244140625, 2846.39990234375))
        except: pass
        try: node_Frame_028.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_028.mute = False
        except: pass
        try: node_Frame_028.bl_label = 'Frame'
        except: pass
        try: node_Frame_028.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_028.bl_icon = 'NONE'
        except: pass
        try: node_Frame_028.bl_width_default = 150.0
        except: pass
        try: node_Frame_028.bl_width_min = 100.0
        except: pass
        try: node_Frame_028.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_028.bl_height_default = 100.0
        except: pass
        try: node_Frame_028.bl_height_min = 30.0
        except: pass
        try: node_Frame_028.bl_height_max = 30.0
        except: pass
        try: node_Frame_028.text = None
        except: pass
        try: node_Frame_028.shrink = True
        except: pass
        try: node_Frame_028.label_size = 20
        except: pass
        created_nodes['Frame.028'] = node_Frame_028
        node_Texture_Coordinate_026 = group.nodes.new('ShaderNodeTexCoord')
        node_Texture_Coordinate_026.location_absolute = (-1100.008544921875, 2632.54541015625)
        try: node_Texture_Coordinate_026.location_absolute = Vector((-1100.008544921875, 2632.54541015625))
        except: pass
        try: node_Texture_Coordinate_026.warning_propagation = 'ALL'
        except: pass
        try: node_Texture_Coordinate_026.mute = False
        except: pass
        try: node_Texture_Coordinate_026.bl_label = 'Texture Coordinate'
        except: pass
        try: node_Texture_Coordinate_026.bl_description = 'Retrieve multiple types of texture coordinates.\nTypically used as inputs for texture nodes'
        except: pass
        try: node_Texture_Coordinate_026.bl_icon = 'NONE'
        except: pass
        try: node_Texture_Coordinate_026.bl_width_default = 140.0
        except: pass
        try: node_Texture_Coordinate_026.bl_width_min = 100.0
        except: pass
        try: node_Texture_Coordinate_026.bl_width_max = 700.0
        except: pass
        try: node_Texture_Coordinate_026.bl_height_default = 100.0
        except: pass
        try: node_Texture_Coordinate_026.bl_height_min = 30.0
        except: pass
        try: node_Texture_Coordinate_026.bl_height_max = 30.0
        except: pass
        try: node_Texture_Coordinate_026.object = None
        except: pass
        try: node_Texture_Coordinate_026.from_instancer = False
        except: pass
        created_nodes['Texture Coordinate.026'] = node_Texture_Coordinate_026
        node_Vector_Math_051 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_051.location_absolute = (-837.5324096679688, 2497.02587890625)
        try: node_Vector_Math_051.location_absolute = Vector((-837.5324096679688, 2497.02587890625))
        except: pass
        try: node_Vector_Math_051.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_051.mute = False
        except: pass
        try: node_Vector_Math_051.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_051.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_051.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_051.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_051.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_051.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_051.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_051.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_051.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_051.operation = 'CROSS_PRODUCT'
        except: pass
        try: node_Vector_Math_051.inputs[1].default_value = [0.0,0.0,1.0]
        except: pass
        try: node_Vector_Math_051.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_051.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.051'] = node_Vector_Math_051
        node_Vector_Math_052 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_052.location_absolute = (-716.7023315429688, 2651.85400390625)
        try: node_Vector_Math_052.location_absolute = Vector((-716.7023315429688, 2651.85400390625))
        except: pass
        try: node_Vector_Math_052.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_052.mute = False
        except: pass
        try: node_Vector_Math_052.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_052.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_052.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_052.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_052.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_052.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_052.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_052.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_052.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_052.operation = 'CROSS_PRODUCT'
        except: pass
        try: node_Vector_Math_052.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_052.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.052'] = node_Vector_Math_052
        node_Vector_Math_053 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_053.location_absolute = (-262.69158935546875, 2821.639404296875)
        try: node_Vector_Math_053.location_absolute = Vector((-262.69158935546875, 2821.639404296875))
        except: pass
        try: node_Vector_Math_053.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_053.mute = False
        except: pass
        try: node_Vector_Math_053.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_053.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_053.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_053.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_053.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_053.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_053.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_053.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_053.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_053.operation = 'MULTIPLY'
        except: pass
        try: node_Vector_Math_053.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_053.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.053'] = node_Vector_Math_053
        node_Vector_Math_054 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_054.location_absolute = (-260.83074951171875, 2661.848388671875)
        try: node_Vector_Math_054.location_absolute = Vector((-260.83074951171875, 2661.848388671875))
        except: pass
        try: node_Vector_Math_054.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_054.mute = False
        except: pass
        try: node_Vector_Math_054.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_054.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_054.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_054.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_054.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_054.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_054.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_054.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_054.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_054.operation = 'MULTIPLY'
        except: pass
        try: node_Vector_Math_054.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_054.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.054'] = node_Vector_Math_054
        node_Vector_Math_055 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_055.location_absolute = (-260.8306579589844, 2500.60693359375)
        try: node_Vector_Math_055.location_absolute = Vector((-260.8306579589844, 2500.60693359375))
        except: pass
        try: node_Vector_Math_055.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_055.mute = False
        except: pass
        try: node_Vector_Math_055.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_055.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_055.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_055.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_055.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_055.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_055.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_055.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_055.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_055.operation = 'MULTIPLY'
        except: pass
        try: node_Vector_Math_055.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_055.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.055'] = node_Vector_Math_055
        node_Vector_Math_056 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_056.location_absolute = (-79.55843353271484, 2765.099365234375)
        try: node_Vector_Math_056.location_absolute = Vector((-79.55843353271484, 2765.099365234375))
        except: pass
        try: node_Vector_Math_056.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_056.mute = False
        except: pass
        try: node_Vector_Math_056.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_056.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_056.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_056.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_056.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_056.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_056.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_056.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_056.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_056.operation = 'ADD'
        except: pass
        try: node_Vector_Math_056.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_056.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.056'] = node_Vector_Math_056
        node_Vector_Math_057 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_057.location_absolute = (145.12310791015625, 2595.0166015625)
        try: node_Vector_Math_057.location_absolute = Vector((145.12310791015625, 2595.0166015625))
        except: pass
        try: node_Vector_Math_057.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_057.mute = False
        except: pass
        try: node_Vector_Math_057.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_057.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_057.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_057.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_057.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_057.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_057.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_057.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_057.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_057.operation = 'ADD'
        except: pass
        try: node_Vector_Math_057.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_057.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.057'] = node_Vector_Math_057
        node_Vector_Math_058 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_058.location_absolute = (306.7969970703125, 2589.1591796875)
        try: node_Vector_Math_058.location_absolute = Vector((306.7969970703125, 2589.1591796875))
        except: pass
        try: node_Vector_Math_058.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_058.mute = False
        except: pass
        try: node_Vector_Math_058.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_058.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_058.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_058.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_058.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_058.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_058.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_058.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_058.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_058.operation = 'NORMALIZE'
        except: pass
        try: node_Vector_Math_058.inputs[1].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_058.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_058.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.058'] = node_Vector_Math_058
        node_Frame_029 = group.nodes.new('NodeFrame')
        node_Frame_029.location_absolute = (-1130.0, 2682.0)
        node_Frame_029.shrink = True
        try: node_Frame_029.location_absolute = Vector((-1130.0, 2682.0))
        except: pass
        try: node_Frame_029.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_029.mute = False
        except: pass
        try: node_Frame_029.bl_label = 'Frame'
        except: pass
        try: node_Frame_029.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_029.bl_icon = 'NONE'
        except: pass
        try: node_Frame_029.bl_width_default = 150.0
        except: pass
        try: node_Frame_029.bl_width_min = 100.0
        except: pass
        try: node_Frame_029.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_029.bl_height_default = 100.0
        except: pass
        try: node_Frame_029.bl_height_min = 30.0
        except: pass
        try: node_Frame_029.bl_height_max = 30.0
        except: pass
        try: node_Frame_029.text = None
        except: pass
        try: node_Frame_029.shrink = True
        except: pass
        try: node_Frame_029.label_size = 20
        except: pass
        created_nodes['Frame.029'] = node_Frame_029
        node_Separate_Color_004 = group.nodes.new('ShaderNodeSeparateColor')
        node_Separate_Color_004.location_absolute = (-2542.749267578125, 2801.177734375)
        try: node_Separate_Color_004.location_absolute = Vector((-2542.749267578125, 2801.177734375))
        except: pass
        try: node_Separate_Color_004.warning_propagation = 'ALL'
        except: pass
        try: node_Separate_Color_004.mute = False
        except: pass
        try: node_Separate_Color_004.bl_label = 'Separate Color'
        except: pass
        try: node_Separate_Color_004.bl_description = 'Split a color into its individual components using multiple models'
        except: pass
        try: node_Separate_Color_004.bl_icon = 'NONE'
        except: pass
        try: node_Separate_Color_004.bl_width_default = 140.0
        except: pass
        try: node_Separate_Color_004.bl_width_min = 100.0
        except: pass
        try: node_Separate_Color_004.bl_width_max = 700.0
        except: pass
        try: node_Separate_Color_004.bl_height_default = 100.0
        except: pass
        try: node_Separate_Color_004.bl_height_min = 30.0
        except: pass
        try: node_Separate_Color_004.bl_height_max = 30.0
        except: pass
        try: node_Separate_Color_004.mode = 'RGB'
        except: pass
        created_nodes['Separate Color.004'] = node_Separate_Color_004
        node_Combine_Color_004 = group.nodes.new('ShaderNodeCombineColor')
        node_Combine_Color_004.location_absolute = (-2143.606201171875, 2810.91796875)
        try: node_Combine_Color_004.location_absolute = Vector((-2143.606201171875, 2810.91796875))
        except: pass
        try: node_Combine_Color_004.warning_propagation = 'ALL'
        except: pass
        try: node_Combine_Color_004.mute = False
        except: pass
        try: node_Combine_Color_004.bl_label = 'Combine Color'
        except: pass
        try: node_Combine_Color_004.bl_description = 'Create a color from individual components using multiple models'
        except: pass
        try: node_Combine_Color_004.bl_icon = 'NONE'
        except: pass
        try: node_Combine_Color_004.bl_width_default = 140.0
        except: pass
        try: node_Combine_Color_004.bl_width_min = 100.0
        except: pass
        try: node_Combine_Color_004.bl_width_max = 700.0
        except: pass
        try: node_Combine_Color_004.bl_height_default = 100.0
        except: pass
        try: node_Combine_Color_004.bl_height_min = 30.0
        except: pass
        try: node_Combine_Color_004.bl_height_max = 30.0
        except: pass
        try: node_Combine_Color_004.mode = 'RGB'
        except: pass
        created_nodes['Combine Color.004'] = node_Combine_Color_004
        node_Frame_030 = group.nodes.new('NodeFrame')
        node_Frame_030.location_absolute = (-2572.39990234375, 2847.199951171875)
        node_Frame_030.label = 'Format'
        node_Frame_030.shrink = True
        try: node_Frame_030.location_absolute = Vector((-2572.39990234375, 2847.199951171875))
        except: pass
        try: node_Frame_030.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_030.mute = False
        except: pass
        try: node_Frame_030.bl_label = 'Frame'
        except: pass
        try: node_Frame_030.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_030.bl_icon = 'NONE'
        except: pass
        try: node_Frame_030.bl_width_default = 150.0
        except: pass
        try: node_Frame_030.bl_width_min = 100.0
        except: pass
        try: node_Frame_030.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_030.bl_height_default = 100.0
        except: pass
        try: node_Frame_030.bl_height_min = 30.0
        except: pass
        try: node_Frame_030.bl_height_max = 30.0
        except: pass
        try: node_Frame_030.text = None
        except: pass
        try: node_Frame_030.shrink = True
        except: pass
        try: node_Frame_030.label_size = 20
        except: pass
        created_nodes['Frame.030'] = node_Frame_030
        node_Invert_Color_004 = group.nodes.new('ShaderNodeInvert')
        node_Invert_Color_004.location_absolute = (-2342.62158203125, 2745.650390625)
        try: node_Invert_Color_004.location_absolute = Vector((-2342.62158203125, 2745.650390625))
        except: pass
        try: node_Invert_Color_004.warning_propagation = 'ALL'
        except: pass
        try: node_Invert_Color_004.mute = False
        except: pass
        try: node_Invert_Color_004.bl_label = 'Invert Color'
        except: pass
        try: node_Invert_Color_004.bl_description = 'Invert a color, producing a negative'
        except: pass
        try: node_Invert_Color_004.bl_icon = 'NONE'
        except: pass
        try: node_Invert_Color_004.bl_width_default = 140.0
        except: pass
        try: node_Invert_Color_004.bl_width_min = 100.0
        except: pass
        try: node_Invert_Color_004.bl_width_max = 700.0
        except: pass
        try: node_Invert_Color_004.bl_height_default = 100.0
        except: pass
        try: node_Invert_Color_004.bl_height_min = 30.0
        except: pass
        try: node_Invert_Color_004.bl_height_max = 30.0
        except: pass
        created_nodes['Invert Color.004'] = node_Invert_Color_004
        node_Vector_Math_059 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_059.location_absolute = (-1309.4456787109375, 2845.650146484375)
        try: node_Vector_Math_059.location_absolute = Vector((-1309.4456787109375, 2845.650146484375))
        except: pass
        try: node_Vector_Math_059.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_059.mute = False
        except: pass
        try: node_Vector_Math_059.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_059.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_059.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_059.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_059.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_059.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_059.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_059.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_059.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_059.operation = 'NORMALIZE'
        except: pass
        try: node_Vector_Math_059.inputs[1].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_059.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_059.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.059'] = node_Vector_Math_059
        node_Vector_Math_060 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_060.location_absolute = (-1491.0594482421875, 2845.67431640625)
        try: node_Vector_Math_060.location_absolute = Vector((-1491.0594482421875, 2845.67431640625))
        except: pass
        try: node_Vector_Math_060.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_060.mute = False
        except: pass
        try: node_Vector_Math_060.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_060.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_060.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_060.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_060.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_060.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_060.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_060.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_060.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_060.operation = 'MULTIPLY'
        except: pass
        try: node_Vector_Math_060.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_060.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.060'] = node_Vector_Math_060
        node_Frame_031 = group.nodes.new('NodeFrame')
        node_Frame_031.location_absolute = (-1521.199951171875, 2881.60009765625)
        node_Frame_031.label = 'Strength'
        node_Frame_031.shrink = True
        try: node_Frame_031.location_absolute = Vector((-1521.199951171875, 2881.60009765625))
        except: pass
        try: node_Frame_031.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_031.mute = False
        except: pass
        try: node_Frame_031.bl_label = 'Frame'
        except: pass
        try: node_Frame_031.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_031.bl_icon = 'NONE'
        except: pass
        try: node_Frame_031.bl_width_default = 150.0
        except: pass
        try: node_Frame_031.bl_width_min = 100.0
        except: pass
        try: node_Frame_031.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_031.bl_height_default = 100.0
        except: pass
        try: node_Frame_031.bl_height_min = 30.0
        except: pass
        try: node_Frame_031.bl_height_max = 30.0
        except: pass
        try: node_Frame_031.text = None
        except: pass
        try: node_Frame_031.shrink = True
        except: pass
        try: node_Frame_031.label_size = 20
        except: pass
        created_nodes['Frame.031'] = node_Frame_031
        node_Separate_XYZ_014 = group.nodes.new('ShaderNodeSeparateXYZ')
        node_Separate_XYZ_014.location_absolute = (-685.7590942382812, 2829.49169921875)
        try: node_Separate_XYZ_014.location_absolute = Vector((-685.7590942382812, 2829.49169921875))
        except: pass
        try: node_Separate_XYZ_014.warning_propagation = 'ALL'
        except: pass
        try: node_Separate_XYZ_014.mute = False
        except: pass
        try: node_Separate_XYZ_014.bl_label = 'Separate XYZ'
        except: pass
        try: node_Separate_XYZ_014.bl_description = 'Split a vector into its X, Y, and Z components'
        except: pass
        try: node_Separate_XYZ_014.bl_icon = 'NONE'
        except: pass
        try: node_Separate_XYZ_014.bl_width_default = 140.0
        except: pass
        try: node_Separate_XYZ_014.bl_width_min = 100.0
        except: pass
        try: node_Separate_XYZ_014.bl_width_max = 700.0
        except: pass
        try: node_Separate_XYZ_014.bl_height_default = 100.0
        except: pass
        try: node_Separate_XYZ_014.bl_height_min = 30.0
        except: pass
        try: node_Separate_XYZ_014.bl_height_max = 30.0
        except: pass
        created_nodes['Separate XYZ.014'] = node_Separate_XYZ_014
        node_Math_010 = group.nodes.new('ShaderNodeMath')
        node_Math_010.location_absolute = (-496.9073181152344, 2861.28759765625)
        try: node_Math_010.location_absolute = Vector((-496.9073181152344, 2861.28759765625))
        except: pass
        try: node_Math_010.warning_propagation = 'ALL'
        except: pass
        try: node_Math_010.mute = False
        except: pass
        try: node_Math_010.bl_label = 'Math'
        except: pass
        try: node_Math_010.bl_description = 'Perform math operations'
        except: pass
        try: node_Math_010.bl_icon = 'NONE'
        except: pass
        try: node_Math_010.bl_width_default = 140.0
        except: pass
        try: node_Math_010.bl_width_min = 100.0
        except: pass
        try: node_Math_010.bl_width_max = 700.0
        except: pass
        try: node_Math_010.bl_height_default = 100.0
        except: pass
        try: node_Math_010.bl_height_min = 30.0
        except: pass
        try: node_Math_010.bl_height_max = 30.0
        except: pass
        try: node_Math_010.operation = 'MULTIPLY'
        except: pass
        try: node_Math_010.use_clamp = False
        except: pass
        try: node_Math_010.inputs[1].default_value = -1.0
        except: pass
        try: node_Math_010.inputs[2].default_value = 0.5
        except: pass
        created_nodes['Math.010'] = node_Math_010
        node_Combine_XYZ_015 = group.nodes.new('ShaderNodeCombineXYZ')
        node_Combine_XYZ_015.location_absolute = (-1316.850341796875, 2692.46337890625)
        try: node_Combine_XYZ_015.location_absolute = Vector((-1316.850341796875, 2692.46337890625))
        except: pass
        try: node_Combine_XYZ_015.warning_propagation = 'ALL'
        except: pass
        try: node_Combine_XYZ_015.mute = False
        except: pass
        try: node_Combine_XYZ_015.bl_label = 'Combine XYZ'
        except: pass
        try: node_Combine_XYZ_015.bl_description = 'Create a vector from X, Y, and Z components'
        except: pass
        try: node_Combine_XYZ_015.bl_icon = 'NONE'
        except: pass
        try: node_Combine_XYZ_015.bl_width_default = 140.0
        except: pass
        try: node_Combine_XYZ_015.bl_width_min = 100.0
        except: pass
        try: node_Combine_XYZ_015.bl_width_max = 700.0
        except: pass
        try: node_Combine_XYZ_015.bl_height_default = 100.0
        except: pass
        try: node_Combine_XYZ_015.bl_height_min = 30.0
        except: pass
        try: node_Combine_XYZ_015.bl_height_max = 30.0
        except: pass
        try: node_Combine_XYZ_015.inputs[2].default_value = 1.0
        except: pass
        created_nodes['Combine XYZ.015'] = node_Combine_XYZ_015
        node_Vector_Math_061 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_061.location_absolute = (-1921.085205078125, 3398.27490234375)
        try: node_Vector_Math_061.location_absolute = Vector((-1921.085205078125, 3398.27490234375))
        except: pass
        try: node_Vector_Math_061.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_061.mute = False
        except: pass
        try: node_Vector_Math_061.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_061.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_061.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_061.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_061.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_061.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_061.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_061.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_061.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_061.operation = 'MULTIPLY'
        except: pass
        try: node_Vector_Math_061.inputs[1].default_value = [2.0,2.0,2.0]
        except: pass
        try: node_Vector_Math_061.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_061.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.061'] = node_Vector_Math_061
        node_Vector_Math_062 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_062.location_absolute = (-1742.98046875, 3395.614013671875)
        try: node_Vector_Math_062.location_absolute = Vector((-1742.98046875, 3395.614013671875))
        except: pass
        try: node_Vector_Math_062.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_062.mute = False
        except: pass
        try: node_Vector_Math_062.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_062.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_062.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_062.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_062.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_062.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_062.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_062.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_062.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_062.operation = 'SUBTRACT'
        except: pass
        try: node_Vector_Math_062.inputs[1].default_value = [1.0,1.0,1.0]
        except: pass
        try: node_Vector_Math_062.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_062.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.062'] = node_Vector_Math_062
        node_Frame_032 = group.nodes.new('NodeFrame')
        node_Frame_032.location_absolute = (-1950.800048828125, 3434.39990234375)
        node_Frame_032.label = 'Unpack'
        node_Frame_032.shrink = True
        try: node_Frame_032.location_absolute = Vector((-1950.800048828125, 3434.39990234375))
        except: pass
        try: node_Frame_032.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_032.mute = False
        except: pass
        try: node_Frame_032.bl_label = 'Frame'
        except: pass
        try: node_Frame_032.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_032.bl_icon = 'NONE'
        except: pass
        try: node_Frame_032.bl_width_default = 150.0
        except: pass
        try: node_Frame_032.bl_width_min = 100.0
        except: pass
        try: node_Frame_032.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_032.bl_height_default = 100.0
        except: pass
        try: node_Frame_032.bl_height_min = 30.0
        except: pass
        try: node_Frame_032.bl_height_max = 30.0
        except: pass
        try: node_Frame_032.text = None
        except: pass
        try: node_Frame_032.shrink = True
        except: pass
        try: node_Frame_032.label_size = 20
        except: pass
        created_nodes['Frame.032'] = node_Frame_032
        node_Texture_Coordinate_027 = group.nodes.new('ShaderNodeTexCoord')
        node_Texture_Coordinate_027.location_absolute = (-1086.56787109375, 3220.453369140625)
        try: node_Texture_Coordinate_027.location_absolute = Vector((-1086.56787109375, 3220.453369140625))
        except: pass
        try: node_Texture_Coordinate_027.warning_propagation = 'ALL'
        except: pass
        try: node_Texture_Coordinate_027.mute = False
        except: pass
        try: node_Texture_Coordinate_027.bl_label = 'Texture Coordinate'
        except: pass
        try: node_Texture_Coordinate_027.bl_description = 'Retrieve multiple types of texture coordinates.\nTypically used as inputs for texture nodes'
        except: pass
        try: node_Texture_Coordinate_027.bl_icon = 'NONE'
        except: pass
        try: node_Texture_Coordinate_027.bl_width_default = 140.0
        except: pass
        try: node_Texture_Coordinate_027.bl_width_min = 100.0
        except: pass
        try: node_Texture_Coordinate_027.bl_width_max = 700.0
        except: pass
        try: node_Texture_Coordinate_027.bl_height_default = 100.0
        except: pass
        try: node_Texture_Coordinate_027.bl_height_min = 30.0
        except: pass
        try: node_Texture_Coordinate_027.bl_height_max = 30.0
        except: pass
        try: node_Texture_Coordinate_027.object = None
        except: pass
        try: node_Texture_Coordinate_027.from_instancer = False
        except: pass
        created_nodes['Texture Coordinate.027'] = node_Texture_Coordinate_027
        node_Vector_Math_063 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_063.location_absolute = (-824.091796875, 3084.933837890625)
        try: node_Vector_Math_063.location_absolute = Vector((-824.091796875, 3084.933837890625))
        except: pass
        try: node_Vector_Math_063.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_063.mute = False
        except: pass
        try: node_Vector_Math_063.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_063.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_063.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_063.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_063.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_063.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_063.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_063.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_063.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_063.operation = 'CROSS_PRODUCT'
        except: pass
        try: node_Vector_Math_063.inputs[1].default_value = [0.0,0.0,1.0]
        except: pass
        try: node_Vector_Math_063.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_063.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.063'] = node_Vector_Math_063
        node_Vector_Math_064 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_064.location_absolute = (-703.26171875, 3239.761962890625)
        try: node_Vector_Math_064.location_absolute = Vector((-703.26171875, 3239.761962890625))
        except: pass
        try: node_Vector_Math_064.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_064.mute = False
        except: pass
        try: node_Vector_Math_064.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_064.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_064.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_064.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_064.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_064.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_064.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_064.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_064.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_064.operation = 'CROSS_PRODUCT'
        except: pass
        try: node_Vector_Math_064.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_064.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.064'] = node_Vector_Math_064
        node_Vector_Math_065 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_065.location_absolute = (-249.2509307861328, 3409.54736328125)
        try: node_Vector_Math_065.location_absolute = Vector((-249.2509307861328, 3409.54736328125))
        except: pass
        try: node_Vector_Math_065.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_065.mute = False
        except: pass
        try: node_Vector_Math_065.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_065.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_065.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_065.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_065.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_065.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_065.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_065.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_065.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_065.operation = 'MULTIPLY'
        except: pass
        try: node_Vector_Math_065.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_065.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.065'] = node_Vector_Math_065
        node_Vector_Math_066 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_066.location_absolute = (-247.3900909423828, 3249.75634765625)
        try: node_Vector_Math_066.location_absolute = Vector((-247.3900909423828, 3249.75634765625))
        except: pass
        try: node_Vector_Math_066.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_066.mute = False
        except: pass
        try: node_Vector_Math_066.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_066.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_066.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_066.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_066.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_066.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_066.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_066.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_066.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_066.operation = 'MULTIPLY'
        except: pass
        try: node_Vector_Math_066.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_066.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.066'] = node_Vector_Math_066
        node_Vector_Math_067 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_067.location_absolute = (-247.39004516601562, 3088.5146484375)
        try: node_Vector_Math_067.location_absolute = Vector((-247.39004516601562, 3088.5146484375))
        except: pass
        try: node_Vector_Math_067.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_067.mute = False
        except: pass
        try: node_Vector_Math_067.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_067.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_067.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_067.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_067.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_067.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_067.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_067.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_067.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_067.operation = 'MULTIPLY'
        except: pass
        try: node_Vector_Math_067.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_067.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.067'] = node_Vector_Math_067
        node_Vector_Math_068 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_068.location_absolute = (-66.11775207519531, 3353.00732421875)
        try: node_Vector_Math_068.location_absolute = Vector((-66.11775207519531, 3353.00732421875))
        except: pass
        try: node_Vector_Math_068.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_068.mute = False
        except: pass
        try: node_Vector_Math_068.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_068.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_068.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_068.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_068.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_068.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_068.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_068.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_068.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_068.operation = 'ADD'
        except: pass
        try: node_Vector_Math_068.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_068.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.068'] = node_Vector_Math_068
        node_Vector_Math_069 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_069.location_absolute = (158.5637969970703, 3182.924560546875)
        try: node_Vector_Math_069.location_absolute = Vector((158.5637969970703, 3182.924560546875))
        except: pass
        try: node_Vector_Math_069.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_069.mute = False
        except: pass
        try: node_Vector_Math_069.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_069.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_069.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_069.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_069.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_069.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_069.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_069.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_069.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_069.operation = 'ADD'
        except: pass
        try: node_Vector_Math_069.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_069.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.069'] = node_Vector_Math_069
        node_Vector_Math_070 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_070.location_absolute = (320.2377014160156, 3177.067138671875)
        try: node_Vector_Math_070.location_absolute = Vector((320.2377014160156, 3177.067138671875))
        except: pass
        try: node_Vector_Math_070.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_070.mute = False
        except: pass
        try: node_Vector_Math_070.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_070.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_070.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_070.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_070.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_070.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_070.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_070.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_070.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_070.operation = 'NORMALIZE'
        except: pass
        try: node_Vector_Math_070.inputs[1].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_070.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_070.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.070'] = node_Vector_Math_070
        node_Frame_033 = group.nodes.new('NodeFrame')
        node_Frame_033.location_absolute = (-1116.4000244140625, 3270.0)
        node_Frame_033.shrink = True
        try: node_Frame_033.location_absolute = Vector((-1116.4000244140625, 3270.0))
        except: pass
        try: node_Frame_033.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_033.mute = False
        except: pass
        try: node_Frame_033.bl_label = 'Frame'
        except: pass
        try: node_Frame_033.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_033.bl_icon = 'NONE'
        except: pass
        try: node_Frame_033.bl_width_default = 150.0
        except: pass
        try: node_Frame_033.bl_width_min = 100.0
        except: pass
        try: node_Frame_033.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_033.bl_height_default = 100.0
        except: pass
        try: node_Frame_033.bl_height_min = 30.0
        except: pass
        try: node_Frame_033.bl_height_max = 30.0
        except: pass
        try: node_Frame_033.text = None
        except: pass
        try: node_Frame_033.shrink = True
        except: pass
        try: node_Frame_033.label_size = 20
        except: pass
        created_nodes['Frame.033'] = node_Frame_033
        node_Separate_Color_005 = group.nodes.new('ShaderNodeSeparateColor')
        node_Separate_Color_005.location_absolute = (-2529.30859375, 3389.08544921875)
        try: node_Separate_Color_005.location_absolute = Vector((-2529.30859375, 3389.08544921875))
        except: pass
        try: node_Separate_Color_005.warning_propagation = 'ALL'
        except: pass
        try: node_Separate_Color_005.mute = False
        except: pass
        try: node_Separate_Color_005.bl_label = 'Separate Color'
        except: pass
        try: node_Separate_Color_005.bl_description = 'Split a color into its individual components using multiple models'
        except: pass
        try: node_Separate_Color_005.bl_icon = 'NONE'
        except: pass
        try: node_Separate_Color_005.bl_width_default = 140.0
        except: pass
        try: node_Separate_Color_005.bl_width_min = 100.0
        except: pass
        try: node_Separate_Color_005.bl_width_max = 700.0
        except: pass
        try: node_Separate_Color_005.bl_height_default = 100.0
        except: pass
        try: node_Separate_Color_005.bl_height_min = 30.0
        except: pass
        try: node_Separate_Color_005.bl_height_max = 30.0
        except: pass
        try: node_Separate_Color_005.mode = 'RGB'
        except: pass
        created_nodes['Separate Color.005'] = node_Separate_Color_005
        node_Combine_Color_005 = group.nodes.new('ShaderNodeCombineColor')
        node_Combine_Color_005.location_absolute = (-2130.166015625, 3398.82568359375)
        try: node_Combine_Color_005.location_absolute = Vector((-2130.166015625, 3398.82568359375))
        except: pass
        try: node_Combine_Color_005.warning_propagation = 'ALL'
        except: pass
        try: node_Combine_Color_005.mute = False
        except: pass
        try: node_Combine_Color_005.bl_label = 'Combine Color'
        except: pass
        try: node_Combine_Color_005.bl_description = 'Create a color from individual components using multiple models'
        except: pass
        try: node_Combine_Color_005.bl_icon = 'NONE'
        except: pass
        try: node_Combine_Color_005.bl_width_default = 140.0
        except: pass
        try: node_Combine_Color_005.bl_width_min = 100.0
        except: pass
        try: node_Combine_Color_005.bl_width_max = 700.0
        except: pass
        try: node_Combine_Color_005.bl_height_default = 100.0
        except: pass
        try: node_Combine_Color_005.bl_height_min = 30.0
        except: pass
        try: node_Combine_Color_005.bl_height_max = 30.0
        except: pass
        try: node_Combine_Color_005.mode = 'RGB'
        except: pass
        created_nodes['Combine Color.005'] = node_Combine_Color_005
        node_Frame_034 = group.nodes.new('NodeFrame')
        node_Frame_034.location_absolute = (-2559.60009765625, 3435.199951171875)
        node_Frame_034.label = 'Format'
        node_Frame_034.shrink = True
        try: node_Frame_034.location_absolute = Vector((-2559.60009765625, 3435.199951171875))
        except: pass
        try: node_Frame_034.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_034.mute = False
        except: pass
        try: node_Frame_034.bl_label = 'Frame'
        except: pass
        try: node_Frame_034.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_034.bl_icon = 'NONE'
        except: pass
        try: node_Frame_034.bl_width_default = 150.0
        except: pass
        try: node_Frame_034.bl_width_min = 100.0
        except: pass
        try: node_Frame_034.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_034.bl_height_default = 100.0
        except: pass
        try: node_Frame_034.bl_height_min = 30.0
        except: pass
        try: node_Frame_034.bl_height_max = 30.0
        except: pass
        try: node_Frame_034.text = None
        except: pass
        try: node_Frame_034.shrink = True
        except: pass
        try: node_Frame_034.label_size = 20
        except: pass
        created_nodes['Frame.034'] = node_Frame_034
        node_Invert_Color_005 = group.nodes.new('ShaderNodeInvert')
        node_Invert_Color_005.location_absolute = (-2329.180908203125, 3333.55810546875)
        try: node_Invert_Color_005.location_absolute = Vector((-2329.180908203125, 3333.55810546875))
        except: pass
        try: node_Invert_Color_005.warning_propagation = 'ALL'
        except: pass
        try: node_Invert_Color_005.mute = False
        except: pass
        try: node_Invert_Color_005.bl_label = 'Invert Color'
        except: pass
        try: node_Invert_Color_005.bl_description = 'Invert a color, producing a negative'
        except: pass
        try: node_Invert_Color_005.bl_icon = 'NONE'
        except: pass
        try: node_Invert_Color_005.bl_width_default = 140.0
        except: pass
        try: node_Invert_Color_005.bl_width_min = 100.0
        except: pass
        try: node_Invert_Color_005.bl_width_max = 700.0
        except: pass
        try: node_Invert_Color_005.bl_height_default = 100.0
        except: pass
        try: node_Invert_Color_005.bl_height_min = 30.0
        except: pass
        try: node_Invert_Color_005.bl_height_max = 30.0
        except: pass
        created_nodes['Invert Color.005'] = node_Invert_Color_005
        node_Vector_Math_071 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_071.location_absolute = (-1296.0050048828125, 3433.55810546875)
        try: node_Vector_Math_071.location_absolute = Vector((-1296.0050048828125, 3433.55810546875))
        except: pass
        try: node_Vector_Math_071.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_071.mute = False
        except: pass
        try: node_Vector_Math_071.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_071.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_071.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_071.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_071.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_071.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_071.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_071.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_071.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_071.operation = 'NORMALIZE'
        except: pass
        try: node_Vector_Math_071.inputs[1].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_071.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_071.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.071'] = node_Vector_Math_071
        node_Vector_Math_072 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_072.location_absolute = (-1477.618896484375, 3433.58203125)
        try: node_Vector_Math_072.location_absolute = Vector((-1477.618896484375, 3433.58203125))
        except: pass
        try: node_Vector_Math_072.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_072.mute = False
        except: pass
        try: node_Vector_Math_072.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_072.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_072.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_072.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_072.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_072.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_072.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_072.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_072.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_072.operation = 'MULTIPLY'
        except: pass
        try: node_Vector_Math_072.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_072.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.072'] = node_Vector_Math_072
        node_Frame_035 = group.nodes.new('NodeFrame')
        node_Frame_035.location_absolute = (-1507.5999755859375, 3469.60009765625)
        node_Frame_035.label = 'Strength'
        node_Frame_035.shrink = True
        try: node_Frame_035.location_absolute = Vector((-1507.5999755859375, 3469.60009765625))
        except: pass
        try: node_Frame_035.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_035.mute = False
        except: pass
        try: node_Frame_035.bl_label = 'Frame'
        except: pass
        try: node_Frame_035.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_035.bl_icon = 'NONE'
        except: pass
        try: node_Frame_035.bl_width_default = 150.0
        except: pass
        try: node_Frame_035.bl_width_min = 100.0
        except: pass
        try: node_Frame_035.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_035.bl_height_default = 100.0
        except: pass
        try: node_Frame_035.bl_height_min = 30.0
        except: pass
        try: node_Frame_035.bl_height_max = 30.0
        except: pass
        try: node_Frame_035.text = None
        except: pass
        try: node_Frame_035.shrink = True
        except: pass
        try: node_Frame_035.label_size = 20
        except: pass
        created_nodes['Frame.035'] = node_Frame_035
        node_Separate_XYZ_015 = group.nodes.new('ShaderNodeSeparateXYZ')
        node_Separate_XYZ_015.location_absolute = (-672.318359375, 3417.399169921875)
        try: node_Separate_XYZ_015.location_absolute = Vector((-672.318359375, 3417.399169921875))
        except: pass
        try: node_Separate_XYZ_015.warning_propagation = 'ALL'
        except: pass
        try: node_Separate_XYZ_015.mute = False
        except: pass
        try: node_Separate_XYZ_015.bl_label = 'Separate XYZ'
        except: pass
        try: node_Separate_XYZ_015.bl_description = 'Split a vector into its X, Y, and Z components'
        except: pass
        try: node_Separate_XYZ_015.bl_icon = 'NONE'
        except: pass
        try: node_Separate_XYZ_015.bl_width_default = 140.0
        except: pass
        try: node_Separate_XYZ_015.bl_width_min = 100.0
        except: pass
        try: node_Separate_XYZ_015.bl_width_max = 700.0
        except: pass
        try: node_Separate_XYZ_015.bl_height_default = 100.0
        except: pass
        try: node_Separate_XYZ_015.bl_height_min = 30.0
        except: pass
        try: node_Separate_XYZ_015.bl_height_max = 30.0
        except: pass
        created_nodes['Separate XYZ.015'] = node_Separate_XYZ_015
        node_Math_012 = group.nodes.new('ShaderNodeMath')
        node_Math_012.location_absolute = (-483.4667053222656, 3449.1953125)
        try: node_Math_012.location_absolute = Vector((-483.4667053222656, 3449.1953125))
        except: pass
        try: node_Math_012.warning_propagation = 'ALL'
        except: pass
        try: node_Math_012.mute = False
        except: pass
        try: node_Math_012.bl_label = 'Math'
        except: pass
        try: node_Math_012.bl_description = 'Perform math operations'
        except: pass
        try: node_Math_012.bl_icon = 'NONE'
        except: pass
        try: node_Math_012.bl_width_default = 140.0
        except: pass
        try: node_Math_012.bl_width_min = 100.0
        except: pass
        try: node_Math_012.bl_width_max = 700.0
        except: pass
        try: node_Math_012.bl_height_default = 100.0
        except: pass
        try: node_Math_012.bl_height_min = 30.0
        except: pass
        try: node_Math_012.bl_height_max = 30.0
        except: pass
        try: node_Math_012.operation = 'MULTIPLY'
        except: pass
        try: node_Math_012.use_clamp = False
        except: pass
        try: node_Math_012.inputs[1].default_value = -1.0
        except: pass
        try: node_Math_012.inputs[2].default_value = 0.5
        except: pass
        created_nodes['Math.012'] = node_Math_012
        node_Combine_XYZ_016 = group.nodes.new('ShaderNodeCombineXYZ')
        node_Combine_XYZ_016.location_absolute = (-1303.40966796875, 3280.37109375)
        try: node_Combine_XYZ_016.location_absolute = Vector((-1303.40966796875, 3280.37109375))
        except: pass
        try: node_Combine_XYZ_016.warning_propagation = 'ALL'
        except: pass
        try: node_Combine_XYZ_016.mute = False
        except: pass
        try: node_Combine_XYZ_016.bl_label = 'Combine XYZ'
        except: pass
        try: node_Combine_XYZ_016.bl_description = 'Create a vector from X, Y, and Z components'
        except: pass
        try: node_Combine_XYZ_016.bl_icon = 'NONE'
        except: pass
        try: node_Combine_XYZ_016.bl_width_default = 140.0
        except: pass
        try: node_Combine_XYZ_016.bl_width_min = 100.0
        except: pass
        try: node_Combine_XYZ_016.bl_width_max = 700.0
        except: pass
        try: node_Combine_XYZ_016.bl_height_default = 100.0
        except: pass
        try: node_Combine_XYZ_016.bl_height_min = 30.0
        except: pass
        try: node_Combine_XYZ_016.bl_height_max = 30.0
        except: pass
        try: node_Combine_XYZ_016.inputs[2].default_value = 1.0
        except: pass
        created_nodes['Combine XYZ.016'] = node_Combine_XYZ_016
        node_Vector_Math_073 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_073.location_absolute = (-1944.641357421875, 2210.560546875)
        try: node_Vector_Math_073.location_absolute = Vector((-1944.641357421875, 2210.560546875))
        except: pass
        try: node_Vector_Math_073.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_073.mute = False
        except: pass
        try: node_Vector_Math_073.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_073.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_073.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_073.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_073.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_073.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_073.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_073.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_073.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_073.operation = 'MULTIPLY'
        except: pass
        try: node_Vector_Math_073.inputs[1].default_value = [2.0,2.0,2.0]
        except: pass
        try: node_Vector_Math_073.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_073.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.073'] = node_Vector_Math_073
        node_Vector_Math_074 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_074.location_absolute = (-1766.5367431640625, 2207.89990234375)
        try: node_Vector_Math_074.location_absolute = Vector((-1766.5367431640625, 2207.89990234375))
        except: pass
        try: node_Vector_Math_074.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_074.mute = False
        except: pass
        try: node_Vector_Math_074.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_074.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_074.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_074.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_074.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_074.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_074.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_074.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_074.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_074.operation = 'SUBTRACT'
        except: pass
        try: node_Vector_Math_074.inputs[1].default_value = [1.0,1.0,1.0]
        except: pass
        try: node_Vector_Math_074.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_074.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.074'] = node_Vector_Math_074
        node_Frame_036 = group.nodes.new('NodeFrame')
        node_Frame_036.location_absolute = (-1974.800048828125, 2246.39990234375)
        node_Frame_036.label = 'Unpack'
        node_Frame_036.shrink = True
        try: node_Frame_036.location_absolute = Vector((-1974.800048828125, 2246.39990234375))
        except: pass
        try: node_Frame_036.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_036.mute = False
        except: pass
        try: node_Frame_036.bl_label = 'Frame'
        except: pass
        try: node_Frame_036.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_036.bl_icon = 'NONE'
        except: pass
        try: node_Frame_036.bl_width_default = 150.0
        except: pass
        try: node_Frame_036.bl_width_min = 100.0
        except: pass
        try: node_Frame_036.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_036.bl_height_default = 100.0
        except: pass
        try: node_Frame_036.bl_height_min = 30.0
        except: pass
        try: node_Frame_036.bl_height_max = 30.0
        except: pass
        try: node_Frame_036.text = None
        except: pass
        try: node_Frame_036.shrink = True
        except: pass
        try: node_Frame_036.label_size = 20
        except: pass
        created_nodes['Frame.036'] = node_Frame_036
        node_Texture_Coordinate_028 = group.nodes.new('ShaderNodeTexCoord')
        node_Texture_Coordinate_028.location_absolute = (-1110.1241455078125, 2032.7388916015625)
        try: node_Texture_Coordinate_028.location_absolute = Vector((-1110.1241455078125, 2032.7388916015625))
        except: pass
        try: node_Texture_Coordinate_028.warning_propagation = 'ALL'
        except: pass
        try: node_Texture_Coordinate_028.mute = False
        except: pass
        try: node_Texture_Coordinate_028.bl_label = 'Texture Coordinate'
        except: pass
        try: node_Texture_Coordinate_028.bl_description = 'Retrieve multiple types of texture coordinates.\nTypically used as inputs for texture nodes'
        except: pass
        try: node_Texture_Coordinate_028.bl_icon = 'NONE'
        except: pass
        try: node_Texture_Coordinate_028.bl_width_default = 140.0
        except: pass
        try: node_Texture_Coordinate_028.bl_width_min = 100.0
        except: pass
        try: node_Texture_Coordinate_028.bl_width_max = 700.0
        except: pass
        try: node_Texture_Coordinate_028.bl_height_default = 100.0
        except: pass
        try: node_Texture_Coordinate_028.bl_height_min = 30.0
        except: pass
        try: node_Texture_Coordinate_028.bl_height_max = 30.0
        except: pass
        try: node_Texture_Coordinate_028.object = None
        except: pass
        try: node_Texture_Coordinate_028.from_instancer = False
        except: pass
        created_nodes['Texture Coordinate.028'] = node_Texture_Coordinate_028
        node_Vector_Math_075 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_075.location_absolute = (-847.6481323242188, 1897.2193603515625)
        try: node_Vector_Math_075.location_absolute = Vector((-847.6481323242188, 1897.2193603515625))
        except: pass
        try: node_Vector_Math_075.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_075.mute = False
        except: pass
        try: node_Vector_Math_075.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_075.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_075.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_075.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_075.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_075.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_075.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_075.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_075.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_075.operation = 'CROSS_PRODUCT'
        except: pass
        try: node_Vector_Math_075.inputs[1].default_value = [1.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_075.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_075.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.075'] = node_Vector_Math_075
        node_Vector_Math_076 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_076.location_absolute = (-726.8180541992188, 2052.04736328125)
        try: node_Vector_Math_076.location_absolute = Vector((-726.8180541992188, 2052.04736328125))
        except: pass
        try: node_Vector_Math_076.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_076.mute = False
        except: pass
        try: node_Vector_Math_076.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_076.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_076.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_076.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_076.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_076.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_076.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_076.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_076.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_076.operation = 'CROSS_PRODUCT'
        except: pass
        try: node_Vector_Math_076.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_076.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.076'] = node_Vector_Math_076
        node_Vector_Math_077 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_077.location_absolute = (-272.8072204589844, 2221.832763671875)
        try: node_Vector_Math_077.location_absolute = Vector((-272.8072204589844, 2221.832763671875))
        except: pass
        try: node_Vector_Math_077.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_077.mute = False
        except: pass
        try: node_Vector_Math_077.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_077.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_077.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_077.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_077.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_077.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_077.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_077.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_077.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_077.operation = 'MULTIPLY'
        except: pass
        try: node_Vector_Math_077.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_077.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.077'] = node_Vector_Math_077
        node_Vector_Math_078 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_078.location_absolute = (-270.9463806152344, 2062.041748046875)
        try: node_Vector_Math_078.location_absolute = Vector((-270.9463806152344, 2062.041748046875))
        except: pass
        try: node_Vector_Math_078.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_078.mute = False
        except: pass
        try: node_Vector_Math_078.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_078.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_078.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_078.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_078.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_078.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_078.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_078.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_078.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_078.operation = 'MULTIPLY'
        except: pass
        try: node_Vector_Math_078.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_078.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.078'] = node_Vector_Math_078
        node_Vector_Math_079 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_079.location_absolute = (-270.9462890625, 1900.8001708984375)
        try: node_Vector_Math_079.location_absolute = Vector((-270.9462890625, 1900.8001708984375))
        except: pass
        try: node_Vector_Math_079.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_079.mute = False
        except: pass
        try: node_Vector_Math_079.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_079.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_079.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_079.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_079.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_079.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_079.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_079.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_079.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_079.operation = 'MULTIPLY'
        except: pass
        try: node_Vector_Math_079.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_079.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.079'] = node_Vector_Math_079
        node_Vector_Math_080 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_080.location_absolute = (-89.67402648925781, 2165.292724609375)
        try: node_Vector_Math_080.location_absolute = Vector((-89.67402648925781, 2165.292724609375))
        except: pass
        try: node_Vector_Math_080.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_080.mute = False
        except: pass
        try: node_Vector_Math_080.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_080.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_080.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_080.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_080.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_080.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_080.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_080.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_080.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_080.operation = 'ADD'
        except: pass
        try: node_Vector_Math_080.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_080.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.080'] = node_Vector_Math_080
        node_Vector_Math_081 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_081.location_absolute = (135.0075225830078, 1995.2099609375)
        try: node_Vector_Math_081.location_absolute = Vector((135.0075225830078, 1995.2099609375))
        except: pass
        try: node_Vector_Math_081.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_081.mute = False
        except: pass
        try: node_Vector_Math_081.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_081.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_081.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_081.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_081.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_081.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_081.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_081.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_081.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_081.operation = 'ADD'
        except: pass
        try: node_Vector_Math_081.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_081.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.081'] = node_Vector_Math_081
        node_Vector_Math_082 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_082.location_absolute = (296.68145751953125, 1989.3525390625)
        try: node_Vector_Math_082.location_absolute = Vector((296.68145751953125, 1989.3525390625))
        except: pass
        try: node_Vector_Math_082.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_082.mute = False
        except: pass
        try: node_Vector_Math_082.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_082.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_082.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_082.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_082.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_082.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_082.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_082.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_082.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_082.operation = 'NORMALIZE'
        except: pass
        try: node_Vector_Math_082.inputs[1].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_082.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_082.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.082'] = node_Vector_Math_082
        node_Frame_037 = group.nodes.new('NodeFrame')
        node_Frame_037.location_absolute = (-1140.4000244140625, 2082.0)
        node_Frame_037.shrink = True
        try: node_Frame_037.location_absolute = Vector((-1140.4000244140625, 2082.0))
        except: pass
        try: node_Frame_037.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_037.mute = False
        except: pass
        try: node_Frame_037.bl_label = 'Frame'
        except: pass
        try: node_Frame_037.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_037.bl_icon = 'NONE'
        except: pass
        try: node_Frame_037.bl_width_default = 150.0
        except: pass
        try: node_Frame_037.bl_width_min = 100.0
        except: pass
        try: node_Frame_037.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_037.bl_height_default = 100.0
        except: pass
        try: node_Frame_037.bl_height_min = 30.0
        except: pass
        try: node_Frame_037.bl_height_max = 30.0
        except: pass
        try: node_Frame_037.text = None
        except: pass
        try: node_Frame_037.shrink = True
        except: pass
        try: node_Frame_037.label_size = 20
        except: pass
        created_nodes['Frame.037'] = node_Frame_037
        node_Separate_Color_006 = group.nodes.new('ShaderNodeSeparateColor')
        node_Separate_Color_006.location_absolute = (-2552.864501953125, 2201.37109375)
        try: node_Separate_Color_006.location_absolute = Vector((-2552.864501953125, 2201.37109375))
        except: pass
        try: node_Separate_Color_006.warning_propagation = 'ALL'
        except: pass
        try: node_Separate_Color_006.mute = False
        except: pass
        try: node_Separate_Color_006.bl_label = 'Separate Color'
        except: pass
        try: node_Separate_Color_006.bl_description = 'Split a color into its individual components using multiple models'
        except: pass
        try: node_Separate_Color_006.bl_icon = 'NONE'
        except: pass
        try: node_Separate_Color_006.bl_width_default = 140.0
        except: pass
        try: node_Separate_Color_006.bl_width_min = 100.0
        except: pass
        try: node_Separate_Color_006.bl_width_max = 700.0
        except: pass
        try: node_Separate_Color_006.bl_height_default = 100.0
        except: pass
        try: node_Separate_Color_006.bl_height_min = 30.0
        except: pass
        try: node_Separate_Color_006.bl_height_max = 30.0
        except: pass
        try: node_Separate_Color_006.mode = 'RGB'
        except: pass
        created_nodes['Separate Color.006'] = node_Separate_Color_006
        node_Combine_Color_006 = group.nodes.new('ShaderNodeCombineColor')
        node_Combine_Color_006.location_absolute = (-2153.721923828125, 2211.111328125)
        try: node_Combine_Color_006.location_absolute = Vector((-2153.721923828125, 2211.111328125))
        except: pass
        try: node_Combine_Color_006.warning_propagation = 'ALL'
        except: pass
        try: node_Combine_Color_006.mute = False
        except: pass
        try: node_Combine_Color_006.bl_label = 'Combine Color'
        except: pass
        try: node_Combine_Color_006.bl_description = 'Create a color from individual components using multiple models'
        except: pass
        try: node_Combine_Color_006.bl_icon = 'NONE'
        except: pass
        try: node_Combine_Color_006.bl_width_default = 140.0
        except: pass
        try: node_Combine_Color_006.bl_width_min = 100.0
        except: pass
        try: node_Combine_Color_006.bl_width_max = 700.0
        except: pass
        try: node_Combine_Color_006.bl_height_default = 100.0
        except: pass
        try: node_Combine_Color_006.bl_height_min = 30.0
        except: pass
        try: node_Combine_Color_006.bl_height_max = 30.0
        except: pass
        try: node_Combine_Color_006.mode = 'RGB'
        except: pass
        created_nodes['Combine Color.006'] = node_Combine_Color_006
        node_Frame_038 = group.nodes.new('NodeFrame')
        node_Frame_038.location_absolute = (-2582.800048828125, 2247.199951171875)
        node_Frame_038.label = 'Format'
        node_Frame_038.shrink = True
        try: node_Frame_038.location_absolute = Vector((-2582.800048828125, 2247.199951171875))
        except: pass
        try: node_Frame_038.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_038.mute = False
        except: pass
        try: node_Frame_038.bl_label = 'Frame'
        except: pass
        try: node_Frame_038.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_038.bl_icon = 'NONE'
        except: pass
        try: node_Frame_038.bl_width_default = 150.0
        except: pass
        try: node_Frame_038.bl_width_min = 100.0
        except: pass
        try: node_Frame_038.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_038.bl_height_default = 100.0
        except: pass
        try: node_Frame_038.bl_height_min = 30.0
        except: pass
        try: node_Frame_038.bl_height_max = 30.0
        except: pass
        try: node_Frame_038.text = None
        except: pass
        try: node_Frame_038.shrink = True
        except: pass
        try: node_Frame_038.label_size = 20
        except: pass
        created_nodes['Frame.038'] = node_Frame_038
        node_Invert_Color_006 = group.nodes.new('ShaderNodeInvert')
        node_Invert_Color_006.location_absolute = (-2352.737060546875, 2145.84375)
        try: node_Invert_Color_006.location_absolute = Vector((-2352.737060546875, 2145.84375))
        except: pass
        try: node_Invert_Color_006.warning_propagation = 'ALL'
        except: pass
        try: node_Invert_Color_006.mute = False
        except: pass
        try: node_Invert_Color_006.bl_label = 'Invert Color'
        except: pass
        try: node_Invert_Color_006.bl_description = 'Invert a color, producing a negative'
        except: pass
        try: node_Invert_Color_006.bl_icon = 'NONE'
        except: pass
        try: node_Invert_Color_006.bl_width_default = 140.0
        except: pass
        try: node_Invert_Color_006.bl_width_min = 100.0
        except: pass
        try: node_Invert_Color_006.bl_width_max = 700.0
        except: pass
        try: node_Invert_Color_006.bl_height_default = 100.0
        except: pass
        try: node_Invert_Color_006.bl_height_min = 30.0
        except: pass
        try: node_Invert_Color_006.bl_height_max = 30.0
        except: pass
        created_nodes['Invert Color.006'] = node_Invert_Color_006
        node_Vector_Math_083 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_083.location_absolute = (-1319.56103515625, 2245.843505859375)
        try: node_Vector_Math_083.location_absolute = Vector((-1319.56103515625, 2245.843505859375))
        except: pass
        try: node_Vector_Math_083.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_083.mute = False
        except: pass
        try: node_Vector_Math_083.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_083.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_083.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_083.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_083.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_083.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_083.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_083.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_083.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_083.operation = 'NORMALIZE'
        except: pass
        try: node_Vector_Math_083.inputs[1].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_083.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_083.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.083'] = node_Vector_Math_083
        node_Vector_Math_084 = group.nodes.new('ShaderNodeVectorMath')
        node_Vector_Math_084.location_absolute = (-1501.1749267578125, 2245.86767578125)
        try: node_Vector_Math_084.location_absolute = Vector((-1501.1749267578125, 2245.86767578125))
        except: pass
        try: node_Vector_Math_084.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Math_084.mute = False
        except: pass
        try: node_Vector_Math_084.bl_label = 'Vector Math'
        except: pass
        try: node_Vector_Math_084.bl_description = 'Perform vector math operation'
        except: pass
        try: node_Vector_Math_084.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Math_084.bl_width_default = 140.0
        except: pass
        try: node_Vector_Math_084.bl_width_min = 100.0
        except: pass
        try: node_Vector_Math_084.bl_width_max = 700.0
        except: pass
        try: node_Vector_Math_084.bl_height_default = 100.0
        except: pass
        try: node_Vector_Math_084.bl_height_min = 30.0
        except: pass
        try: node_Vector_Math_084.bl_height_max = 30.0
        except: pass
        try: node_Vector_Math_084.operation = 'MULTIPLY'
        except: pass
        try: node_Vector_Math_084.inputs[2].default_value = [0.0,0.0,0.0]
        except: pass
        try: node_Vector_Math_084.inputs[3].default_value = 1.0
        except: pass
        created_nodes['Vector Math.084'] = node_Vector_Math_084
        node_Frame_039 = group.nodes.new('NodeFrame')
        node_Frame_039.location_absolute = (-1530.800048828125, 2281.60009765625)
        node_Frame_039.label = 'Strength'
        node_Frame_039.shrink = True
        try: node_Frame_039.location_absolute = Vector((-1530.800048828125, 2281.60009765625))
        except: pass
        try: node_Frame_039.warning_propagation = 'ALL'
        except: pass
        try: node_Frame_039.mute = False
        except: pass
        try: node_Frame_039.bl_label = 'Frame'
        except: pass
        try: node_Frame_039.bl_description = 'Collect related nodes together in a common area. Useful for organization when the re-usability of a node group is not required'
        except: pass
        try: node_Frame_039.bl_icon = 'NONE'
        except: pass
        try: node_Frame_039.bl_width_default = 150.0
        except: pass
        try: node_Frame_039.bl_width_min = 100.0
        except: pass
        try: node_Frame_039.bl_width_max = 3.4028234663852886e+38
        except: pass
        try: node_Frame_039.bl_height_default = 100.0
        except: pass
        try: node_Frame_039.bl_height_min = 30.0
        except: pass
        try: node_Frame_039.bl_height_max = 30.0
        except: pass
        try: node_Frame_039.text = None
        except: pass
        try: node_Frame_039.shrink = True
        except: pass
        try: node_Frame_039.label_size = 20
        except: pass
        created_nodes['Frame.039'] = node_Frame_039
        node_Separate_XYZ_016 = group.nodes.new('ShaderNodeSeparateXYZ')
        node_Separate_XYZ_016.location_absolute = (-695.8746948242188, 2229.68505859375)
        try: node_Separate_XYZ_016.location_absolute = Vector((-695.8746948242188, 2229.68505859375))
        except: pass
        try: node_Separate_XYZ_016.warning_propagation = 'ALL'
        except: pass
        try: node_Separate_XYZ_016.mute = False
        except: pass
        try: node_Separate_XYZ_016.bl_label = 'Separate XYZ'
        except: pass
        try: node_Separate_XYZ_016.bl_description = 'Split a vector into its X, Y, and Z components'
        except: pass
        try: node_Separate_XYZ_016.bl_icon = 'NONE'
        except: pass
        try: node_Separate_XYZ_016.bl_width_default = 140.0
        except: pass
        try: node_Separate_XYZ_016.bl_width_min = 100.0
        except: pass
        try: node_Separate_XYZ_016.bl_width_max = 700.0
        except: pass
        try: node_Separate_XYZ_016.bl_height_default = 100.0
        except: pass
        try: node_Separate_XYZ_016.bl_height_min = 30.0
        except: pass
        try: node_Separate_XYZ_016.bl_height_max = 30.0
        except: pass
        created_nodes['Separate XYZ.016'] = node_Separate_XYZ_016
        node_Math_013 = group.nodes.new('ShaderNodeMath')
        node_Math_013.location_absolute = (-507.02294921875, 2261.48095703125)
        try: node_Math_013.location_absolute = Vector((-507.02294921875, 2261.48095703125))
        except: pass
        try: node_Math_013.warning_propagation = 'ALL'
        except: pass
        try: node_Math_013.mute = False
        except: pass
        try: node_Math_013.bl_label = 'Math'
        except: pass
        try: node_Math_013.bl_description = 'Perform math operations'
        except: pass
        try: node_Math_013.bl_icon = 'NONE'
        except: pass
        try: node_Math_013.bl_width_default = 140.0
        except: pass
        try: node_Math_013.bl_width_min = 100.0
        except: pass
        try: node_Math_013.bl_width_max = 700.0
        except: pass
        try: node_Math_013.bl_height_default = 100.0
        except: pass
        try: node_Math_013.bl_height_min = 30.0
        except: pass
        try: node_Math_013.bl_height_max = 30.0
        except: pass
        try: node_Math_013.operation = 'MULTIPLY'
        except: pass
        try: node_Math_013.use_clamp = False
        except: pass
        try: node_Math_013.inputs[1].default_value = -1.0
        except: pass
        try: node_Math_013.inputs[2].default_value = 0.5
        except: pass
        created_nodes['Math.013'] = node_Math_013
        node_Combine_XYZ_017 = group.nodes.new('ShaderNodeCombineXYZ')
        node_Combine_XYZ_017.location_absolute = (-1326.9659423828125, 2092.65673828125)
        try: node_Combine_XYZ_017.location_absolute = Vector((-1326.9659423828125, 2092.65673828125))
        except: pass
        try: node_Combine_XYZ_017.warning_propagation = 'ALL'
        except: pass
        try: node_Combine_XYZ_017.mute = False
        except: pass
        try: node_Combine_XYZ_017.bl_label = 'Combine XYZ'
        except: pass
        try: node_Combine_XYZ_017.bl_description = 'Create a vector from X, Y, and Z components'
        except: pass
        try: node_Combine_XYZ_017.bl_icon = 'NONE'
        except: pass
        try: node_Combine_XYZ_017.bl_width_default = 140.0
        except: pass
        try: node_Combine_XYZ_017.bl_width_min = 100.0
        except: pass
        try: node_Combine_XYZ_017.bl_width_max = 700.0
        except: pass
        try: node_Combine_XYZ_017.bl_height_default = 100.0
        except: pass
        try: node_Combine_XYZ_017.bl_height_min = 30.0
        except: pass
        try: node_Combine_XYZ_017.bl_height_max = 30.0
        except: pass
        try: node_Combine_XYZ_017.inputs[2].default_value = 1.0
        except: pass
        created_nodes['Combine XYZ.017'] = node_Combine_XYZ_017
        node_Mapping = group.nodes.new('ShaderNodeMapping')
        node_Mapping.location_absolute = (-3065.286865234375, 2813.09619140625)
        try: node_Mapping.location_absolute = Vector((-3065.286865234375, 2813.09619140625))
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
        node_Mapping_004.location_absolute = (-3074.95263671875, 3399.552734375)
        try: node_Mapping_004.location_absolute = Vector((-3074.95263671875, 3399.552734375))
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
        node_Mapping_005.location_absolute = (-3077.07666015625, 2203.684326171875)
        try: node_Mapping_005.location_absolute = Vector((-3077.07666015625, 2203.684326171875))
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
        node_Vector_Transform_004 = group.nodes.new('ShaderNodeVectorTransform')
        node_Vector_Transform_004.location_absolute = (1463.296630859375, 1741.5445556640625)
        try: node_Vector_Transform_004.location_absolute = Vector((1463.296630859375, 1741.5445556640625))
        except: pass
        try: node_Vector_Transform_004.warning_propagation = 'ALL'
        except: pass
        try: node_Vector_Transform_004.mute = False
        except: pass
        try: node_Vector_Transform_004.bl_label = 'Vector Transform'
        except: pass
        try: node_Vector_Transform_004.bl_description = 'Convert a vector, point, or normal between world, camera, and object coordinate space'
        except: pass
        try: node_Vector_Transform_004.bl_icon = 'NONE'
        except: pass
        try: node_Vector_Transform_004.bl_width_default = 140.0
        except: pass
        try: node_Vector_Transform_004.bl_width_min = 100.0
        except: pass
        try: node_Vector_Transform_004.bl_width_max = 700.0
        except: pass
        try: node_Vector_Transform_004.bl_height_default = 100.0
        except: pass
        try: node_Vector_Transform_004.bl_height_min = 30.0
        except: pass
        try: node_Vector_Transform_004.bl_height_max = 30.0
        except: pass
        try: node_Vector_Transform_004.vector_type = 'NORMAL'
        except: pass
        try: node_Vector_Transform_004.convert_from = 'OBJECT'
        except: pass
        try: node_Vector_Transform_004.convert_to = 'WORLD'
        except: pass
        created_nodes['Vector Transform.004'] = node_Vector_Transform_004
        node_Math_003 = group.nodes.new('ShaderNodeMath')
        node_Math_003.location_absolute = (-5726.10400390625, 1537.556884765625)
        try: node_Math_003.location_absolute = Vector((-5726.10400390625, 1537.556884765625))
        except: pass
        try: node_Math_003.warning_propagation = 'ALL'
        except: pass
        try: node_Math_003.mute = False
        except: pass
        try: node_Math_003.bl_label = 'Math'
        except: pass
        try: node_Math_003.bl_description = 'Perform math operations'
        except: pass
        try: node_Math_003.bl_icon = 'NONE'
        except: pass
        try: node_Math_003.bl_width_default = 140.0
        except: pass
        try: node_Math_003.bl_width_min = 100.0
        except: pass
        try: node_Math_003.bl_width_max = 700.0
        except: pass
        try: node_Math_003.bl_height_default = 100.0
        except: pass
        try: node_Math_003.bl_height_min = 30.0
        except: pass
        try: node_Math_003.bl_height_max = 30.0
        except: pass
        try: node_Math_003.operation = 'DIVIDE'
        except: pass
        try: node_Math_003.use_clamp = False
        except: pass
        try: node_Math_003.inputs[1].default_value = 100.0
        except: pass
        try: node_Math_003.inputs[2].default_value = 0.5
        except: pass
        created_nodes['Math.003'] = node_Math_003

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
        if 'Vector Math.013' in created_nodes and 'Frame.016' in created_nodes:
            created_nodes['Vector Math.013'].parent = created_nodes['Frame.016']
        if 'Vector Math.014' in created_nodes and 'Frame.016' in created_nodes:
            created_nodes['Vector Math.014'].parent = created_nodes['Frame.016']
        if 'Frame.016' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Frame.016'].parent = created_nodes['Frame.004']
        if 'Texture Coordinate.023' in created_nodes and 'Frame.017' in created_nodes:
            created_nodes['Texture Coordinate.023'].parent = created_nodes['Frame.017']
        if 'Vector Math.028' in created_nodes and 'Frame.017' in created_nodes:
            created_nodes['Vector Math.028'].parent = created_nodes['Frame.017']
        if 'Vector Math.042' in created_nodes and 'Frame.017' in created_nodes:
            created_nodes['Vector Math.042'].parent = created_nodes['Frame.017']
        if 'Vector Math.015' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Vector Math.015'].parent = created_nodes['Frame.004']
        if 'Vector Math.016' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Vector Math.016'].parent = created_nodes['Frame.004']
        if 'Vector Math.029' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Vector Math.029'].parent = created_nodes['Frame.004']
        if 'Vector Math.030' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Vector Math.030'].parent = created_nodes['Frame.004']
        if 'Vector Math.031' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Vector Math.031'].parent = created_nodes['Frame.004']
        if 'Vector Math.032' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Vector Math.032'].parent = created_nodes['Frame.004']
        if 'Frame.017' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Frame.017'].parent = created_nodes['Frame.004']
        if 'Separate Color.001' in created_nodes and 'Frame.018' in created_nodes:
            created_nodes['Separate Color.001'].parent = created_nodes['Frame.018']
        if 'Combine Color.001' in created_nodes and 'Frame.018' in created_nodes:
            created_nodes['Combine Color.001'].parent = created_nodes['Frame.018']
        if 'Frame.018' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Frame.018'].parent = created_nodes['Frame.004']
        if 'Invert Color.001' in created_nodes and 'Frame.018' in created_nodes:
            created_nodes['Invert Color.001'].parent = created_nodes['Frame.018']
        if 'Vector Math.025' in created_nodes and 'Frame.024' in created_nodes:
            created_nodes['Vector Math.025'].parent = created_nodes['Frame.024']
        if 'Vector Math.026' in created_nodes and 'Frame.024' in created_nodes:
            created_nodes['Vector Math.026'].parent = created_nodes['Frame.024']
        if 'Frame.024' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Frame.024'].parent = created_nodes['Frame.004']
        if 'Separate XYZ.011' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Separate XYZ.011'].parent = created_nodes['Frame.004']
        if 'Math.005' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Math.005'].parent = created_nodes['Frame.004']
        if 'Combine XYZ.012' in created_nodes and 'Frame.024' in created_nodes:
            created_nodes['Combine XYZ.012'].parent = created_nodes['Frame.024']
        if 'Vector Math.021' in created_nodes and 'Frame.022' in created_nodes:
            created_nodes['Vector Math.021'].parent = created_nodes['Frame.022']
        if 'Vector Math.022' in created_nodes and 'Frame.022' in created_nodes:
            created_nodes['Vector Math.022'].parent = created_nodes['Frame.022']
        if 'Frame.022' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Frame.022'].parent = created_nodes['Frame.004']
        if 'Texture Coordinate.024' in created_nodes and 'Frame.023' in created_nodes:
            created_nodes['Texture Coordinate.024'].parent = created_nodes['Frame.023']
        if 'Vector Math.033' in created_nodes and 'Frame.023' in created_nodes:
            created_nodes['Vector Math.033'].parent = created_nodes['Frame.023']
        if 'Vector Math.043' in created_nodes and 'Frame.023' in created_nodes:
            created_nodes['Vector Math.043'].parent = created_nodes['Frame.023']
        if 'Vector Math.023' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Vector Math.023'].parent = created_nodes['Frame.004']
        if 'Vector Math.024' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Vector Math.024'].parent = created_nodes['Frame.004']
        if 'Vector Math.034' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Vector Math.034'].parent = created_nodes['Frame.004']
        if 'Vector Math.044' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Vector Math.044'].parent = created_nodes['Frame.004']
        if 'Vector Math.045' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Vector Math.045'].parent = created_nodes['Frame.004']
        if 'Vector Math.046' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Vector Math.046'].parent = created_nodes['Frame.004']
        if 'Frame.023' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Frame.023'].parent = created_nodes['Frame.004']
        if 'Separate Color.003' in created_nodes and 'Frame.025' in created_nodes:
            created_nodes['Separate Color.003'].parent = created_nodes['Frame.025']
        if 'Combine Color.002' in created_nodes and 'Frame.025' in created_nodes:
            created_nodes['Combine Color.002'].parent = created_nodes['Frame.025']
        if 'Frame.025' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Frame.025'].parent = created_nodes['Frame.004']
        if 'Invert Color.003' in created_nodes and 'Frame.025' in created_nodes:
            created_nodes['Invert Color.003'].parent = created_nodes['Frame.025']
        if 'Vector Math.027' in created_nodes and 'Frame.026' in created_nodes:
            created_nodes['Vector Math.027'].parent = created_nodes['Frame.026']
        if 'Vector Math.047' in created_nodes and 'Frame.026' in created_nodes:
            created_nodes['Vector Math.047'].parent = created_nodes['Frame.026']
        if 'Frame.026' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Frame.026'].parent = created_nodes['Frame.004']
        if 'Separate XYZ.012' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Separate XYZ.012'].parent = created_nodes['Frame.004']
        if 'Math.011' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Math.011'].parent = created_nodes['Frame.004']
        if 'Combine XYZ.013' in created_nodes and 'Frame.026' in created_nodes:
            created_nodes['Combine XYZ.013'].parent = created_nodes['Frame.026']
        if 'Vector Math.017' in created_nodes and 'Frame.019' in created_nodes:
            created_nodes['Vector Math.017'].parent = created_nodes['Frame.019']
        if 'Vector Math.018' in created_nodes and 'Frame.019' in created_nodes:
            created_nodes['Vector Math.018'].parent = created_nodes['Frame.019']
        if 'Frame.019' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Frame.019'].parent = created_nodes['Frame.004']
        if 'Texture Coordinate.025' in created_nodes and 'Frame.020' in created_nodes:
            created_nodes['Texture Coordinate.025'].parent = created_nodes['Frame.020']
        if 'Vector Math.035' in created_nodes and 'Frame.020' in created_nodes:
            created_nodes['Vector Math.035'].parent = created_nodes['Frame.020']
        if 'Vector Math.048' in created_nodes and 'Frame.020' in created_nodes:
            created_nodes['Vector Math.048'].parent = created_nodes['Frame.020']
        if 'Vector Math.019' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Vector Math.019'].parent = created_nodes['Frame.004']
        if 'Vector Math.020' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Vector Math.020'].parent = created_nodes['Frame.004']
        if 'Vector Math.036' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Vector Math.036'].parent = created_nodes['Frame.004']
        if 'Vector Math.037' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Vector Math.037'].parent = created_nodes['Frame.004']
        if 'Vector Math.038' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Vector Math.038'].parent = created_nodes['Frame.004']
        if 'Vector Math.039' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Vector Math.039'].parent = created_nodes['Frame.004']
        if 'Frame.020' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Frame.020'].parent = created_nodes['Frame.004']
        if 'Separate Color.002' in created_nodes and 'Frame.021' in created_nodes:
            created_nodes['Separate Color.002'].parent = created_nodes['Frame.021']
        if 'Combine Color.003' in created_nodes and 'Frame.021' in created_nodes:
            created_nodes['Combine Color.003'].parent = created_nodes['Frame.021']
        if 'Frame.021' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Frame.021'].parent = created_nodes['Frame.004']
        if 'Invert Color.002' in created_nodes and 'Frame.021' in created_nodes:
            created_nodes['Invert Color.002'].parent = created_nodes['Frame.021']
        if 'Vector Math.040' in created_nodes and 'Frame.027' in created_nodes:
            created_nodes['Vector Math.040'].parent = created_nodes['Frame.027']
        if 'Vector Math.041' in created_nodes and 'Frame.027' in created_nodes:
            created_nodes['Vector Math.041'].parent = created_nodes['Frame.027']
        if 'Frame.027' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Frame.027'].parent = created_nodes['Frame.004']
        if 'Separate XYZ.013' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Separate XYZ.013'].parent = created_nodes['Frame.004']
        if 'Math.009' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Math.009'].parent = created_nodes['Frame.004']
        if 'Combine XYZ.014' in created_nodes and 'Frame.027' in created_nodes:
            created_nodes['Combine XYZ.014'].parent = created_nodes['Frame.027']
        if 'Vector Rotate.003' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Vector Rotate.003'].parent = created_nodes['Frame.004']
        if 'Vector Rotate.004' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Vector Rotate.004'].parent = created_nodes['Frame.004']
        if 'Vector Rotate.005' in created_nodes and 'Frame.004' in created_nodes:
            created_nodes['Vector Rotate.005'].parent = created_nodes['Frame.004']
        if 'Vector Math.049' in created_nodes and 'Frame.028' in created_nodes:
            created_nodes['Vector Math.049'].parent = created_nodes['Frame.028']
        if 'Vector Math.050' in created_nodes and 'Frame.028' in created_nodes:
            created_nodes['Vector Math.050'].parent = created_nodes['Frame.028']
        if 'Frame.028' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Frame.028'].parent = created_nodes['Frame.012']
        if 'Texture Coordinate.026' in created_nodes and 'Frame.029' in created_nodes:
            created_nodes['Texture Coordinate.026'].parent = created_nodes['Frame.029']
        if 'Vector Math.051' in created_nodes and 'Frame.029' in created_nodes:
            created_nodes['Vector Math.051'].parent = created_nodes['Frame.029']
        if 'Vector Math.052' in created_nodes and 'Frame.029' in created_nodes:
            created_nodes['Vector Math.052'].parent = created_nodes['Frame.029']
        if 'Vector Math.053' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Vector Math.053'].parent = created_nodes['Frame.012']
        if 'Vector Math.054' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Vector Math.054'].parent = created_nodes['Frame.012']
        if 'Vector Math.055' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Vector Math.055'].parent = created_nodes['Frame.012']
        if 'Vector Math.056' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Vector Math.056'].parent = created_nodes['Frame.012']
        if 'Vector Math.057' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Vector Math.057'].parent = created_nodes['Frame.012']
        if 'Vector Math.058' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Vector Math.058'].parent = created_nodes['Frame.012']
        if 'Frame.029' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Frame.029'].parent = created_nodes['Frame.012']
        if 'Separate Color.004' in created_nodes and 'Frame.030' in created_nodes:
            created_nodes['Separate Color.004'].parent = created_nodes['Frame.030']
        if 'Combine Color.004' in created_nodes and 'Frame.030' in created_nodes:
            created_nodes['Combine Color.004'].parent = created_nodes['Frame.030']
        if 'Frame.030' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Frame.030'].parent = created_nodes['Frame.012']
        if 'Invert Color.004' in created_nodes and 'Frame.030' in created_nodes:
            created_nodes['Invert Color.004'].parent = created_nodes['Frame.030']
        if 'Vector Math.059' in created_nodes and 'Frame.031' in created_nodes:
            created_nodes['Vector Math.059'].parent = created_nodes['Frame.031']
        if 'Vector Math.060' in created_nodes and 'Frame.031' in created_nodes:
            created_nodes['Vector Math.060'].parent = created_nodes['Frame.031']
        if 'Frame.031' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Frame.031'].parent = created_nodes['Frame.012']
        if 'Separate XYZ.014' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Separate XYZ.014'].parent = created_nodes['Frame.012']
        if 'Math.010' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Math.010'].parent = created_nodes['Frame.012']
        if 'Combine XYZ.015' in created_nodes and 'Frame.031' in created_nodes:
            created_nodes['Combine XYZ.015'].parent = created_nodes['Frame.031']
        if 'Vector Math.061' in created_nodes and 'Frame.032' in created_nodes:
            created_nodes['Vector Math.061'].parent = created_nodes['Frame.032']
        if 'Vector Math.062' in created_nodes and 'Frame.032' in created_nodes:
            created_nodes['Vector Math.062'].parent = created_nodes['Frame.032']
        if 'Frame.032' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Frame.032'].parent = created_nodes['Frame.012']
        if 'Texture Coordinate.027' in created_nodes and 'Frame.033' in created_nodes:
            created_nodes['Texture Coordinate.027'].parent = created_nodes['Frame.033']
        if 'Vector Math.063' in created_nodes and 'Frame.033' in created_nodes:
            created_nodes['Vector Math.063'].parent = created_nodes['Frame.033']
        if 'Vector Math.064' in created_nodes and 'Frame.033' in created_nodes:
            created_nodes['Vector Math.064'].parent = created_nodes['Frame.033']
        if 'Vector Math.065' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Vector Math.065'].parent = created_nodes['Frame.012']
        if 'Vector Math.066' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Vector Math.066'].parent = created_nodes['Frame.012']
        if 'Vector Math.067' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Vector Math.067'].parent = created_nodes['Frame.012']
        if 'Vector Math.068' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Vector Math.068'].parent = created_nodes['Frame.012']
        if 'Vector Math.069' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Vector Math.069'].parent = created_nodes['Frame.012']
        if 'Vector Math.070' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Vector Math.070'].parent = created_nodes['Frame.012']
        if 'Frame.033' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Frame.033'].parent = created_nodes['Frame.012']
        if 'Separate Color.005' in created_nodes and 'Frame.034' in created_nodes:
            created_nodes['Separate Color.005'].parent = created_nodes['Frame.034']
        if 'Combine Color.005' in created_nodes and 'Frame.034' in created_nodes:
            created_nodes['Combine Color.005'].parent = created_nodes['Frame.034']
        if 'Frame.034' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Frame.034'].parent = created_nodes['Frame.012']
        if 'Invert Color.005' in created_nodes and 'Frame.034' in created_nodes:
            created_nodes['Invert Color.005'].parent = created_nodes['Frame.034']
        if 'Vector Math.071' in created_nodes and 'Frame.035' in created_nodes:
            created_nodes['Vector Math.071'].parent = created_nodes['Frame.035']
        if 'Vector Math.072' in created_nodes and 'Frame.035' in created_nodes:
            created_nodes['Vector Math.072'].parent = created_nodes['Frame.035']
        if 'Frame.035' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Frame.035'].parent = created_nodes['Frame.012']
        if 'Separate XYZ.015' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Separate XYZ.015'].parent = created_nodes['Frame.012']
        if 'Math.012' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Math.012'].parent = created_nodes['Frame.012']
        if 'Combine XYZ.016' in created_nodes and 'Frame.035' in created_nodes:
            created_nodes['Combine XYZ.016'].parent = created_nodes['Frame.035']
        if 'Vector Math.073' in created_nodes and 'Frame.036' in created_nodes:
            created_nodes['Vector Math.073'].parent = created_nodes['Frame.036']
        if 'Vector Math.074' in created_nodes and 'Frame.036' in created_nodes:
            created_nodes['Vector Math.074'].parent = created_nodes['Frame.036']
        if 'Frame.036' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Frame.036'].parent = created_nodes['Frame.012']
        if 'Texture Coordinate.028' in created_nodes and 'Frame.037' in created_nodes:
            created_nodes['Texture Coordinate.028'].parent = created_nodes['Frame.037']
        if 'Vector Math.075' in created_nodes and 'Frame.037' in created_nodes:
            created_nodes['Vector Math.075'].parent = created_nodes['Frame.037']
        if 'Vector Math.076' in created_nodes and 'Frame.037' in created_nodes:
            created_nodes['Vector Math.076'].parent = created_nodes['Frame.037']
        if 'Vector Math.077' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Vector Math.077'].parent = created_nodes['Frame.012']
        if 'Vector Math.078' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Vector Math.078'].parent = created_nodes['Frame.012']
        if 'Vector Math.079' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Vector Math.079'].parent = created_nodes['Frame.012']
        if 'Vector Math.080' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Vector Math.080'].parent = created_nodes['Frame.012']
        if 'Vector Math.081' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Vector Math.081'].parent = created_nodes['Frame.012']
        if 'Vector Math.082' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Vector Math.082'].parent = created_nodes['Frame.012']
        if 'Frame.037' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Frame.037'].parent = created_nodes['Frame.012']
        if 'Separate Color.006' in created_nodes and 'Frame.038' in created_nodes:
            created_nodes['Separate Color.006'].parent = created_nodes['Frame.038']
        if 'Combine Color.006' in created_nodes and 'Frame.038' in created_nodes:
            created_nodes['Combine Color.006'].parent = created_nodes['Frame.038']
        if 'Frame.038' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Frame.038'].parent = created_nodes['Frame.012']
        if 'Invert Color.006' in created_nodes and 'Frame.038' in created_nodes:
            created_nodes['Invert Color.006'].parent = created_nodes['Frame.038']
        if 'Vector Math.083' in created_nodes and 'Frame.039' in created_nodes:
            created_nodes['Vector Math.083'].parent = created_nodes['Frame.039']
        if 'Vector Math.084' in created_nodes and 'Frame.039' in created_nodes:
            created_nodes['Vector Math.084'].parent = created_nodes['Frame.039']
        if 'Frame.039' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Frame.039'].parent = created_nodes['Frame.012']
        if 'Separate XYZ.016' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Separate XYZ.016'].parent = created_nodes['Frame.012']
        if 'Math.013' in created_nodes and 'Frame.012' in created_nodes:
            created_nodes['Math.013'].parent = created_nodes['Frame.012']
        if 'Combine XYZ.017' in created_nodes and 'Frame.039' in created_nodes:
            created_nodes['Combine XYZ.017'].parent = created_nodes['Frame.039']
        if 'Mapping' in created_nodes and 'Frame.010' in created_nodes:
            created_nodes['Mapping'].parent = created_nodes['Frame.010']
        if 'Mapping.004' in created_nodes and 'Frame.011' in created_nodes:
            created_nodes['Mapping.004'].parent = created_nodes['Frame.011']
        if 'Mapping.005' in created_nodes and 'Frame.009' in created_nodes:
            created_nodes['Mapping.005'].parent = created_nodes['Frame.009']

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
        try: group.links.new(created_nodes['Voronoi Texture.001'].outputs[0], created_nodes['Map Range'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Math.001'].outputs[0], created_nodes['Math.002'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Group Input'].outputs[3], created_nodes['Math.004'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Voronoi Texture.003'].outputs[2], created_nodes['Vector Math.006'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Noise Texture.002'].outputs[0], created_nodes['Math.006'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.006'].outputs[0], created_nodes['Vector Rotate'].inputs[0])
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
        try: group.links.new(created_nodes['Math.002'].outputs[0], created_nodes['Map Range.002'].inputs[2])
        except: pass
        try: group.links.new(created_nodes['Math.002'].outputs[0], created_nodes['Map Range.001'].inputs[2])
        except: pass
        try: group.links.new(created_nodes['Math.002'].outputs[0], created_nodes['Map Range'].inputs[2])
        except: pass
        try: group.links.new(created_nodes['Group Input'].outputs[2], created_nodes['Math'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.005'].outputs[0], created_nodes['Vector Math.009'].inputs[0])
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
        try: group.links.new(created_nodes['Mapping.003'].outputs[0], created_nodes['Image Texture.004'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Voronoi Texture.005'].outputs[2], created_nodes['Noise Texture.004'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Voronoi Texture.004'].outputs[2], created_nodes['Noise Texture.003'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Voronoi Texture.003'].outputs[2], created_nodes['Noise Texture.002'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Math'].outputs[0], created_nodes['Mapping.001'].inputs[3])
        except: pass
        try: group.links.new(created_nodes['Math'].outputs[0], created_nodes['Mapping.002'].inputs[3])
        except: pass
        try: group.links.new(created_nodes['Math'].outputs[0], created_nodes['Mapping.003'].inputs[3])
        except: pass
        try: group.links.new(created_nodes['Math.004'].outputs[0], created_nodes['Voronoi Texture.003'].inputs[2])
        except: pass
        try: group.links.new(created_nodes['Math.004'].outputs[0], created_nodes['Voronoi Texture.004'].inputs[2])
        except: pass
        try: group.links.new(created_nodes['Math.004'].outputs[0], created_nodes['Voronoi Texture.005'].inputs[2])
        except: pass
        try: group.links.new(created_nodes['Vector Math.013'].outputs[0], created_nodes['Vector Math.014'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Mix.001'].outputs[2], created_nodes['Vector Transform.003'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Texture Coordinate.005'].outputs[3], created_nodes['Separate XYZ'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Group Input'].outputs[5], created_nodes['Vector Math.002'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Group Input'].outputs[6], created_nodes['Vector Math.005'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Mapping.002'].outputs[0], created_nodes['Image Texture.001'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Texture Coordinate.023'].outputs[1], created_nodes['Vector Math.028'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Texture Coordinate.023'].outputs[1], created_nodes['Vector Math.042'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.028'].outputs[0], created_nodes['Vector Math.042'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.028'].outputs[0], created_nodes['Vector Math.015'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.042'].outputs[0], created_nodes['Vector Math.016'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Texture Coordinate.023'].outputs[1], created_nodes['Vector Math.029'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.016'].outputs[0], created_nodes['Vector Math.030'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.030'].outputs[0], created_nodes['Vector Math.031'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.029'].outputs[0], created_nodes['Vector Math.031'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Separate Color.001'].outputs[1], created_nodes['Invert Color.001'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Separate Color.001'].outputs[2], created_nodes['Combine Color.001'].inputs[2])
        except: pass
        try: group.links.new(created_nodes['Image Texture.001'].outputs[0], created_nodes['Separate Color.001'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate Color.001'].outputs[0], created_nodes['Combine Color.001'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Combine Color.001'].outputs[0], created_nodes['Vector Math.013'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Invert Color.001'].outputs[0], created_nodes['Combine Color.001'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.026'].outputs[0], created_nodes['Vector Math.025'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Rotate.005'].outputs[0], created_nodes['Vector Math.026'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.025'].outputs[0], created_nodes['Separate XYZ.011'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.011'].outputs[1], created_nodes['Vector Math.016'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.011'].outputs[2], created_nodes['Vector Math.029'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Math.005'].outputs[0], created_nodes['Vector Math.015'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.015'].outputs[0], created_nodes['Vector Math.030'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.011'].outputs[0], created_nodes['Math.005'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Combine XYZ.012'].outputs[0], created_nodes['Vector Math.026'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.031'].outputs[0], created_nodes['Vector Math.032'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.021'].outputs[0], created_nodes['Vector Math.022'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Texture Coordinate.024'].outputs[1], created_nodes['Vector Math.033'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Texture Coordinate.024'].outputs[1], created_nodes['Vector Math.043'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.033'].outputs[0], created_nodes['Vector Math.043'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.033'].outputs[0], created_nodes['Vector Math.023'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.043'].outputs[0], created_nodes['Vector Math.024'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Texture Coordinate.024'].outputs[1], created_nodes['Vector Math.034'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.024'].outputs[0], created_nodes['Vector Math.044'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.044'].outputs[0], created_nodes['Vector Math.045'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.034'].outputs[0], created_nodes['Vector Math.045'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Separate Color.003'].outputs[1], created_nodes['Invert Color.003'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Separate Color.003'].outputs[2], created_nodes['Combine Color.002'].inputs[2])
        except: pass
        try: group.links.new(created_nodes['Separate Color.003'].outputs[0], created_nodes['Combine Color.002'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Combine Color.002'].outputs[0], created_nodes['Vector Math.021'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Invert Color.003'].outputs[0], created_nodes['Combine Color.002'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.047'].outputs[0], created_nodes['Vector Math.027'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Rotate.004'].outputs[0], created_nodes['Vector Math.047'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.027'].outputs[0], created_nodes['Separate XYZ.012'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.012'].outputs[1], created_nodes['Vector Math.024'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.012'].outputs[2], created_nodes['Vector Math.034'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Math.011'].outputs[0], created_nodes['Vector Math.023'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.023'].outputs[0], created_nodes['Vector Math.044'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.012'].outputs[0], created_nodes['Math.011'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Combine XYZ.013'].outputs[0], created_nodes['Vector Math.047'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.045'].outputs[0], created_nodes['Vector Math.046'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Image Texture'].outputs[0], created_nodes['Separate Color.003'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.017'].outputs[0], created_nodes['Vector Math.018'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.035'].outputs[0], created_nodes['Vector Math.048'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.035'].outputs[0], created_nodes['Vector Math.019'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.048'].outputs[0], created_nodes['Vector Math.020'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.020'].outputs[0], created_nodes['Vector Math.037'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.037'].outputs[0], created_nodes['Vector Math.038'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.036'].outputs[0], created_nodes['Vector Math.038'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Separate Color.002'].outputs[1], created_nodes['Invert Color.002'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Separate Color.002'].outputs[2], created_nodes['Combine Color.003'].inputs[2])
        except: pass
        try: group.links.new(created_nodes['Separate Color.002'].outputs[0], created_nodes['Combine Color.003'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Combine Color.003'].outputs[0], created_nodes['Vector Math.017'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Invert Color.002'].outputs[0], created_nodes['Combine Color.003'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.041'].outputs[0], created_nodes['Vector Math.040'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Rotate.003'].outputs[0], created_nodes['Vector Math.041'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.040'].outputs[0], created_nodes['Separate XYZ.013'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.013'].outputs[1], created_nodes['Vector Math.020'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.013'].outputs[2], created_nodes['Vector Math.036'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Math.009'].outputs[0], created_nodes['Vector Math.019'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.019'].outputs[0], created_nodes['Vector Math.037'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.013'].outputs[0], created_nodes['Math.009'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Combine XYZ.014'].outputs[0], created_nodes['Vector Math.041'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.038'].outputs[0], created_nodes['Vector Math.039'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Image Texture.004'].outputs[0], created_nodes['Separate Color.002'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Texture Coordinate.025'].outputs[1], created_nodes['Vector Math.048'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Texture Coordinate.025'].outputs[1], created_nodes['Vector Math.035'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Texture Coordinate.025'].outputs[1], created_nodes['Vector Math.036'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.018'].outputs[0], created_nodes['Vector Rotate.003'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Math.008'].outputs[0], created_nodes['Vector Rotate.003'].inputs[3])
        except: pass
        try: group.links.new(created_nodes['Vector Math.022'].outputs[0], created_nodes['Vector Rotate.004'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Math.006'].outputs[0], created_nodes['Vector Rotate.004'].inputs[3])
        except: pass
        try: group.links.new(created_nodes['Vector Math.014'].outputs[0], created_nodes['Vector Rotate.005'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Math.007'].outputs[0], created_nodes['Vector Rotate.005'].inputs[3])
        except: pass
        try: group.links.new(created_nodes['Vector Math.049'].outputs[0], created_nodes['Vector Math.050'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Texture Coordinate.026'].outputs[1], created_nodes['Vector Math.051'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Texture Coordinate.026'].outputs[1], created_nodes['Vector Math.052'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.051'].outputs[0], created_nodes['Vector Math.052'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.051'].outputs[0], created_nodes['Vector Math.053'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.052'].outputs[0], created_nodes['Vector Math.054'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Texture Coordinate.026'].outputs[1], created_nodes['Vector Math.055'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.054'].outputs[0], created_nodes['Vector Math.056'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.056'].outputs[0], created_nodes['Vector Math.057'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.055'].outputs[0], created_nodes['Vector Math.057'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Separate Color.004'].outputs[1], created_nodes['Invert Color.004'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Separate Color.004'].outputs[2], created_nodes['Combine Color.004'].inputs[2])
        except: pass
        try: group.links.new(created_nodes['Separate Color.004'].outputs[0], created_nodes['Combine Color.004'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Combine Color.004'].outputs[0], created_nodes['Vector Math.049'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Invert Color.004'].outputs[0], created_nodes['Combine Color.004'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.060'].outputs[0], created_nodes['Vector Math.059'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.059'].outputs[0], created_nodes['Separate XYZ.014'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.014'].outputs[1], created_nodes['Vector Math.054'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.014'].outputs[2], created_nodes['Vector Math.055'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Math.010'].outputs[0], created_nodes['Vector Math.053'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.053'].outputs[0], created_nodes['Vector Math.056'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.014'].outputs[0], created_nodes['Math.010'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Combine XYZ.015'].outputs[0], created_nodes['Vector Math.060'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.057'].outputs[0], created_nodes['Vector Math.058'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.058'].outputs[0], created_nodes['Mix.005'].inputs[7])
        except: pass
        try: group.links.new(created_nodes['Vector Math.061'].outputs[0], created_nodes['Vector Math.062'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Texture Coordinate.027'].outputs[1], created_nodes['Vector Math.063'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Texture Coordinate.027'].outputs[1], created_nodes['Vector Math.064'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.063'].outputs[0], created_nodes['Vector Math.064'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.063'].outputs[0], created_nodes['Vector Math.065'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.064'].outputs[0], created_nodes['Vector Math.066'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Texture Coordinate.027'].outputs[1], created_nodes['Vector Math.067'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.066'].outputs[0], created_nodes['Vector Math.068'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.068'].outputs[0], created_nodes['Vector Math.069'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.067'].outputs[0], created_nodes['Vector Math.069'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Separate Color.005'].outputs[1], created_nodes['Invert Color.005'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Separate Color.005'].outputs[2], created_nodes['Combine Color.005'].inputs[2])
        except: pass
        try: group.links.new(created_nodes['Separate Color.005'].outputs[0], created_nodes['Combine Color.005'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Combine Color.005'].outputs[0], created_nodes['Vector Math.061'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Invert Color.005'].outputs[0], created_nodes['Combine Color.005'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.072'].outputs[0], created_nodes['Vector Math.071'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.071'].outputs[0], created_nodes['Separate XYZ.015'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.015'].outputs[1], created_nodes['Vector Math.066'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.015'].outputs[2], created_nodes['Vector Math.067'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Math.012'].outputs[0], created_nodes['Vector Math.065'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.065'].outputs[0], created_nodes['Vector Math.068'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.015'].outputs[0], created_nodes['Math.012'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Combine XYZ.016'].outputs[0], created_nodes['Vector Math.072'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.069'].outputs[0], created_nodes['Vector Math.070'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.070'].outputs[0], created_nodes['Mix.005'].inputs[6])
        except: pass
        try: group.links.new(created_nodes['Vector Math.073'].outputs[0], created_nodes['Vector Math.074'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Texture Coordinate.028'].outputs[1], created_nodes['Vector Math.075'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Texture Coordinate.028'].outputs[1], created_nodes['Vector Math.076'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.075'].outputs[0], created_nodes['Vector Math.076'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.075'].outputs[0], created_nodes['Vector Math.077'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.076'].outputs[0], created_nodes['Vector Math.078'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Texture Coordinate.028'].outputs[1], created_nodes['Vector Math.079'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.078'].outputs[0], created_nodes['Vector Math.080'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.080'].outputs[0], created_nodes['Vector Math.081'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.079'].outputs[0], created_nodes['Vector Math.081'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Separate Color.006'].outputs[1], created_nodes['Invert Color.006'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Separate Color.006'].outputs[2], created_nodes['Combine Color.006'].inputs[2])
        except: pass
        try: group.links.new(created_nodes['Separate Color.006'].outputs[0], created_nodes['Combine Color.006'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Combine Color.006'].outputs[0], created_nodes['Vector Math.073'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Invert Color.006'].outputs[0], created_nodes['Combine Color.006'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.084'].outputs[0], created_nodes['Vector Math.083'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.083'].outputs[0], created_nodes['Separate XYZ.016'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.016'].outputs[1], created_nodes['Vector Math.078'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.016'].outputs[2], created_nodes['Vector Math.079'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Math.013'].outputs[0], created_nodes['Vector Math.077'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.077'].outputs[0], created_nodes['Vector Math.080'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Separate XYZ.016'].outputs[0], created_nodes['Math.013'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Combine XYZ.017'].outputs[0], created_nodes['Vector Math.084'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Vector Math.081'].outputs[0], created_nodes['Vector Math.082'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Image Texture.002'].outputs[0], created_nodes['Separate Color.006'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.082'].outputs[0], created_nodes['Mix.006'].inputs[7])
        except: pass
        try: group.links.new(created_nodes['Mapping'].outputs[0], created_nodes['Image Texture.006'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Mapping.004'].outputs[0], created_nodes['Image Texture.005'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Mapping.005'].outputs[0], created_nodes['Image Texture.002'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Image Texture.006'].outputs[0], created_nodes['Separate Color.004'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Image Texture.005'].outputs[0], created_nodes['Separate Color.005'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.074'].outputs[0], created_nodes['Vector Math.084'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.050'].outputs[0], created_nodes['Vector Math.060'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Math.062'].outputs[0], created_nodes['Vector Math.072'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Combine XYZ.010'].outputs[0], created_nodes['Mapping'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Combine XYZ.011'].outputs[0], created_nodes['Mapping.004'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Combine XYZ.009'].outputs[0], created_nodes['Mapping.005'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Math'].outputs[0], created_nodes['Mapping.005'].inputs[3])
        except: pass
        try: group.links.new(created_nodes['Math'].outputs[0], created_nodes['Mapping'].inputs[3])
        except: pass
        try: group.links.new(created_nodes['Math'].outputs[0], created_nodes['Mapping.004'].inputs[3])
        except: pass
        try: group.links.new(created_nodes['Group Input'].outputs[4], created_nodes['Math.001'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Mix.002'].outputs[2], created_nodes['Group Output'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Math.004'].outputs[0], created_nodes['Voronoi Texture.001'].inputs[2])
        except: pass
        try: group.links.new(created_nodes['Math.004'].outputs[0], created_nodes['Voronoi Texture.002'].inputs[2])
        except: pass
        try: group.links.new(created_nodes['Math.004'].outputs[0], created_nodes['Voronoi Texture.006'].inputs[2])
        except: pass
        try: group.links.new(created_nodes['Vector Math.046'].outputs[0], created_nodes['Mix'].inputs[6])
        except: pass
        try: group.links.new(created_nodes['Vector Math.032'].outputs[0], created_nodes['Mix'].inputs[7])
        except: pass
        try: group.links.new(created_nodes['Vector Math.039'].outputs[0], created_nodes['Mix.001'].inputs[7])
        except: pass
        try: group.links.new(created_nodes['Vector Transform.003'].outputs[0], created_nodes['Mix.002'].inputs[7])
        except: pass
        try: group.links.new(created_nodes['Mix.006'].outputs[2], created_nodes['Vector Transform.004'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Vector Transform.004'].outputs[0], created_nodes['Mix.002'].inputs[6])
        except: pass
        try: group.links.new(created_nodes['Group Input'].outputs[0], created_nodes['Invert Color.004'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Group Input'].outputs[0], created_nodes['Invert Color.005'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Group Input'].outputs[0], created_nodes['Invert Color.006'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Group Input'].outputs[0], created_nodes['Invert Color.003'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Group Input'].outputs[0], created_nodes['Invert Color.001'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Group Input'].outputs[0], created_nodes['Invert Color.002'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Math.003'].outputs[0], created_nodes['Combine XYZ.014'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Math.003'].outputs[0], created_nodes['Combine XYZ.014'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Math.003'].outputs[0], created_nodes['Combine XYZ.012'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Math.003'].outputs[0], created_nodes['Combine XYZ.012'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Math.003'].outputs[0], created_nodes['Combine XYZ.013'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Math.003'].outputs[0], created_nodes['Combine XYZ.013'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Math.003'].outputs[0], created_nodes['Combine XYZ.017'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Math.003'].outputs[0], created_nodes['Combine XYZ.017'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Math.003'].outputs[0], created_nodes['Combine XYZ.015'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Math.003'].outputs[0], created_nodes['Combine XYZ.015'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Math.003'].outputs[0], created_nodes['Combine XYZ.016'].inputs[1])
        except: pass
        try: group.links.new(created_nodes['Math.003'].outputs[0], created_nodes['Combine XYZ.016'].inputs[0])
        except: pass
        try: group.links.new(created_nodes['Group Input'].outputs[1], created_nodes['Math.003'].inputs[0])
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
    self.layout.operator("node.add_node", text="TriplanarVoronoiNormal").type = Generated_TriplanarVoronoiNormal_Node.bl_idname

def register():
    bpy.utils.register_class(Generated_TriplanarVoronoiNormal_Node)
    
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
    
    bpy.utils.unregister_class(Generated_TriplanarVoronoiNormal_Node)

if __name__ == "__main__":
    register()
