from os import path
from setuptools import find_namespace_packages, setup

from mr_wolf.weather_forecast_chart import __version__


with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='mr-wolf.weather-forecast-chart',
    version=__version__,
    license='AGPLv3+',

    description=('Command line tool for downloading the weather forecast charts from '
                 'http://wetter.com'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://bitbucket.org/stefanbunde/mr-wolf/',

    author='Stefan Bunde',
    author_email='stefanbunde+git@posteo.de',

    python_requires='~=3.6',
    install_requires=[
        'selenium',
    ],

    packages=find_namespace_packages(),

    entry_points={
        'console_scripts': [
            'mr-wolf-weather-forecast-chart=mr_wolf.weather_forecast_chart.main:main',
        ],
    },

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
