import boto3
import logging
import os
import shlex
import subprocess
import uuid
from PIL import Image
from botocore.exceptions import ClientError
from io import BytesIO

s3_client = boto3.client('s3')


def load_image_from_s3(bucket, key):
    file_byte_string = s3_client.get_object(Bucket=bucket, Key=key)['Body'].read()
    return Image.open(BytesIO(file_byte_string))


def create_presigned_url(bucket_name, object_name, expiration=3600):
    """Generate a presigned URL to share an S3 object

    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name, 'Key': object_name},
                                                    ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response


def handle(event, context):
    logger.info(event)

    bucket = event['s3']['bucket']['name']
    key = event['s3']['object']['key']

    if 'video' in key:

        url = create_presigned_url(bucket, key, expiration=60)
        if url:
            thumbnail = f'/tmp/thumbnail-{uuid.uuid4().hex}.png'

            # -ss Input seeking (https://trac.ffmpeg.org/wiki/Seeking#Inputseeking)
            #     Needs to be specified somewhere before -i.
            #
            # -filter:v scale=...
            #     (https://trac.ffmpeg.org/wiki/Scaling see "Fitting into a Rectangle / Statically-sized Player")
            cmd = f"/opt/python/ffmpeg -ss 00:00:00.500 -i {url!r} -frames:v 1 -filter:v scale=w=185:h=328:force_original_aspect_ratio=decrease {thumbnail!r}"
            subprocess.run(shlex.split(cmd), check=True)

            if os.path.isfile(thumbnail):
                s3_client.upload_file(thumbnail, bucket, new_key)

    return
