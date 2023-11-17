from torch.utils.data import Dataset
from pycocotools.coco import COCO
from pathlib import Path
from SoiUtils.datasets.base import ImageDetectionSample,Detection
import cv2 as cv
class ImageDetectionDataset(Dataset):
    ANNOTATION_FILE_NAME = 'annotations.json'
    FRAMES_DIR_NAME = "frames"
    BBOX_FORMAT = 'coco'

    def __init__(self,dataset_root_dir:str, transforms = None):
        super().__init__()
        self.dataset_root_dir = Path(dataset_root_dir)
        all_dataset_info = COCO(self.dataset_root_dir/ImageDetectionDataset.ANNOTATION_FILE_NAME)
        self.image_info = all_dataset_info.imgs
        self.imgToAnns = all_dataset_info.imgToAnns
        self.transforms = transforms

    def __getitem__(self, index:int) -> ImageDetectionSample:
        image_file_path = self.dataset_root_dir/self.image_info[index]['file_name']
        image = cv.imread(image_file_path)
        detections = [Detection.load_generic_mode(bbox=detection_annotation['bbox'],cl=detection_annotation['category_id'],
                                                  mode =ImageDetectionDataset.BBOX_FORMAT, image_size=image.shape[:2][-1])
                       for detection_annotation in self.imgToAnns[index]]


        image_detection_sample = ImageDetectionSample(image=image,detections=detections)

        if self.transforms is not None:
            item = self.transforms(image_detection_sample)
        
        else:
            item = image_detection_sample
        
        return item
    

class ImageDetectionDatasetCollection(Dataset):
    def __init__(self,collection_root_dir,**kwargs) -> None:
        super().__init__()
        self.collection_root_dir = Path(collection_root_dir)
        self.collection_items_root_dirs = [f for f in self.collection_root_dir.iterdir if f.is_dir()]
        self.kwargs = kwargs
    
    def __getitem__(self, index:int) -> ImageDetectionDataset:
        
        return ImageDetectionDataset(self.collection_items_root_dirs[index],**self.kwargs) 


