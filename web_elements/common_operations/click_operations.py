from selenium.webdriver import ActionChains

from conf.web_driver_decorators import check_web_driver
from web_elements.finders.find_by import FindStrategies


class click(object):
    def __init__(self, find_strategy: FindStrategies=None, web_elem_to_click_locator=None):
        self.web_elem_to_click_locator = web_elem_to_click_locator
        self.find_startegy = find_strategy

    def __call__(self, web_elem):
        web_elem_to_click_locator = self.web_elem_to_click_locator
        find_strategy = self.find_startegy

        class wrapped(web_elem):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

            def click(self):
                if find_strategy and web_elem_to_click_locator:
                    self.web_element.find_element(find_strategy.meth, web_elem_to_click_locator).click()
                else:
                    self.web_element.click()

        return wrapped

class focus_and_click(object):
    def __init__(self, find_strategy: FindStrategies=None, web_elem_to_click_locator=None):
        self.web_elem_to_click_locator = web_elem_to_click_locator
        self.find_startegy = find_strategy

    def __call__(self, web_elem):
        web_elem_to_click_locator = self.web_elem_to_click_locator
        find_strategy = self.find_startegy
        tmp_actions = lambda elem: ActionChains(check_web_driver.web_driver) \
            .move_to_element(elem) \
            .click(elem) \
            .perform()

        class wrapped(web_elem):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

            def focus_and_click(self):
                if find_strategy and web_elem_to_click_locator:
                    tmp_actions(self.web_element.find_element(find_strategy.meth, web_elem_to_click_locator))
                else:
                    tmp_actions(self.web_element)

        return wrapped

class click_js(object):
    def __init__(self, find_strategy: FindStrategies=None, web_elem_to_click_locator=None):
        self.web_elem_to_click_locator = web_elem_to_click_locator
        self.find_startegy = find_strategy

    def __call__(self, web_elem):
        web_elem_to_click_locator = self.web_elem_to_click_locator
        find_strategy = self.find_startegy
        tmp_actions = lambda elem: check_web_driver.web_driver.execute_script("arguments[0].click();", elem)

        class wrapped(web_elem):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

            def click_js(self):
                if find_strategy and web_elem_to_click_locator:
                    tmp_actions(self.web_element.find_element(find_strategy.meth, web_elem_to_click_locator))
                else:
                    tmp_actions(self.web_element)

        return wrapped