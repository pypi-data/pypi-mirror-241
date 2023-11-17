
from google.cloud import storage
from pathlib import Path

def download_folder(destination_dir_path,remote_bucket_name,remote_folder_path_relative_to_bucket):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(remote_bucket_name)
    blobs = bucket.list_blobs(prefix=remote_folder_path_relative_to_bucket)  # Get list of files
    for blob in blobs:
        if blob.name.endswith("/"):
            continue

        file_split = blob.name.split("/")
        file_name = file_split[-1]
        relative_dir = Path("/".join(file_split[0:-1]))
        final_file_local_path = destination_dir_path/relative_dir/file_name
        if final_file_local_path.exists():
            continue
        (destination_dir_path/relative_dir).mkdir(parents=True, exist_ok=True)
        blob.download_to_filename(final_file_local_path)