from chalice import Chalice
import boto3
import boto3
import json
import yaml
import requests

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
def test_put():
    dynamodb.Table('Portfolios').put_item(
        Item={
            'user': 'Chino',
            'stocks': [{'symbol': 'BRK.B', 'price': 205, 'quantity': 5},
                       {'symbol': 'SNAP', 'price': 1, 'quantity': 150}]
        })
    return {'hello': 'world'}


@app.route('/addstocks/user/{user}', methods=['POST', 'OPTIONS'])
def test_update(user):
    stocks2 = list()
    json_input = app.current_request.json_body['stocks']
    for stock in json_input:
        new_stock = json.dumps(stock)
        new_stock = yaml.safe_load(new_stock)
        new_stock2 = {
            'symbol': new_stock['symbol'], 'price': new_stock['price'], 'quantity': new_stock['quantity']}
        stocks2.append(new_stock2)

    dynamodb.Table('Portfolios').update_item(
        Key={
            'user': user
        },
        UpdateExpression="SET stocks = list_append(if_not_exists(stocks, :empty_list), :stockvals)",
        ExpressionAttributeValues={":stockvals": stocks2, ":empty_list": []}
    )
    return 200


@app.route('/addcryptos/user/{user}', methods=['POST', 'OPTIONS'])
def test_update(user):
    cryptos2 = list()
    json_input = app.current_request.json_body['crypto']
    for stock in json_input:
        crypto = json.dumps(stock)
        crypto = yaml.safe_load(crypto)
        crypto2 = {
            'symbol': crypto['symbol'], 'price': crypto['price'], 'quantity': crypto['quantity']}
        cryptos2.append(crypto2)

    dynamodb.Table('Portfolios').update_item(
        Key={
            'user': user
        },
        UpdateExpression="SET cryptos = list_append(if_not_exists(cryptos, :empty_list), :cryptovals)",
        ExpressionAttributeValues={":cryptovals": cryptos2, ":empty_list": []}
    )
    return 200


@app.route('/value/portfolio/user/{user}', methods=['GET'])
def portfolio_value(user):
    stuff = dynamodb.Table('Portfolios').get_item(
        Key={'user': user}
    )
    stocks = list()
    for stock in stuff['Item']['stocks']:
        stocks.append({'symbol': stock['symbol'], 'quantity': stock['quantity']})
    return total_stock_value(stocks)


@app.route('/addvalue/crypto/user/{user}', methods=['POST', 'OPTIONS'])
def add_value(user):
    stuff = app.current_request.json_body
    return {user: stuff}


def total_stock_value(stock_symbols):
    value = 0
    symbols = ""
    for symbol in stock_symbols:
        symbols += (symbol['symbol'] + ",")
    results = yaml.safe_load(requests.get("https://api.iextrading.com/1.0/stock/market/batch?symbols={}&types=price".format(symbols)).content)
    for result in results:
        quant = int()
        for symbol in stock_symbols:
            print type(symbol['quantity'])
            if symbol['symbol'].encode('ascii') == result:
                quant = int(symbol['quantity'])
            price = results[result]['price']
        value += (price * quant)
    return {'total_stock': value}
