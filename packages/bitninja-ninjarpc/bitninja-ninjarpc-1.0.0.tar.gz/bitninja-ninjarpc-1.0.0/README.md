# BitNinjaIO NinjaRPC

RabbitMQ rpc server and client by [BitNinja.io](https://bitninja.io) based on [PHP implementation](https://packagist.org/packages/bitninja/ninjarpc)

## Usage

The package contains a client, and a server as well, which can communicate with each other.

### Server

```python
# import the package
from ninjarpc import Server
from ninjarpc.Encoders import JsonEncoder
from ninjarpc.Routers import SimpleRouter
from ninjarpc.QueueManagers import RabbitMQ

def endpoint_handler(params):
    print(f'endpoint was called with {params} parameters.')

if __name__ == '__main__':
    queue_manager = RabbitMQ(host='hostname',
                             port='port',
                             username='username',
                             password='password')
    encoder = JsonEncoder()
    endpoints = {"endpoint": endpoint_handler}
    router = SimpleRouter(endpoints)

    server = Server('TEST_SERVICE', queue_manager, encoder, router)

    while True:
        server.listen()
```

### Client

```python
# import the package
from ninjarpc import Client
from ninjarpc.Encoders import JsonEncoder
from ninjarpc.Exceptions import CallTimeoutException
from ninjarpc.QueueManagers import RabbitMQ

if __name__ == '__main__':
    queue_manager = RabbitMQ(host='hostname',
                             port='port',
                             username='username',
                             password='password')
    encoder = JsonEncoder()
    client = Client(queue_manager, encoder)
    
    call = client.async_call(service_name='TEST_SERVICE',
                             method_name='endpoint',
                             parameters=())
    try: 
        result = call.wait()
    except CallTimeoutException as e:
        print('Call timeouted')

```