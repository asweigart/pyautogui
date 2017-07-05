import os
from setuptools import setup


__version__ = ""
version_file = os.path.join(os.path.split(__file__)[0], "pyautogui", "_version.py")
with open(version_file) as module:
    # execute the code in version.py to populate __version__ variable
    # this way, a race condition on sdist or install is avoided
    exec(compile(module.read(), version_file, 'exec'))

setup(
    name='PyAutoGUI',
    version=__version__,
    url='https://github.com/asweigart/pyautogui',
    author='Al Sweigart',
    author_email='al@inventwithpython.com',
    description=('A cross-platform module for GUI automation for human beings. '
                 'Control the keyboard and mouse from a Python script.'),
    license='BSD',
    packages=['pyautogui'],
    test_suite='tests',
    install_requires=['pymsgbox', 'PyTweening>=1.0.1', 'Pillow', 'pyscreeze'],
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
