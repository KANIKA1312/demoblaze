# 1. Using Selenium WebDriver, open the web browser.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import datetime
from time import sleep

s = Service(executable_path='D:\PythonCourse\chromedriver.exe')
driver = webdriver.Chrome(service=s)

# 2. Maximize the browser window.

driver.maximize_window()

# 3. Navigate to web page URL - https://www.demoblaze.com/ (Links to an external site.)

demo_url = 'https://www.demoblaze.com/'
demo_title = 'STORE'


def setUp():
    driver.implicitly_wait(20)
    driver.get(demo_url)

    # 4. Check URL and title are as expected.

    assert driver.find_element(By.ID, 'nava').is_displayed()
    assert driver.current_url == demo_url
    assert driver.title == demo_title
    print('Demoblaze Launched Successfully!!')
    print('')
    print('This is the Demoblaze URL : ', driver.current_url)
    print('This is the Demoblaze title : ', driver.title)
    print('')
    sleep(1)

    # 5. On the home page, find the Nexus 6 model and click on it.
def add_product_to_cart():
    driver.find_element(By.LINK_TEXT, 'Nexus 6').click()
    sleep(0.25)

    # 6. On the product page, check Nexus 6 h2 title is displayed. Use assert.

    assert driver.find_element(By.CLASS_NAME, 'name').is_displayed()

    # 7. Click by Add to Cart button. If you'll see an alert at the top, use this command - driver.switch_to.alert.accept()

    driver.find_element(By.LINK_TEXT, 'Add to cart').click()
    sleep(0.25)
    driver.switch_to.alert.accept()
    sleep(0.25)

    # 8. Go to Cart at the top menu and click on it.

    driver.find_element(By.LINK_TEXT, 'Cart').click()
    sleep(0.25)

    # 9. Check the order is displayed and click by Delete link.
def delete_product_from_cart():

    assert driver.find_element(By.XPATH, '//table[contains(.,"Nexus 6")]').is_displayed()
    assert driver.find_element(By.XPATH, '//table[contains(.,"650")]').is_displayed()
    sleep(0.25)

    product_name = driver.find_element(By.XPATH, '//id[@tbodyid,"Nexus 6"]').text
    product_price = driver.find_element(By.XPATH, '//table[@td,"650")]').text

    sleep(0.25)
    print(
        f'Dear Customer, You item is {Fore.GREEN + product_name + Style.RESET_ALL} & '
        f'your order total is CAD $ {Fore.GREEN + product_price + Style.RESET_ALL}. '
        f'Click on Place Order Button to proceed. Thank you for shopping with us. ')
    print('')
    driver.find_element(By.LINK_TEXT, 'Delete').click()
    sleep(0.25)

    # 10. Close the browser and display a user-friendly messages:



    print(f'The product {Fore.RED + product_name + Style.RESET_ALL} is deleted. '
          f'Choose the product from Home Page & add to the cart again. ')
    print('')
    print('Cart is Empty!')
    print('')


def tearDown():
    if driver is not None:
        print('-----------------~~~~~~-------------------')
        print('Test is Complete at : ', datetime.datetime.now())
        sleep(0.25)
        driver.close()
        driver.quit()


setUp()
add_product_to_cart()
delete_product_from_cart()
tearDown()
