import os

def IP():
    return os.getenv('LOCAL-TARGET-IP')

def PORT():
    return os.environ.get('LOCAL-TARGET-PORT', '8060')
    
def WEBHOOK_URL():
    return os.getenv('ON-READY-WEBHOOK-URL')
