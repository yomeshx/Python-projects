#I asked Chat GPT to : "Write a python program that can run in the background of the windows that creates a log file in text format in the google drive that shows items of a given directory and update that when changes made to that directory"
import os
import time
import datetime
import shutil
import logging

from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set the directory you want to monitor and the Google Drive folder ID where you want to store the log file
directory_to_monitor = "C:\\Users\\User\\Documents\\MyFolder"
google_drive_folder_id = "1234567890abcdefghijklmnopqrstuvwxyz"

# Set the file name and path for the log file
log_file_name = "directory_log.txt"
log_file_path = os.path.join(directory_to_monitor, log_file_name)

# Set up the Google Drive API client
SCOPES = ['https://www.googleapis.com/auth/drive']
service = build('drive', 'v3', credentials=credentials)

def get_folder_id(folder_name, parent_id):
    """Get the ID of the folder with the given name and parent ID.
    
    If the folder does not exist, create it.
    """
    query = f"'{parent_id}' in parents and mimeType='application/vnd.google-apps.folder' and trashed = false and name='{folder_name}'"
    try:
        # Search for the folder
        response = service.files().list(q=query, spaces='drive').execute()
        # Get the folder ID
        folder_id = response['files'][0]['id']
    except IndexError:
        # Create the folder
        folder_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [parent_id]
        }
        folder = service.files().create(body=folder_metadata, fields='id').execute()
        # Get the folder ID
        folder_id = folder['id']
    return folder_id

def check_for_changes():
    """Check for changes in the directory and update the log file as necessary."""
    # Get the current list of items in the directory
    current_items = os.listdir(directory_to_monitor)
    # Open the log file
    with open(log_file_path, "a") as log_file:
        # Check for added items
        for item in current_items:
            if item not in previous_items:
                # An item has been added, log it and update the previous items list
                log_file.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {item} was added.\n")
                previous_items.append(item)
        # Check for removed items
        for item in previous_items:
            if item not in current_items:
                # An item has been removed, log it and update the previous items list
                log_file.
