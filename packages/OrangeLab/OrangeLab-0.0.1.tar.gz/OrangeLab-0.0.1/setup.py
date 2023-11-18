from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='OrangeLab',
  version='0.0.1',
  description='The Python module developed for the Orange Python Tool Plugin serves a dual purpose, providing functionalities for both image processing using OpenCV and the generation of synthetic datasets through the Faker library.',
  long_description_content_type='text/markdown',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://www.pythonanywhere.com/',
  author='NagiPragalathan',
  author_email='nagipragalathan@gmail.com',
  license='MIT', 
  classifiers=classifiers,     
  keywords = ["Image Processing","Computer Vision","Color Analysis","Color Design","Color Palette","Image Enhancement","Image Filters","Feature Extraction","Pattern Recognition","Color Manipulation","Image Segmentation","Color Spaces","Histogram Equalization","Edge Detection","Contrast Adjustment","Saturation Control","Hue Adjustment","Color Grading","Image Restoration","Color Correction","Digital Image Processing","Visual Perception","Color Harmony","Color Psychology","Image Effects","Texture Synthesis","Color Transfer","Image Compression","Color Quantization","Optical Character Recognition (OCR)","Machine Learning for Image Processing","Deep Learning in Image Processing","Neural Networks and Fuzzy Logic","Robotics and Autonomous Vehicles","Medical Imaging","Microscopy","Remote Sensing","Astronomy","Geological Surveying"],       
  packages=find_packages(),
  install_requires=[
        'numpy>=1.18.0',
        'opencv-python>=4.2.0',
        'matplotlib>=3.1.0',
        'Faker>=8.14.0',
        'Pillow>=8.2.0',
        'pandas>=1.0.0',
    ] 
)