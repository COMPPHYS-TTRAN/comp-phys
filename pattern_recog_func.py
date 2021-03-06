from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns; sns.set()
from sklearn import decomposition
from sklearn.decomposition import PCA
from sklearn.datasets import load_digits
from sklearn import svm

############################################

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

############################################

def pca_X(X, n_comp = 10):
    
    md_pca = PCA(n_comp)  
    Xproj = pca.fit_transform(X)
    
    return md_pca, Xproj

############################################

def svm_train(gamma = 0.001, C = 100):
    
    md_clf = svm.SVC(gamma, C)
    
    return md_clf

############################################

def pca_svm_pred(imfile, md_pca, md_clf, dim1 = 45, dim2 = 60):
    
    im = mpimg.imread(imfile) #loads the image contained in imfile
    im_new, im_flat = interpol_im(im) #interpolates the image by calling interpol_im():
    md_pca, Xproj = pca_X(X) # projects interpolated, flattened image array onto PCA space
    md_clf = svm_train() #calls md_clf
    md_clf.fit(Xproj, y) #applies boundaries
    pred = md_clf.predict(Xproj) #makes a prediction using md_clf
    
    return pred 

############################################

def rescale_pixel(X, unseen, ind = 0):

    want = (min(X[ind]), max(X[ind]))
    scale = pre.MinMaxScaler(want)
    scale_un = scale.fit_transform(X[ind])
    
    return scale_un

