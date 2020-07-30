import os
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from skimage import img_as_bool, io, color
import numpy as np
# se leen todas la imagenes de un directorio, se convierten en matriz y se guardan en imglist
# el tipo de imagen se guarda en labels
def appendImgs(directories):
    imglist = []
    labels = []
    for directory in directories:
        imgs = os.listdir(directory)
        for img in imgs:
            imgPath = directory + img
            if not os.path.isdir(imgPath) :
                x = load_img(imgPath)
                x = img_as_bool(color.rgb2gray(io.imread(imgPath)))
                imglist.append(x)
                if 'thick' in imgPath:
                    labels.append(1)
                elif 'thin' in imgPath:
                    labels.append(2)
                elif 'medium' in imgPath:
                    labels.append(3)
    return imglist, labels


def loadData(directory, categories):
    img_list = []
    labels = []
    subdirectories = os.listdir(directory)
    for subdir in subdirectories:
        images = os.listdir(os.path.join(directory, subdir))
        label = categories.index(subdir)
        for image in images:
            if os.path.isdir(image):
                continue
            img_path = os.path.join(directory,subdir,image)
            #x = load_img(img_path)
            x = img_as_bool(color.rgb2gray(io.imread(img_path)))
            img_list.append(x)
            labels.append(label)
    return np.array(img_list).astype(int), np.array(labels)
    

if __name__ == "__main__":

    thickTrainDir = "data/train/thick/"
    thinTrainDir = "data/train/thin/"
    mediumTrainDir = "data/train/medium/"

    thickValDir = "data/validation/thick/"
    thinValDir = "data/validation/thin/"
    mediumValDir = "data/validation/thin/"

    X_train, y_train = appendImgs([thickTrainDir,thinTrainDir,mediumTrainDir])

    print(y_train)