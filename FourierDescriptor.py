'''
extract_shape(im_file, blowup = 1., plot_img = False, \
plot_contour = False, plot_contour_pts = False)

FD(x, y, plot_FD = False, y_lim = None)

filt_FD(Z, n_keep, no_zeroth = True)

get_FD_abs(x, y, order = 10, norm = True, no_zeroth = True)

recover_shape(Z)

size_norm(Z)
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import argparse 
import pdb

order = 10
norm = False
no_zeroth = False

def extract_shape(im_file, blowup = 1., plot_img = False, plot_contour = False, plot_contour_pts = False):
    
    im = mpimg.imread(im_file)
    # Take one of RGB(A) channels
    if len(im.shape) > 2:
        im = im[:, :, 0]
    
    if plot_img:
        plt.figure()
        plt.title('Original Shape')
        plt.imshow(im, cmap = plt.cm.gray)
	plt.show()

    # Note: by convention, in this case, y values comes from the 0th index.
    # Otherwise one has to transpose the image and the contour will appear sideways 
    x = np.arange(im.shape[1])*blowup  
    y = np.arange(im.shape[0])*blowup
    
    # Have to flip y to get the orientation right, again just a peculiar convention we have to work around
    # Note the [::] notation: a[3:20:2] means from the 3rd element to the 20th element, choose every 2nd element.
    y = y[::-1]

    # In case I want to shift x.
    #x_shift = 200
    #x += x_shift

    X, Y = np.meshgrid(x, y)
    
    plt.figure()
    plt.title('Contours')
    # Note the dimensions of x and y may NOT the same, thus the necessity of the 
    # tranpose operation (an oddity, I admit...)
    CS = plt.contour(X, Y, im, 1)
    levels = CS.levels
    #plt.show()
    print 'contour level', levels
    if not plot_contour:
        plt.close()

    cs_paths = CS.collections[0].get_paths()

    print 'number of contour path', len(cs_paths)

    p = cs_paths[0]
    v = p.vertices
    x_arr = v[:,0]
    y_arr = v[:,1]

    if plot_contour_pts:
        plt.figure()
        plt.title("Verify the contour points are correct")
        plt.scatter(x_arr, y_arr)
	plt.show()

    return x_arr, y_arr
 
'''#######################################################################'''

def FD(x, y, plot_FD = False, y_lim = None):

    N = len(x)
    n = np.arange(N)


    z = x + y*1j

    Z = np.fft.fft(z)

    if plot_FD:
        plt.figure()
        plt.title('FD real and imag')
        plt.plot(Z.real, 'b-')
        plt.plot(Z.imag, 'g-')
	plt.show()
        if y_lim != None:
            plt.ylim([-y_lim, y_lim])

    return Z

'''#######################################################################'''

def filt_FD(Z, order = 10, no_zeroth = False):
    N = len(Z)
    n = np.arange(len(Z))
    print 'Nyquist index', N/2
    # in case I want the centroid position.
    filt0 = n > 0 if no_zeroth else 1
    filt1 = filt0*(n <= order)
    
    filt2 = (n > ((N-1) - order))
    print 'Number of components from both sides:', filt1.sum(), filt2.sum()
    filt = filt1 + filt2
    #print Z.real[N/2]
    return Z*filt

'''#######################################################################'''

def get_FD_abs(x, y, order = 10, norm = True, no_zeroth = False):
    '''Finds the Fourier Descriptors and the recovered x and y for a shape.'''
    Z = FD(x, y)
    print 'len(Z)', len(Z)

    Z_filt = filt_FD(Z, order, no_zeroth=no_zeroth)
    if norm:
        Z_filt = size_norm(Z_filt)
    print 'len(Z_filt)', len(Z_filt)
    x_rec, y_rec = recover_shape(Z_filt)

    # throw away zero terms
    fd_mag = np.abs(Z_filt[Z_filt != 0])
#     fd_mag = fd_mag[fd_mag > 0]
    
    return fd_mag, x_rec, y_rec
    
'''#######################################################################'''

