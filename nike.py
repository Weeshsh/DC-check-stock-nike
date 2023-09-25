import json
import requests
from bs4 import BeautifulSoup
from config import SIZES
#SKU = "DV0834-101"

def nike(SKU):
    SKU = SKU.upper()
    try:
        print('Fetching Nike product...')
        headers = {
          "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
          "accept-language": "en-GB,en;q=0.9,pl-PL;q=0.8,pl;q=0.7",
          "cache-control": "max-age=0",
          "if-none-match": "\"27d1e-ppnN2Y0lnueY+eQgJxDQOV1vzDY\"",
          "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Brave\";v=\"110\"",
          "sec-ch-ua-mobile": "?1",
          "sec-ch-ua-platform": "\"Android\"",
          "sec-fetch-dest": "document",
          "sec-fetch-mode": "navigate",
          "sec-fetch-site": "same-origin",
          "sec-fetch-user": "?1",
          "sec-gpc": "1",
          "upgrade-insecure-requests": "1"
        }
        headers2 = {
            'authority': 'product-proxy-v2.adtech-prod.nikecloud.com',
            'accept': '*/*',
            'accept-language': 'en-GB,en;q=0.9,pl-PL;q=0.8,pl;q=0.7',
            'content-type': 'application/json',
            'origin': 'https://www.nike.com',
            'referer': 'https://www.nike.com/',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Brave";v="110"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36',
        }
        url = f'https://www.nike.com/pl/w?q={SKU}'
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.content, 'lxml')
        url2=''
        for x in soup.find_all('a', href = True):
            if SKU in x['href']:
                url2 = x['href']
                break
        res2 = requests.get(url2)
        soup2 = BeautifulSoup(res2.content, 'lxml')
        for i in soup2.find('script', id='__NEXT_DATA__'):
                asdasd = json.loads(i)['props']['pageProps']['initialState']['Threads']['products'][f'{SKU}']['id']

        json_data = {
            'experienceProducts': [
                {
                    'cloudProductId': f'{asdasd}'
                },
            ],
            'country': 'pl',
        }
        sizes = []
        res = {}
        resres = requests.post('https://product-proxy-v2.adtech-prod.nikecloud.com/products', headers=headers2, json=json_data)
        for x in resres.json()['hydratedProducts'][0]['skuData']:
            sizes.append(x['size'])

        url3 = f'https://api.nike.com/deliver/available_gtins/v3?filter=styleColor({SKU})&filter=merchGroup(EU)'
        res3 = requests.get(url3)
        for i,x  in enumerate(res3.json()['objects']):
            res[sizes[i]] = x['available']
        return res
    except:
         print('debil')
         return ''
    
#print(nike(input()))