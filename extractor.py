import utils

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from rule import xpath_rules


class Extractor(object):

    @staticmethod
    def get_options():
        options = Options()
        options.headless = True
        return options

    def __init__(self):
        self.driver = webdriver.Chrome(options=self.get_options())

    @staticmethod
    def _background_img(prop):
        found = prop.find("url(")
        if found == -1:
            return None
        start_index = found + len("url(")
        end_index = prop.find(")", start_index)
        url = prop[start_index:end_index]
        return url.strip("'").strip('"')

    def _find_background_image(self, element):
        if not element:
            return None
        background = self._background_img(element.value_of_css_property("background"))
        background_image = self._background_img(element.value_of_css_property("background-image"))
        if background or background_image:
            return background or background_image
        children = element.find_elements_by_xpath('.//*')
        for child in children:
            return self._find_background_image(child)

    def _extract_by_id_logo(self, url):
        self.driver.get(url=url)
        try:
            element = self.driver.find_element_by_id("logo")
            return element and self._find_background_image(element)
        except NoSuchElementException as e:
            pass
        return None

    def _extract_by_class_logo(self, url):
        self.driver.get(url=url)

        try:
            element = self.driver.find_element_by_class_name("logo")
            return element and self._find_background_image(element)
        except NoSuchElementException as e:
            pass
        return None

    def _extract_by_image_size(self, url):
        self.driver.get(url)

        images = self.driver.find_elements_by_tag_name('img')

        for image in images[:4]:
            src = image.get_property('src')

            if not src:
                continue

            image_url = utils.image_src_to_url(url, src)

            try:
                width, height = utils.get_image_size(image_url)
                if (50 <= width <= 100) and (50 <= height <= 100):
                    return image_url
            except Exception as e:
                pass

        return None

    @staticmethod
    def _extract_with_xpath_rules(response):
        for rule in xpath_rules():
            result = response.xpath(rule.xpath).extract()
            if result:
                return result[0]
        return None

    def _extract_logo(self, response):
        result = self._extract_with_xpath_rules(response)
        if result:
            return result

        result = self._extract_by_id_logo(response.url)
        if result:
            return result

        result = self._extract_by_class_logo(response.url)
        if result:
            return result

        result = self._extract_by_image_size(response.url)

        return result

    def extract_logo_url(self, response):
        src = self._extract_logo(response)
        return utils.image_src_to_url(response.url, src)
