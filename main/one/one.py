import warnings
import cv2
from keras import backend as K
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')
### Load trained model modules
from keras.applications.vgg16 import VGG16
#from keras.applications.vgg19 import VGG19
#from keras.applications.nasnet import NASNetMobile, preprocess_input, decode_predictions
#from keras.applications.mobilenet import MobileNet, preprocess_input, decode_predictions
### Load image processing modules
from keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt

### Load additional modules for feature extraction
from keras.models import Model

import numpy as np
import matplotlib.pyplot as plt
import imageio
import scipy, scipy.misc, scipy.signal
import cv2
import sys
from one import data123

#img_path = "one.png"

def path_img(img_path):
    img224 = image.load_img(path=img_path, grayscale=False, color_mode="rgb", target_size=(224,224), interpolation="nearest")
    img_tensor224 = image.img_to_array(img=img224, data_format="channels_last", dtype="float32")
    img_tensor224 = np.expand_dims(img_tensor224, axis=0)
    img_tensor224 /= img_tensor224.max()
    return img_tensor224

def get_layer_names(model, verbose=False):
    layer_names = []
    for layer in model.layers:
        if verbose:
            pass
            #print(layer.name)
        layer_names.append(layer.name)
    return layer_names

def check_valid_layer_name(model, layer_name):
    layer_names = [layer.name for layer in model.layers]
    check_val = layer_name in layer_names
    return  check_val

def get_layer_output(model, layer_name):
    assert check_valid_layer_name(model, layer_name), ("layer_name '{}' not included in model! Check layer_name variable.".format(layer_name))
    try:
        intermediate_layer_model = Model(inputs=model.input,
                                         outputs=model.get_layer(layer_name).output)
        
        return intermediate_layer_model
    except ValueError as ve:
        print(ve)


'''
model_names = get_layer_names(vgg16, verbose=True)

## Extract output from first convolutional layer "block1_conv1"
first_conv_layer_output = get_layer_output(vgg16, layer_name="block1_conv1")
## Get activations from first convolutional layer
activations_first_conv_layer = first_conv_layer_output.predict(img_tensor224)
print(activations_first_conv_layer.shape)
## Visualization without postprocessing:
## Visualize 3rd filter:
plt.matshow(activations_first_conv_layer[0, :, :, 4-1])
## Visualize 10th filter:
plt.matshow(activations_first_conv_layer[0, :, :, 11-1])
## Visualize 20th filter:
plt.matshow(activations_first_conv_layer[0, :, :, 21-1])
## Visualize 64th (last) filter:
plt.matshow(activations_first_conv_layer[0, :, :, 64-1])

'''
def plot_activations(model, img_tensor, layer_names=None, images_per_row=16, verbose=False, do_postprocess=True):
    if layer_names is None:
        ## Get layer_names (except the first one, because it is the input layer)
        layer_names = [layer.name for layer in model.layers][1:]
    else:
        ## Check if names in layer_names are valid names
        checks = []
        for layer_name in layer_names:
            checks.append(check_valid_layer_name(model=model, layer_name=layer_name))
        checks = np.array(checks)
        if not np.sum(checks) == len(layer_names):
            raise ValueError('layer_names incorrect')
    ## Create keras model using functional API mapping one input to several layer outputs
    layer_outputs = [layer.output for layer in model.layers[1:]]
    
    intermediate_models = Model(inputs=model.input, outputs=layer_outputs)
    if verbose:
        pass
        #print("Intermediate models summary:")
        #print(intermediate_models.summary())
    ## Display feature maps
    activations = intermediate_models.predict(img_tensor)
    counter1=0
    str1=0
    for layer_name, layer_activation in zip(layer_names, activations):
        #print(str1)
        str1+=1
        ## Get number of features/filters in the feature map
        n_filters = layer_activation.shape[-1]
        ## The feature map has shape (1, size, size, n_filters)
        size = layer_activation.shape[1]
        ## Divide the activation channels/filters into matrix
        n_cols = n_filters // images_per_row
        ## Init empty numpy matrix
        display_grid = np.zeros(shape=(size*n_cols, images_per_row*size))
        
        ## Divide each filter into big horizontal grid
        filter_image_counter=0
        for col in range(n_cols):
            for row in range(images_per_row):
                ## Get base filter image, note this has shape = (size,size)
                filter_image = layer_activation[0,
                                                 :, :,
                                                 col*images_per_row+row]
                if do_postprocess:
                    ## Postprocess the features in filter to make it visually palatable
                    filter_image -= filter_image.mean()
                    filter_image /= filter_image.std()
                    filter_image *= 64
                    filter_image += 128
                    filter_image = np.clip(a=filter_image, a_min=0, a_max=255).astype("uint8")
                
                ## Populate filter_image into the display_grid matrix
                try:
                    jetcam = cv2.applyColorMap(np.uint8(filter_image), cv2.COLORMAP_JET)
                    if filter_image_counter==1:
                        cv2.imwrite('one/three/'+str(layer_name)+"-"+str(filter_image_counter)+'.jpg', jetcam)
                    filter_image_counter+=1
                    display_grid[col*size:(col+1)*size,
                                 row*size:(row+1)*size] = filter_image
                except:
                    pass
            
        ## Display the grid
        scale = 1./size
        try:
            jetcam = cv2.applyColorMap(np.uint8(display_grid), cv2.COLORMAP_JET)
            print(str1)
            data123.third123+=5
            cv2.imwrite('one/one/'+layer_name+'.jpg', jetcam)
        except:
            pass
        counter1+=1
        scale = 1./size
        #plt.figure(figsize=(scale*display_grid.shape[1],
                            #cale*display_grid.shape[0]))
        #plt.title(layer_name)
        #plt.grid(False)
        #plt.imshow(display_grid, aspect='auto', cmap='viridis')
    #plt.show()
    K.clear_session()
    return None
def build():
    nasnet = VGG16(weights="imagenet", include_top=False)
    return nasnet
#print(get_layer_names(nasnet),len(get_layer_names(nasnet)))
#def run(model=):
#plot_activations(model=nasnet, img_tensor=img_tensor224, images_per_row=16, verbose=False, do_postprocess=True)
