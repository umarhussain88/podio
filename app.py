import requests
from dotenv import load_dotenv
import os


load_dotenv()

api_key = os.getenv('CLIENT_ID')
api_secret = os.getenv('CLIENT_SECRET')

def authenticate_podio_api(api_key, api_secret):
    auth_url = 'https://podio.com/oauth/token'
    auth_data = {
        'grant_type': 'client_credentials',
        'client_id': api_key,
        'client_secret': api_secret
    }
    auth_response = requests.post(auth_url, data=auth_data)
    if auth_response.status_code == 200:
        access_token = auth_response.json()['access_token']
        return access_token
    else:
        raise Exception('Failed to authenticate with Podio API')
    
def get_all_contacts(access_token):
    contacts_url = 'https://api.podio.com/contact/'
    headers = {'Authorization': 'OAuth2 {}'.format(access_token)}
    contacts_response = requests.get(contacts_url, headers=headers)
    if contacts_response.status_code == 200:
        contacts = contacts_response.json()
        return contacts
    else:
        raise Exception('Failed to retrieve contacts from Podio API')

def get_all_tasks(access_token):
    tasks_url = 'https://api.podio.com/task/'
    headers = {'Authorization': 'OAuth2 {}'.format(access_token)}
    tasks_response = requests.get(tasks_url, headers=headers)
    if tasks_response.status_code == 200:
        tasks = tasks_response.json()
        return tasks
    else:
        raise Exception('Failed to retrieve tasks from Podio API')    

    
if __name__ == '__main__':
    access_token = authenticate_podio_api(api_key, api_secret)
    print(access_token)
    # contacts = get_all_contacts(access_token)
    tasks = get_all_tasks(access_token)
    print(tasks)