#!/bin/bash
"""
Provides methods to remove exif data from photos.

Classes:
- ExifEdit(): Retrieves photos and removes the exif data.
"""

import os
import sys
import argparse
# from PIL.ExifTags import Base, GPS, Interop, IFD, LightSource
from PIL import Image

class ExifEdit:
    """Retrieves photos and removes the exif data.
    """
    images: list[str] = list()
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

    def __check_path(self) -> bool:
        """Checks if the passed path exists.

        Returns:
            bool: True if the path does exist.
        """
        if os.path.exists(self.path):
            return True
        print(f"{self.path} is not found.")
        sys.exit(1)

    def __get_images(self) -> None:
        """Gets all image files names.
        """
        if os.path.isdir(self.path):
            images = os.listdir(self.path)
        elif os.path.isfile(self.path):
            images.append(os.path.basename(self.path))

    def __check_file_extensions(self) -> None:
        """Drops unsupported file types.
        """
        for file in self.images:
            split_file_name: list = file.split('.')
            if not split_file_name[-1] in self.supported_extensions:
                self.images.remove(file)
                print(f"The extension {split_file_name[-1]} is not supported. Dropping {file}.")

    def __edit_exif(self) -> None:
        """Edits the exif data
        """
        for file in self.images:
            img: Image = Image.open(file)

    def run(self) -> None:
        """Runs the process to retrieve and remove/alter exif data from photos.
        """
        self.__check_path()
        self.__get_images()
        self.__check_file_extensions()
        self.__edit_exif()

if __name__ == "__main__":
    cli = argparse.ArgumentParser()
