# -*- coding: utf-8 -*-
# @Created : DOLW 
# @Time    : 2021/4/17 14:24
# @Project : demo
# @FileName: setup.py
# @Software: PyCharm
# Copyright (c) 2021 DOLW. All rights reserved.


import setuptools
import os
import shutil


def clean_dir(Dir):
    if os.path.isdir(Dir):
        paths = os.listdir(Dir)
        for path in paths:
            filePath = os.path.join(Dir, path)
            if os.path.isfile(filePath):
                os.remove(filePath)
            elif os.path.isdir(filePath):
                if filePath[-4:].lower() == ".svn".lower():
                    continue
                shutil.rmtree(filePath, True)
        os.rmdir(Dir)
    return True


if os.path.exists('dist'):
    clean_dir('dist')

readme = open('README.rst', 'r', encoding='utf-8')
README_TEXT = readme.read()
readme.close()

setuptools.setup(
    name="itaxs",
    version="0.0.0.1",
    author="DOWL",
    author_email="1298528585@qq.com",
    maintainer='DOWL',
    maintainer_email="1298528585@qq.com",
    description='深圳跨税云公司中用到的函数封装',
    long_description=README_TEXT,
    long_description_content_type="text/markdown",
    url="https://www.itaxs.com/",
    packages=setuptools.find_packages(exclude=[".tests", ".tests.", "tests.", "tests"]),
    python_requires='>=3.6',
    platforms='windows10',
    install_requires=[
        "python-utils==2.5.6",
        'aiohttp==3.7.4post0',
        'APScheduler==3.7.0',
        'bs4==0.0.1',
        'click==7.1.2',
        'loguru==0.5.3',
        'lxml==4.6.2',
        'openpyxl==3.0.7',
        'opencv-python==4.5.1.48',
        'node==0.9.25',
        'PyExecJS==1.5.1',
        'pywin32==300',
        'pypiwin32==223',
        'pillow==8.1.2',
        'requests==2.25.1',
        'selenium==3.141.0',
        'qrcode==6.1',
        'wxPython==4.1.1',
        'win32-setctime==1.0.3',
        'pypinyin==0.41.0'
    ]
)
