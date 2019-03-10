from google.cloud import storage
from google.oauth2 import service_account

PROJECT = "jasonrdsouza"
BUCKET = "dsouza-logs"
TEST_FILE = "test.txt"
CREDENTIALS_FILE = "credentials.json"


def upload_blob(bucket_client, source_filename, destination_name):
    blob = bucket_client.blob(destination_name)
    blob.upload_from_filename(source_filename)


if __name__ == "__main__":
    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIALS_FILE)
    scoped_credentials = credentials.with_scopes(
        ['https://www.googleapis.com/auth/devstorage.read_write'])
    storage_client = storage.Client(
        project=PROJECT, credentials=scoped_credentials)
    bucket_client = storage_client.bucket(BUCKET)
    upload_blob(bucket_client, TEST_FILE, "test/{}".format(TEST_FILE))
    print("Log upload complete")
