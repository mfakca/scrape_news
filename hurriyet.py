from requests_html import HTMLSession
from bs4 import BeautifulSoup
import func
import time
import os


session = HTMLSession()


main_topic_list = ['televizyon','yasam','sporarena/basketbol','sporarena/futbol', 'dunya','gundem','sporarena/tenis','sporarena/voleybol']
total_fail_page = 0

for main_topic in main_topic_list:

    for page_idx in range(1,50):

        start_url = f"https://www.hurriyet.com.tr/{main_topic}/?p={page_idx}"

        r = session.get(start_url)
        soup = BeautifulSoup(r.content, "lxml")
        news = soup.find('div',attrs={'class':'category__list'})



        url, title = '',''
        
        try:
            for i in news.find_all('div',attrs= {'class':'category__list__item'}):
                
                try:
                
                    page = i.find('a',attrs={'target':'_self'})
                    page_url = 'https://www.hurriyet.com.tr' + page.get('href')
                    page_url_extended = page_url.split('/')[-1]
                    title = page.get('title')
                    print(page_url_extended)


                    print(f'Main Topic: {main_topic}')
                    print(f'Page Index: {page_idx}')
                    print(page_url)
                    print(title)
                    
                    
                    page_r = session.get(page_url)
                    page_soup = BeautifulSoup(page_r.content, "lxml")
                    
                    
                    page_text = page_soup.find('div',attrs={'class':'col-xl-17 col-lg-16 news-left-content'})
                    page_header = page_text.find('h2').text
                    page_paragraph = func.edit_upper_text(page_text.find('div',attrs={'class':'news-content readingTime'}).text) 
                    
                    print(page_header)
                    print(page_paragraph)
                    print('///////////////////////////////////////////////')
                    
                except:
                    total_fail_page+=1
                
                try:
                    os.mkdir('data/hurriyet/' + main_topic)
                except: pass
                
                try:
                    f = open(f"data/hurriyet/{main_topic}/{page_url_extended}.txt", "w", encoding='utf-8')
                    f.write(page_header + ' ' + page_paragraph)
                    f.close()
                except:
                    total_fail_page+=1

        except: continue    
       
        print(f'Fail Page Count: {total_fail_page}') 
    sleep_time = round(func.get_rand_normal_dist(),2)
    print(f'Sleep time: {sleep_time}')
    time.sleep(sleep_time)
           
        
        