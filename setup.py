from setuptools import setup


setup(
    name='PyAutoGUI',
    version=__import__('pyautogui').__version__,
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