# Sample Flask app integrated with GitHub actions
Sample Flask app with CI part configured using GitHub actions

## Run application
Run application

```sh
flask run

 * Serving Flask app "app.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 207-112-103
```

Execute tests and get coverage report

```sh
coverage run
============================================================ test session starts ============================================================
platform darwin -- Python 3.7.3, pytest-6.1.2, py-1.9.0, pluggy-0.13.1 -- /Users/aromanov/projects/github-actions-flask/venv/bin/python3
cachedir: .pytest_cache
rootdir: /Users/aromanov/projects/github-actions-flask
collected 7 items

tests/test_app.py::test_get_hello_endpoint PASSED                                                                                     [ 14%]
tests/test_app.py::test_post_hello_endpoint PASSED                                                                                    [ 28%]
tests/test_app.py::test_get_api_endpoint PASSED                                                                                       [ 42%]
tests/test_app.py::test_correct_post_api_endpoint PASSED                                                                              [ 57%]
tests/test_app.py::test_not_dict_post_api_endpoint PASSED                                                                             [ 71%]
tests/test_app.py::test_no_name_post_api_endpoint PASSED                                                                              [ 85%]
tests/test_app.py::test_bad_age_post_api_endpoint PASSED                                                                              [100%]

============================================================= 7 passed in 0.22s =============================================================

coverage report
Name       Stmts   Miss  Cover
------------------------------
app.py        25      3    88%
tests.py      37      1    97%
------------------------------
TOTAL         62      4    94%
```