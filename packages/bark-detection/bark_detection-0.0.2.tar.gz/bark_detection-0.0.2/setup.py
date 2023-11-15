from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Package for bark detection in audio file'

# Setting up
setup(
    name="bark_detection",
    version=VERSION,
    author="jgab",
    #author_email="<mail@neuralnine.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    package_data={'bark_detection': ['model/bark_detection.keras']},
    install_requires=['librosa==0.10.1','tensorflow==2.13.0'],
    keywords=['python', 'ML', 'bark', 'detection'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
    ]
)