import Perspective_image
import cv2
import os


with os.scandir('Dataset2/') as entries:
    for entry in entries:
        print(entry.name)
        img = cv2.imread('Dataset2/'+str(entry.name))
        img = Perspective_image.process_img_scanned(img)
        #cv2.imshow('win', img)
        os.chdir('Dataset3')
        cv2.imwrite(str(entry.name), img)
        os.chdir('..')
        #cv2.imwrite()
        #cv2.waitKey(0)
print(os.getcwd())
