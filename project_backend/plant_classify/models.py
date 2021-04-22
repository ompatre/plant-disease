from django.db import models
from django.conf import settings
from PIL import Image
import tensorflow as tf
from keras.preprocessing import image
import cv2
import numpy as np
import os

classnames=['Apple___Apple_scab',
 'Apple___Black_rot',
 'Apple___Cedar_apple_rust',
 'Apple___healthy',
 'Blueberry___healthy',
 'Cherry_(including_sour)___Powdery_mildew',
 'Cherry_(including_sour)___healthy',
 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
 'Corn_(maize)___Common_rust_',
 'Corn_(maize)___Northern_Leaf_Blight',
 'Corn_(maize)___healthy',
 'Grape___Black_rot',
 'Grape___Esca_(Black_Measles)',
 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
 'Grape___healthy',
 'Orange___Haunglongbing_(Citrus_greening)',
 'Peach___Bacterial_spot',
 'Peach___healthy',
 'Pepper,_bell___Bacterial_spot',
 'Pepper,_bell___healthy',
 'Potato___Early_blight',
 'Potato___Late_blight',
 'Potato___healthy',
 'Raspberry___healthy',
 'Soybean___healthy',
 'Squash___Powdery_mildew',
 'Strawberry___Leaf_scorch',
 'Strawberry___healthy',
 'Tomato___Bacterial_spot',
 'Tomato___Early_blight',
 'Tomato___Late_blight',
 'Tomato___Leaf_Mold',
 'Tomato___Septoria_leaf_spot',
 'Tomato___Spider_mites Two-spotted_spider_mite',
 'Tomato___Target_Spot',
 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
 'Tomato___Tomato_mosaic_virus',
 'Tomato___healthy']
# Create your models here.
class Plant(models.Model):
    image = models.ImageField(upload_to='post_images')
    result=models.CharField(max_length=20,blank=True)
    
    def __str__(self):
        return str(self.image)
    def save(self,*args,**kwargs):
        img = Image.open(self.image)
        img_array=image.img_to_array(img)
        dim = (50,50)
        resized = cv2.resize(img_array,dim,interpolation=cv2.INTER_AREA)
        ready=np.expand_dims(resized,axis=0)
        try:
            file_model=os.path.join(settings.BASE_DIR,'model_using_keras_epoch_25.h5')
            graph = tf.compat.v1.get_default_graph()
            with graph.as_default():
                model=tf.keras.models.load_model(file_model)
                pred = np.argmax(model.predict(ready))
                self.result=str(classnames[pred])
                print("Classified as ",classnames[pred])
        except:
            print('Failed to Classify')
            self.result = 'failed to classify' 
        return super().save(*args,**kwargs)