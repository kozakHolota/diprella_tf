from selenium.webdriver import ActionChains

from conf.web_driver_decorators import check_web_driver
from web_elements.finders.find_by import FindStrategies

class fill_field(object):
    def __init__(self, find_strategy: FindStrategies=None, web_elem_to_click_locator=None):
        self.web_elem_to_click_locator = web_elem_to_click_locator
        self.find_startegy = find_strategy

    def __call__(self, web_elem):
        web_elem_to_click_locator = self.web_elem_to_click_locator
        find_strategy = self.find_startegy

        class wrapped(web_elem):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

            def fill_field(self, text: str):
                if find_strategy and web_elem_to_click_locator:
                    self.web_element.find_element(find_strategy.meth, web_elem_to_click_locator).send_keys(text)
                else:
                    self.web_element.send_keys(text)

        return wrapped

class fill_field_js(object):
    def __init__(self, find_strategy: FindStrategies=None, web_elem_to_click_locator=None):
        self.web_elem_to_click_locator = web_elem_to_click_locator
        self.find_startegy = find_strategy

    def __call__(self, web_elem):
        web_elem_to_click_locator = self.web_elem_to_click_locator
        find_strategy = self.find_startegy

        tmp_action = lambda elem, text: check_web_driver.web_driver.execute_script \
                (
                f"arguments[0].value = '{text}';",
                elem
            )

        class wrapped(web_elem):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

            def fill_field_js(self, text: str):
                if find_strategy and web_elem_to_click_locator:
                    tmp_action(self.web_element.find_element(find_strategy.meth, web_elem_to_click_locator), text)
                else:
                    tmp_action(self.web_element, text)

        return wrapped

class focus_and_fill_field(object):
    def __init__(self, find_strategy: FindStrategies=None, web_elem_to_click_locator=None):
        self.web_elem_to_click_locator = web_elem_to_click_locator
        self.find_startegy = find_strategy

    def __call__(self, web_elem):
        web_elem_to_click_locator = self.web_elem_to_click_locator
        find_strategy = self.find_startegy

        tmp_action = lambda elem, text: ActionChains(check_web_driver.web_driver) \
            .move_to_element(elem) \
            .click() \
            .send_keys_to_element(elem, text) \
            .perform()

        class wrapped(web_elem):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

            def focus_and_fill_field(self, text: str):
                if find_strategy and web_elem_to_click_locator:
                    tmp_action(self.web_element.find_element(find_strategy.meth, web_elem_to_click_locator), text)
                else:
                    tmp_action(self.web_element, text)

        return wrapped