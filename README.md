# sirius
> shipping method optimization

## purpose
the purpose of the app is to expose a webservice to find the optimal means of shipping an order.

ideally, you should send a cart"s json data and receive a json response giving you the boxes with items, their shipping method and cost, and total cost for the order.

## requirements
all reqs are listed in the `requirement.txt` file. to install, just run the usual:  
```
$ pip install -r requirements.txt
```

the full listing of requirements is:  

```
Flask==0.10.1
Jinja2==2.7.1
MarkupSafe==0.18
PyYAML==3.10
Werkzeug==0.9.4
itsdangerous==0.23
wsgiref==0.1.2
```

## examples
### input data
```
{
    "zip": 60631,                     // :int/str:      destination zipcode
    "items": [
        {
            "sku": "bully sticks",    // :str:          product identifier
            "qty": 2,                 // :int:          quantity
            "weight": 10,             // :int/float:    weight per item in ounces
            "is_irregular": false     // :bool:         [optional] is the item irregularly shaped
        },
        {
            "sku": "antler",
            "qty": 1,
            "weight": 24,
            "is_irregular": true
        }
    ]
}
```
input data is expected to have two keys in the first level document: `zip` and `items`. `zip` is the destination zipcode of the order.  

`items` is an array of the items ordered. each _item_ is another json document: it is expected to have a `sku` identified, `qty` of the item ordered, `weight` in ounces, and an __optional__ `is_irregular` flag.

### output data
```
{
    "boxes": [
        {
            "items": [
                {
                    "sku": u"bully sticks",
                    "qty": 1
                }
            ],
            "cost": 2.5,
            "method": "UPS Mail Innovations"
        },
        {
            "items": [
                {
                    "sku": u"bully sticks",
                    "qty": 1
                }
            ],
            "cost": 2.5,
            "method": "UPS Mail Innovations"
        },
        {
            "items": [
                {
                    "sku": u"antler",
                    "qty": 1
                }
            ],
            "cost": 8.64,
            "method": "UPS Ground"
        }
    ],
    "cost": 13.64
}
```
output data will have two keys as well in the first level document: `boxes` and `cost`. `cost` lists the total cost of shipping the order. `boxes` is an array of _box_ objects.  

a _box_ object will have the following three keys: `items`, `cost` and `method`. `cost` and `method` are pretty self-explanitory. `items` is an array of items from the original order. each _item_ will list the `sku` identifier and the `qty` of the item that should be packed in the box.  

__note:__ some items that are ordered > 1 could be shipped seperately.

### usage example (using curl)
send data:  

```
$ curl -i -H "Content-Type: application/json" -X POST -d '{ "zip": 67098, "items": [ { "sku": "antler", "qty": 2, "weight": 24, "is_irregular": true }, { "sku": "treat", "qty": 3, "weight": 20 }, { "sku": "pizzle", "qty": 1, "weight": 16 }, { "sku": "ball", "qty": 5, "weight": 2 } ] }' http://localhost:5000/optimize_shipping/
```

and recieve:

```
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 326
Server: Werkzeug/0.9.4 Python/2.7.6
Date: Mon, 23 Dec 2013 16:52:21 GMT

{'boxes': [{'items': [{'sku': u'ball', 'qty': 5}, {'sku': u'treat', 'qty': 3}, {'sku': u'pizzle', 'qty': 1}], 'cost': 9.68, 'method': 'UPS Ground'}, {'items': [{'sku': u'antler', 'qty': 1}], 'cost': 8.88, 'method': 'UPS Ground'}, {'items': [{'sku': u'antler', 'qty': 1}], 'cost': 8.88, 'method': 'UPS Ground'}], 'cost': 27.44}
```





