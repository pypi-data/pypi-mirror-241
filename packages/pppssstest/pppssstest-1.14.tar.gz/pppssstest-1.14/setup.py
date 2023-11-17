

import setuptools

def readme():
    try:
        with open('README.md') as f:
            return f.read()
    except IOError:
        return ''


setuptools.setup(
name="pppssstest",
version="1.14",
author="author",
author_email="author@email.com",
install_requires=["PySimpleGUI"],
description="Desc here",
long_description=readme(),
long_description_content_type="text/markdown",
license='Free To Use But Restricted',
keywords="pp ss tt",
url="",
packages=setuptools.find_packages(),
python_requires="",
classifiers=[
"Framework :: PySimpleGUI :: 4",
"Framework :: PySimpleGUI :: 5",
"Framework :: PySimpleGUI",
],
package_data={"": 
[""]
        },
entry_points={'gui_scripts': [
"pptest=pppssstest.pppssstest:main",
    ]
    },
)

