import requests

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def download_file_from_google_drive(gdrive_url):

    id = gdrive_url.split('/')[5]

    URL = "https://docs.google.com/uc?export=download"
    session = requests.Session()
    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)
    print('Response status code - {response.status_code}')
    params = { 'id' : id, 'confirm' : token }
    response = session.get(URL, params = params, stream = True)
    return response
    # return None