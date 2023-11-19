import setuptools
from pathlib import Path

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements_file = Path('requirements.txt')
if requirements_file.exists():
    install_requires = requirements_file.read_text('utf-8').splitlines()
else:
    install_requires = []

setuptools.setup(
    name="SOMENDER",
    version="1.1",
    author="Zhiyuan Yuan",
    author_email="zhiyuan@fudan.edu.cn",
    description="TBD",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/yuanzhiyuan/SOMENDER',    
    packages=['MENDER'], #setuptools.find_packages(),
    install_requires=[
        l.strip() for l in Path('requirements.txt').read_text('utf-8').splitlines()
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9.0',
)
