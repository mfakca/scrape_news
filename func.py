import numpy as np
import time


punc = ['!', ',', '.','?']  


text = """
his bugüne kadar gücünü AAAA AAA hiç  AAA kaybetmed"""       
       
      

def get_rand_normal_dist(mu: int = 5, sigma: float = .5, len: int = 100):
    
    return np.random.choice(np.random.normal(mu,sigma, len))



def replace_text(text):
    text = text.replace('Gözden Kaçmasın','')
    text = text.replace('Haberin Devamı','')
    text = text.replace('\n','')
    text = text.replace('\r','')
    text = text.replace('\t','')
    
    
    #for i in punc:       text = text.replace(i,f'{i} ')
        
    return text
      



def edit_upper_text(text):
    
    back_is_upper = 0
    all_text = ''  
    uppercase_combo = 0

    for i in replace_text(text).split():
                
        if i.isupper() == 0 and back_is_upper == 1 and '(' not in back_text and uppercase_combo > 1:
            
            uppercase_combo = 0
            upper = ''.join(c for c in i if c.isupper())
            lower = ''.join(c for c in i if c.islower())
            
            i = upper[:-1] + '. ' + upper[-1:] + lower
        else: 
        
            if i.isupper(): uppercase_combo+=1
            else: uppercase_combo = 0

        back_is_upper = i.isupper()
        back_text = i
        
        all_text = all_text + i + ' '
    
    return all_text


#print(edit_upper_text(text))


#print(list('ARKSAba')[:max([list('ARKSAba')[::-1].index(i) for i in list('ARKSAba') if i.isupper() == 1])-1])

