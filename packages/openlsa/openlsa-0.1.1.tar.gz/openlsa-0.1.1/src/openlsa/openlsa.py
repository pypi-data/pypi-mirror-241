#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 13:49:59 2022

This is a simple python script wrote by the Clermont's EM team to
retrieve displacement maps for a pair of images, pattern beeing periodic.

These python codes can be used for non-profit academic research only. They are
distributed under the terms of the GNU general public license v3.

Anyone finding the python codes useful is kindly asked to cite:

# [LSA] M. Grédiac, B. Blaysat, and F. Sur. Extracting displacement and strain
fields from checkerboard images with the localized spectrum analysis.
Experimental Mechanics, 59(2):207–218, 2019.

@author: UCA/IP - M3G - EM team
"""

# %% Required Libraries
import numpy as np
from numpy import ma
from scipy.ndimage import map_coordinates
from PIL import Image
from skimage.restoration import unwrap_phase as unwrap
import cv2
from scipy import ndimage

# %% Class LSA
class OpenLSA():

    # %% Class constructor
    def __init__(self, img=None, vec_k=None, max_pitch=30, roi=None, init_angle=0):

        if img is None:
            if vec_k is None:
                print(["Please feed me, I have nothing to eat here... I need an image or the",
                       " pitch and the angle of the periodic pattern"])
                return

        if img is not None:
            if vec_k is None:
                vec_k = self.find_k(img, max_pitch=max_pitch,
                                    init_angle=init_angle)

        if vec_k is not None:
            if isinstance(vec_k, list) and len(vec_k) == 2:
                self.vec_k = vec_k
            elif vec_k.dtype == 'complex':
                self.vec_k = [vec_k, vec_k*np.exp(1j*np.pi/2)]
            else:
                print('error')

        self.roi = roi

    # %% Some usefull functions
    def copy(self):
        return OpenLSA(vec_k=self.vec_k, roi=self.roi)

    def pitch(self):
        return 1/np.abs(self.vec_k)

    def vec_dir(self):
        return np.exp(1j*np.angle(self.vec_k))

    def find_k(self, img, max_pitch=30, init_angle=0):
        """Compute the Pitch and the Angle from the location of the peak in the spectral
        representation of a given image "img"
        "max_pitch"" refers to the highest possible pitch"""

        img_odd = np.hstack((img,
                             np.zeros([img.shape[0], np.mod(img.shape[1], 2)+1])))
        img_odd = np.vstack((img_odd,
                             np.zeros([np.mod(img_odd.shape[0], 2)+1, img_odd.shape[1]])))
        
        dim = img_odd.shape
        fft_img_abs = np.abs(np.fft.fftshift(np.fft.fft2(img_odd)))
        freq_x, freq_y = np.meshgrid(np.linspace(-0.5, 0.5, dim[1]),
                                     np.linspace(-0.5, 0.5, dim[0]),
                                     indexing='xy')

        # removing central peak
        min_freq = 1/max_pitch
        fft_img_abs[np.sqrt(freq_x**2+freq_y**2) < min_freq] = 1

        # only a quarter is considered:
        # the first direction should be within init_angle + [-pi/4, pi/4]
        fft_img_abs_quarter = fft_img_abs.copy()
        fft_img_abs_quarter[np.angle(freq_x + 1j*freq_y) < init_angle-np.pi/4] = 1
        fft_img_abs_quarter[np.angle(freq_x + 1j*freq_y) >= init_angle+np.pi/4] = 1

        # search peak
        loc_max = np.argmax(fft_img_abs_quarter.ravel())
        vec_k = freq_x.ravel()[loc_max] + 1j*freq_y.ravel()[loc_max]

        return vec_k

    # %% Kernel building
    def compute_kernel(self, std=None):
        """Compute the LSA gaussian kernel, of standard diviation "std"."""

        if std is None:
            std = self.pitch().max()

        t_noy = np.ceil(4*std)
        px_x, px_y = np.meshgrid(np.arange(-t_noy, t_noy+1), np.arange(-t_noy, t_noy+1))
        kernel = np.exp(-(px_x**2+px_y**2)/(2*std**2))
        kernel = kernel/np.sum(kernel)

        return kernel

    # %% LSA core functions
    def compute_mod_arg(self, px_x, px_y, img, img_size, kernel, vec_k,
                        size_pad, border):
        """Compute the convolution between the kernel and the WFT taken at the "freq_c" frequency
        and along direction angle.
        px_x, px_y are the pixel corrdinate of image "img", of size "img_size"
        kernel is the kernel used for LSA
        angle, freq_c characterize the pattern periodicity
        size_pad, border refer to the enlarged iamge for fft"""

        ima = img*np.exp(-1j*2*np.pi*(np.real(vec_k)*px_x+np.imag(vec_k)*px_y))
        fft2ima = np.fft.fft2(ima, size_pad)
        w_f = np.fft.ifft2(fft2ima*np.fft.fft2(kernel, size_pad))
        w_f = w_f[border[0]:border[0]+img_size[0], border[1]:border[1]+img_size[1]]
        mod = np.abs(w_f)
        phi = np.angle(w_f)
        return mod, phi

    def compute_mod_phases(self, px_x, px_y, img, kernel=None, roi_coef=0.25):
        """LSA core.
        px_x, px_y are the pixel corrdinate of image "img"
        kernel is the kernel used for LSA
        roi_coef defines the thresshold used for defining the region of interest"""

        if kernel is None:
            self.compute_kernel()

        kernel_size = np.array(kernel.shape)

        img_size = np.array(img.shape)
        size_pad = img_size+kernel_size-1
        border = ((kernel_size-1+np.mod(kernel_size-1, 2))/2 - 1).astype(int)

        # theta-direction
        mod_0, phi_0 = self.compute_mod_arg(px_x, px_y, img, img_size, kernel,
                                            self.vec_k[0], size_pad, border)

        # theta+pi/2-direction
        mod_1, phi_1 = self.compute_mod_arg(px_x, px_y, img, img_size, kernel,
                                            self.vec_k[1], size_pad, border)

        mod = mod_0*self.vec_dir()[0] + mod_1*self.vec_dir()[1]
        mod_abs = np.abs(mod)

        loc_roi = mod_abs < mod_abs.max()*roi_coef

        # define the RoI if undefined
        if self.roi is None:
            self.roi = mod_abs > mod_abs.max()*roi_coef

        phi_0 = ma.masked_array(phi_0, loc_roi)
        phi_1 = ma.masked_array(phi_1, loc_roi)
        phi_0 = unwrap(phi_0)
        phi_1 = unwrap(phi_1)
        phi_0 = np.array(phi_0.filled(0))
        phi_1 = np.array(phi_1.filled(0))

        return phi_0*self.vec_dir()[0] + phi_1*self.vec_dir()[1], mod

    def rough_point2point(self, img1, img2, point1,
                          point2=None, dis_init=None):
        """Calculation of the rough displacement thanks to open cv"""

        if point2 is None:
            point2 = point1

        # calculation of the rough displacement thanks to open cv
        f_size = (self.pitch().max()/np.sqrt(2))/2
        flow = estimate_u(img1, img2, filter_size=f_size, dis_init=dis_init)

        if np.linalg.norm(point1-point1.astype(int)) == 0:
            point2 = point1 + np.flip((np.real(flow)[point1[0], point1[1]],
                                       np.imag(flow)[point1[0], point1[1]]))
            return point2, flow

        print('The given point is not an integer, an interpolation is required')
        ux = map_coordinates(np.real(flow[:, :, 0]), [[point1[0]], [point1[1]]])
        uy = map_coordinates(np.imag(flow[:, :, 1]), [[point1[0]], [point1[1]]])

        point2 = point1 + (ux, uy)
        return point2, flow


    def jump_correction(self, phi_1, phi_2, point1_2_point2, lsa_2=None):
        """Update the second phase in order to ensure that LSA retrieves the
        same displacement than the one given in PointInfo"""
        where_its_not_null = (phi_2!=0)
        u_xy = (point1_2_point2[1, :] - point1_2_point2[0, :]) @ np.array([[1j], [1]])
        phi_1_point1 = map_coordinates(phi_1, [[point1_2_point2[0, 0]],
                                               [point1_2_point2[0, 1]]], order=1)
        phi_2_point2 = map_coordinates(phi_2, [[point1_2_point2[1, 0]],
                                               [point1_2_point2[1, 1]]], order=1)

        if lsa_2 is None:
            lsa_2 = self
        lsa_12 = LSA12(self, lsa_2)
        k1_abs = np.abs(self.vec_k[0])
        k2_abs = np.abs(lsa_2.vec_k[0])

        md = point1_2_point2[0, :] @ [[1j], [1]]

        Corr = (k1_abs*lsa_12.rot_1*(md+phi_1_point1/(2*np.pi*k1_abs))
                - k2_abs*lsa_12.rot_2*(md+u_xy
                                       + phi_2_point2/(2*np.pi*k2_abs)))
        phi_2[where_its_not_null] += 2*np.pi*np.round(scal_prod(Corr, lsa_12.vec_dir)) @ lsa_2.vec_dir()
        return phi_2

    def compute_displacement(self, phi_1, phi_2,
                             lsa_2=None,
                             list_of_points=None, max__iter=15, flag=False, uinit=None):
        """Computation of the displacement field from the reference and current phases"""

        if list_of_points is None:
            pt_x, pt_y = np.meshgrid(np.arange(phi_1.shape[1]), np.arange(phi_1.shape[0]))
            x_roi = np.array(pt_x[self.roi]).reshape(-1, 1)
            y_roi = np.array(pt_y[self.roi]).reshape(-1, 1)
        else:
            x_roi = list_of_points[:, 0]
            y_roi = list_of_points[:, 1]

        if lsa_2 is None:
            lsa_2 = self
        lsa_12 = LSA12(self, lsa_2)
        k1_abs = np.abs(self.vec_k[0])
        k2_abs = np.abs(lsa_2.vec_k[0])
        tmp_cst = ((k1_abs/k2_abs)*lsa_12.rot_1m2-1)*(x_roi+1j*y_roi)

        phi_1_roi = map_coordinates(phi_1, [y_roi, x_roi], order=1)
        phi_1_roi_rot = lsa_12.rot_1m2*phi_1_roi

        if uinit is None:
            phi_2_roi = map_coordinates(phi_2, [y_roi, x_roi], order=1)
            u = tmp_cst + (phi_1_roi_rot - phi_2_roi)/(2*np.pi*k1_abs)
        else:
            u = map_coordinates(uinit, [y_roi, x_roi], order=1)

        stop_crit = 5e-4
        nb_px = len(x_roi)
        loop_n = 0
        for loop_n in range(max__iter):

            tmp_phi2 = map_coordinates(phi_2, [y_roi+u.imag, x_roi+u.real], order=2)
            new_u = tmp_cst + (phi_1_roi_rot - tmp_phi2)/(2*np.pi*k2_abs)

            delta = new_u - u
            u = new_u

            if np.linalg.norm(delta[np.isfinite(delta)], 2) < np.sqrt(2)*stop_crit*nb_px:
                break

        flag_iter = False
        if loop_n == max__iter-1:
            flag_iter = True
            print('Displacement calculation did not converge')

        if list_of_points is None:
            output_u = np.zeros(phi_1.shape, complex)
            output_u[self.roi] = u.ravel()
            if flag:
                return output_u, flag_iter
            return output_u

        if flag:
            return u, flag_iter
        return u

    # %% extra function
    def compute_refstate_from_im_stack(self, kernel, img_stack, Point1, roi_coef=0.1):
        """ Often, multiple images are taken at reference state. This function extracts phase
        fields for all images, and averages them by taking into account the rigid body motion
        that might occur in between. The reference coordinate system corresponds to the one
        given by the first image"""

        nb_img = len(img_stack)
        print('Computing reference phase: %i/%i' % (1, len(img_stack)))
        img_ref = np.array(Image.open(img_stack[0]), dtype=float)
        X, Y = np.meshgrid(np.arange(0, img_ref.shape[1]),
                           np.arange(0, img_ref.shape[0]))
        phi_ref, __ = self.compute_mod_phases(X, Y, img_ref, kernel, roi_coef=roi_coef)
        phi_REF = phi_ref.copy()/nb_img
        i = 0
        for img_name in img_stack[1::]:
            i += 1
            print('Computing reference phase: %i/%i' % (i+1, len(img_stack)))
            img_loc = np.array(Image.open(img_name), dtype=float)
            phi_loc = self.compute_mod_phases(X, Y, img_loc, kernel, roi_coef=roi_coef/2)[0]
            Point2, DisFlow_U = self.rough_point2point(img_ref, img_loc, Point1)
            phi_loc = self.jump_correction(phi_ref, phi_loc, np.array([Point1, Point2]))
            uxy_loc = self.compute_displacement(phi_ref, phi_loc, uinit=DisFlow_U)
            uxy_loc_rbm = compute_RBM(uxy_loc[self.roi], X[self.roi], Y[self.roi])
            phi_loc_rbm = map_coordinates(phi_loc,
                                          [Y[self.roi]+uxy_loc_rbm.imag,
                                           X[self.roi]+uxy_loc_rbm.real], order=2)
            phi_REF[self.roi] += (phi_loc_rbm + (2*np.pi/self.pitch()[0])*uxy_loc_rbm)/nb_img
        return phi_REF


