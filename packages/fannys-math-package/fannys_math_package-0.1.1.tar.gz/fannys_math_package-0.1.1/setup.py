from setuptools import setup
from fannys_math_package import __version__

setup(
    name='fannys_math_package',
    version=__version__,
    author='Fanny',
    packages=['fannys_math_package', 'fannys_math_package.test'],
    description='An awesome package that does simple math'
)
