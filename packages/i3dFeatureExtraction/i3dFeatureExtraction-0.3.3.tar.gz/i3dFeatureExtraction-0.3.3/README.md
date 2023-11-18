# I3D_Feature_Extraction
Hello, I am Hao Vy Phan. I have develop this package using ResNet-50 to convert a video into an extracted i3D features numpy file.

## Overview
**Input**: a directory which store 1 or more videos.

**Output**: 1 or many `.npy` files (extracted i3D features). Each features file is shaped `n/16 * 2048` where `n` is the number of frames in the video

If there is a problem installing or implementing this package, please do not hesitate to contact me via my email. I am pleased to have people use my product.

**Update**:
* **Version 0.3.2**: Fix bug of searching for video files. Now it looks for extensions *.webm, .avi, .wmv, .mp4, .m4v, .m4p* inside folder *datasetpath*.
* **Version 0.3.1.1**: The function can receive directly the path to just 1 video, if **multiplefiles** is set *False*.

---

## Usage

### Installation
Before installing my package, please install these pakages:
```commandline
(python 3.8)
pip install torchvision-0.11.2+cu113-cp38-cp38-win_amd64.whl
pip install torchaudio-0.10.1+cu113-cp38-cp38-win_amd64.whl
pip install torch-1.10.1+cu113-cp38-cp38-win_amd64.whl
pip install opencv_python-4.5.5-cp38-cp38-win_amd64.whl
```
Those wheel files can be downloaded from [this link](https://download.pytorch.org/whl/cu113/torch_stable.html):
* [Opencv-Python==4.5.5](https://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv)
* [torch==1.10.1+cu113](https://download.pytorch.org/whl/cu113/torch-1.10.1%2Bcu113-cp38-cp38-win_amd64.whl)
* [torchaudio==0.10.1+cu113](https://download.pytorch.org/whl/cu113/torchaudio-0.10.1%2Bcu113-cp38-cp38-win_amd64.whl)
* [torchvision==0.11.2+cu113](https://download.pytorch.org/whl/cu113/torchvision-0.11.2%2Bcu113-cp38-cp38-win_amd64.whl)

If you are using a **non-GPU** environment, try this:
```commandline
(python 3.8)
pip install torch==1.10.1 torchvision==0.11.2 torchaudio==0.10.1 opencv_python==4.5.5
```

After 4 above packages, to install `i3dFeatureExtraction` package into your Python environment, run this code on your terminal:
```commandline
pip install i3dFeatureExtraction
```

### Implementing
The main function of this package is `FeatureExtraction` which converts a directory of videos into numpy feature files.

```Python
from i3dFeatureExtraction import FeatureExtraction
FeatureExtraction.generate(
    datasetpath="directory/of/input/videos",
    outputpath = "directory/to/store/output/numpy/files",
    pretrainedpath = "path/to/i3D/pretrained/weight",
    sample_mode = "oversample/center_crop"
    multiplefiles = True/False
)
```
* **datasetpath** (REQUIRED): path to videos.
* If **multiplefiles** is _True_ (default), the **datasetpath** is the path to a directory which contains 1 or more videos.
* If **multiplefiles** is _False_, the **datasetpath** is the path to a video.
* **outputpath** (optional, default: *"output/"*): the proccessed numpy feature files would be stored in this directory.
* **pretrainedpath** (optional, default: *"pretrained/"*): the path of the pretrained i3d weight. If the weight is not existed, it will be downloaded and created manually.
* **sample_mode** (optional, default: *"oversample/"*) receive "oversample" or "center_crop". If *oversample*, each frame will be cropped and flipped to be turned into 10 frames.


---
## Structure of this package

I am not good at drawing UML diagram but I hope this image helps illustrate the package's structure.

![i3dFeatureExtraction - UML Diagram](https://vyhaoromanletters.s3.us-east-2.amazonaws.com/i3dExtract.png)

---

## Credits
This code is based on the following repositories:
* [pytorch-resnet3d](https://github.com/Tushar-N/pytorch-resnet3d)
* [pytorch-i3d-feature-extraction](https://github.com/Finspire13/pytorch-i3d-feature-extraction)
* [E2E-Action-Segmentation/feature_extraction](https://github.com/nguyenphwork/E2E-Action-Segmentation/tree/main/feature_extraction)

I would like to extend a special thank-you to the original authors of these repositories for providing the foundation on which this implementation is built.


