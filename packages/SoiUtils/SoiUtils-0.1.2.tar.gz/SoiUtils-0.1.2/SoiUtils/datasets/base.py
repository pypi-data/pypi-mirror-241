import dataclasses
from pybboxes import BoundingBox
from typing import Union,List
from dataclasses import dataclass
import numpy as np
import torch
from PIL import Image

@dataclass
class Detection:
    bbox: BoundingBox
    cls: Union[str,int] = None
    constructors_of_supported_formats = {'yolo': BoundingBox.from_yolo,'coco':BoundingBox.from_yolo,
                                         'voc':BoundingBox.from_voc,'fiftyone':BoundingBox.from_fiftyone,
                                         'albumentations':BoundingBox.from_albumentations}

    @classmethod
    def load_generic_mode(cls, bbox, cl=None, mode='yolo', **kwargs):
        bbox = Detection.constructors_of_supported_formats[mode](*bbox, **kwargs).to_coco()
        return cls(bbox, cl)
        
@dataclass
class ImageDetectionSample:
    image: Union[np.array, torch.Tensor, Image.Image]
    detections: List[Detection] = None





