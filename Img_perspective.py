import Perspective_image
import cv2
import os


with os.scandir('../obj/') as entries:
    for entry in entries:
        print(entry.name)
        if entry.name.split('.')[-1] == 'txt':
            continue
        img = cv2.imread('../obj/'+str(entry.name))
        img = Perspective_image.process_img_scanned(img)
        os.chdir('../Dataset3')
        cv2.imwrite(str(entry.name), img)
        os.chdir('../IMG_Perspective')
        
print(os.getcwd())
