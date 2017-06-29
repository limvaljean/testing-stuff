# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 13:17:40 2017

@author: 
"""

import kairos_face
from PIL import Image
import face_recognition
import matplotlib.pyplot as plt 
import time 
import os 
#%matplotlib inline 

kairos_face.settings.app_id = '9311364a'
kairos_face.settings.app_key = '21645ea39b84fccd009e59f1114ce9b8'

#putting in training data
for i in range(1,7): 
    fname = 'kim' + str(i) + '.jpg'
    print(fname)
    if os.path.exists(fname) != True:
        print('no such file')            
    kairos_face.enroll_face(file=fname, subject_id='Kim Jong Un', gallery_name='kju-gallery')
    
recognized_faces = kairos_face.recognize_face(file='kjursj.jpg', gallery_name='kju-gallery')
image = face_recognition.load_image_file('kjursj.jpg')

for i in range(len(recognized_faces['images'])): 
    a_face = recognized_faces['images'][i]['transaction']
    status = a_face['status']
    top = a_face['topLeftY']
    bottom = a_face['topLeftY'] + a_face['height']
    left = a_face['topLeftX']
    right = a_face['topLeftX'] + a_face['width']
       
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    
    file_name = 'image' + str(i) + '.jpg'    
    pil_image.save(file_name)    
    pil_image.show()
       
    if status == 'success': 
        print('This person is ' + a_face['subject_id'] + ' and our confidence level is ' + str(a_face['confidence']*100) + ' percent' )
    else: 
        print('We do not know who this is')
    time.sleep(5)
        
