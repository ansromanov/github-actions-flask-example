# Sample app

## Run app
Run app

```sh

```

Execute tests and get coverage report

 ```sh
coverage run --include tests.py -m unittest -v

test_bad_age_post_api_endpoint (tests.FlaskAppTests) ... ok
test_correct_post_api_endpoint (tests.FlaskAppTests) ... ok
test_get_api_endpoint (tests.FlaskAppTests) ... ok
test_get_hello_endpoint (tests.FlaskAppTests) ... ok
test_no_name_post_api_endpoint (tests.FlaskAppTests) ... ok
test_not_dict_post_api_endpoint (tests.FlaskAppTests) ... ok
test_post_hello_endpoint (tests.FlaskAppTests) ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.015s

coverage report
Name       Stmts   Miss  Cover
------------------------------
app.py        25      3    88%
tests.py      37      1    97%
------------------------------
TOTAL         62      4    94%
```