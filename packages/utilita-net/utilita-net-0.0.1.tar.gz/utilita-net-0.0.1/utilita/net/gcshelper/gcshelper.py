"""
gcshelp = new GCSHelper()

- should accept a way to pub a message to whatever
- should accept upload a file to a bucket (parameter to compress???)

"""

import sys
import argparse
import os
import json
from io import BytesIO
from tempfile import NamedTemporaryFile
from google.cloud import pubsub_v1


class GCSHelper:
    
    def __init__(self, project_id:str):
        assert project_id is not None, 'project_id must be set'
        assert 'GOOGLE_APPLICATION_CREDENTIALS' in os.environ, 'Missing GOOGLE_APPLICATION_CREDENTIALS environment variable.'
        self.project_id = project_id

    def pub_get_messages(self, topic:str, batch_size:int=25) -> list:
        """Get a json string from pubsub. Will be a list of json objects."""
        pass

    def pub_pub_messages(self, topic:str, data:dict) -> int:
        """Pub a dict message to pubsub. Will be converted to json when the request actually gets submitted."""
        pass

    def download_bucket_data_to_bytes(self, full_path:str, download_path:str) -> bytes:
        """Downloads a file from a GCS bucket. Returns as bytes.

        full_path - Fully qualified path name, in the form of gs://bucket_name/path/to/blob.txt
        """
        pass

    def download_bucket_data_to_path(self, full_path:str, download_path:str) -> str:
        """Downloads a file from a GCS bucket. Downloads to a directory.

        full_path - Fully qualified path name, in the form of gs://bucket_name/path/to/blob.txt
        
        download_path - Full path of download file (inclduing filename)
        """
        pass

        # Might not implement this....
    def download_bucket_data_to_str(self, full_path:str, download_path:str) -> str:
        """Downloads a file from a GCS bucket. Returns as a str

        full_path - Fully qualified path name, in the form of gs://bucket_name/path/to/blob.txt
        
        download_path - Directory where file(s) should be stored.
        """
        pass


    def upload_bucket_data_from_path(self, file_path:str, gcs_full_path:str) -> str:
        '''Open a path on the filesystem, the uploads it to GCS.
        
        args:
            file_path (str): Full or relative file path on the filesystem.
        '''
        pass

    def upload_bucket_data_from_str(self, data:str, gcs_full_path:str) -> str:
        """Gets data as a str, then sends it up to GCS as a blob."""
        pass

    def upload_bucket_data_from_bytes(self, bytes_data:bytes, gcs_full_path:str) -> str:
        """Gets data as a bytes object, then sends it up to GCS"""
        pass



def parse_gs_string(input_str: str) -> dict:
    assert input_str.lower().startswith('gs://'), f"Missing gs:// identifier"
    chunks = input_str[5:].split('/')  # Skipping 'gs://'
    bucket = chunks[0]
    object_path = '/'.join(chunks[1:])
    return {
        'bucket': bucket,
        'object_path': object_path
    }

def to_gs_string(bucket_name: str, list_of_blobs: list) -> list:
    return [f'gs://{bucket_name}/{b}' for b in list_of_blobs]

###



a = GCSHelper(project_id='derp')

a.upload_bucket_data_from_path()
