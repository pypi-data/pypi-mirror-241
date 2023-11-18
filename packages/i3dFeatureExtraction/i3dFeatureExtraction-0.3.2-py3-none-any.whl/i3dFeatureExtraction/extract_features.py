import os, cv2
import numpy as np
import torch
from natsort import natsorted
from PIL import Image
from i3dFeatureExtraction.models.resnet import i3_res50
from torch.autograd import Variable
# import ffmpeg
from i3dFeatureExtraction.utils.pretrained_existed import get_pth_weight


def extract_frames(video_path, temppath, width=640, height=480):
    if not os.path.exists(temppath):
        os.makedirs(temppath)

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    # Initialize the frame counter
    frame_count = 0
    # Loop over all frames
    while cap.isOpened():
        # Read a new frame
        ret, frame = cap.read()

        # If the frame was not successfully read, break the loop
        if not ret:
            break

        # Resize the frame to desired width and height
        frame = cv2.resize(frame, (width, height))

        # Save the frame as image
        filename = os.path.join(temppath, f"{frame_count:06d}.jpg")
        cv2.imwrite(filename, frame)

        # Increment the frame counter
        frame_count += 1

    # Release the video capture object
    print("Frames extraction completed!")
    cap.release()

class I3DFeaturesExtractor:
    def __init__(self, freq=16, sample_mode='oversample',
                 batch_size=20, 
                 pretrainedpath = "pretrained/i3d_r50_kinetics.pth"):
        os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.frequency = freq  # default value, can be adjusted
        self.batch_size = batch_size  # default value, can be adjusted
        self.pretrainedpath = pretrainedpath
        self.model = self._load_i3d_model()

        import cv2


    
    @staticmethod
    def resize_input(video_path, size=None, temppath='temp/'):
        if not size:
            size = (256, 256)
        
        print("... video path: ", video_path)
        print("... resizing frames to size {} ...".format(size))

        width, height = size[0], size[1] 

        return extract_frames(video_path, temppath, width, height)
        # return ffmpeg.input(video_path). \
        #   filter('scale', width, height).\
        #   output('{}%d.jpg'.format(temppath),start_number=0, format='image2', vcodec='mjpeg').\
        #     global_args('-loglevel', 'quiet').run()


    def _load_i3d_model(self):
        # code to load the I3D model
        print("-"*50)
        print("... Loading i3d model ...")
        weight_file_path = get_pth_weight(os.path.dirname(self.pretrainedpath))
        model = i3_res50(num_classes=400, pretrainedpath=self.pretrainedpath)
        model.load_state_dict(torch.load(weight_file_path))
        if self.device == 'cuda:0':
          print("CUDA available.")
          model.cuda()
        model.train(False) # Set model to evaluate mode
        print("... i3d model loaded ...")
        print("-"*50)
        return model

    def _load_rgb_frames(self, frames_dir, frame_indices):
        batch_data = np.zeros(frame_indices.shape + (256, 340, 3))
        for i in range(frame_indices.shape[0]):
            for j in range(frame_indices.shape[1]):
                frame_path = os.path.join(frames_dir, self.rgb_files[frame_indices[i][j]])
                data = Image.open(frame_path).resize((340, 256), Image.ANTIALIAS)
                data = np.array(data).astype(float)
                data = (data * 2 / 255) - 1
                assert (data.max() <= 1.0)
                assert (data.min() >= -1.0)
                batch_data[i, j, :, :, :] = data
        return batch_data

    def _oversample_data(self, data):
        data_flip = np.array(data[:,:,:,::-1,:])

        data_1 = np.array(data[:, :, :224, :224, :])
        data_2 = np.array(data[:, :, :224, -224:, :])
        data_3 = np.array(data[:, :, 16:240, 58:282, :])
        data_4 = np.array(data[:, :, -224:, :224, :])
        data_5 = np.array(data[:, :, -224:, -224:, :])

        data_f_1 = np.array(data_flip[:, :, :224, :224, :])
        data_f_2 = np.array(data_flip[:, :, :224, -224:, :])
        data_f_3 = np.array(data_flip[:, :, 16:240, 58:282, :])
        data_f_4 = np.array(data_flip[:, :, -224:, :224, :])
        data_f_5 = np.array(data_flip[:, :, -224:, -224:, :])

        data_oversampled = [data_1, data_2, data_3, data_4, data_5,
            data_f_1, data_f_2, data_f_3, data_f_4, data_f_5]
        return data_oversampled

    def _forward_batch(self, b_data):
        b_data = b_data.transpose([0, 4, 1, 2, 3])
        b_data = torch.from_numpy(b_data).to(self.device)
        with torch.no_grad():
            b_data = Variable(b_data).float()
            inp = {'frames': b_data}
            features = self.model(inp)
        return features.cpu().numpy()

    def run(self,video_path, frames_dir, sample_mode='oversample'):
        assert (sample_mode in ['oversample', 'center_crop'])
        size = (340,256) if sample_mode != 'oversample' else (256, 256)
        self.resize_input(video_path, size=size, temppath=frames_dir)
        self.rgb_files = natsorted([i for i in os.listdir(frames_dir)])
        frame_cnt = len(self.rgb_files)
        assert (frame_cnt > 16)  # chunk size
        clipped_length = frame_cnt - 16
        clipped_length = (clipped_length // self.frequency) * self.frequency
        frame_indices = []
        for i in range(clipped_length // self.frequency + 1):
            frame_indices.append([j for j in range(i * self.frequency, i * self.frequency + 16)])
        frame_indices = np.array(frame_indices)
        chunk_num = frame_indices.shape[0]
        batch_num = int(np.ceil(chunk_num / self.batch_size))
        frame_indices = np.array_split(frame_indices, batch_num, axis=0)
        if sample_mode == 'oversample':
            full_features = [[] for i in range(10)]
        else:
            full_features = [[]]
        for batch_id in range(batch_num):
            batch_data = self._load_rgb_frames(frames_dir, frame_indices[batch_id])
            if sample_mode == 'oversample':
                batch_data = self._oversample_data(batch_data)
                for i in range(10):
                    assert (batch_data[i].shape[-2] == 224)
                    assert (batch_data[i].shape[-3] == 224)
                    temp = self._forward_batch(batch_data[i])
                    full_features[i].append(temp)
            elif sample_mode == 'center_crop':
                batch_data = batch_data[:, :, 16:240, 58:282, :]
                assert (batch_data.shape[-2] == 224)
                assert (batch_data.shape[-3] == 224)
                temp = self._forward_batch(batch_data)
                full_features[0].append(temp)
        full_features = [np.concatenate(i, axis=0) for i in full_features]
        full_features = [np.expand_dims(i, axis=0) for i in full_features]
        full_features = np.concatenate(full_features, axis=0)
        full_features = full_features[:, :, :, 0, 0, 0]
        full_features = np.array(full_features).transpose([1, 0, 2])
        return full_features

# import os
# os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"

# import numpy as np
# import torch
# from natsort import natsorted
# from PIL import Image
# from torch.autograd import Variable


# def load_frame(frame_file):
#   data = Image.open(frame_file)
#   data = data.resize((340, 256), Image.ANTIALIAS)
#   data = np.array(data)
#   data = data.astype(float)
#   data = (data * 2 / 255) - 1
#   # device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
#   # data = Variable(data.cuda()).float()
#   assert(data.max()<=1.0)
#   assert(data.min()>=-1.0)
#   return data


# def load_rgb_batch(frames_dir, rgb_files, frame_indices):
#   batch_data = np.zeros(frame_indices.shape + (256,340,3))
#   # device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
#   # print("cpu/conda?:", str(device), "\n", "*"*10)
#   for i in range(frame_indices.shape[0]):
#     for j in range(frame_indices.shape[1]):
#       batch_data[i,j,:,:,:] = load_frame(os.path.join(frames_dir, rgb_files[frame_indices[i][j]]))
#   return batch_data


# def oversample_data(data):
# 	data_flip = np.array(data[:,:,:,::-1,:])

# 	data_1 = np.array(data[:, :, :224, :224, :])
# 	data_2 = np.array(data[:, :, :224, -224:, :])
# 	data_3 = np.array(data[:, :, 16:240, 58:282, :])
# 	data_4 = np.array(data[:, :, -224:, :224, :])
# 	data_5 = np.array(data[:, :, -224:, -224:, :])

# 	data_f_1 = np.array(data_flip[:, :, :224, :224, :])
# 	data_f_2 = np.array(data_flip[:, :, :224, -224:, :])
# 	data_f_3 = np.array(data_flip[:, :, 16:240, 58:282, :])
# 	data_f_4 = np.array(data_flip[:, :, -224:, :224, :])
# 	data_f_5 = np.array(data_flip[:, :, -224:, -224:, :])

# 	return [data_1, data_2, data_3, data_4, data_5,
# 		data_f_1, data_f_2, data_f_3, data_f_4, data_f_5]


# def run(i3d, frequency, frames_dir, batch_size, sample_mode):
#   assert(sample_mode in ['oversample', 'center_crop'])
#   print("batchsize", batch_size)
#   chunk_size = 16
#   def forward_batch(b_data):
#     b_data = b_data.transpose([0, 4, 1, 2, 3])
#     b_data = torch.from_numpy(b_data)   # b,c,t,h,w  # 40x3x16x224x224
#     with torch.no_grad():
#       b_data = Variable(b_data).float()
#       inp = {'frames': b_data}
#       features = i3d(inp)
#     return features.cpu().numpy()
  
#   rgb_files = natsorted([i for i in os.listdir(frames_dir)])
#   frame_cnt = len(rgb_files)
#   # Cut frames
#   assert(frame_cnt > chunk_size)
#   clipped_length = frame_cnt - chunk_size
#   clipped_length = (clipped_length // frequency) * frequency  # The start of last chunk
#   frame_indices = [] # Frames to chunks
#   for i in range(clipped_length // frequency + 1):
#     frame_indices.append([j for j in range(i * frequency, i * frequency + chunk_size)])
#   frame_indices = np.array(frame_indices)
#   chunk_num = frame_indices.shape[0]
#   batch_num = int(np.ceil(chunk_num / batch_size))    # Chunks to batches
#   frame_indices = np.array_split(frame_indices, batch_num, axis=0)
  
#   if sample_mode == 'oversample':
#     full_features = [[] for i in range(10)]
#   else:
#     full_features = [[]]
    
#   for batch_id in range(batch_num): 
#     batch_data = load_rgb_batch(frames_dir, rgb_files, frame_indices[batch_id])
#     if(sample_mode == 'oversample'):
#       batch_data_ten_crop = oversample_data(batch_data)
#       for i in range(10):
#         assert(batch_data_ten_crop[i].shape[-2]==224)
#         assert(batch_data_ten_crop[i].shape[-3]==224)
#         temp = forward_batch(batch_data_ten_crop[i])
#         full_features[i].append(temp)
#       3
#     elif(sample_mode == 'center_crop'):
#       batch_data = batch_data[:,:,16:240,58:282,:]
#       assert(batch_data.shape[-2]==224)
#       assert(batch_data.shape[-3]==224)
#       temp = forward_batch(batch_data)
#       full_features[0].append(temp)
      
#   full_features = [np.concatenate(i, axis=0) for i in full_features]
#   full_features = [np.expand_dims(i, axis=0) for i in full_features]
#   full_features = np.concatenate(full_features, axis=0)
#   full_features = full_features[:,:,:,0,0,0]
#   full_features = np.array(full_features).transpose([1,0,2])
#   return full_features
