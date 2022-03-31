
class AddNewCustomer:
    lnk_customers_menu_xpath = "//a[@href = "#"]//[contains(text(), "Customers")]"
    lnk_customers_menu_item_xpath = "//a[@href="Admin/Customer/List/"]"

    def __init__(self, driver):
        self.driver = driver

    def add_NewCustomer(self):


