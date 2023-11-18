from distutils.core import setup
from setuptools import find_packages
import setuptools

setup(
    name='kalapaocr',
    version='0.0.5',
    license='MIT',
    description='Kalapa Challenge OCR',
    author='HyphenOCR',
    author_email='hieubkls98@gmail.com',
    url='https://github.com/tranbaohieu/ocr_inference_onnx',
    download_url='https://github.com/tranbaohieu/ocr_inference_onnx/archive/dev-0.0.1.tar.gz',
    keywords=['Handwriting', 'Vietnamese', 'OCR'],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"
)