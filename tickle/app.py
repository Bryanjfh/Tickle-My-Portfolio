from chalice import Chalice
import boto3
import json
import yaml

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

app = Chalice(app_name='tickle')


@app.route('/xping')
def index():
    return {'Success': 'Bro'}


@app.route('/testput')
def test_put():
    dynamodb.Table('Portfolios').put_item(
        Item={
            'user': 'Chino',
            'stocks': [{'symbol': 'BRK.B', 'price': 205, 'quantity': 5},
                       {'symbol': 'SNAP', 'price': 1, 'quantity': 150}]
        })
    return {'hello': 'world'}


@app.route('/addstocks/{user}', methods=['POST', 'OPTIONS'])
def test_update(user):
    print 'we here tho'
    print type(app.current_request.json_body)
    stocks2 = build_stock_list(app.current_request.json_body)
    stocks = [{'symbol': 'ADAM', 'price': 205, 'quantity': 5},
                {'symbol': 'SNAP', 'price': 1, 'quantity': 150}]
    print '\n\n\n\n\n\n\n\n'
    print stocks
    print '\n\n\n\n\n\n\n\n'
    print stocks2
    print '\n\n\n\n\n\n\n\ncomparing: '
    print cmp(stocks, stocks2)
    dynamodb.Table('Portfolios').update_item(
        Key={
            'user': user
        },
        UpdateExpression="SET stocks = list_append(stocks, :stockvals)",
        ExpressionAttributeValues={":stockvals": stocks2}
    )
    return {'hello': 'world'}


@app.route('/value/portfolio/user/{user}', methods=['GET'])
def portfolio_value(user):
    return {"portfolio value for user: {}".format(user): 90000000000}


@app.route('/addvalue/crypto/user/{user}', methods=['POST', 'OPTIONS'])
def add_value(user):
    stuff = app.current_request.json_body
    return {user: stuff}


def build_stock_list(json_input):
    print 'we here now'
    stocks = list()
    json_input = json_input['stocks']
    for stock in json_input:
        new_stock = json.dumps(stock)
        new_stock = yaml.safe_load(new_stock)
        new_stock2 = {'symbol': new_stock['symbol'], 'price': new_stock['price'], 'quantity': new_stock['quantity']}
        stocks.append(new_stock2)
    return stocks
