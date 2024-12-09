import time
import pandas as pd
from selenium import webdriver
from tkinter import messagebox
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def scraping():

    input_csv = "products.csv"
    input_df = pd.read_csv(input_csv)
    
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.co.jp/")
    time.sleep(5)

    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    
    for index, row in input_df.iterrows():

        product_info = {}

        if pd.notna(row["ASINコード"]):
            product_info['asin'] = row['ASINコード']
            keyword = product_info['asin']
        else:
            product_info['title'] = row['商品名']
            keyword = product_info['title']

        # try:
        search_box.send_keys(keyword)
        time.sleep(3)
        result_link = driver.find_element(By.CSS_SELECTOR, "div.s-main-slot div.s-result-item a.a-link-normal")
        product_info['url'] = f"https://www.amazon.co.jp{result_link.get_attribute('href')}"
        print(f"url _____ _____ _____ {product_info['url']}")

        driver.get(product_info['url'])
        time.sleep(3)
        
        # -------------------------
        # title or asin
        # -------------------------
        if product_info['asin']:
            product_info['title'] = driver.find_element(By.ID, 'productTitle').text
            print(f"title _____ _____ _____ {product_info['title']}")
        else:
            product_info['asin'] = driver.find_element(By.ID, 'title_feature_div').get_attribute('data-csa-c-asin')
            print(f"asin _____ _____ _____ {product_info['asin']}")

        # -------------------------
        # price
        # -------------------------
        try:
            price_text = driver.find_element(By.CSS_SELECTOR, 'span[class="a-price-whole"]').text
            product_info['price'] = int(price_text.replace("￥","").replace(",",""))
            print(f"price _____ _____ _____ {product_info['price']}")
        except:
            continue
        
        # -------------------------
        # quantity
        # -------------------------
        try:
            qty_elmnt = driver.find_element(By.ID, 'quantity')
            qty_options = qty_elmnt.find_elements(By.TAG_NAME, "option")
            product_info['quantity'] = len(qty_options)
        except NoSuchElementException:
            product_info['quantity'] = 1

        print(f"quantity _____ _____ _____ {product_info['quantity']}")
        
        # -------------------------
        # main image url
        # -------------------------
        img_ul = driver.find_element(By.CSS_SELECTOR, ".a-unordered-list.a-nostyle.a-horizontal.list.maintain-height")
        image_main_li = img_ul.find_element(By.ID, "imgTagWrapperId")
        image_main_tag = image_main_li.find_element(By.TAG_NAME, 'img')
        product_info['img_url_main'] = image_main_tag.get_attribute('src')
        
        print(f"main image url _____ _____ _____ {product_info['img_url_main']}")
        
        # -------------------------
        # thumb image url
        # -------------------------
        image_li = driver.find_elements(By.CSS_SELECTOR, "li.imageThumbnail")
        image_li_count = len(image_li)
        image_other = []
        
        for x in range(image_li_count):
            image_other_li = driver.find_element(By.XPATH, f"//li[@data-csa-c-posy='{x+1}']")
            image_other_tag = image_other_li.find_element(By.TAG_NAME, 'img')
            image_other_src = image_other_tag.get_attribute('src').replace("US40", "SL875")
            image_other.append(image_other_src)
            
        product_info['img_url_thumb'] = image_other
        
        print(f"thumb image url _____ _____ _____ {product_info['img_url_thumb']}")
        
        # except:
        #     pass
        
        data = {
            "ASINコード": product_info['asin'],
            "商品名": product_info['title'],
            "価格": product_info['price'],
            "商品詳細URL": product_info['url'],
            "画像URL": product_info['img_url_main'],
        }

        # Save to CSV
        out = pd.DataFrame([data])
        out.to_csv("output.csv", mode="a", header=not pd.io.common.file_exists("output.csv"), index=False, encoding="utf-8-sig")

        
    driver.quit()
    
    messagebox.showinfo("OK", "スクレイピング完了しました。")


if __name__ == "__main__":
    scraping()