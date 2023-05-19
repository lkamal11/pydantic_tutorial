from pydantic import BaseModel

class Foo(BaseModel):
    count: int
    size: float | None = None

class Bar(BaseModel):
    apple = 'x'
    banana = 'y'

class Spam(BaseModel):
    foo: Foo
    bars: list[Bar]
m = Spam(foo={'count': 4}, bars=[{'apple': 'x1'}, {'apple': 'x2'}])
print(m)

#> foo=Foo(count=4, size=None) bars=[Bar(apple='x1', banana='y'),
#> Bar(apple='x2', banana='y')]
print(m.dict())


