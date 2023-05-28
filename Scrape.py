import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

def url(page):
    return "https://tabelog.com/sushi/atw/rvw/COND-0-0-1-0/D-edited_at/"+str(page)+"/?rvw_part=all&sw=%E3%82%B7%E3%83%A3%E3%83%AA"

reviews = []

def get_review(page_url):
    r = requests.get(page_url)
    soup = BeautifulSoup(r.content, "html.parser")
    
    comment_divs = soup.find_all("div", class_="rvw-item__rvw-comment")
    
    for div in comment_divs:
        reviews.append(div.p.text.strip())

for cnt in tqdm(range(1, 100)):
    r = requests.get(url(cnt))
    soup = BeautifulSoup(r.content, "html.parser")
    
    clickable_divs = soup.find_all("div", class_ = "rvw-item__frame")
    
    for div in clickable_divs:
        get_review("http://tabelog.com" + div.get("data-detail-url"))
        
for cnt in range(len(reviews)):
    reviews[cnt] = reviews[cnt].replace("\n", "<br>")

with open("reviews.csv", "w", encoding="utf-8") as f:
    f.write('\n'.join(reviews))