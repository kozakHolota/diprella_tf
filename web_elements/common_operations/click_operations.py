from selenium.webdriver import ActionChains

from conf.web_driver_decorators import check_web_driver


def click(web_elem, web_elem_to_click=None):
    class wrapped(web_elem):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def click(self):

            if web_elem_to_click:
                web_elem_to_click.click()
            else:
                self.web_element.click()
    return wrapped


def focus_and_click(web_elem, web_elem_to_click=None):
    def tmp_actions(elem):
        ActionChains(check_web_driver.web_driver) \
            .move_to_element(elem) \
            .click(elem) \
            .perform()

    class wrapped(web_elem):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def focus_and_click(self):
            if web_elem_to_click:
                tmp_actions(web_elem_to_click)
            else:
                tmp_actions(self.web_element)

    return wrapped

def click_js(web_elem, web_elem_to_click=None):
    def tmp_action(elem):
        check_web_driver.web_driver.execute_script("arguments[0].click();", elem)
    class wrapped(web_elem):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def click_js(self):
            if web_elem_to_click:
                tmp_action(web_elem_to_click)
            else:
                tmp_action(self.web_element)

    return wrapped