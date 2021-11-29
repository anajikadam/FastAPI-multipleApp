import requests
# import pandas as pd
# import bs4
from bs4 import BeautifulSoup as bs

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

class TransMR:
    def __init__(self, word):
        self.word = word
        
    def TransToMR(self):
        word = self.word
        url = "https://en.glosbe.com/en/mr/{}".format(word)
        # print(url)
        try:
            response = requests.get(url, headers=headers).text
            soup = bs(response,"html.parser")
            mr_trans = []
            for i in soup.findAll('li',class_='translation__item'):
                mr_trans.append(i.find('h3','translation').text.strip())
            if len(mr_trans)<1:
                guess_trans = []
                for i in soup.findAll('li',class_='py-4'):
                    guess_trans.append(i.find('button','font-medium').text.strip()) 
                mr_trans = guess_trans[:4]
            for i in soup.findAll('div',{"id":'tmem_first_examples'}):
                ex_english = i.findAll('div',{"class":"w-1/2 pr-2"})
                ex_marathi = i.findAll('div',{"class":"w-1/2 relative pl-2"})
            example = list (map ( lambda x,y: [x.text, y.text], ex_english, ex_marathi))[:4]
        except:
            print("An exception in TransEG_mean")
            mr_trans, example = None, None
        return mr_trans, example


class TransEG:
    def __init__(self, word):
        self.word = word

    def TransEG_mean(self):
        word = self.word
        meaning, c=[], 0
        url= 'https://www.yourdictionary.com/{}'.format(word)
        # print(url)
        try:
            response = requests.get(url, headers=headers).text
            soup = bs(response,"html.parser")
            data = soup.find_all('div',class_='definition flex-align-self-center')
            for i in data:
                if(c<5):
                    meaning.append(i.text.strip())
                    c+=1
                else:
                    pass
        except:
            print("An exception in TransEG_mean")
            meaning = None
        return meaning
    
    def TransEG_syn(self):
        word = self.word
        synonyms, c=[], 0
        url= 'https://thesaurus.yourdictionary.com/{}'.format(word)
        # print(url)
        try:
            response = requests.get(url, headers=headers).text
            soup = bs(response,"html.parser")
            # data = soup.find_all('div',class_='definition flex-align-self-center')
            for i in soup.find_all('div', class_='synonym-link-wrapper'):
                if(c<5):
                    synonyms.append(i.text.strip())
                    c+=1
                else:
                    pass
        except:
            print("An exception in TransEG_syn")
            synonyms = None
        return synonyms
    
    def TransEG_exmple(self):
        word = self.word
        example, c=[], 0
        url= 'https://sentence.yourdictionary.com/{}'.format(word)
        # print(url)
        try:
            response = requests.get(url, headers=headers).text
            soup = bs(response,"html.parser")
            # data = soup.find_all('div',class_='definition flex-align-self-center')
            for i in soup.find_all('div', class_='sentence-item'):
                if(c<5):
                    example.append(i.text.strip())
                    c+=1
                else:
                    pass
        except:
            print("An exception in TransEG_exmple")
            example = None
        return example
    
    
