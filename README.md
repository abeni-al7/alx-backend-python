# ALX Backend Python

Python back-end specialization exercises from the ALX Africa Software Engineering programme (2023–2024), covering type annotations, asynchronous programming, and testing.

## Contents

| Directory | Topic |
|-----------|-------|
| `0x00-python_variable_annotations` | Type annotations and type-hinted functions |
| `0x01-python_async_function` | `async`/`await` coroutines, `asyncio` tasks, runtime measurement |
| `0x02-python_async_comprehension` | Async generators and async comprehensions |
| `0x03-Unittests_and_integration_tests` | `unittest`, mocking, parameterized and integration tests for `utils.py`/`client.py` |

## Built with

- Python 3 (standard library: `typing`, `asyncio`, `unittest`, `unittest.mock`)
- `parameterized` for the test module

## Run it

Scripts are standalone. Many tasks include a `*-main.py` driver:

```bash
./0-main.py
```

Run the test suite:

```bash
python3 -m unittest discover 0x03-Unittests_and_integration_tests
```

Educational coursework; each task directory has its own README describing the requirements.
