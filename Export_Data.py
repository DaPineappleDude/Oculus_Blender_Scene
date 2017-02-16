import sys
import bpy
import os

#All coordinates in the world frame
#Camera extrinsics
"""
cam_ex = bpy.data.objects["Camera.000"]

cam_position = cam_ex.location
cam_rotation = cam_ex.rotation_quaternion
cam_scale = cam_ex.scale
"""

#Camera intrinsics
"""
cam_in = bpy.data.cameras['Camera.000']

cam_f = cam_in.lens
cam_snsr_x = cam_in.sensor_width
cam_snsr_y = cam_in.sensor_height 
"""


#Image Settings
res_x = bpy.data.scenes["Scene"].render.resolution_x
res_y = bpy.data.scenes["Scene"].render.resolution_y

aspect_x = bpy.data.scenes["Scene"].render.pixel_aspect_x
aspect_y = bpy.data.scenes["Scene"].render.pixel_aspect_y


#Mesh Data
ico_obj = bpy.data.objects['Icosphere']
ico_obj.data.polygons[1]

#Test
for cam in bpy.data.cameras:
    print('%s\n focal length = %fmm\n sensor width = %fmm\n sensor height = %fmm\n Resolution (Width x Height) = %fX%f px\n' %(cam.name, cam.lens, cam.sensor_width, cam.sensor_height,bpy.data.scenes["Scene"].render.resolution_x, bpy.data.scenes["Scene"].render.resolution_y))
    

'''for cam in bpy.data.objects:
    print('%s has a location of %s & orientation %s' %(cam.name, cam.location, cam.rotation_quaternion))'''
    
print('\n')

num_camera = len(bpy.data.cameras) 

for idx in range(0, num_camera):
    cam = bpy.data.objects[idx]
    #Location
    print('%s is located at:\nCartesian\n x = %fcm\n y = %fcm\n z = %fcm\n' %(cam.name, cam.location.x, cam.location.y, cam.location.z,))
    #Orientation
    print('Quaternion\n w = %f\n x = %f\n y = %f\n z = %f\n' %(cam.rotation_quaternion[0], cam.rotation_quaternion[1], cam.rotation_quaternion[2], cam.rotation_quaternion[3]))

