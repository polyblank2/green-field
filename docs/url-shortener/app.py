import os
import boto3
import hashlib

from chalice import Chalice, Response, BadRequestError
from chalice import NotFoundError

# Setup
app = Chalice(app_name='url-shortener')
app.debug = True

DDB = boto3.client('dynamodb')


@app.route('/', methods=['POST'])
def shorten():
	# Grab request url
	url = app.current_request.json_body.get('url', '')
	# url=url.encode('utf-8')
	#url = str(url)
	if not url:
		raise BadRequestError("Missing URL")
	digest = hashlib.md5(url.encode('utf-8')).hexdigest()[:6]
	# Store in dynamodb.
	DDB.put_item(
		TableName=os.environ['APP_TABLE_NAME'],
		Item={'identifier': {'S': digest},
				'url': {'S': url}})
	return {'shortened': digest}


@app.route('/{identifier}', methods=['GET'])
def retrieve(identifier):
	# Retrieve url from dynamodb
	try:
		record = DDB.get_item(Key={'identifier': {'S': identifier}},
		TableName=os.environ['APP_TABLE_NAME'])
	except Exception as e:
		raise NotFoundError(identifier)
	return Response(
		status_code=301,
		headers={'Location': record['Item']['url']['S']},
		body='')