![PyPi Version](https://img.shields.io/pypi/v/mr-wolf-weather-forecast-chart.svg)
![PyPi Status](https://img.shields.io/pypi/status/mr-wolf-weather-forecast-chart)
![PyPI Downloads](https://img.shields.io/pypi/dm/mr-wolf-weather-forecast-chart)
![PyPI License](https://img.shields.io/pypi/l/mr-wolf-weather-forecast-chart?color=yellow)
![Python Versions](https://img.shields.io/pypi/pyversions/mr-wolf-weather-forecast-chart.svg)

Command line tool for downloading the weather forecast charts from http://wetter.com as png file.



# Requirements & Compatibility

* Python >=3.6
* selenium
* geckodriver



# Installation

You can easily install this tool using pip:

    pip install mr-wolf.weather-forecast-chart



# Shell Usage

    usage: mr-wolf-weather-forecast-chart [-h] [-o FILENAME]
                                          [--tomorrow | -d {3,7,16}]
                                          zip_code

    Command line tool for downloading the weather forecast charts from
    http://wetter.com as png file.

    positional arguments:
      zip_code              The zip code for the location for which you want to
                            get the chart data

    optional arguments:
      -h, --help            show this help message and exit
      -o FILENAME, --output-file FILENAME
                            save the chart in FILENAME (default: ./weather_forecast_chart.png)
      --tomorrow            get forecast chart for tomorrow
      -d {3,7,16}, --days {3,7,16}
                            get forecast chart for the next {3,7,16} days
