from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns; sns.set()
from sklearn import decomposition
from sklearn.decomposition import PCA
from sklearn.datasets import load_digits
from sklearn import svm

'''It should interpolate the input image, im, onto a grid that is dim1 ⨉ dim2, referring to the
number of pixels for the horizontal and vertical directions, respectively. If plot_new_im
is True, display the interpolated image using plt.imshow(), with the keyword argument
interpolation set to “nearest”. This way, the image will show each pixel as is,
without interpolation, making clear useful diagnostic information, such as the number of
pixels in the image and which pixels have high (or low) values. Also, as the default, it should
show a grid. But if the flag grid_off is True then turn off plt.grid. The function
should return the interpolated, flattened image array
'''

def interpol_im(im, dim1 = 8, dim2 = 8, plot_new_im = False, cmap = 'binary', axis_off = False):
    
    x = np.arange(im.shape[1])
    y = np.arange(im.shape[0])
    f2d = interp2d(x, y, im)
    x_new = np.linspace(0, im.shape[1], dim1)
    y_new = np.linspace(0, im.shape[0], dim2)

    im_new = f2d(x_new, y_new)
    im_flat = im_new.flatten()    

    if plot_new_im:
        plt.imshow(im_new, cmap = 'binary', interpolation = 'nearest')
        plt.grid('off')
        plt.show()

    return im_new, im_flat

'''It returns md_pca and X_proj, where X_proj contains
the projections of the data array X in the PCA space. 
'''

def pca_X(X, n_comp = 10):
    
    md_pca = PCA(n_comp)  
    Xproj = pca.fit_transform(X)
    
    return md_pca, Xproj

'''It returns the md_clf. The meanings of gamma and C were explained in class. For our
purposes, you may leave gamma and C at their default values for both Parts I and II. 
'''

def svm_train(gamma = 0.001, C = 100):
    
    md_clf = svm.SVC(gamma, C)
    
    return md_clf

'''This function will be used in Part II and it
- loads the image contained in imfile;
- interpolates the image by calling interpol_im();
- projects the interpolated, flattened image array onto the PCA space by using md_pca;
- makes a prediction as to the identity of the image, by using md_clf; and finally,
- returns the prediction.
'''

def pca_svm_pred(imfile, md_pca, md_clf, dim1 = 45, dim2 = 60):
    
    im = mpimg.imread(imfile) #loads the image contained in imfile
    im_new, im_flat = interpol_im(im) #interpolates the image by calling interpol_im():
    md_pca, Xproj = pca_X(X) # projects interpolated, flattened image array onto PCA space
    md_clf = svm_train() #calls md_clf
    md_clf.fit(Xproj, y) #applies boundaries
    pred = md_clf.predict(Xproj) #makes a prediction using md_clf
    
    return pred 

'''This function will be used in Part I. It uses one of the images in the sklearn digit data set, X,
X[ind] (the default for ind is 0, but it can be anything) to rescale the pixel values of the
image unseen, so that this image, when compared with any image in X[ind], has the
same (or very similar) mean (around 5) and a similar pixel value range (roughly between 0
and 15). 
'''

def rescale_pixel(X, unseen, ind = 0):

    feature_range = (min(X[ind]), max(X[ind]))
    scale = pre.MinMaxScaler(feature_range)
    scaling_unseen = scaling.fit_transform(X[ind])
    
    return scaling_unseen

