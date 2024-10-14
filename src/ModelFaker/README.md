# ModelFaker

The `JTRFaker` domain is a utility module in your project that is primarily focused on generating 
fake data for testing and development purposes. It leverages the power of the Faker library to 
create realistic yet random data that can be used to populate your database during `development` 
or for `testing` your application's functionality.

## Usage

```python
from JTRFaker.Faker.ModelFaker import ModelFaker
from path-to-model import Users

ModelFaker(Users).create(5)
```