###############################################################################
# %% Class LSA12
#                        If carrier waves change
class LSA12():

    def __init__(self, lsa_1, lsa_2):
        pitch = (lsa_1.pitch()+lsa_2.pitch())/2
        angle_vec_k = (np.angle(lsa_1.vec_k[0])+np.angle(lsa_2.vec_k[0]))/2
        vec_dir = [np.exp(1j*angle_vec_k), np.exp(1j*(angle_vec_k+np.pi/2))]
        self.vec_k = vec_dir/pitch
        self.vec_dir = vec_dir
        self.vec_k1 = lsa_1.vec_k[0]
        self.vec_k2 = lsa_2.vec_k[0]
        self.rot_1 = np.exp(1j*(angle_vec_k-np.angle(self.vec_k1)))
        self.rot_2 = np.exp(1j*(angle_vec_k-np.angle(self.vec_k2)))
        self.rot_1m2 = np.exp(1j*(np.angle(self.vec_k2)-np.angle(self.vec_k1)))


###############################################################################
# %% Usefull functions
def scal_prod(input_1, input_2):
    """ Scalar product"""
    return np.real(input_1)*np.real(input_2) + np.imag(input_1)*np.imag(input_2)


def compute_RBM(u, x, y):
    """ Computing the RBM part of a displacement"""
    x = (x - x.mean())/(2*(x.max()-x.min()))
    y = (y - y.mean())/(2*(y.max()-y.min()))
    Op = np.array([[len(x), 0, np.sum(x)],
                   [0, len(y), np.sum(y)],
                   [np.sum(x), np.sum(y), np.sum(x**2+y**2)]])
    RHM = np.array([np.sum(u.real), np.sum(u.imag), np.sum(y*u.real + x*u.imag)])
    dof = np.linalg.lstsq(Op, RHM, rcond=None)[0]
    return dof[0] + 1j*dof[1] + dof[2]*(y + 1j*x)

 
