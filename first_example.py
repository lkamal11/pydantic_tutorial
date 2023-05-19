from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3'],
}
user = User(**external_data)
# The ** operator allows us to take a dictionary of key-value pairs and unpack it into keyword arguments in a function call.
print(user.id)
#> 123
print(repr(user.signup_ts))
#> datetime.datetime(2019, 6, 1, 12, 22)
print(user.friends)
#> [1, 2, 3]
print(user.dict())
"""
{
    'id': 123,
    'signup_ts': datetime.datetime(2019, 6, 1, 12, 22),
    'friends': [1, 2, 3],
    'name': 'John Doe',
}
"""
print("............." + "\n")
from pydantic import ValidationError

try:
    User(signup_ts='broken', friends=[1, 2, 'not number'])
except ValidationError as e:
    print(e.json())




