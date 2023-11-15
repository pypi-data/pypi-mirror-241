from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

#with codecs.open(os.path.join(here, "README.txt"), encoding="utf-8") as fh:
    #long_description = "\n" + fh.read()


# Setting up
setup(
    name="hugobio",
    version='1.3',
    author="Hugo Dijkstra",
    author_email="h.dijkstra@student.han.nl",
    description='bio-informatics',
    long_description_content_type="text/markdown",
    long_description='something for bio-informatics',
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'bio-informatics'],
)
