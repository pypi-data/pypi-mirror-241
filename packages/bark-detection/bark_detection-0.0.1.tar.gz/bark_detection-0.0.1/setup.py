from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Package for bark detection in audio file'

# Setting up
setup(
    name="bark_detection",
    version=VERSION,
    author="jgab",
    #author_email="<mail@neuralnine.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'ML', 'bark', 'detection'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
    ]
)