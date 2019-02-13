import json
import os

import boto3
import dotenv
from flask import Flask, jsonify, request

app = Flask(__name__)
dotenv.load_dotenv()

S3_BUCKET_NAME = 'nl.opper.aws-test'


@app.route('/validate/<string:id>', methods=['POST'])
def post(id: str) -> None:
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.environ.get('AWS_SECRET_KEY_ID'),
        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
    )
    key = 'aws-test.{}.json'.format(id)

    try:
        obj = s3.get_object(Bucket=S3_BUCKET_NAME, Key=key)

        return jsonify({
            'data': json.loads(obj['Body'].read())
        })
    except s3.exceptions.NoSuchKey:
        response = s3.put_object(Body=json.dumps(request.json.get('data')).encode(), Key=key, Bucket=S3_BUCKET_NAME)

        return jsonify({
            'data': response
        })


if __name__ == '__main__':
    app.run(debug=True)
