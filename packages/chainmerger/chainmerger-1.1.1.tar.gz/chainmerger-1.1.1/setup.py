from setuptools import setup, find_packages

from chainmerger.__version__ import __version__

with open('README.md', 'r') as f:
    long_description = f.read()

from pkg_resources import parse_requirements
install_requires = [str(r) for r in parse_requirements(open('requirements.txt'))]

setup(
    name='chainmerger',
    version=__version__,
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'chainmerger=chainmerger.__main__:main'
        ]
    },
    author='bitdruid',
    author_email='bitdruid@outlook.com',
    description='Merge chainalysis csv files into one report file.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/bitdruid/chainmerger',
)

    