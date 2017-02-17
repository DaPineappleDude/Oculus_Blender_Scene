import sys
import bpy
import os


#Scene Information
scene_info = bpy.context.scene

#Mesh 
ico_obj = bpy.data.meshes['Icosphere']

#Test
for frame in range(scene_info.frame_start, scene_info.frame_end+1):
    scene_info.frame_set(frame)
    print('\nImage Number %i'%frame)
    
    for idx in range(0, len(ico_obj.polygons)):
        print('Normal of Face %i is: %s' %(idx, ico_obj.polygons[idx].normal))
        
        
f = open('G:/Blender/target_data.txt', 'w', encoding= 'utf-8')

for frame in range(scene_info.frame_start, scene_info.frame_end+1):
    scene_info.frame_set(frame)
    f.write('\n\nImage Number %i'%frame)
    
    for idx in range(0, len(ico_obj.polygons)):
        f.write('\nNormal of Face %i is: %s' %(idx, ico_obj.polygons[idx].normal))
        

f.close
        
    
