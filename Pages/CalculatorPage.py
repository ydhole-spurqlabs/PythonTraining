from selenium.webdriver.common.by import By
import time
from Pages.BasePage import BasePage


class CalculatorPage:
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.context = context

        self.calculatebtn_xpath = "//span[text()= '=']"
        self.result_id = "sciOutPut"

    def enter_number(self):
        for row in self.table:
            num1 = row[0][0]
            n1 = str(num1)
            operator = row[1][0]
            num2 = row[2][0]
            n2 = str(num2)
            for i in n1:
                n = n1[i]
                self.driver.find_element(By.XPATH, "//span[text()= '" + n + "']").click()
                time.sleep(2)

            self.driver.find_element(By.XPATH, "//span[text()= '" + operator + "']").click()
            time.sleep(2)

            for j in n2:
                m = n2[j]
                self.driver.find_element(By.XPATH, "//span[text()= '" + m + "']").click()
                time.sleep(2)

    def calculatebtn_click(self):
        self.driver.find_element(By.XPATH, self.calculatebtn_xpath).click()

    def verify_result(self):
        try:
            act_result = self.driver.find_element(By.ID, "sciOutPut").text()
            print(act_result)
            exp_result = " 352456"
            assert act_result == exp_result, "Test passed"
            self.driver.close()
        except:
            self.driver.close()
            assert False, "Test failed"
