from typing import List, Protocol

# list of operation available
class Operations:
    addProduct = 'addProduct'
    listProducts = 'listProducts'
    
    @classmethod
    def get_operations_list(cls) -> List[str]:
        ops_list = []
        for name, value in vars(cls).items():
            if name.startswith('__'):
                continue

            if callable(value):
                continue

            if isinstance(value, (classmethod, staticmethod)):
                continue

            ops_list.append(value)

        return ops_list

class DynamoDBTableLike(Protocol):
    def put_item(self, **kwargs) -> dict: ...
    def scan(self, **kwargs) -> dict: ...

