import requests
from selectolax.parser import HTMLParser



r = requests.get('https://www.dideban.com/signals?s=open&market=3&sort=like')

parser = HTMLParser(r.content)
arzs = []
users = []
signals = []

for arz in parser.css('.sginals-page .signal-symbol-title'):
    arzs.append(arz.text())


for u in parser.css('.signal-links.mb-1 > a.text-secondary.py-1.px-3.rounded-pill'):
    users.append(u.attributes.get('title'))

for sig in parser.css('div.d-flex.justify-content-around > div:nth-child(1) > div'):
    signals.append(sig.text().strip())




for uu in users:
    rr = requests.get(f'https://www.dideban.com/u/{uu}')
    self = HTMLParser(rr.content)
    point = self.css_first('span.text-success.font-weight-bold')
    #print(type(point.text()))
    if float(point.text()) > 0:
        for namad,user,signal in zip(arzs,users,signals):
            print(f'{namad} - {user} \n {signal}')
            print('-------')
            TOKEN = "dassdada"
            url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
            print(requests.get(url).json())
    else:
        continue












