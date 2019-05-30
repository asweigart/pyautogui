import re
from setuptools import setup

# Load version from module (without loading the whole module)
with open('pyautogui/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

# Read in the README.md for the long description.
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='PyAutoGUI',
    version=version,
    url='https://github.com/asweigart/pyautogui',
    author='Al Sweigart',
    author_email='al@inventwithpython.com',
    description=('A cross-platform module for GUI automation for human beings. '
                 'Control the keyboard and mouse from a Python script.'),
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='BSD',
    packages=['pyautogui'],
    test_suite='tests',
    install_requires=['pymsgbox', 'PyTweening>=1.0.1', 'Pillow', 'pyscreeze>=0.1.21', 'pygetwindow>=0.0.5'],
    keywords="gui automation test testing keyboard mouse cursor click press keystroke control",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ],
)
