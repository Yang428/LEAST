from pytracking.evaluation import Tracker, VOTDataset, TrackingNetDataset, GOT10KDatasetTest, VOT16Dataset, VOT18Dataset, VOT19Dataset

########## Coding by Yang 2020.10 ######## run experiments on benchmarks #####################################
def got10k():
    # Run experiment on the Got10k dataset
    trackers = [Tracker('segm', 'default_params')]

    dataset = GOT10KDatasetTest()
    return trackers, dataset      

def trackingnet():
    # Run experiment on the TrackingNet dataset
    trackers = [Tracker('segm', 'default_params')]

    dataset = TrackingNetDataset()
    return trackers, dataset    

def vot2016():
    # Run unsupervised experiment on the VOT2016 dataset
    trackers = [Tracker('segm', 'default_params')]

    dataset = VOT16Dataset()
    return trackers, dataset  

def vot2018():
    # Run unsupervised experiment on the VOT2018 dataset
    trackers = [Tracker('segm', 'default_params')]

    dataset = VOT18Dataset()
    return trackers, dataset  

def vot2019():
    # Run unsupervised experiment on the VOT2018 dataset
    trackers = [Tracker('segm', 'default_params')]

    dataset = VOT18Dataset()
    return trackers, dataset  
