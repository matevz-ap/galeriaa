from __future__ import print_function

from typing import Any

from allauth.socialaccount.models import SocialToken
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def get_google_credentials(user_id: int) -> Credentials:
    social_token = SocialToken.objects.get(account__user=user_id)
    credentials = Credentials(
        token=social_token.token,
        refresh_token=social_token.token_secret,
        client_id=social_token.app.client_id,
        client_secret=social_token.app.secret,
        token_uri="https://accounts.google.com/o/oauth2/token",
    )
    if credentials and credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())
    return credentials


def get_files_from_folder(user_id: int, folder_id: int):
    credentials = get_google_credentials(user_id)
    try:
        service = build("drive", "v3", credentials=credentials)
        files = []
        page_token = None
        while True:
            query = f"parents='{folder_id}' and trashed=false"

            response = (
                service.files()
                .list(
                    q=query,
                    spaces="drive",
                    fields="nextPageToken, files(id, name, mimeType)",
                    pageToken=page_token,
                )
                .execute()
            )
            files.extend(response.get("files", []))
            page_token = response.get("nextPageToken", None)
            if page_token is None:
                break

    except HttpError as error:
        print(f"An error occurred: {error}")
        files = None

    return files


def update_gallery_data(gallery):
    files = get_files_from_folder(gallery.user_id, gallery.folder)
    # for i, file in enumerate(files):
    #     file["order"] = i
    gallery.data = files
    gallery.save(update_fields=("data",))


def get_drive_folders(user_id: int) -> list[Any] | None:
    credentials = get_google_credentials(user_id)

    try:
        service = build("drive", "v3", credentials=credentials)
        files = []
        page_token = None
        while True:
            query = "mimeType='application/vnd.google-apps.folder' and trashed=false"
            response = (
                service.files()
                .list(
                    q=query,
                    spaces="drive",
                    fields="nextPageToken, files(id, name, mimeType)",
                    pageToken=page_token,
                )
                .execute()
            )
            files.extend(response.get("files", []))
            page_token = response.get("nextPageToken", None)
            if page_token is None:
                break

    except HttpError as error:
        print(f"An error occurred: {error}")
        files = None

    return files
