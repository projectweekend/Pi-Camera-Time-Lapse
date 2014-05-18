from dropbox import client
from .settings import DROPBOX_TOKEN_FILE, DROPBOX_KEY, DROPBOX_SECRET


def save_auth_token(auth_token):
    with open(DROPBOX_TOKEN_FILE, 'w+') as f:
        f.write(auth_token)
    return auth_token


def authentication_flow():
    auth_successful = False
    while not auth_successful:
        flow = client.DropboxOAuth2FlowNoRedirect(DROPBOX_KEY, DROPBOX_SECRET)
        authorize_url = flow.start()
        print('1. Go to: ' + authorize_url)
        print('2. Click "Allow" (you might have to log in first)')
        print('3. Copy the authorization code')
        code = raw_input('Enter the authorization code here: ').strip()
        try:
            auth_token, user_id = flow.finish(code)
        except client.ErrorResponse:
            print('ERROR: Invalid authorization code. Please try again.')
            print('')
        else:
            save_auth_token(auth_token)
            auth_successful = True
