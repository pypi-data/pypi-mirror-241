from setuptools import setup
import os,glob
requires = [
    'cffi==1.15.1',
    'cryptography==41.0.3',
    'pycparser==2.21',
    'beautifulsoup4==4.12.2',
    'lxml==4.9.3',
    'requests==2.31.0',
    'easy-db==0.9.15',
    'hcloud==1.26.0',
    'cloudflare==2.11.6'


]

packages = [ '/'.join(i.split('/')[-2:]) for i in glob.glob('./starco/*') if os.path.isdir(i)]
# packages =['/'+i for i in packages]
setup(
    name = 'Starco',
    version='2.3.1',
    author='Mojtaba Tahmasbi',
    packages=packages,
    include_dirs=packages,
    install_requires=requires,
)