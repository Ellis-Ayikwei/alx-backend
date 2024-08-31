# Unit Tests and Integration Tests

## Overview

This project focuses on unit testing and integration testing for Python code. It includes various tasks that involve parameterizing tests, mocking functions and properties, and testing integration points.

## Requirements

- Python 3.7
- Libraries: `unittest`, `unittest.mock`, `parameterized`
- All files should use `pycodestyle` (version 2.5) style.
- Code must be executable and include documentation.

## Files

- **`utils.py`**: Contains utility functions to be tested.
- **`client.py`**: Contains the `GithubOrgClient` class to be tested.
- **`fixtures.py`**: Provides fixtures used for integration testing.
- **`test_utils.py`**: Contains unit tests for functions in `utils.py`.
- **`test_client.py`**: Contains unit and integration tests for functions in `client.py`.

## Tasks

1. **Parameterize a Unit Test**  
   - Implement tests for the `access_nested_map` function using various inputs.

2. **Parameterize a Unit Test with Exceptions**  
   - Test the `access_nested_map` function to ensure it raises `KeyError` for invalid inputs.

3. **Mock HTTP Calls**  
   - Test the `get_json` function without making actual HTTP requests.

4. **Parameterize and Patch**  
   - Test the `GithubOrgClient.org` method with parameterized inputs and mock HTTP requests.

5. **Mocking a Property**  
   - Test the `_public_repos_url` method of `GithubOrgClient` using mocked properties.

6. **More Patching**  
   - Test the `public_repos` method of `GithubOrgClient` with mocked HTTP responses and properties.

7. **Parameterize**  
   - Test the `has_license` method of `GithubOrgClient` with various license keys.

8. **Integration Test with Fixtures**  
   - Perform integration tests on the `public_repos` method of `GithubOrgClient` using predefined fixtures.

## Running Tests

To run the tests, use the following command:

```bash
$ python -m unittest discover -s path/to/tests
