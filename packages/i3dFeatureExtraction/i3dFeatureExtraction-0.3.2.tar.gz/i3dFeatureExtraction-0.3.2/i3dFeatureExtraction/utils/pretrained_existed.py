######IMPORT PACKAGES#######
import os, re
import requests
import glob
from .convert_weights import convert_weights

def is_weight_existed(path_to_pretrained = './pretrained/') -> bool:
        '''
        Check if any i3d pretrained weight is existed and ending with .pth
        If existed, return True. Else False.
        Coded by HaoPV8. 
        '''
        # find the files ending with .pth extension
        pth_ext_found = glob.glob(path_to_pretrained + '/*.pth') 
        if pth_ext_found and os.path.isfile(pth_ext_found[0]):
            i3d_pretrained_out = pth_ext_found[0]
            print("Weight existed:{0}".format(i3d_pretrained_out))
            return True
        print("Weight not existed!")
        return False        
        

def get_pretrained_pkl_weights(path_to_pretrained = './pretrained') -> None:
        """
        Download the i3d features pretrained pkl file from nonlocal source.
        Args: 
            path_to_pretrained (str): path to the directory
        Return the path to .pkl pretrained weight.
        """        
        pretrained_path = os.path.join(os.getcwd(),re.sub("/|\.","", path_to_pretrained))
        # find the files ending with .pth extension
        pkl_ext_found = glob.glob(pretrained_path + '/*.pkl') 
        if pkl_ext_found and os.path.isfile(pkl_ext_found[0]):
            # found file? >> return path to file
            print("Found {}\n".format(pkl_ext_found[0]), "-"*20)
            return pkl_ext_found[0]
        
        # if i3d_baseline_32x2_IN_pretrain_400k.pkl not here, download it
        i3dpretrain_pkl = 'i3d_baseline_32x2_IN_pretrain_400k.pkl'
        print("-"*50, "\n{} not detected! Start downloading...\n".format(i3dpretrain_pkl))
        if not os.path.exists(pretrained_path):
              os.makedirs(pretrained_path)
        pretrained_path = os.path.join(pretrained_path, i3dpretrain_pkl)
        url = 'https://dl.fbaipublicfiles.com/video-nonlocal/'+i3dpretrain_pkl
        r = requests.get(url, verify=False)
        open(pretrained_path, 'wb').write(r.content)
        print("Done downloading {0}!\n".format(i3dpretrain_pkl), "-"*50)
        return glob.glob(os.path.dirname(pretrained_path) + '/*.pkl')[0]

def get_pth_weight(path_to_pretrained = './pretrained/') -> str:
        """
        Check the weight existed. If False, convert weight from pkl.
        Args: 
            path_to_pretrained (str): path to the directory
        Return the absolute path to .pth pretrained weight.
        """
        if not is_weight_existed(path_to_pretrained):
            # get path to pkl weight
            pkl_weight = get_pretrained_pkl_weights(path_to_pretrained)            
            convert_weights(pkl_weight)
            weight_found = glob.glob(os.path.dirname(pkl_weight) + '/*.pth')
            weight_file_path = os.path.join(os.path.dirname(pkl_weight), weight_found[0])
            return os.path.abspath(weight_file_path)
        weight_found = glob.glob(path_to_pretrained + '/*.pth')[0]
        weight_file_path = os.path.abspath(weight_found)
        return weight_file_path

# if __name__=='__main__':
#       print("--",get_pth_weight())