from azure.storage.blob import BlockBlobService
from azure.storage.blob import PublicAccess

import os

account_name = 'weekcookrecipestorage'
account_key = 'CSsRDZuNlvEnOHnTzPL1ju7hXBwU2EBEqOIIketvrgPDBdNqic88/rz37h+wG8su/B50ALwz/kV7ZMXy+pKS4g=='
container_name = 'betterhome'
src_dir = 'postprocess'

service = BlockBlobService(
    account_name=account_name,
    account_key=account_key,
)

service.create_container(container_name)
print('create_container')
for i in os.listdir(src_dir):
    print(i)
    service.create_blob_from_path(container_name, str(i), os.path.join(src_dir, i))
