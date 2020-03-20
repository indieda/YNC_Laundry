# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2 import service_account

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1HHw4EQUwgcE-n5SEb7VRSkdObEtFvK3CUlYZlvj9Oy8'
SAMPLE_RANGE_NAME = 'Cendana!C1:D3'
SERVICE_ACCOUNT_FILE = '/Users/IndieDa/Documents/GitHub/YNCLaundryViewer-/app/cred.json'
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    service = build('sheets', 'v4', credentials=credentials)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print(row)
            #print('%s, %s' % (row[0], row[4]))

if __name__ == '__main__':
    main()