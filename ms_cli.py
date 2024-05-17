import os
import sys
import argparse
from PIL.ExifTags import Base, GPS, Interop, IFD, LightSource
from PIL import Image

class MetaSpoof:
    """Alters meta data found in photos.
    """
    images: list = list()
    supported_extensions = [
        "bmp",
        "gif",
        "jpeg",
        "png",
        "webp"
    ]
    def __init__(
        self,
        path: str,
        remove_all: bool,
        randomize_all: bool,
        remove_gps: bool,
        remove_tags: bool,
        remove_gps_tags: bool
        ) -> None:
        self.path = os.path.realpath(path)

    def __get_images(self) -> None:
        """Gets all image files names.
        """
        if os.path.isdir(self.path):
            images = os.listdir(self.path)
        elif os.path.isfile(self.path):
            images.append(os.path.basename(self.path))
        else:
            print("Path is neither file nor dir")
            exit(1)
    
    def __make_copy(self) -> None:
        
