import os
import webbrowser

import requests
from bs4 import BeautifulSoup
'''
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
'''

def findLink(songName):
    import urllib.request
    import re       
    query = songName
    query = query.replace(' ', '+')
    args = '+'.join(query)
    args=args.replace(" ", "%20").replace('&','%26') 
    html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={args}")
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    webbrowser.open('https://www.youtube.com/watch?v=' + video_ids[0])
