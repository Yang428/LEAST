from pytracking.evaluation import Tracker, TrackingNetDataset, GOT10KDatasetTest

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
