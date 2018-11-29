from selenium.webdriver import ActionChains

from conf.web_driver_decorators import check_web_driver


def fill_field(web_elem, web_elem_to_fill=None):
    class wrapped(web_elem):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    def fill_field(self, text: str):
        if web_elem_to_fill:
            web_elem_to_fill.send_keys(text)
        else:
            self.web_element.send_keys(text)

    return wrapped


def fill_field_js(web_elem, web_elem_to_fill=None):
    def tmp_action(elem, text):
        check_web_driver.web_driver.execute_script \
                (
                f"arguments[0].value = '{text}';",
                elem
            )

    class wrapped(web_elem):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    def fill_field_js(self, text: str):
        if web_elem_to_fill:
            tmp_action(web_elem_to_fill, text)
        else:
            tmp_action(self.web_element, text)

    return wrapped


def focus_and_fill_field(web_elem, web_elem_to_fill=None):
    def tmp_action(elem, text):
        ActionChains(check_web_driver.web_driver) \
            .move_to_element(elem) \
            .click() \
            .send_keys_to_element(elem, text) \
            .perform()

    class wrapped(web_elem):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    def focus_and_fill_field(self, text: str):
        if web_elem_to_fill:
            tmp_action(web_elem_to_fill, text)
        else:
            tmp_action(self.web_element, text)

    return wrapped