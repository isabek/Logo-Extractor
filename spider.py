import scrapy

from extractor import Extractor
from lxml.etree import FunctionNamespace


def lowercase(context, elements):
    if isinstance(elements, (list,)):
        for index, elem in enumerate(elements):
            if isinstance(elem, str):
                elements[index] = elem.lower()
    return elements


def contains_any(context, elements, *args):
    if isinstance(elements, list):
        if len(elements):
            for s in args:
                if elements[0].find(s) != -1:
                    return True
    return False


ns = FunctionNamespace(None)
ns['lower'] = lowercase
ns['any'] = contains_any


class LogoSpider(scrapy.Spider):
    name = 'logo'
    allowed_hosts = ['*']

    def __init__(self, input_file_path=None, **kwargs):
        super().__init__(**kwargs)
        self.input_file_path = input_file_path
        self.extractor = Extractor()

    @staticmethod
    def _split_line_to_urls(line):
        parts = [s.strip() for s in line.split(",")]
        return parts[0], parts[1]

    def read_file_skip_header_lazy(self):
        with open(self.input_file_path, "r") as f:
            next(f)
            for line in f.readlines():
                yield self._split_line_to_urls(line)

    def start_requests(self):
        for web_page_url, _ in self.read_file_skip_header_lazy():
            yield scrapy.Request(url=web_page_url, callback=self.parse)

    def parse(self, response):
        logo_url = self.extractor.extract_logo_url(response)
        yield {
            'webpage_url': response.url,
            'logo_url': logo_url
        }
