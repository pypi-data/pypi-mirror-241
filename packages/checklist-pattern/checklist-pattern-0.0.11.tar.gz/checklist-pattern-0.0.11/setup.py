from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
from setuptools.command.bdist_egg import bdist_egg
from setuptools.command.egg_info import egg_info
from setuptools.command.build_py import build_py

from subprocess import check_call
import sys

import notebook

def enable_visual_interface():
    notebook.nbextensions.install_nbextension_python(
        "checklist.viewer", user=True, overwrite=True)
    notebook.nbextensions.enable_nbextension_python(
        "checklist.viewer")

def enable_visual_interface_shell_cmd(direction):
    sys.path.append(direction)
    enable_visual_interface()
    #"""

class PostDevelopCommand(develop):
    """Pre-installation for development mode."""
    def run(self):
        develop.run(self)
        #enable_visual_interface()
        self.execute(enable_visual_interface_shell_cmd, (self.install_lib,), msg="Running post install task")

class PostInstallCommand(install):
    def run(self):
        #super().do_egg_install()
        install.run(self)
        self.execute(enable_visual_interface_shell_cmd, (self.install_lib,), msg="Running post install task")
        #enable_visual_interface()

setup(name='checklist-pattern',
      version='0.0.11',
      description='Beyond Accuracy: Behavioral Testing of NLP Models with CheckList',
      url='http://github.com/marcotcr/checklist',
      author='Marco Tulio Ribeiro',
      author_email='marcotcr@gmail.com',
      license='MIT',
      packages= find_packages(exclude=['js', 'node_modules', 'tests']),
      install_requires=[
        'numpy>=1.18',
        'spacy>=2.2',
        'munch>=2.5',
        'dill>=0.3.1',
        'jupyter>=1.0',
        'ipywidgets>=7.5',
        'transformers>=2.8',
        'patternfork-nosql-fix',
        'pycountry'
      ],
      cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,

     },
      package_data={'viewer':['static/*'], "data": ["*"], 'checklist': ['data/*', 'data/lexicons/*', 'viewer/static/*']},
      #include_package_data=True,
      zip_safe=False
)
