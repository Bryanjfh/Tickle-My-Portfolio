from chalice import Chalice
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

app = Chalice(app_name='tickle')


@app.route('/xping')
def index():
    print("Table status: trying")
    table = dynamodb.create_table(
        TableName='Portfolios',
        KeySchema=[
            {
                'AttributeName': 'user',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'user',
                'AttributeType': 'S'
            }

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

    print("Table status:", table.table_status)
    return {'hello': 'world'}


@app.route('/testput')
def index():
    dynamodb.Table('Portfolios').put_item(
        Item={
            'user': 'Chino'
        })
    return {'hello': 'world'}


@app.route('/value/portfolio/user/{user}', methods=['GET'])
def portfolio_value(user):
    return {"portfolio value for user: {}".format(user): 90000000000}


@app.route('/addvalue/crypto/user/{user}', methods=['POST'])
def add_value(user):
    return user

