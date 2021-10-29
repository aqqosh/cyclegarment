from os import listdir
from numpy import asarray
from numpy import vstack
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
from numpy import savez_compressed
 

def load_images(path, size=(256,256)):
    data_list = list()
    for filename in listdir(path):
        pixels = load_img(path + filename, target_size=size)
        # convert to numpy array
        pixels = img_to_array(pixels)
        # store
        data_list.append(pixels)
    return asarray(data_list)
 
if __name__ == "__main__":
    # dataset path
    path = 'data/'
    # load dataset A
    dataA1 = load_images(path + 'trainA/')
    dataAB = load_images(path + 'testA/')
    dataA = vstack((dataA1, dataAB))
    print('Loaded dataA: ', dataA.shape)
    # load dataset B
    dataB1 = load_images(path + 'trainB/')
    dataB2 = load_images(path + 'testB/')
    dataB = vstack((dataB1, dataB2))
    print('Loaded dataB: ', dataB.shape)
    # save as compressed numpy array
    filename = 'garment1_256.npz'
    savez_compressed(filename, dataA, dataB)
    print('Saved dataset: ', filename)