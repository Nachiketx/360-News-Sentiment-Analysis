from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests


# Update the link of the item
link = "https://www.ebay.com/itm/295585653789?hash=item44d247241d:g:fzIAAOSwWBBk89Um&amdata=enc%3AAQAIAAAA4Hn5PovGXYC194qe653Dnb8Azo9ZoTWH4fFAeuUoqmp%2FjOPuCEmfx1cPOX%2BONqcxyxEFcelUqlX%2FD1TiZ3OpDlFa%2FvVBITF0l3M90FqR66YQRanfOOwLGSfWeza1GFbbLoQl0Hij8L5VbaDwX0xuHkz6rRhUwcO8mnQOkZYToV%2Bsu3JfEwbs%2FAOLuThod53l4oJ9bzQon%2FmGuLwFN7TnYtgJFXDobuwd4HeMrSGdtiOEXukzAmatklxbW3G8pG6nNq2v8yCC%2F8ZAGuFvvtvccHJXBhqWH%2BAJG3hFcCLJZ9Oh%7Ctkp%3ABFBMov-MwdRi"
req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

with requests.Session() as dick:    
    soup = BeautifulSoup(webpage,'html5lib')
    print(soup)
