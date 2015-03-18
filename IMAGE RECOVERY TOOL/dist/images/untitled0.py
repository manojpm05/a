# -*- coding: utf-8 -*-
"""
Created on Fri Dec 05 19:04:16 2014

@author: Hi
"""

import cStringIO
from PIL import Image,TemporaryUploadedFile
import TemporaryUploadedFile
import image

if isinstance(image, TemporaryUploadedFile):
    temp_file = open(image.temporary_file_path(), 'rb+')
    content = cStringIO.StringIO(temp_file.read())
    image = Image.open(content)
    temp_file.close()