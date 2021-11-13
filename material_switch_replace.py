# Get list of all material switches
material_switches = getMaterialVariants()

# Loop through material switches
for count, value in enumerate(material_switches, start = 1):
    print(f'{count} {value}:')

    # Get the material pointer    
    switch_ptr = findMaterial(value)
        
    # Get list of nodes with switch assigned
    nodes_with_switch = switch_ptr.getNodes()
    
    # Get count of nodes
    node_count = len(nodes_with_switch)
    
    # Get active material name
    active_material_name = getMaterialVariantCurrent(value)
    
    # Get active material pointer
    active_material_ptr = findMaterial(active_material_name)
    
    print(f'   Active: {active_material_name}\n   Nodes: {node_count}')
    
    # Loop through nodes and set to active material
    for node in nodes_with_switch:
        node.setMaterial(active_material_ptr)