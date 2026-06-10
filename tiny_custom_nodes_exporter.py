bl_info = {
    "name": "Tiny Custom Nodes Exporter",
    "author": "MoxTools",
    "version": (1, 1, 0),
    "blender": (4, 0, 0),
    "location": "Shader Editor > Context Menu (Right Click)",
    "description": "Exports shader node groups as standalone, ready-to-install Blender add-ons including texture pointers and ColorRamps.",
    "warning": "",
    "doc_url": "https://github.com/MoxTools/blender-tiny-custom-nodes-exporter",
    "tracker_url": "https://github.com/MoxTools/blender-tiny-custom-nodes-exporter/issues",
    "category": "Node",
}

import bpy
import os

def setup_temporary_properties():
    try:
        bpy.types.WindowManager.exported_addon_code_buffer = bpy.props.StringProperty(options={'HIDDEN'})
    except Exception:
        pass

def clear_temporary_properties():
    try:
        del bpy.types.WindowManager.exported_addon_code_buffer
    except Exception:
        pass


class WM_OT_ExportAddonFileDialog(bpy.types.Operator):
    bl_idname = "wm.export_addon_file_dialog"
    bl_label = "Save Custom Node As..."
    
    filepath: bpy.props.StringProperty(subtype="FILE_PATH") # type: ignore
    filter_glob: bpy.props.StringProperty(default="*.py", options={'HIDDEN'}) # type: ignore
    use_filter: bpy.props.BoolProperty(default=True, options={'HIDDEN'}) # type: ignore
    filter_python: bpy.props.BoolProperty(default=True, options={'HIDDEN'}) # type: ignore

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def execute(self, context):
        try:
            target_path = os.path.abspath(self.filepath)
            if not target_path.lower().endswith(".py"):
                target_path += ".py"
                
            generated_code = context.window_manager.exported_addon_code_buffer
            if not generated_code:
                self.report({'ERROR'}, "Error: Generated code buffer was empty.")
                return {'CANCELLED'}

            with open(target_path, 'w', encoding='utf-8', newline='\n') as f:
                f.write(generated_code)
                
            self.report({'INFO'}, f"Custom node successfully saved to: {target_path}")
            context.window_manager.exported_addon_code_buffer = ""
            
        except Exception as e:
            self.report({'ERROR'}, f"Error while saving: {str(e)}")
        return {'FINISHED'}


