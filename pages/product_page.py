from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_card(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CARD).click()

    def should_be_correct_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        notification_product_name = self.browser.find_element(*ProductPageLocators.NOTIFICATION_PRODUCT_NAME).text
        assert product_name == notification_product_name, "The product name in the notification " \
                                                          "doesn't match product name"

    def should_be_correct_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        notification_price = self.browser.find_element(*ProductPageLocators.NOTIFICATION_PRICE).text
        assert product_price == notification_price, "The price in the notification doesn't match product price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)
