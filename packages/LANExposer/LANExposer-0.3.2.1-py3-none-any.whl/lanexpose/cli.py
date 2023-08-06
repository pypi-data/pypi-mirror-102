from flask import Flask, request
from pyngrok import ngrok

from .env import IP, PORT
from .webhooks import notify_on_start_webhook

import requests as r
import click
import os
import threading

app = Flask(__name__)



@app.route('/',  defaults={'path': ''}, methods=['GET', 'POST', 'DELETE', 'PUT'])
@app.route('/<path:path>')
def path(path):
    ip = IP()
    port = PORT()

    if ip:
        target = os.path.join(f'http://{ip}:{port}', path)
        resp = getattr(r, request.method.lower())(target, headers=request.headers, cookies=request.cookies, data=request.data)
        if app.debug:
            print(resp.content, resp.status_code, resp.headers.items())
        return resp.content, resp.status_code, resp.headers.items() 
    else:
        return {'error': 'No LAN target specified'}


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
        

    tunnel = ngrok.connect(host_port)
    try:
        t = threading.Thread(target=app.run, args=(host_ip, host_port), kwargs={'debug': debug})
        t.start()
        notify_on_start_webhook(tunnel.public_url)
        t.join()
    except KeyboardInterrupt:
        ngrok.disconnect(tunnel.public_url)

if __name__ == '__main__':
    cli()
