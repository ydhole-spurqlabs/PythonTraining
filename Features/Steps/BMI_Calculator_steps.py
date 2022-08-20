from behave import *

use_step_matcher("re")


# @given(": BMI Calculator Homepage")
# def step_impl(context):
#     context.driver = webdriver.Chrome("G:/Python/Training/Resources/chromedriver.exe")
#     context.driver.maximize_window()
#     context.driver.get("https://www.calculator.net/bmi-calculator.html?ctype=metric")
#     context.driver.implicitly_wait(3)


@when(': You enter the "(?P<Age>.+)"')
def step_impl(context, Age):
    # AgeInput = context.driver.find_element(By.XPATH, "//input[@id='cage']")
    # AgeInput.clear()
    # AgeInput.send_keys(Age)
    # time.sleep(2)
    context.bmipage.age_input(Age)


@step(': Click on "(?P<Gender>.+)"')
def step_impl(context, Gender):
    context.bmipage.gender_radio(Gender)

# try:
#     MaleGender = context.driver.find_element(By.XPATH, "//label[normalize-space()='" + Gender + "']")
#     MaleGender.click()
#     time.sleep(2)
# except:
#     FemaleGender = context.driver.find_element(By.XPATH, "//label[normalize-space()='" + Gender + "']")
#     FemaleGender.click()
#     time.sleep(3)


@step(': Enter "(?P<height>.+)"')
def step_impl(context, height):
    context.bmipage.height_input(height)

# HeightInput = context.driver.find_element(By.XPATH, "//input[@id='cheightmeter']")
# HeightInput.clear()
# HeightInput.send_keys(height)
# time.sleep(3)


@step(': Enter your "(?P<weight>.+)"')
def step_impl(context, weight):
    context.bmipage.weight_input(weight)

# WeightInput = context.driver.find_element(By.XPATH, "//input[@id='ckg']")
# WeightInput.clear()
# WeightInput.send_keys(weight)
# time.sleep(3)


@step(": Click on Calculate btn")
def step_impl(context):
    context.bmipage.calculatebtn_click()

# Calculatebtn = context.driver.find_element(By.XPATH, "//input[@value='Calculate']")
# Calculatebtn.click()
# time.sleep(3)


@step(': Verify Result with "(?P<expresult>.+)"')
def step_impl(context, expresult):
    context.bmipage.result_validation(expresult)
# try:
#     Result = context.driver.find_element(By.XPATH, "//body[1]/div[3]/div[1]/div[4]/div[1]/b[1]")
#     Actualresult = Result.text
#     Expectedresult = expresult
#     assert Actualresult == Expectedresult, "Expected Result Matched"
#     time.sleep(5)
# except:
#     context.driver.close()
#     assert False, "Expected Result mismatched"


# @then(": Close browser")
# def step_impl(context):
#     context.driver.close()
