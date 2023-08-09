import requests
from selectolax.parser import HTMLParser

# Define your send_to_telegram function
def send_to_telegram(message):
    apiToken = 'YOUR_TELEGRAM_BOT_TOKEN'
    chatID = 'YOUR_CHAT_ID'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

# Main part of the code
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

    if float(point.text()) > 0:
        for namad, user, signal in zip(arzs, users, signals):
            message = f'{namad} - {user}\n{signal}\n-------'
            send_to_telegram(message)
    else:
        continue
