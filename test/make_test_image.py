import os
import numpy as np
import matplotlib.pyplot as plt
import mpl_utils
import np_utils

def make_test_image(show=False):
    plt.subplot(211)
    lines = [[[i,2.3],[i+0.5,2.4],[i,2.5]]
             for i in np.arange(0, 3.6,0.4)]
    mpl_utils.plot_lines(lines, 'k-')
    
    mpl_utils.xyfill([(0, 0), (1, 0.5), (2, -0.5), (3, 0)])
    
    mpl_utils.error_plot([0, 1, 2, 3, 4],
                         [0, 1, 2, 1, 2],
                         [0.1, 0.4, 0.1, 0.2, 0.1],
                         'b', 'that')
    
    mpl_utils.circle([2, 1], 0.1, color='r')
    
    plt.subplot(223)
    mpl_utils.imshow_array([[0,2,3],[5,1,6]])
    plt.colorbar()
    
    plt.subplot(224)
    f = lambda x, y: x**2 + y**2
    x, y = np_utils.build_grid([10, 10], [1,4], [15,19])
    mpl_utils.imshow_function(f, x, y)
    plt.colorbar()
    
    d = os.path.split(__file__)[0]
    if show:
        plt.show()
    else:
        plt.savefig(os.path.join(d,'test_image.png'))

def plot_test_image():
    make_test_image(show=True)

if __name__ == '__main__':
    plt.figure(figsize=(10,10))
    make_test_image()
    plt.clf()
    plot_test_image()
