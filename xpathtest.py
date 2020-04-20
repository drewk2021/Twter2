from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time



# Function of waiting until the present of the element on the web page
def waiting_func(driver, by_variable, attribute):
    try:
        WebDriverWait(driver, 20).until(lambda x: x.find_element(by=by_variable,  value=attribute))
    except ():
        print('{} {} not found'.format(by_variable, attribute))
        exit()


def main():

    URL = 'http://www.quotationspage.com/random.php'

    driver = webdriver.Chrome()
    driver.get(URL)       # 1
    time.sleep(3)
    for x in range(5):
        quoted = driver.find_element_by_xpath('//*[@id="content"]/dl/dd['+str(x)+']/b/a')
        print(quoted)




if __name__ == "__main__":
    main()
