from .env import WEBHOOK_URL

import requests as r

def notify_on_start_webhook(tunnel_url: str = ''):
    payload = {
        'tunnel-url': tunnel_url
    }
    webhook_url = WEBHOOK_URL()

    if webhook_url:
        print('Webhook URL found')
        print('Posting to webhook...')
        r.post(webhook_url, params=payload)
        print('Webhook contacted')
    else:
        print('Webhook URL not provided')
