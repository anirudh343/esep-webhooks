import requests

def handler(event, context):
    message = 'Issue Created: ' + event['issue']['html_url']
    payload = {'text': message}
    response =  requests.post(
        url='{do not check in this URL}', 
        json = payload,
        headers={'Content-Type': 'application/json'}
    )
    return response.text 