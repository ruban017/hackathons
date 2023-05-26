#grive.py


import os
import io
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.errors import HttpError



scopes = ['https://www.googleapis.com/auth/drive']

def auth():
  global creds
  global service
  creds = None
  if (os.path.exists('token.json')):
    print('good')
    creds = Credentials.from_authorized_user_file('token.json', scopes)
    service = build('drive', 'v3', credentials = creds)
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file("secrets.json", scopes)
      creds = flow.run_local_server(port = 0)
    with open('token.json', 'w') as token:
      token.write(creds.to_json())


def search_file(path):

    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)
        files = []
        page_token = None
        folder_id = '1zapr6zulAKckwAhNOaQDlH2ZsxirsdMj'
        query = f"parents = '{folder_id}'"
        while True:
            # pylint: disable=maybe-no-member
            response = service.files().list(q=query,
                                            spaces='drive',
                                            fields='nextPageToken, '
                                                   'files(id, name)',
                                            pageToken=page_token).execute()
            for file in response.get('files', []):
                if file.get("name") == path:
                    print("desired file found")
                    file_id = file.get("id")
                    file_name = path
                    print(file_id)
                    print(file_name)
                    request = service.files().get_media(fileId=file_id)
                    fh = io.BytesIO()
                    downloader = MediaIoBaseDownload(fd=fh, request= request)
                    done = False
                    while not done:
                        status, done = downloader.next_chunk()
                        print(f"Download progress {status.progress()*100}")
                    fh.seek(0)
                    with open(os.path.join('C:/Users/raman/Desktop/code/srm ramapuram', file_name), 'wb') as f:
                        f.write(fh.read())
                        f.close()

                    return path
                    

            files.extend(response.get('files', []))
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break

    except HttpError as error:
        print(F'An error occurred: {error}')
        files = None