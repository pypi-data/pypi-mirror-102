from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os
import __main__

def imagecrawler(keyword, amount, path = None):
    '''구글 이미지 크롤링을 시작합니다.

    저장 위치: File/keyword/~.jpg

    Args:
        keyword (String): 검색할 키워드.
        amount (int): 다운할 사진 개수.
        path (String): 사진 저장할 절대위치.
    '''

    try:
        amount = int(amount)
    except:
        print('amount는 int형으로 전달해야합니다.')
        exit()
    if path == None:
        save_path = '{0}/{1}/'.format(os.path.dirname(os.path.realpath(__main__.__file__)), keyword)
    else:
        if path[-1] != '/':
            save_path =  path + '/'

    driver = webdriver.Chrome('../chromedriver.exe')
    driver.get('https://www.google.co.kr/search?q={0}&hl=ko&tbm=isch'.format(keyword))
    driver.implicitly_wait(3)
    body = driver.find_element_by_class_name('islrc')
    last_height = driver.execute_script('return document.body.scrollHeight;')

    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        new_height = driver.execute_script('return document.body.scrollHeight;')
        img_amount = len(body.find_elements_by_tag_name('img'))
        
        if last_height == new_height:
            time.sleep(1)
            if last_height != driver.execute_script('return document.body.scrollHeight;'):
                continue
            if amount > img_amount:
                try:
                    driver.find_element_by_class_name('mye4qd').click()
                except:
                    break
            else:
                break
        last_height = new_height
    
    
    if not os.path.isdir(save_path):
        os.makedirs(save_path)

    images = body.find_elements_by_tag_name('img')
    for i in range(amount):
        try:
            urllib.request.urlretrieve(images[i].get_attribute('src'), '{0}{1}.jpg'.format(save_path, i))
        except:
            pass