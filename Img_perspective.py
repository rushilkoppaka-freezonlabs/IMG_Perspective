import Perspective_image
import cv2
import os


with os.scandir('Images/') as entries:
    for entry in entries:
        print(entry.name)
        img = cv2.imread('Images/'+str(entry.name))
        img = Perspective_image.process_img_scanned(img)
        #cv2.imshow('win', img)
        os.chdir('Images_transformed')
        cv2.imwrite(str(entry.name), img)
        os.chdir('..')
        #cv2.imwrite()
        #cv2.waitKey(0)
print(os.getcwd())