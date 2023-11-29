from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(by="id", value="cookie")

timeout_5_min = time.time() + 60*5
while time.time() < timeout_5_min:
    timeout_5_sec = time.time() + 3
    while time.time() < timeout_5_sec:
        cookie.click()

    store = driver.find_elements(by="css selector", value="#store b")
    prices = []
    item_bought = False
    counter = 0
    for element in store:
        text = element.text.split("\n")[0]
        if text:
            text = text.split()[-1].replace(",", "")
            price = int(text)
            prices.append(price)

    money_text = driver.find_element(by="id", value="money").text
    money = int(money_text.replace(",", ""))
    while not item_bought:
        for price in prices:
            if money < price and counter == 0:
                item_bought = True
                break
            elif money < price:
                store[counter-1].click()
                item_bought = True
                break
            else:
                counter += 1

score_element = driver.find_element(by="id", value="cps")

score = score_element.text.split()[-1]
print(score)
