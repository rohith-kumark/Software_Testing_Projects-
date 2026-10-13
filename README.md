# Project 1 — Login & Authentication Testing

**Target app:** https://www.saucedemo.com/ (a demo e-commerce site built for test automation practice)
**Goal:** Practice manual test case design, then automate the same cases with Selenium + Python.

## Test users on this site
| Username | Password | Behavior |
|---|---|---|
| `standard_user` | `secret_sauce` | Logs in normally |
| `locked_out_user` | `secret_sauce` | Blocked — "this user has been locked out" |
| `problem_user` | `secret_sauce` | Logs in but has UI bugs (good for Project 6 bug-hunting) |
| `performance_glitch_user` | `secret_sauce` | Logs in slowly |

## Part A — Manual Test Cases (write these yourself first, then compare)

| ID | Title | Steps | Expected Result |
|---|---|---|---|
| TC_01 | Valid login | Enter `standard_user` / `secret_sauce`, click Login | Redirected to `/inventory.html`, "Products" title visible |
| TC_02 | Invalid password | Enter `standard_user` / `wrong_pass`, click Login | Error: "Username and password do not match any user in this service" |
| TC_03 | Locked out user | Enter `locked_out_user` / `secret_sauce`, click Login | Error: "Sorry, this user has been locked out." |
| TC_04 | Empty username | Leave username blank, enter password, click Login | Error: "Username is required" |
| TC_05 | Empty password | Enter username, leave password blank, click Login | Error: "Password is required" |
| TC_06 | Both fields empty | Click Login with nothing entered | Error: "Username is required" |

Before looking at `tests/test_login.py`, try writing 2–3 more test cases yourself — e.g., SQL injection in the username field, case-sensitivity of the username, very long input strings.

## Part B — Automated version (this repo)

### Setup
```bash
pip install -r requirements.txt
```

### Run tests
```bash
pytest -v tests/
```

### Files
- `pages/login_page.py` — Page Object for the login form
- `pages/inventory_page.py` — Page Object for the post-login products page
- `tests/conftest.py` — pytest fixture that creates/quits the browser
- `tests/test_login.py` — automated version of the manual test cases above

## Try extending it yourself
1. Add a test for `problem_user` and `performance_glitch_user`.
2. Add a test asserting the page URL doesn't change on a failed login.
3. Parametrize the whole suite so all test cases run from one function with a data table (see Module 7 of the course for the `@pytest.mark.parametrize` pattern).
