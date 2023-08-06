from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'A camera package that allows you to take photos with just a few lines of code'
LONG_DESCRIPTION = 'A camera package that allows you to take photos, look at photos, and add filters with some basic code'

# Setting up
setup(
    name="camera.py",
    version=VERSION,
    author="Max Keller",
    author_email="max_max_123@icloud.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['opencv-python', 'pyautogui', 'os'],
    keywords=['python', 'camera'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)