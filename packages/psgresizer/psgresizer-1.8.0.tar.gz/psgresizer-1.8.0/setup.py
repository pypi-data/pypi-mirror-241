

import setuptools

def readme():
    try:
        with open('README.md') as f:
            return f.read()
    except IOError:
        return ''


setuptools.setup(
name="psgresizer",
version="1.8.0",
author="PySimpleGUI",
author_email="PySimpleGUI@PySimpleGUI.org",
install_requires=["PySimpleGUI","Pillow"],
description="PySimpleGUI demo tool and utility to resize your images and encode them to Bas64 format.",
long_description=readme(),
long_description_content_type="text/markdown",
license='Free To Use But Restricted',
keywords="GUI UI PySimpleGUI tkinter psgresizer base64 resize",
url="https://github.com/PySimpleGUI",
packages=setuptools.find_packages(),
python_requires=">=3.6",
classifiers=[
"Development Status :: 5 - Production/Stable",
"Framework :: PySimpleGUI",
"Framework :: PySimpleGUI :: 4",
"Framework :: PySimpleGUI :: 5",
"Intended Audience :: Developers",
"License :: Free To Use But Restricted",
"Operating System :: OS Independent",
"Programming Language :: Python :: 3",
"Programming Language :: Python :: 3.6",
"Programming Language :: Python :: 3.7",
"Programming Language :: Python :: 3.8",
"Programming Language :: Python :: 3.9",
"Programming Language :: Python :: 3.10",
"Programming Language :: Python :: 3.11",
"Programming Language :: Python :: 3.12",
"Topic :: Multimedia :: Graphics",
"Topic :: Software Development :: User Interfaces",
],
package_data={"": 
["psgresizer.ico"]
        },
entry_points={'gui_scripts': [
"psgresizer=psgresizer.psgresizer:main",
    ]
    },
)

