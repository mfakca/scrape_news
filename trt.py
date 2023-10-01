from requests_html import HTMLSession
from bs4 import BeautifulSoup
import func
import time
import os


session = HTMLSession()


main_topic_list = ['gundem','turkiye','dunya','ekonomi','spor']
total_fail_page = 0

counter = 0

for main_topic in main_topic_list:

    for page_idx in range(1,10000):

        start_url = f"https://www.trthaber.com/haber/{main_topic}/{page_idx}.sayfa.html"

        r = session.get(start_url)
        soup = BeautifulSoup(r.content, "lxml")
        news = soup.find('div',attrs={'class':'news-container'})



        url, title = '',''
        
        #try:
        for i in news.find_all('a',attrs= {'class':'site-url'}):
            
            page_url = i.get('href')
            page_url_extended = page_url.split('/')[-1].replace('.html','')
            title = i.get('title')
            
            #print(page_url)
            #print(title)
            #print(page_url_extended)
            
            page_r = session.get(page_url)
            page_soup = BeautifulSoup(page_r.content, "lxml")
            

            a = page_soup.find('div',attrs={'class':'news-content'})
            
            if a is None: continue
                
                
            page_text = a.text.split('ETİKETLER')[0]
            page_header = page_soup.find('h2',attrs={'class':'news-spot'}).text
                
                
            #print(page_header)
            #print(page_text)
            
            
            
            #page_text = page_soup.find('div',attrs={'class':'news-content'}).find('p').text #.split('ETİKETLER')[0]
            #page_header = page_soup.find('h2',attrs={'class':'news-spot'}).text
            #page_paragraph = func.edit_upper_text(page_text.find('div',attrs={'class':'news-content readingTime'}).text) 
            
            
            page_paragraph = func.replace_text(page_text)
            
            
            
            try:
                os.mkdir('data/trt/' + main_topic)
            except: pass
            
            try:
                    f = open(f"data/trt/{main_topic}/{page_url_extended}.txt", "w", encoding='utf-8')
                    f.write(page_header + ' ' + page_paragraph)
                    f.close()
                    counter += 1
                    if counter % 1000 == 0: print(f'{counter} kayıt toplandı.')
            except:
                total_fail_page+=1
            
        #except: 
        #    print('hata aldı')
        #    continue    
       
        #print(f'Fail Page Count: {total_fail_page}') 
    #sleep_time = round(func.get_rand_normal_dist(),2)
    #print(f'Sleep time: {sleep_time}')
    #time.sleep(sleep_time)
           
        
        