###############################################################################
# %% OpenCV functions for raw estimating of the displacement field
def estimate_u(img1, img2, filter_size=None, dis_init=None):
    # optical flow will be needed, so it is initialized
    dis = cv2.DISOpticalFlow_create()
    
    img1_uint8 = np.uint8(img1*2**(8-round(np.log2(img1.max()))))
    img2_uint8 = np.uint8(img2*2**(8-round(np.log2(img1.max()))))  
    
    if filter_size is not None:
        img1_uint8 = ndimage.gaussian_filter(img1_uint8, filter_size)
        img2_uint8 = ndimage.gaussian_filter(img2_uint8, filter_size)

    if dis_init is not None:
        dis_init_mat = np.zeros([img1_uint8.shape[0], img1_uint8.shape[1], 2], dtype='float32')
        dis_init_mat[:,:,0] = dis_init.real
        dis_init_mat[:,:,1] = dis_init.imag
        flow = dis.calc(img1_uint8, img2_uint8,  warp_flow(dis_init_mat, dis_init_mat))
    else:
        flow = dis.calc(img1_uint8, img2_uint8, None)

    return flow[:,:,0] + 1j*flow[:,:,1]


def warp_flow(img, flow):
    h, w = flow.shape[:2]
    flow = -flow
    flow[:,:,0] += np.arange(w)
    flow[:,:,1] += np.arange(h)[:,np.newaxis]
    res = cv2.remap(img, flow, None, cv2.INTER_LINEAR)
    return res   