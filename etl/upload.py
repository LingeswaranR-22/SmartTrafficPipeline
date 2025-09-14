# etl/upload.py
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

FOLDER_MIME = "application/vnd.google-apps.folder"

def get_drive() -> GoogleDrive:
    """
    Authenticate once and return a GoogleDrive instance.
    Requires client_secrets.json in project root.
    First run opens a browser; token will be cached for reuse.
    """
    gauth = GoogleAuth()
    # Optional: uncomment and configure settings.yaml if needed
    # gauth.LoadClientConfigFile("client_secrets.json")
    gauth.LocalWebserverAuth()
    return GoogleDrive(gauth)

def _find_or_create_folder(drive: GoogleDrive, name: str, parent_id: str | None = None) -> str:
    """
    Return folder ID by name under parent_id; create if missing.
    """
    q = f"mimeType='{FOLDER_MIME}' and trashed=false and title='{name}'"
    if parent_id:
        q += f" and '{parent_id}' in parents"
    matches = drive.ListFile({"q": q}).GetList()
    if matches:
        return matches[0]["id"]

    metadata = {"title": name, "mimeType": FOLDER_MIME}
    if parent_id:
        metadata["parents"] = [{"id": parent_id}]
    folder = drive.CreateFile(metadata)
    folder.Upload()
    return folder["id"]

def upload_to_drive(file_path: str, drive: GoogleDrive,
                    root_folder: str = "SmartTrafficPipeline",
                    subfolder: str | None = None,
                    upload_name: str | None = None) -> str:
    """
    Upload a local file using the provided drive instance.
    Returns uploaded file ID.
    """
    root_id = _find_or_create_folder(drive, root_folder)
    parent_id = root_id
    if subfolder:
        parent_id = _find_or_create_folder(drive, subfolder, parent_id=root_id)

    title = upload_name if upload_name else os.path.basename(file_path)
    gfile = drive.CreateFile({"title": title, "parents": [{"id": parent_id}]})
    gfile.SetContentFile(file_path)
    gfile.Upload()
    print(f"📤 Uploaded {title} to Drive folder: {root_folder}/{subfolder or ''}".rstrip('/'))
    return gfile["id"]