def recover_shape(Z):
    z_rec = np.fft.ifft(Z)

    x_rec = z_rec.real
    y_rec = z_rec.imag
    
    return x_rec, y_rec

'''#######################################################################'''

def size_norm(Z):
    return Z/np.sqrt( np.abs(Z[1])*np.abs(Z[-1]) )

'''#######################################################################'''

x1, y1 = extract_shape('number1.png') #blowup = 1., plot_img = True, plot_contour = True, #plot_contour_pts = True)
Z = FD(x1, y1, plot_FD = False, y_lim = None)
Zfilt = filt_FD(Z, order = 10, no_zeroth = True) #N_KEEP LIST HERE AS 10 IS THE ARGPARSE ORDER
x1_rec = []
y1_rec = []
fd1_mag = []
for n in range(len(x1)):
    fd_mag1, x_rec1, y_rec1 = get_FD_abs(x1, y1, order = 10, norm = False, no_zeroth = False)
    x1_rec.append(x_rec1)
    y1_rec.append(y_rec1)
    fd1_mag.append(fd_mag1)
#x1_rec, y1_rec = recover_shape(Z)
#size_norm = size_norm(Z)

x2, y2 = extract_shape('number2.png') #blowup = 1., plot_img = True, plot_contour = True, #plot_contour_pts = True)
Z = FD(x2, y2, plot_FD = False, y_lim = None)
Zfilt = filt_FD(Z, order = 10, no_zeroth = True) #N_KEEP LIST HERE AS 10 IS THE ARGPARSE ORDER
x2_rec = []
y2_rec = []
fd2_mag = []
for n in range(len(x2)):
    fd_mag2, x_rec2, y_rec2 = get_FD_abs(x2, y2, order = 10, norm = False, no_zeroth = False)
    x2_rec.append(x_rec2)
    y2_rec.append(y_rec2)
    fd2_mag.append(fd_mag2)    
#x2_rec, y2_rec = recover_shape(Z)
#size_norm = size_norm(Z)
   
x6, y6 = extract_shape('number6.png') #blowup = 1., plot_img = True, plot_contour = True, plot_contour_pts = True)
Z = FD(x6, y6, plot_FD = False, y_lim = None)
Zfilt = filt_FD(Z, order = 10, no_zeroth = True) #N_KEEP LIST HERE AS 10 IS THE ARGPARSE ORDER
x6_rec = []
y6_rec = []
fd6_mag = []
for n in range(len(x2)):
    fd_mag6, x_rec6, y_rec6 = get_FD_abs(x6, y6, order = 10, norm = False, no_zeroth = False)
    x6_rec.append(x_rec6)
    y6_rec.append(y_rec6)
    fd6_mag.append(fd_mag6)    
#x6_rec, y6_rec = recover_shape(Z)
#size_norm = size_norm(Z)

'''#######################################################################'''

plt.figure()
for n in range(len(x1)):
    plt.plot(x1_rec[n], y1_rec[n], 'b')

for n in range(len(x2)):
    plt.plot(x2_rec[n], y2_rec[n], 'g')

for n in range(len(x6)):
    plt.plot(x6_rec[n], y6_rec[n], 'r')

plt.show()

'''#######################################################################'''

if no_zeroth == True:
    start = 1
else:
    start = 2

plt.figure()
for n in range(len(x1)):
    plt.plot(np.arange(2, 2*order), fd2_mag[n][start:-1], 'bo')

for n in range(len(x2)):
    plt.plot(np.arange(2, 2*order), fd2_mag[n][start:-1], 'gx')

for n in range(len(x6)):
    plt.plot(np.arange(2, 2*order), fd6_mag[n][start:-1], 'r8')

plt.show()


'''#######################################################################'''


parser = argparse.ArgumentParser()
parser.add_argument('-order', type = int)
parser.add_argument('-norm', type = bool)parser.add_argument('-no_zeroth', type = bool)#parser.set_defaults(order = 10, no_zeroth = False, norm = False)
args = parser.parse_args()
order = args.order
norm = args.norm
no_zeroth = args.no_zeroth

