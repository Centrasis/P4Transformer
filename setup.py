from logging import exception
import os
from shutil import copyfile
from setuptools import setup, find_packages

module_files = [os.path.join(os.path.abspath(os.path.dirname(__file__)), 'modules-pytorch-1.8.1', f) for f in os.listdir(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'modules-pytorch-1.8.1')) if not ("setup.py" in f.lower()) and f.lower().endswith(".py")]

for f in module_files:
    bn = os.path.basename(f)
    target = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'P4Transformer', bn)
    if os.path.exists(target):
        try:
            os.remove(target)
        except Exception:
            pass
    copyfile(f, target)

setup(name='P4Transformer',
      packages=find_packages(),
      version='1.0.0',
      namespace_packages=['P4Transformer'],
      install_requires=[
         'numpy',
         'torch>=1.8.0',
         'torchvision>=0.9.2+cu111',
         'torchaudio>=0.8.2',
         'einops',
         'pointnet2 @ file://localhost/' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'modules-pytorch-1.8.1').replace('\\', '/')
      ],
      cmdclass={},
      author="",
      license='MIT',
      long_description=open('README.md').read(),
      python_requires='>=3.9',
      command_options={}
)