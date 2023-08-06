from flask import Flask, request
from pyngrok import ngrok

import requests as r
import click
import os


app = Flask(__name__)

def IP():
    return os.getenv('LOCAL-TARGET-IP')

def PORT():
    return os.environ.get('LOCAL-TARGET-PORT', '8060')
    
def WEBHOOK_URL():
    return os.getenv('ON-READY-WEBHOOK-URL')


@app.route('/',  defaults={'path': ''})
@app.route('/<path:path>')
def path(path):
    ip = IP()
    port = PORT()

    if ip:
        target = os.path.join(f'http://{ip}:{port}', path)
        resp = r.get(target, headers=request.headers, cookies=request.cookies, payload=request.data)
        return (resp.text, resp.status_code, resp.headers.items())
    else:
        return {'error': 'No LAN target specified'}


def notify_on_start_webhook(tunnel_url: str = ''):
    payload = {
        'tunnel-url': tunnel_url,
        'comment': 'Have a nice a day!'
    }
    webhook_url = WEBHOOK_URL()

    if webhook_url:
        r.post(webhook_url, params=payload)


@click.command()
@click.argument('host-ip', type=str)
@click.argument('host-port', type=int)
@click.option('-i', '--target-ip', type=str, default=None)
@click.option('-p', '--target-port', type=str, default=None)
@click.option('-d', '--debug', is_flag=True)
@click.option('-t', '--token', type=str, default=None)
@click.option('-w', '--on-start-webhook-url', type=str, default=None)
def cli(
        host_ip: str, 
        host_port: int, 
        target_ip: str, 
        target_port: int, 
        debug: bool, 
        token: str,
        on_start_webhook_url: str
        ):

    if target_ip:
        os.environ['LOCAL-TARGET-IP'] = target_ip
    if target_port:
        os.environ['LOCAL-TARGET-PORT'] = target_port
    if on_start_webhook_url:
        os.environ['ON-READY-WEBHOOK-URL'] = on_start_webhook_url

    if token:
        ngrok.set_auth_token(token)
        

    tunnel = ngrok.connect(host_port, enforce_tls=True)
    notify_on_start_webhook(tunnel.public_url)

    try:
        app.run(host_ip, host_port, debug=debug)
    except KeyboardInterrupt:
        ngrok.disconnect(tunnel.public_url)

if __name__ == '__main__':
    cli()
