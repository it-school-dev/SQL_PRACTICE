from selenium import webdriver 
from selenium.webdriver.common.by import By
import codecs
import time
import json

driver = webdriver.Chrome(executable_path="./webdriver/chromedriver.exe")



def main():
    try:
        driver.get("https://www.wildberries.ru/")
        time.sleep(15)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(15)

        goods_arr = driver.find_elements(By.CLASS_NAME, "goods__item")

        goods_str = ''

        json_list =[]

        for good in goods_arr:
            good_title = good.find_elements(By.CSS_SELECTOR, ".goods-card__description span")[1].text
            good_price =  good.find_element(By.CSS_SELECTOR, ".goods-card__price-now").text[:-2]
            good_link = good.find_element(By.CLASS_NAME, 'goods-card__container').get_attribute('href')
            
            jsn = {
                'title': good_title,
                'price_rub': good_price,
                'link': good_link
                }

            json_list.append(jsn)




        with codecs.open("parsed_data.json", "wb", "utf-8") as stream:
            json.dump(json_list, stream, ensure_ascii = False)

    except Exception as ex:
        print("An error occured: \n" + str(ex))


main()


driver = webdriver.Chrome(executable_path="./webdriver/chromedriver.exe")

driver.get("https://www.wildberries.ru/")
time.sleep(10)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

goods_arr = driver.find_elements(By.CLASS_NAME, "goods__item")

good_price =  goods_arr[0].find_element(By.CSS_SELECTOR, ".goods-card__price-now").text[:-2]
print(good_price)
good_link = goods_arr[0]
print(good_link)

goods_arr[0].find_element(By.CLASS_NAME, 'goods-card__container').get_attribute('href')