from selenium import webdriver
import os
import urllib
import time

path = 'C:\Program Files\chromedriver.exe'

url_prefix = "https://www.google.com.sg/search?q="
url_postfix = "&source=lnms&tbm=isch&sa=X&ei=0eZEVbj3IJG5uATalICQAQ&ved=0CAcQ_AUoAQ&biw=939&bih=591"

save_folder = 'Train Images'

def main():
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
    download_images()
    
def download_images():
    topic = input("What do you want to search for? ")
    n_images = int(input('How many images do you want? '))
    
    # search_url = url_prefix+topic+url_postfix
    #print(search_url)
    search_url = 'https://www.copart.com/lot/26755730/Photos/salvage-2008-audi-a4-2-0t-quattro-nj-trenton'
    
    path = 'C:\Program Files\chromedriver.exe'
    
    driver = webdriver.Chrome(path)
    driver.get(search_url)
    
    # value = 0
    # for i in range(3):
    #     driver.execute_script("scrollBy("+ str(value) +",+1000);")
    #     value += 1000
    #     time.sleep(1)
    
    elem1 = driver.find_element_by_id('lot-images-wrapper')
    sub = elem1.find_elements_by_tag_name('img')

main()
    
