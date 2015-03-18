# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 12:43:23 2014

@author: manom
"""

from distutils.core import setup
import py2exe

setup(
        console=['image recovery tool.py'],
        options = {
            "py2exe": {
                "dll_excludes": ["MSVCP90.dll","OLEAUT32.dll","USER32.dll","SHELL32.dll","KERNEL32.dll","ADVAPI32.dll","WS2_32.dll","GDI32.dll","VERSION.dll","ole32.dll","ntdll.dll","WINMM.dll","MSVCR100.dll","MSVCP100.dll","COMCTL32.dll","msvcrt.dll"]
        }
    }
)