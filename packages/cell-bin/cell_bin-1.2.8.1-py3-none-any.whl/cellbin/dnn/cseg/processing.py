from cellbin.image.augmentation import f_ij_16_to_8, f_rgb2gray, f_ij_16_to_8_v2
from cellbin.image.mask import f_instance2semantics
from cellbin.image.augmentation import f_percentile_threshold, f_histogram_normalization, f_equalize_adapthist
from cellbin.image.augmentation import f_padding as f_pad
from cellbin.image.morphology import f_deep_watershed

import numpy as np
import cv2
from skimage.exposure import rescale_intensity
import tifffile


def f_prepocess(img):
    """
    2023/09/20 @fxzhao 优化图像16转8;增加对img的dtype判断,降低类型转换开销;支持传入图片路径
    """
    if isinstance(img, str):
        img = tifffile.imread(img)
    img = np.squeeze(img)
    if img.dtype != 'uint8':
        img = f_ij_16_to_8_v2(img)
    img = f_rgb2gray(img, True)
    img = f_percentile_threshold(img)
    img = f_equalize_adapthist(img, 128)
    img = f_histogram_normalization(img)
    if img.dtype != np.float32:
        img = np.array(img).astype(np.float32)
    img = np.ascontiguousarray(img)
    return img


def f_postpocess(pred):
    pred = pred[0, :, :, 0]

    # pred[pred > 0] = 1
    # pred = np.uint8(pred)

    pred = f_instance2semantics(pred)
    return pred


def f_preformat(img):
    img = np.expand_dims(img, axis=2)
    img = np.expand_dims(img, axis=0)
    return img


def f_postformat(pred):
    if not isinstance(pred, list):
        pred = [np.uint8(rescale_intensity(pred,out_range=(0,255)))]
    else:
        pred = [np.uint8(rescale_intensity(pred[0],out_range=(0,255)))]
    # p_max = np.max(pred[-1])
    pred = f_deep_watershed(pred,
                            maxima_threshold=round(0.1 * 255),
                            maxima_smooth=0,
                            interior_threshold=round(0.2 * 255),
                            interior_smooth=0,
                            fill_holes_threshold=15,
                            small_objects_threshold=15,
                            radius=2,
                            watershed_line=0)
    return f_postpocess(pred)


def f_preformat_mesmer(img):
    img = np.stack((img, img), axis=-1)
    img = np.expand_dims(img, axis=0)
    return img


def f_postformat_mesmer(pred):
    if isinstance(pred, list):
        pred = [pred[0], pred[1][..., 1:2]]
    pred = f_deep_watershed(pred,
                            maxima_threshold=0.075,
                            maxima_smooth=0,
                            interior_threshold=0.2,
                            interior_smooth=2,
                            small_objects_threshold=15,
                            fill_holes_threshold=15,
                            radius=2,
                            watershed_line=0)
    return f_postpocess(pred)


def f_padding(img, shape, mode='constant'):
    h, w = img.shape[:2]
    win_h, win_w = shape[:2]
    img = f_pad(img, 0, abs(win_h - h), 0, abs(win_w - w), mode)
    return img


def f_fusion(img1, img2):
    img1 = cv2.bitwise_or(img1, img2)
    return img1
