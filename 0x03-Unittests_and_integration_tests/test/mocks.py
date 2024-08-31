from unittest.mock import patch, PropertyMock
import requests


class Dog:
    
    def __init__(self) -> None:
        self.energy = 100
    def bark(self):
        return "Woof!"
    
    def run(self):
        return "Running fast!"



class DoSum():
    def __init__(self) -> None:
        pass
    def add(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
    
    
def dog_status():
    d = Dog()
    return d.energy

def dog_activity():
    d = Dog()
    return d.bark(), d.run()

with patch('__main__.Dog.bark', return_value="Mocked Woof!"):
    result = dog_activity()
    print(result)
    
# with patch.object(Dog, 'energy', new=70):
#     result = dog_status()
#     print(result)


def get_status_code(url):
    response = requests.get(url)
    return response.status_code

with patch('requests.get') as MockGet:
    MockGet.return_value.status_code = 200
    status = get_status_code("http://example.com")
    print(status)
    
    
with patch('__main__.DoSum') as MockClass:
    instance = MockClass()
    instance.method.return_value = "patched"
    instance.printsum.return_value = 56
    print(instance.method())
    
@patch('__main__.DoSum')
def test_DoSum(MockClass):
    instance = MockClass.return_value
    instance.method.return_value = "patched"
    instance.printsum.return_value = 77
    MockClass.return_value.add.return_value = 12  # Define the return value for add method

    print(MockClass.return_value.add(12,13))  # This will now print 12
    
test_DoSum()
 
 
with patch('__main__.Dog.energy', new_callable=PropertyMock) as mock_energy:
    mock_energy.return_value = 50
    result = dog_status()
    print(result)