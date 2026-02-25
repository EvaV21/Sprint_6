from pages.base_page import BasePage

class DzenPage(BasePage):
    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])