from allure_commons._allure import attach, tag
from allure_commons.types import AttachmentType
from selenium import webdriver
from Pages.BasePage import BasePage
from Pages.BmiPage import BmiPage
# from Pages.CalculatorPage import CalculatorPage
import json

data = json.load(open("Resources/config.json"))


def before_all(context):
    # tag = str(scenario.tag)
    # print(tag)
    context.driver = webdriver.Chrome("G:/Python/Training/Resources/chromedriver.exe")
    context.driver.maximize_window()
    basepage = BasePage(context.driver)
    context.bmipage = BmiPage(basepage)
    # context.stepid = 1

    # if "web" in tag:
    context.driver.get(data['BMIWEBURL'])
    context.driver.implicitly_wait(3)

    # else:
    #     context.calpage = CalculatorPage(basepage)
    #     context.driver.get(data['CALCULATORWEBURL'])
    #     context.driver.implicitly_wait(3)


# def after_step(context):
#     attach(context.driver.get_screenshot_as_png(), name=context.stepid, attachment_type=AttachmentType.PNG)
#     context.stepid = context.stepid + 1


def after_all(context):
    # print("After scenario", scenario)
    context.driver.close()
