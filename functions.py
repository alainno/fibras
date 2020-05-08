import os
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from skimage import img_as_bool, io, color
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

thickTrainDir = "data/train/thick/"
thinTrainDir = "data/train/thin/"
mediumTrainDir = "data/train/medium/"

thickValDir = "data/validation/thick/"
thinValDir = "data/validation/thin/"
mediumValDir = "data/validation/thin/"

X_train, y_train = appendImgs([thickTrainDir,thinTrainDir,mediumTrainDir])

print(y_train)