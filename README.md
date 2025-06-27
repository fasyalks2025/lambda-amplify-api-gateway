# AWS Lambda, Amplify, and Api-Gateway
Simple app to learn serverless AWS   
these are the explanations for each functions and what it does  
i also add some very simple type in extra_type.py because boto3 type sucks  
for proper types you can check [boto3-stubs](https://pypi.org/project/boto3-stubs/) but since i dont want to depend on too much 3rd party library i didnt uuse it

### `lambda_handler(event: dict, ctx)`

Handles the incoming request and routes it based on the `operation` field.

#### Parameters

* `event`: Dictionary containing the request.
* `ctx`: Lambda context object (not used).

#### Behavior

* If `operation` is `"addProduct"`, it calls `saveProduct`.
* If `operation` is `"listProducts"`, it calls `getProducts`.
* Returns 404 if the operation is unrecognized.

#### Example Input

```python
event = {
    "operation": "addProduct",
    "productCode": "ABC123",
    "price": 49.99
}
result = lambda_handler(event, None)
```

#### Example Output

```python
{
    "status_code": 200,
    "body": "\"Product with ProductCode : ABC123 created at Fri, 28 Jun 2025 04:23:11\""
}
```

---

### `saveProduct(event: dict, table: DynamoDBTableLike)`

Inserts a new product into the DynamoDB table with a timestamp.

#### Parameters

* `event`: Should contain `productCode` and `price`.
* `table`: A DynamoDB table instance (e.g., `dynamodb.Table("Product")`).

#### Example Input

```python
event = {
    "productCode": "XYZ456",
    "price": 25.00
}
table = boto3.resource("dynamodb").Table("Product")
result = saveProduct(event, table)
```

#### Example Output

```python
{
    "status_code": 200,
    "body": "\"Product with ProductCode : XYZ456 created at Fri, 28 Jun 2025 04:23:11\""
}
```

---

### `getProducts(table: DynamoDBTableLike)`

Scans and returns all products in the DynamoDB table.

#### Parameters

* `table`: A DynamoDB table instance.

#### Example Usage

```python
table = boto3.resource("dynamodb").Table("Product")
result = getProducts(table)
```

#### Example Output

```python
{
    "statusCode": 200,
    "body": "[{\"productCode\": \"ABC123\", \"price\": 49.99, \"createdAt\": \"...\"}]",
    "headers": {
        "Content-Type": "application/json"
    }
}
```
> aws should hire me to write better sdk
