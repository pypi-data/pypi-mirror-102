from setuptools import setup

with open("README.md") as README:
    long_description = README.read()

setup(
    name='PyPiPythonCodeThemeTest',
    version='1.0.0',
    description='This is a test for PyPi python formatting in markdown based READMEs.',
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Steven Shrewsbury',
    url='https://pypi.python.org/pypi/PyPiPythonCodeThemeTest',
    packages=['placeholder'],
    python_requires='>=3.6',
)
