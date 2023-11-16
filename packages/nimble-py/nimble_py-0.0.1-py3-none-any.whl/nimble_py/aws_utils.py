
def get_s3_last_modified(s3_client, s3_path):
    s3_path_split = s3_path.replace('s3://', '').split('/')
    
    bucket = s3_path_split[0]
    prefix = '/'.join(s3_path_split[1:])
    
    objects = s3_client.list_objects(Bucket=bucket, Prefix=prefix)
    max_modified_date = datetime.datetime(1970, 1, 1)
    if 'Contents' in objects:
        for object_ in objects['Contents']:
            last_modified = object_['LastModified'].replace(tzinfo=None)
            if max_modified_date < last_modified:
                max_modified_date = last_modified
    return max_modified_date

def read_latest_file_from_s3(s3_client, s3_path, return_file_name = False):

    s3_path_split = s3_path.replace('s3://', '').split('/')
    
    bucket = s3_path_split[0]
    prefix = '/'.join(s3_path_split[1:])
    
    contents = s3_client.list_objects(Bucket=bucket, Prefix=prefix)['Contents']

    objs = {}
    for objects in contents:
        last_modified = objects['LastModified'].replace(tzinfo=None)
        objs[last_modified] = objects['Key']

    latest_datetime = sorted(objs)[-1]
    latest_file = objs[latest_datetime]

    log_info(f"Read latest rider file from s3 - Filename : {latest_file}, updated_at : {latest_datetime}")

    response_file = s3_client.get_object(Bucket=bucket, Key=latest_file)
    
    latest_file_df = pd.read_feather(io.BytesIO(response_file['Body'].read()))

    if return_file_name:
        return latest_file_df, latest_file
    
    return latest_file_df
