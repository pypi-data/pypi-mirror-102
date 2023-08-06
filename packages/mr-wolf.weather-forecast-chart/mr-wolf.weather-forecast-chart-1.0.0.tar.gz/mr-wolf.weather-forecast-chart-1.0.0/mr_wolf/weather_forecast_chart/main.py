import argparse
import os
from urllib.parse import urlparse

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


def main():
    parser = initialize_argument_parser()
    args = parser.parse_args()

    driver = initialize_webdriver()

    weather_chart = WeatherChart(
        driver, args.postal_code, args.output_file, args.tomorrow, args.days
    )

    try:
        weather_chart.make_screenshot()
    except Exception as e:
        print(f'failed - {e}')
        exit(0)
    finally:
        driver.close()


def initialize_argument_parser():
    parser = argparse.ArgumentParser(
        description=('Command line tool for downloading the weather forecast charts '
                     'from http://wetter.com as png file.'),
    )

    parser.add_argument('postal_code', help=('The postal code for the location for which you want '
                                             'to get the chart data'))
    parser.add_argument('-o', '--output-file', metavar='FILENAME',
                        default='./weather_forecast_chart.png',
                        help='save the chart in FILENAME (default: ./weather_forecast_chart.png)')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('--tomorrow', action='store_true',
                       help='get forecast chart for tomorrow')
    group.add_argument('-d', '--days', type=int, choices=[3, 7, 16],
                       help='get forecast chart for the next {3,7,16} days')
    return parser


def initialize_webdriver():
    options = webdriver.firefox.options.Options()
    options.headless = True
    return webdriver.Firefox(options=options, service_log_path=os.path.devnull)


class WeatherChart:
    def __init__(self, driver, postal_code, output_file, tomorrow, days):
        self.driver = driver
        self.postal_code = postal_code
        self.output_file = output_file
        self.tomorrow = tomorrow
        self.days = days

    def make_screenshot(self):
        self.driver.get(f'https://www.wetter.com/suche/?q={self.postal_code}')

        if self.driver.find_element_by_class_name('title').text == 'Die Suche ergab keine Treffer':
            print('Die Suche ergab keine Treffer')
            return

        self._accept_cookies()

        element = self._get_chart_element()
        self.driver.execute_script('arguments[0].scrollIntoView();', element)
        element.screenshot(self.output_file)

    def _accept_cookies(self):
        WebDriverWait(self.driver, 10).until(
            visibility_of_element_located((By.ID, 'cmp-btn-accept'))
        ).click()

    def _get_chart_element(self):
        if self.days is None and self.tomorrow is False:
            return self._get_chart_element_for_the_next_24_hours()
        elif self.days is None:
            return self._get_chart_element_for_tomorrow()
        else:
            return self._get_chart_element_for_serveral_days()

    def _get_chart_element_for_the_next_24_hours(self):
        self.driver.find_element_by_link_text('Diagramm').click()
        element = self.driver.find_element_by_id('vhs-detail-diagram')
        for child in element.find_elements_by_tag_name('tr')[11:]:
            self._remove_child_element(child)
        return element

    def _get_chart_element_for_tomorrow(self):
        self.driver.get(f'https://www.wetter.com/wetter_aktuell/wettervorhersage/morgen/'
                        f'{urlparse(self.driver.current_url).path}#diagramm')
        element = self.driver.find_element_by_id('vhs-detail-diagram')
        for child in element.find_elements_by_tag_name('tr')[11:]:
            self._remove_child_element(child)
        return element

    def _get_chart_element_for_serveral_days(self):
        self.driver.get(f'https://www.wetter.com/wetter_aktuell/wettervorhersage/'
                        f'{self.days}_tagesvorhersage/{urlparse(self.driver.current_url).path}')
        return self.driver.find_element_by_id(f'chartdiv-{self.days}')

    def _remove_child_element(self, child):
        self.driver.execute_script(
            'var element = arguments[0]; element.parentNode.removeChild(element);', child
        )


if __name__ == '__main__':
    main()
