import numpy as np
import cv2
import matplotlib.pyplot as plt

class OpencvProcessing:
    def __init__(self):
        self.name=""
    def openPic(self,file_path):
        pic=cv2.imread(file_path)
        return pic
    def convertPic(self,cv_file):
        pic=cv2.cvtColor(cv_file,cv2.COLOR_BGR2RGB)
        return pic
    def gain(self,cv_file,gain=1.0):
        pic=cv_file*gain
        pic=np.clip(pic,0,255).astype(np.uint8)
        return pic
    def gamma(self,cv_file,gamma=1.0):
        gamma_cvt = np.zeros((256,1),dtype = 'uint8')
        for i in range(256):
            gamma_cvt[i][0] = 255 * (float(i)/255) ** (1.0/gamma)
        pic = cv2.LUT(cv_file,gamma_cvt)
        return pic

if __name__=="__main__":
    open_file= "D:\python\dev\ImageProcessing\image\DSC_0104_FHDhalf.jpg"
    cvtest= OpencvProcessing()
    img= cvtest.openPic(open_file)
    img= cvtest.gain(img,1)
    img= cvtest.gamma(img,0.5)
    img= cvtest.convertPic(img)

    plt.imshow(img)
    plt.show()