import codecs
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.2'
DESCRIPTION = "This package is used for image processing,deep learning,personal learning",  #介绍
LONG_DESCRIPTION = 'pyzjr is a computer vision library that supports both Win and Mac'

setup(
    name="Ipcsvision",    #名字
    version=VERSION,      #版本
    author="DIYUFENG111", #作者
    author_email="2832984935@qq.com",    #作者邮箱
    url='https://github.com/DIYUFENG111',
    description="This package is used for image processing,deep learning,personal learning",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    license='MIT',
    install_requires=[
        "opencv-python",
        "matplotlib",
    ],
    keywords=['python', 'computer vision', 'Ipcsvision', 'windows', 'mac', 'linux'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)