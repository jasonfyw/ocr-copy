import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text(encoding = 'utf-8', errors = 'ignore')

setup(
    name="ocr-copy",
    version="0.1.0",
    description="A program that copies text by using Tesseract's OCR engine on a selected portion of the screen",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jasonfyw/ocr-copy",
    author="Jason Wang",
    author_email="jasonwang0610@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["pynput", "pyglet==1.3.0", "pyscreenshot", "pytesseract", "pyperclip", "numpy", "Pillow"],
    download_url="https://github.com/jasonfyw/ocr-copy/archive/v0.1.0.tar.gz",
    entry_points={
        'gui_scripts': [
            'ocr-copy = ocrcopy.__main__:main'
        ]
    }
)