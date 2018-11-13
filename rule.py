class XpathRule(object):
    def __init__(self, xpath):
        self.xpath = xpath

    def __str__(self):
        return "XpathRule[xpath={}]".format(self.xpath)


def xpath_rules():
    rules = [
        XpathRule('//div[any(lower(@id), "header")]//*/img[any(lower(@src), "logo", "icon")]/@src'),
        XpathRule('//div[any(lower(@class), "header")]//*/img[any(lower(@src), "logo", "icon")]/@src'),
        XpathRule('//div[any(lower(@id), "header")]//*/img/@src'),
        XpathRule('//div[any(lower(@class), "header")]//*/img/@src'),
        XpathRule('//header//*/img[any(lower(@alt), "logo", "icon")]/@src'),
        XpathRule('//header//*/img[any(lower(@title), "logo", "icon")]/@src'),
        XpathRule('//img[any(lower(@src), "header_logo", "logo", "icon")]/@src'),
        XpathRule('//img[any(lower(@alt), "logo", "icon")]/@src'),
        XpathRule('//img[any(lower(@title), "logo", "icon")]/@src'),
        XpathRule('//div[any(lower(@id), "bottom")]//*/img[any(lower(@src), "logo", "icon")]/@src'),
        XpathRule('//div[any(lower(@class), "bottom")]//*/img[any(lower(@src), "logo", "icon")]/@src'),
        XpathRule('//table//*/img[any(lower(@src), "logo", "icon")]/@src'),
        XpathRule('//div[any(lower(@id), "logo", "icon")]//*/img/@src'),
        XpathRule('//div[any(lower(@class), "logo", "icon")]//*/img/@src'),
    ]
    return rules
