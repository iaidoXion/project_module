import boto3
import os

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
TSoIPFS = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['FILE']['Storage']
TSoIPFNM = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['FILE']['FileName']
TSoIPFT = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['INPUT']['FILE']['FileType']

TSoOPFS = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['OUTPUT']['FILE']['Storage']
TSoOPFNM = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['OUTPUT']['FILE']['FileName']
TSoOPFT = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['OUTPUT']['FILE']['FileType']
TSoOPCS = SETTING['CORE']['Tanium']['MODULE']['SOURCE']['PLUGIN']['OUTPUT']['FILE']['chunkSize']



def main() :
    service_name = 's3'
    endpoint_url ='http://192.168.3.101:9020'
    region_name = 'kr-standard'
    access_key = 'object_user1'
    secret_key = 'ChangeMeChangeMeChangeMeChangeMeChangeMe'
    bucket_name = 'tera'

    s3 = boto3.client(service_name, endpoint_url=endpoint_url, aws_access_key_id=access_key,
                      aws_secret_access_key=secret_key)




#버킷생성
    # bucket_name = 'tera'
    # s3.create_bucket(Bucket=bucket_name)
#버킷삭제
    # bucket_name = 'sample-bucket'
    # s3.delete_bucket(Bucket=bucket_name)
#버킷조회
    # response = s3.list_buckets()
    # for bucket in response.get('Buckets', []):
    #     print(bucket.get('Name'))
    #     print(bucket.get('Size'))

#파일목록조회
    # bucket_name = 'bk1'
    #
    # # list all in the bucket
    # max_keys = 300
    # response = s3.list_objects(Bucket=bucket_name, MaxKeys=max_keys)
    # print(response)
    # print('list all in the bucket')
    #
    # while True:
    #     print('IsTruncated=%r' % response.get('IsTruncated'))
    #     print('Marker=%s' % response.get('Marker'))
    #     print('NextMarker=%s' % response.get('NextMarker'))
    #
    #     print('Object List')
    #     for content in response.get('Contents'):
    #         print(' Name=%s, Size=%d, Owner=%s' % \
    #               (content.get('Key'), content.get('Size'), content.get('Owner').get('ID')))
    #
    #     if response.get('IsTruncated'):
    #         response = s3.list_objects(Bucket=bucket_name, MaxKeys=max_keys,
    #                                    Marker=response.get('NextMarker'))
    #     else:
    #         break
    #
    # # top level folders and files in the bucket
    # # / 로  최상위 디렉토리로 가는코드
    # delimiter = '/'
    # max_keys = 300
    #
    # response = s3.list_objects(Bucket=bucket_name, Delimiter=delimiter, MaxKeys=max_keys)
    #
    # print('top level folders and files in the bucket')
    #
    # while True:
    #     print('IsTruncated=%r' % response.get('IsTruncated'))
    #     print('Marker=%s' % response.get('Marker'))
    #     print('NextMarker=%s' % response.get('NextMarker'))
    #
    #     print('Folder List')
    #     for folder in response.get('CommonPrefixes'):
    #         print(response)
    #         print(' Name=%s' % folder.get('Prefix'))
    #
    #     print('File List')
    #     for content in response.get('Contents'):
    #         print(' Name=%s, Size=%d, Owner=%s' % \
    #               (content.get('Key'), content.get('Size'), content.get('Owner').get('ID')))
    #
    #     if response.get('IsTruncated'):
    #         response = s3.list_objects(Bucket=bucket_name, Delimiter=delimiter, MaxKeys=max_keys,
    #                                    Marker=response.get('NextMarker'))
    #     else:
    #         break


#파일 다운로드
    # bucket_name = 'bk1'
    #
    # object_name = '16MBfile.json'  #버킷에 올라와있는 실제파일
    # local_file_path = '/test2222.json' #경로 및 저장할 파일명
    #
    # s3.download_file(bucket_name, object_name, local_file_path)

#파일업로드
    # bucket_name = 'bk1'
    #
    # # create folder
    # object_name = 'test2/' #폴더이름 /이거 써야 폴더
    #
    # s3.put_object(Bucket=bucket_name, Key=object_name)
    #
    # # upload file
    # object_name = 'test2/hello.txt'  #생성할 파일명
    # local_file_path = '/test22.txt' #가져올 파일명
    #
    # s3.upload_file(local_file_path, bucket_name, object_name)

#파일 삭제
    # bucket_name = 'bk1'
    # object_name = 'hello'
    #
    # s3.delete_object(Bucket=bucket_name, Key=object_name)

#멀티파트 업로드

    file = os.listdir(TSoOPFS)
    filecount = len(file)

    for i in range(0, filecount):
        object_name = '16MBfile/'+TSoOPFNM+str(i)+TSoOPFT
        local_file = TSoOPFNM + str(i) + TSoOPFT

        # initialize and get upload ID
        create_multipart_upload_response = s3.create_multipart_upload(Bucket=bucket_name, Key=object_name)
        upload_id = create_multipart_upload_response['UploadId']

        part_size = 10 * 1024 * 1024
        parts = []

        # upload parts
        with open(TSoOPFS+local_file, 'rb') as f:
            part_number = 1
            while True:
                data = f.read(part_size)
                if not len(data):
                    break
                upload_part_response = s3.upload_part(Bucket=bucket_name, Key=object_name, PartNumber=part_number,
                                                      UploadId=upload_id, Body=data)
                parts.append({
                    'PartNumber': part_number,
                    'ETag': upload_part_response['ETag']
                })
                part_number += 1

        multipart_upload = {'Parts': parts}

        # abort multipart upload
        # s3.abort_multipart_upload(Bucket=bucket_name, Key=object_name, UploadId=upload_id)

        # complete multipart upload
        s3.complete_multipart_upload(Bucket=bucket_name, Key=object_name, UploadId=upload_id,
                                     MultipartUpload=multipart_upload)