class NODE_OT_ExportGroupAsAddon(bpy.types.Operator):
    bl_idname = "node.export_group_as_addon"
    bl_label = "Export as Custom Node"
    bl_description = "Generates a standalone add-on from the selected node group"

    def execute(self, context):
        space = context.space_data
        if not space or space.type != 'NODE_EDITOR':
            self.report({'WARNING'}, "No active Node Editor found.")
            return {'CANCELLED'}
            
        active_node = context.active_node
        if not active_node or not hasattr(active_node, "node_tree") or not active_node.node_tree:
            self.report({'WARNING'}, "Please select a node group first.")
            return {'CANCELLED'}
            
        source_tree = active_node.node_tree
        target_group_name = source_tree.name
        
        has_images = any(node.type == 'TEX_IMAGE' for node in source_tree.nodes)
        clean_name = "".join([c for c in target_group_name if c.isalnum() or c == '_'])

        # --- CODE GENERATION ---
        tree_code = f"        # Generate a unique tree name for this instance\n"
        tree_code += f"        tree_name = f'.internal_{clean_name}_' + str(id(self))\n"
        tree_code += f"        group = bpy.data.node_groups.new(name=tree_name, type='ShaderNodeTree')\n\n"
        
        for item in source_tree.interface.items_tree:
            if item.item_type != 'SOCKET':
                continue
            socket_type = repr(item.socket_type)
            tree_code += f"        sock = group.interface.new_socket(name='{item.name}', in_out='{item.in_out}', socket_type={socket_type})\n"
            if hasattr(item, "default_value"):
                val = item.default_value
                if hasattr(val, "__len__"):
                    tree_code += f"        try: sock.default_value = [{','.join(map(str, val))}]\n        except: pass\n"
                else:
                    tree_code += f"        try: sock.default_value = {repr(val)}\n        except: pass\n"
            if item.in_out == 'INPUT':
                if hasattr(item, "min_value") and item.min_value is not None:
                    tree_code += f"        try: sock.min_value = {item.min_value}\n        except: pass\n"
                if hasattr(item, "max_value") and item.max_value is not None:
                    tree_code += f"        try: sock.max_value = {item.max_value}\n        except: pass\n"

        tree_code += "\n        # Dictionary for exact node mapping\n        created_nodes = {}\n\n"
        tree_code += "        group_input = group.nodes.new('NodeGroupInput')\n        created_nodes['Group Input'] = group_input\n\n"
        tree_code += "        group_output = group.nodes.new('NodeGroupOutput')\n        created_nodes['Group Output'] = group_output\n\n"

        orig_input_node = next((n for n in source_tree.nodes if n.bl_idname == 'NodeGroupInput'), None)
        orig_output_node = next((n for n in source_tree.nodes if n.bl_idname == 'NodeGroupOutput'), None)
        if orig_input_node:
            tree_code += f"        group_input.location_absolute = ({orig_input_node.location_absolute.x}, {orig_input_node.location_absolute.y})\n"
        if orig_output_node:
            tree_code += f"        group_output.location_absolute = ({orig_output_node.location_absolute.x}, {orig_output_node.location_absolute.y})\n"

        for node in source_tree.nodes:
            if node.bl_idname in ('NodeGroupInput', 'NodeGroupOutput'):
                continue
            safe_node_var = "node_" + "".join([c if c.isalnum() else "_" for c in node.name])
            node_line = f"        {safe_node_var} = group.nodes.new('{node.bl_idname}')\n"
            node_line += f"        {safe_node_var}.location_absolute = ({node.location_absolute.x}, {node.location_absolute.y})\n"
            if hasattr(node, "label") and node.label:
                node_line += f"        {safe_node_var}.label = '{node.label}'\n"
            if hasattr(node, "shrink") and node.bl_idname == 'NodeFrame':
                node_line += f"        {safe_node_var}.shrink = {node.shrink}\n"
                
            # --- SPEZIALFALL: COLORRAMP (ValToRGB) ---
            if node.bl_idname == 'ShaderNodeValToRGB':
                node_line += f"        # ColorRamp Setup\n"
                node_line += f"        ramp_{safe_node_var} = {safe_node_var}.color_ramp\n"
                node_line += f"        ramp_{safe_node_var}.interpolation = '{node.color_ramp.interpolation}'\n"
                # Bestehende Standard-Elemente löschen (Blender erstellt immer 2)
                node_line += f"        while len(ramp_{safe_node_var}.elements) > 1:\n"
                node_line += f"            ramp_{safe_node_var}.elements.remove(ramp_{safe_node_var}.elements[-1])\n"
                
                for idx, element in enumerate(node.color_ramp.elements):
                    color_list = [element.color[0], element.color[1], element.color[2], element.color[3]]
                    if idx == 0:
                        node_line += f"        ramp_{safe_node_var}.elements[0].position = {element.position}\n"
                        node_line += f"        ramp_{safe_node_var}.elements[0].color = {color_list}\n"
                    else:
                        node_line += f"        elem_{idx} = ramp_{safe_node_var}.elements.new({element.position})\n"
                        node_line += f"        elem_{idx}.color = {color_list}\n"

            excluded_props = {'name', 'type', 'location', 'width', 'height', 'select', 'hide', 'inputs', 'outputs', 'internal_links', 'parent', 'draw_buttons', 'draw_buttons_ext', 'rna_type', 'bl_idname', 'label', 'color', 'use_custom_color', 'show_options', 'show_texture', 'show_preview'}
            for prop in node.rna_type.properties:
                p_id = prop.identifier
                if p_id not in excluded_props and not prop.is_readonly:
                    try:
                        val = getattr(node, p_id)
                        node_line += f"        try: {safe_node_var}.{p_id} = {repr(val)}\n        except: pass\n"
                    except: pass
                
            for i, inp in enumerate(node.inputs):
                if not inp.is_linked and hasattr(inp, "default_value"):
                    val = inp.default_value
                    # Fix für Colors / Vektoren / Listen in Inputs
                    if hasattr(val, "__len__") and not isinstance(val, str):
                        val_list = list(val)
                        node_line += f"        try: {safe_node_var}.inputs[{i}].default_value = {val_list}\n        except: pass\n"
                    elif type(val) in (float, int, str, bool):
                        node_line += f"        try: {safe_node_var}.inputs[{i}].default_value = {repr(val)}\n        except: pass\n"
            
            node_line += f"        created_nodes[{repr(node.name)}] = {safe_node_var}\n"
            tree_code += node_line

        tree_code += "\n        # --- PACK NODES INTO FRAMES ---\n"
        for node in source_tree.nodes:
            if node.parent:
                tree_code += f"        if {repr(node.name)} in created_nodes and {repr(node.parent.name)} in created_nodes:\n"
                tree_code += f"            created_nodes[{repr(node.name)}].parent = created_nodes[{repr(node.parent.name)}]\n"

        tree_code += "\n        # --- CONNECT LINKS ---\n"
        for link in source_tree.links:
            try:
                from_node_name = "Group Input" if link.from_node.bl_idname == 'NodeGroupInput' else link.from_node.name
                to_node_name = "Group Output" if link.to_node.bl_idname == 'NodeGroupOutput' else link.to_node.name
                from_idx = list(link.from_node.outputs).index(link.from_socket)
                to_idx = list(link.to_node.inputs).index(link.to_socket)
                tree_code += f"        try: group.links.new(created_nodes[{repr(from_node_name)}].outputs[{from_idx}], created_nodes[{repr(to_node_name)}].inputs[{to_idx}])\n        except: pass\n"
            except: pass

        if has_images:
            draw_buttons_code = '        layout.template_ID(self, "image_pointer", open="image.open")'
            pointer_property_code = '    image_pointer: bpy.props.PointerProperty(type=bpy.types.Image, name="Texture", update=lambda self, context: self.update_image(context))'
        else:
            draw_buttons_code = '        pass'
            pointer_property_code = ''

        addon_template = f'''bl_info = {{
    "name": "Custom Node - {target_group_name}",
    "author": "MoxTools Generator",
    "version": (1, 0, 0),
    "blender": (4, 0, 0),
    "location": "Shader Editor > Shift+A > Custom Nodes",
    "description": "Automatically exported standalone custom node",
    "category": "Node",
}}

import bpy
from bpy.types import ShaderNodeCustomGroup

class Generated_{clean_name}_Node(ShaderNodeCustomGroup):
    bl_idname = 'ShaderNode_{clean_name}_Generated'
    bl_label = '{target_group_name}'
    bl_icon = 'NONE'

{pointer_property_code}

    def update_image(self, context):
        if hasattr(self, "image_pointer") and self.node_tree:
            img = self.image_pointer if (self.image_pointer and self.image_pointer.name in bpy.data.images) else None
            for node in self.node_tree.nodes:
                if node.type == 'TEX_IMAGE':
                    node.image = img
            if context and hasattr(context, "area") and context.area:
                context.area.tag_redraw()

    def init(self, context):
{tree_code}
        self.node_tree = group
        if hasattr(self, "update_image"):
            self.update_image(context)

    def draw_buttons(self, context, layout):
{draw_buttons_code}

    def free(self):
        if self.node_tree and self.node_tree.users <= 1:
            try: bpy.data.node_groups.remove(self.node_tree)
            except: pass


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
    self.layout.operator("node.add_node", text="{target_group_name}").type = Generated_{clean_name}_Node.bl_idname

def register():
    bpy.utils.register_class(Generated_{clean_name}_Node)
    
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
    
    bpy.utils.unregister_class(Generated_{clean_name}_Node)

if __name__ == "__main__":
    register()
'''
        filename = f"customnode_{clean_name.lower()}.py"
        if bpy.data.filepath:
            base_dir = os.path.dirname(bpy.data.filepath)
        else:
            base_dir = os.path.join(os.path.expanduser('~'), 'Documents')
            
        absolute_default_filepath = os.path.join(base_dir, filename)
        context.window_manager.exported_addon_code_buffer = addon_template

        bpy.ops.wm.export_addon_file_dialog(
            'INVOKE_DEFAULT', 
            filepath=absolute_default_filepath
        )
        return {'FINISHED'}


def draw_context_menu_export(self, context):
    active_node = context.active_node
    if active_node and hasattr(active_node, "node_tree") and active_node.node_tree:
        layout = self.layout
        layout.separator() 
        layout.operator(NODE_OT_ExportGroupAsAddon.bl_idname, text=f"Export '{active_node.node_tree.name}' as Custom Node...", icon='SCRIPT')


classes = (
    WM_OT_ExportAddonFileDialog,
    NODE_OT_ExportGroupAsAddon,
)

def register():
    setup_temporary_properties()
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.NODE_MT_context_menu.append(draw_context_menu_export)

def unregister():
    bpy.types.NODE_MT_context_menu.remove(draw_context_menu_export)
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    clear_temporary_properties()

if __name__ == "__main__":
    register()
