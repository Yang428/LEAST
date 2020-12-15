# LEAST Tracker

The main codes of the LEAST tracker will be available as soon as possible.

## Running Environments
* Pytorch 1.1.0, Python 3.6.12, Cuda 10.0, torchvision 0.3.0, cudatoolkit 10.0, Matlab R2016b.
* Ubuntu 16.04, NVIDIA GeForce GTX 1080Ti.

## Installation
The instrustions have been tested on an Ubuntu 16.04 system. In case of issues, we refer to [D3S](https://github.com/alanlukezic/d3s) and [pytracking](https://github.com/visionml/pytracking).

#### Clone the GIT repository
'''bash
git clone https://github.com/Yang428/LEAST.git.
'''

#### Install dependent libraries
Run the installation script 'install.sh' to install all dependencies. We refer to [this link](https://github.com/visionml/pytracking/blob/master/INSTALL.md) for step-by-step instructions.
'''bash
bash install.sh conda_install_path pytracking
'''

#### Download the pre-trained networks
You can download the models from the [Baidu cloud link](https://pan.baidu.com/s/11kn8IyxN0AJ8D0C780FLUg), the extraction code is lxa4. Then put the model files 'SegmNet.pth.tar and SegmNet_maskInitNet.pth.tar' to the subfolder 'pytracking/networks'.

## Testing the tracker
1) Change the following paths to you own paths.
'''bash
Network path: pytracking/parameters/segm/default_params.py  params.segm_net_path.
Results path: pytracking/evaluation/local.py  settings.network_path, settings.results_path, dataset_path.
'''
2) Run the LEAST tracker on VOT19 sequences.
'''bash
cd pytracking
python run_tracker.py segm default_params --dataset vot19 --sequence ants1 --debug 1
'''
3) Run the LEAST tracker on Got10k and TrackingNet datasets.
'''bash
cd pytracking
python run_experiment.py myexperiments got10k
python run_experiment.py myexperiments trackingnet
'''

## Evaluation on VOT2019 using Matlab R2016b
We provide a VOT Matlab toolkit integration for the LEAST tracker. There is the tracker_D3S.m Matlab file in the 'pytracking/utils', which can be connected with the toolkit. It uses the 'pytracking/vot_wrapper.py' script to integrate the tracker to the toolkit.

## Training the networks
The LEAST tracker is pre-trained for segmentation task only on the YouTube VOS dataset. Download the VOS training dataset (2018 version) and copy the files vos-list-train.txt and vos-list-val.txt from ltr/data_specs to the train directory of the VOS dataset. Set the vos_dir variable in ltr/admin/local.py to the VOS train directory on your machine. Download the bounding boxes from this link and copy them to the sequence directories. Run training by running the following command:
1) Download the training dataset from [this link](https://youtube-vos.org/challenge/2018/).

2) Change the following paths to you own paths.
'''bash
Workspace: ltr/admin/local.py  workspace_dir.
Dataset: ltr/admin/local.py  vos_dir.
'''
2) Run training.
'''bash
cd ltr
python run_training.py segm segm_default
'''


## Acknowledgement
This a modified version of [D3S](https://github.com/alanlukezic/d3s) tracker which is based on the [pytracking](https://github.com/visionml/pytracking) framework. We would like to thank the author Martin Danelljan of pytracking and the author Alan Lukežič of D3S.
