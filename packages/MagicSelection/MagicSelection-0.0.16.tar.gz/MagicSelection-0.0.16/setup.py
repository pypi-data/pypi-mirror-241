### find packages find sub-packages if you have 
from setuptools import find_packages, setup
import os 
import io 

def read(*paths, **kwargs):
    """Read the contents of a text file safely."""

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content

def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]

setup(
    name = 'MagicSelection',
    version = "0.0.16", 
    description = 'feature selection method with support for combined features' , 
    long_description= read('README.md'), ### a readme file 
    long_description_content_type = 'text/markdown',
    author= 'Di Wu',
    author_email= 'wudi1629@gmail.com',
    maintainer= 'Di Wu', 
    maintainer_email= 'wudi1629@gmail.com',
    download_url= 'https://github.com/dwu12/feature_selection',
    url = 'https://github.com/dwu12/feature_selection', 
    packages = find_packages(exclude = ['tests','.github']), 
    install_requires = read_requirements('requirements.txt'), 
    extras_require = {}, 
    classifiers=[],
    license= 'MIT',
    keywords= [],
    package_data= {},
    entry_points = {} #{'console_scripts':['feature_selection = main']}
)