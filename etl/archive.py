import os
import zipfile

def archive_file(file_path: str) -> str:
    """
    Create a ZIP archive of the given file.
    Returns the path to the ZIP file.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    base, _ = os.path.splitext(file_path)
    zip_path = f"{base}.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(file_path, arcname=os.path.basename(file_path))
    print(f"🗜️ Archived to {zip_path}")
    return zip_path
