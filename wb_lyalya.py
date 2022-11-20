from selenium import webdriver 
from selenium.webdriver.common.by import By
import codecs
import time
import sqlite3


driver = webdriver.Chrome(executable_path="./webdriver/chromedriver.exe")

db1 = sqlite3.connect('wb_prikols.sqlite3')
cursor = db1.cursor()
cursor.execute('''
    DROP TABLE IF EXISTS wb_prikols
''')
db1.close()


db = sqlite3.connect('wb_prikols.sqlite3')

cursor = db.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS wb_prikols(
            id INTEGER PRIMARY KEY,
            name TEXT,
            link INTEGER,
            price INTEGER
        )
''')

def main():
    try:
        driver.get("https://www.wildberries.ru/")
        time.sleep(3)

        driver.execute_script("window.scrollTo(0, 1080);")
        time.sleep(0.7)
        
        driver.execute_script("window.scrollTo(1080, 1580);")
        time.sleep(0.7)

        driver.execute_script("window.scrollTo(1580, 2080);")
        time.sleep(0.7)

        driver.execute_script("window.scrollTo(2080, 2580);")
        time.sleep(0.7)

        driver.execute_script("window.scrollTo(2580, document.body.scrollHeight);")
        time.sleep(2)

        goods_arr = driver.find_elements(By.CLASS_NAME, "goods-card")

        goods_str = ''

        for good in goods_arr:
            good_title = good.find_elements(By.CSS_SELECTOR, ".goods-card__description span")[1].text
            good_link = good.find_element(By.CSS_SELECTOR, "a").get_attribute('href')
            good_price = good.find_element(By.CSS_SELECTOR, "ins").text
            print(good_title + ' ' + good_link + ' ' + good_price)
            goods_str = goods_str + good_title + ' ' + good_link + ' ' + good_price + "\n"
            name = good_title
            link = good_link
            price = good_price
            cursor.execute('''
                INSERT INTO wb_prikols(name, link, price) VALUES(?, ?, ?)
            ''', (name, link, price))
            db.commit()

        with codecs.open("wb_prikols.txt", "w", "utf-16") as stream:   # or utf-8
            stream.write(goods_str)

    except Exception as ex:
        print("An error occured: \n" + str(ex))

main()