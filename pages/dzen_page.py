from pages.base_page import BasePage

class DzenPage(BasePage):
    def switch_to_new_tab(self):
        self.switch_to_last_tab()