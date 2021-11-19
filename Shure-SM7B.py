# Shure SM7B Mic - One Product - Different Websites
# Tutorial from John Watson Rooney YouTube channel

from requests_html import HTML, HTMLSession
import re
from datetime import date
from csv import DictWriter


def get_price_ander():
    r = s.get('https://www.andertons.co.uk/shure-sm7b-dynamic-vocal-mic-sm7b')
    return r.html.find('span.product-price', first=True).text

def get_price_gear(): 
    r = s.get('https://www.gear4music.com/PA-DJ-and-Lighting/Shure-SM7B-Dynamic-Studio-Microphone/G6X')
    return r.html.find('span.c-val', first=True).text

def get_price_west():
    r = s.get('https://www.westenddj.co.uk/shure-sm7b')
    return r.html.find('span[itemprop=price]', first=True).text

def clean(price):
    return float(re.sub(r'[^0-9.]', '', price))

def main(): 
    today = date.today()
    entry = {
        'date': today.strftime('%m-%d-%Y'),
        'ander': clean(get_price_ander()),
        'gear': clean(get_price_gear()),
        'west': clean(get_price_west()),
    }
    return entry

def save_to_csv(entry):
    columns = ['date', 'ander', 'gear', 'west']
    with open('product_data.csv', 'a') as f:
        w = DictWriter(f, fieldnames=columns)
        w.writerow(entry)
        print('File written.')
    return

if __name__ == '__main__':
    s = HTMLSession()
    print('Running script...')
    entry = main()
    save_to_csv(entry)