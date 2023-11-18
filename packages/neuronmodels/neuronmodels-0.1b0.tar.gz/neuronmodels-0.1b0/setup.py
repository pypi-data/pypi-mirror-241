from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.1b'
DESCRIPTION = 'Neural Network base models'
LONG_DESCRIPTION = 'A package that allows you to simulate Pitts-Mcculloch neuron , A back propogation network, and a perceptron model.For more info go to https://github.com/Mosbius/Neuronmodels'

# Setting up
setup(
    name="neuronmodels",
    version=VERSION,
    author="Mosbius(Kaushik Aadhithya Ch)",
    author_email="<strikerlight85@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy'],
    keywords=['MP Neuron','Perceptron','Backpropogation network','Neural networks models'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)