import tifffile
from cellbin.modules import StainType
from cellbin.modules.tissue_segmentation import TissueSegmentation
from cellbin.dnn.tseg.yolo.detector import TissueSegmentationYolo


def main(model_type="bcdu"):
    model_path = r"D:\code\public\cell_segmentation_v03\model\tissueseg_bcdu_SHDI_230523_tf.onnx"
    #model_path = r"D:\code\public\tissuecut\model\weight_rna_220909.onnx"
    #model_path = r"D:\code\envs\tissuecut_yolo\tissueseg_yolo_SH_20230131.onnx"
    input_path = r"E:\dapitest\img\C01528B2.tif"
    out_path = r"E:\dapitest\C01528B2.tif"
    gpu = "-1"
    num_threads = 0

    if model_type == "yolo":
        seg = TissueSegmentationYolo()
        seg.f_init_model(model_path)

        img = tifffile.imread(input_path)
        mask = seg.f_predict(img)
        tifffile.imwrite(out_path, mask)
    else:
        tissue_bcdu = TissueSegmentation(
            model_path=model_path,
            stype=StainType.ssDNA.value,
            #stype="rna",
            gpu=gpu,
            num_threads=int(num_threads))

        img = tifffile.imread(input_path)
        mask = tissue_bcdu.run(img)
        tifffile.imwrite(out_path, mask)

    return


if __name__ == '__main__':
    import sys

    main("bcdu")
    sys.exit()
