# 0x03. Unittests and Integration Tests

This project contains tasks for learning to write unittests and integration tests in Python 3.

## Resources
Read or watch:
- [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
- [unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html)
- [How to mock a readonly property with mock?](https://stackoverflow.com/questions/11836436/how-to-mock-a-readonly-property-with-mock)
- [parameterized](https://pypi.org/project/parameterized/)
- [Memoization](https://en.wikipedia.org/wiki/Memoization)

## Learning Objectives
- The difference between unit and integration tests.
- Common testing patterns such as mocking, parametrizations and fixtures

## Required Modules
- parameterized.

## installation
```
pip install parameterized
```

## Testing
With unittest:
```
python -m unittest path/to/test_file.py
```

With nose (nose3):
```
nosetests3 -v path/to/test_file.py
```

# Tasks
## 0. Parameterize a unit test 

Familiarize yourself with the `utils.access_nested_map` function and understand its purpose. Play with it in the Python console to make sure you understand.

In this task you will write the first unit test for `utils.access_nested_map`.

Create a `TestAccessNestedMap` class that inherits from `unittest.TestCase`.

Implement the `TestAccessNestedMap.test_access_nested_map` method to test that the method returns what it is supposed to.

Decorate the method with `@parameterized.expand` to test the function for following inputs:
```
nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")
```
For each of these inputs, test with `assertEqual` that the function returns the expected result.

The body of the test method should not be longer than 2 lines.
