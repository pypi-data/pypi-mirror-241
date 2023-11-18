import os
import math
import requests
from tqdm import tqdm

class MultipartUpload():
    UPLOAD_PART_SIZE = (1024 * 1024) * 8

    def __init__(self, local_path: str, remote_path: str, endpoint: str, headers: dict, use_path: bool = False):
        self._local_file_path = local_path
        self._remote_file_path = remote_path
        self._file_size = os.path.getsize(local_path)
        self._file_parts = math.ceil(self._file_size / self.UPLOAD_PART_SIZE)
        self._use_path = use_path
        
        self._endpoint = endpoint
        self._headers  = headers

        # Dynamically update upload threshold based on file size
        self.UPLOAD_PART_SIZE = min(self.UPLOAD_PART_SIZE, self._file_size)
        
    @property
    def local_file_path(self) -> str:
        return self._local_file_path
    
    @property
    def remote_file_path(self) -> str:
        return self._remote_file_path
    
    @property
    def file_name(self) -> str:
        return self.local_file_path.split('/')[-1]

    @property
    def file_size(self) -> int:
        return os.stat(self.local_file_path).st_size

    @property
    def file_parts(self) -> int:
        return self._file_parts


    def upload(self):
        upload_id = self._upload_multipart_init()
        parts     = self._upload_multipart_parts(upload_id)
        self._upload_multipart_complete(upload_id, parts)


    def _upload_multipart_init(self):
        '''
        Begin the multi-part upload process.
        
        This returns an upload ID that is used to identify the upload. All
        subsequent actions will use this upload ID.
        '''
        return requests.post(
            url = f'{self._endpoint}/upload',
            headers = self._headers,
            json = {
                'key': self.remote_file_path if self._use_path else self.file_name
            }
        ).json()['uploadId']


    def _upload_multipart_parts(self, upload_id):
        '''
        Upload the file, piece by piece.
        
        Uploads the file in pieces, dictated by the UPLOAD_PART_SIZE constant.
        Each part requests a signed URL, uploads the part, and then returns the
        hash/etag of the part.
        '''
        parts = []
        with tqdm(
            desc=self.file_name,
            total=self.file_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            with open(self.local_file_path, 'rb') as file:
                while True:
                    # read() will just read up to EOF - once it's out of data, it
                    # will return an empty string
                    data = file.read(self.UPLOAD_PART_SIZE)
                    if not data:
                        return parts

                    # We need to get a signed URL for each and every part
                    response = requests.post(
                        url =  f'{self._endpoint}/presign',
                        headers = self._headers,
                        json = {
                            'key': self.remote_file_path if self._use_path else self.file_name,
                            'uploadId': upload_id,
                            'partNumber': len(parts) + 1
                        }
                    ).json()['url']

                    # Actually upload the part
                    upload_response = requests.put(
                        url = response,
                        data = data
                    )

                    # The response from the upload will contain the hash/etag of the
                    # part - this is used to complete the upload
                    parts.append(
                        {
                            'PartNumber': len(parts) + 1, 
                            'ETag': upload_response.headers['ETag']
                        }
                    )

                    # Add read file size to tqdm bar
                    bar.update(self.UPLOAD_PART_SIZE)


    def _upload_multipart_complete(self, upload_id, parts):
        '''
        Signal that the upload is complete.
        '''
        requests.post(
            url =  f'{self._endpoint}/complete',
            headers = self._headers,
            json = {
                'key': self.remote_file_path if self._use_path else self.file_name,
                'uploadId': upload_id,
                'parts': parts
            }
        )
