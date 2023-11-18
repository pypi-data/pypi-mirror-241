from pathlib import Path
import shutil
import argparse
import numpy as np
import time
import ffmpeg
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.optim import lr_scheduler
from torch.autograd import Variable
import torchvision
import os

from .extract_features import I3DFeaturesExtractor

class FeatureExtraction:
    def __init__(self, datasetpath="samplevideos/", outputpath="output", 
                 pretrainedpath="pretrained/i3d_r50_kinetics.pth",
                 frequency=16, batch_size=20, sample_mode="oversample"):
        self.datasetpath = datasetpath
        self.outputpath = outputpath
        self.pretrainedpath = pretrainedpath
        self.frequency = frequency
        self.batch_size = batch_size
        self.sample_mode = sample_mode
    @staticmethod
    def generate(datasetpath="samplevideos/", outputpath="output",
                 pretrainedpath="pretrained/i3d_r50_kinetics.pth", 
                 frequency=16, batch_size=20, sample_mode="oversample", multiplefiles = True):
        '''
        Processing to turn an input video into a i3d features numpy file.
        Arg:
          outputpath (str): path to the directory saving the i3d generated output feature files.
          datasetpath (str): path to the directory placing the videos that need to be converted.
          pretrainedpath (str): path to the Resnet-50 i3d pretrained model.
            If the pretrained file is not existed, the file will be downloaded online and converted.
          frequency (int=16): number of chunks = total frames / frequency
          batch_size (int=20): number of batches = number of chunks / batch_size
          sample_mode (str): if the mode is 'oversample', each 1 frame will be flipped and cropped
            to become 10 frames.
        Return:
          A set of .npy files in the outputpath.
        '''
        assert os.path.exists(datasetpath), f"Dataset path {datasetpath} does not exist. Please check."
        Path(outputpath).mkdir(parents=True, exist_ok=True)
        temppath = outputpath + "/temp/"
        rootdir = Path(datasetpath)
        extensions = ['.webm', '.avi', '.wmv', '.mp4', '.m4v', '.m4p']
        if multiplefiles:
            # videos = [str(f) for f in rootdir.glob('**/*.avi')]
            videos = [str(f) for ext in extensions for f in rootdir.glob(f'**/*{ext}')]
        else:
            videos = [str(rootdir)]


        with torch.no_grad():
            for video in videos:
                outfilename = Path(outputpath) / (Path(video).stem + ".npy")
                video = Path(video).absolute()
                video = r"{}".format(video).replace('\\', '/')

                startime = time.time()
                if not os.path.exists(outfilename):
                    print("Generating for {0}".format(video))
                    Path(temppath).mkdir(parents=True, exist_ok=True)
                    i3d_extractor = I3DFeaturesExtractor(
                        freq=frequency,
                        sample_mode=sample_mode,
                        batch_size=batch_size,
                        pretrainedpath=pretrainedpath
                    )
                    features = i3d_extractor.run(video_path=video, frames_dir=temppath, sample_mode=sample_mode)

                    # Save features
                    np.save(outfilename, features)
                    print("Obtained features of size: ", features.shape)
                    shutil.rmtree(temppath)
                print("done in {0}.".format(time.time() - startime))

# if __name__ == '__main__':
# 	parser = argparse.ArgumentParser()
# 	parser.add_argument('--datasetpath', type=str, default="samplevideos/")
# 	parser.add_argument('--outputpath', type=str, default="output")
# 	parser.add_argument('--pretrainedpath', type=str, default="pretrained/i3d_r50_kinetics.pth")
# 	parser.add_argument('--frequency', type=int, default=16)
# 	parser.add_argument('--batch_size', type=int, default=20)
# 	parser.add_argument('--sample_mode', type=str, default="oversample", help='center_crop or oversample')
# 	args = parser.parse_args()
# 	FeatureExtraction.generate(args.datasetpath, str(args.outputpath), args.pretrainedpath, args.frequency, args.batch_size, args.sample_mode)
