import json
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from selenium import webdriver

from Pages.BasePage import BasePage
from Pages.BmiPage import BmiPage
from Pages.CalculatorPage import CalculatorPage

data = json.load(open("Resources/config.json"))


def before_scenario(context, scenario):
    tag = str(scenario.tags)
    print(tag)
    context.driver = webdriver.Chrome("G:/Python/Training/Resources/chromedriver.exe")
    basepage = BasePage(context.driver)
    context.bmipage = BmiPage(basepage)
    context.calpage = CalculatorPage(basepage)
    context.stepid = 1
    try:
        if "web" in tag:
            context.driver.get(data['BMIWEBURL'])
            context.driver.maximize_window()
            context.driver.implicitly_wait(3)
        else:
            pass
    except:
        if "cal" in tag:
            context.driver.get(data['CALCULATORURL'])
            context.driver.maximize_window()
        else:
            pass


def after_step(context, step):
    attach(context.driver.get_screenshot_as_png(), name=context.stepid, attachment_type=AttachmentType.PNG)
    context.stepid = context.stepid + 1


def after_scenario(context, scenario):
    print("After scenario", scenario)
    context.driver.close()
