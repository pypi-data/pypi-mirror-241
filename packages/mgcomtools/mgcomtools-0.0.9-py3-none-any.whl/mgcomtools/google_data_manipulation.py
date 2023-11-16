from google.cloud import storage
storage_client = storage.Client()


class gcsfiles:

    def __init__(self, destination=destination, source=None,  method='copy'):
        
        if source:
            self.source_bucket, self.source_blob = self.prepare_link(source)
            
        self.destination_bucket, self.destination_blob = self.prepare_link(destination)
        self.status = f"{method}:\n{self.source_blob.name}\n===>\n{self.destination_blob.name}"
        
        print(self.status)
        if method == 'copy':
            self.copy()
        elif method == 'move':
            self.remove()
        elif method == 'delete':
            self.delete()
            
            
    def prepare_link(self, path):
        
        parsed_path = path.replace('gs://', '').split('/')
        bucket_name = parsed_path[0]
        blob_name = '/'.join(parsed_path[1:])
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        return bucket, blob
        
    
    def copy(self):
        
        rewrite_token = ''
        while rewrite_token is not None:
            rewrite_token, bytes_rewritten, bytes_to_rewrite = self.destination_blob.rewrite(
              self.source_blob, token=rewrite_token)
            print(f'Progress so far: {bytes_rewritten}/{bytes_to_rewrite} bytes.')
            
            
    def delete(self):

        blobs = self.destination_bucket.list_blobs(prefix=self.destination_blob.name)
        
        count = 0
        for blob in blobs:
            blob.delete()
            print('deleted:', blob.name)
            count += 1
        
        if count == 0:
            print('No one file has been deleted')
            
            
    def remove(self):
        self.copy()
        self.delete()
        
source = 'gs://adriver-raw/ftp/MGCom_/202311010838__2023-10-31.logad.csv.gz'
destination = 'gs://archive-old-files/adriver/raw/ftp/MGCom_/test/large.csv.gz'
        
a = GcsFiles(source=source, destination=destination, method='move')