from __future__ import print_function
from django.http import JsonResponse
from django.shortcuts import render

import os
import sys


import os.path
from django import apps

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

arr_id = [] 
def test(request):
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=9009)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('drive', 'v3', credentials=creds)

        # Call the Drive v3 API
        
        
        results = service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)" ,q="'1-5WOgdVjb4ybBX0DQE7qKaUMfBc6m3Ee' in parents and mimeType = 'application/vnd.google-apps.folder'" ).execute()
        
        print(results)
        items = results.get('files', [])
        
        
        
        
        #results = service.files().listFile( {'q': "'1-5WOgdVjb4ybBX0DQE7qKaUMfBc6m3Ee' in parents"}).getList()
        #items = results.get('files', [])

        arr_name= []
        global arr_id
        
        count = 100
        
        if not items:
            print('No files found.')
            return
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))
            arr_name.append(item['name'])
            arr_id.append(item['id'])
        
        
        
        
        
            
        return render(request,'base.html',{'items':items,'result':results,'arr_name':arr_name,'arr_id': arr_id,'count':count})
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')
        
        

def test_user2(request):
    result = request.GET['filename']
   # i  = request.GET['flag_counter']
    #items = request.GET['items']
    
    #print(items)

   # j = int(i)

    #print(arr_id[j])
    
    print(result) 
   # print(i)
    flag_data = 1 
    
    data = {"flag_data": flag_data}
    
    return JsonResponse(data)



