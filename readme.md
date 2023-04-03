## API

`public_key` and `secret_key` are created for each user.

### Get all transactions:
* method: **GET**
* endpoint: **/api/transaction/**


### Get specific transaction:
* method: **GET**
* endpoint: **/api/transaction/[uid]/**
- `uid`: unique identifier transaction


### Create a new transaction:
* method: **POST**
* endpoint: **/api/transaction/**

Example:
```
{
    "uid": "12345678",
    "device_timestamp": "2023-03-28T12:34:56+03:00",
    "received_at": "2023-03-28T12:35:00+03:00",
    "tags": ["payment", "bus", "mobile"],
    "transaction_data": {
        "uid": "d7fc4388-ca3b-4bf1-a3f2-cf525ff9a85b",
        "method": "transport_card",
        "transaction_type": "fare_purchase",
        "device_idn": "8765432198765432198",
        "additional_field1": "example_value1",
        "additional_field2": "example_value2",
        "document_number": "ABC123456"
    },
    "public_key": "f87c38f74a32275c40414580f099bb7d04bac39c",
    "sign": "a1RLIG38f7TRgevcoLRUintfUDSngLnsvMem0INRKHI="
}
```
- `uid`: unique identifier transaction
- `device_timestamp`: device time in ISO-8601 **YYYY-MM-DDThh:mm:ssTZD**
- `received_at`: received time in ISO-8601 **YYYY-MM-DDThh:mm:ssTZD**
- `tags`: _list_ of tags
- `transaction_data`: transaction data in raw form
- `public_key`: user ID 
- `sign`: unique signature of each request 

### Create sign:

#### Forming a sign string:
[_METHOD_]-[_api endpoint_]-[_request json data exclude "sign" and "private_key"_]
Example: 
`POST-/api/transaction/-{"uid":"12345678","device_timestamp":"2023-03-28T12:34:56+03:00","received_at":"2023-03-28T12:35:00+03:00","tags":["payment","bus","mobile"],"transaction_data":{"uid":"d7fc4388-ca3b-4bf1-a3f2-cf525ff9a85b","method":"transport_card","transaction_type":"fare_purchase","device_idn":"8765432198765432198","additional_field1":"example_value1","additional_field2":"example_value2","document_number":"ABC123456"}}`

#### Calculate signature from string:
Generate hmac-sha256 an authentication code from secret_key

Python example:
```
def calc_signature_from_str(sign_string):
    byte_key = bytes.fromhex(secret_key)
    lhmac = hmac.new(byte_key, digestmod=hashlib.sha256)
    lhmac.update(sign_string.encode('utf8'))
    return base64.b64encode(lhmac.digest())
```

For `secret_key` = a621e547612e6e219bd4113bdc6643dadb3d68ac 

Result `sign` = qTck456D/g/uueP5jnBtA9KePB3NPZH5dfKqd5t0XvE=

___

# Deploy with Docker
1. Install Docker
2. run `docker-compose up -d --build`
3. set migrations `docker-compose exec web python manage.py migrate`
4. add admin `docker-compose exec web python manage.py createsuperuser`
