import os
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import resource
import numpy as np
from skimage import img_as_bool, io, color
import tensorflow as tf
from functions import appendImgs

os.environ["CUDA_VISIBLE_DEVICES"]="3"

thickTrainDir = "data/train/thick/"
thinTrainDir = "data/train/thin/"
mediumTrainDir = "data/train/medium/"

thickValDir = "data/validation/thick/"
thinValDir = "data/validation/thin/"
mediumValDir = "data/validation/thin/"

X_train, y_train = appendImgs([thickTrainDir,thinTrainDir,mediumTrainDir])
X_val, y_val = appendImgs([thickValDir,thinValDir,mediumValDir])

## continua...


####################
NUM_CLASSES = 3
NUM_FILTERS = 128

X_train = X_train.reshape(X_train.shape[0], 256, 256, 1)
X_val = X_val.reshape(X_val.shape[0], 256, 256, 1)

input_shape = (256, 256, 1)

model = Sequential()
model.add(Conv2D(NUM_FILTERS, kernel_size=(3,3), activation='relu', input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(4, 4)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(4, 4)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(NUM_CLASSES,activation='softmax'))

model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy', 
              metrics=['accuracy'])

model.summary()



# trainning

BATCH_SIZE = 8
EPOCHS = 20

log = model.fit(x=X_train,y=y_train, batch_size=BATCH_SIZE, epochs=EPOCHS, validation_data=(X_val, y_val), verbose=1)

score = model.evaluate(X_val, y_val, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

model.save("model_multiclass.h5")

################
# prediccion
################

model = tf.keras.models.load_model('model_multiclass.h5')

test_dir = "data/test/"
test_imgs = os.listdir(test_dir)

#predicciones = []
#imagenes = []

for img in test_imgs:
    imgPath = test_dir + img
    if not os.path.isdir(imgPath):
        imgBool = img_as_bool(color.rgb2gray(io.imread(imgPath)))
        #imagenes.append(imgBool)
        
        x = img_to_array(imgBool)
        x = np.expand_dims(x, axis=0)
        clases = model.predict_classes(x)
        print(clases)
        '''
        clase = None
        if 1 in clases:
            clase = "Fibra gruesa"
        elif 2 in clases:
            clase = "Fibra media"
        elif 3 in clases:
            clase = "Fibra delgada"
            
        #predicciones.append(clase)
        print("\'", img, "' es ", clase)
        '''
