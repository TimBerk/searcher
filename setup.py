import os
from setuptools import setup, find_packages

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='searcher',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='GNU General Public License v3.0',
    description='Search program use several search system',
    url='https://github.com/TimBerk/searcher',
    author='Tatiana Lysak',
    author_email='lysak-tatiana2501@ya.ru',
    keywords=['python', 'parse', 'json', 'csv'],
    classifiers=[],
    entry_points={
        'console_scripts': [
            'searcher = searcher.cli:main',
        ]
    },
    install_requires=['requests', 'bs4']
)
