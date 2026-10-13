import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_tc01_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    assert inventory_page.is_loaded(), "Expected to land on the Products page after valid login"


def test_tc02_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "wrong_pass")

    assert "do not match any user" in login_page.get_error_text()


def test_tc03_locked_out_user(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("locked_out_user", "secret_sauce")

    assert "locked out" in login_page.get_error_text()


def test_tc04_empty_username(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("", "secret_sauce")

    assert "Username is required" in login_page.get_error_text()


def test_tc05_empty_password(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "")

    assert "Password is required" in login_page.get_error_text()


@pytest.mark.parametrize("username,password,expected_error_snippet", [
    ("", "", "Username is required"),
    ("standard_user", "", "Password is required"),
    ("standard_user", "bad_pass", "do not match any user"),
    ("locked_out_user", "secret_sauce", "locked out"),
])
def test_login_negative_cases_parametrized(driver, username, password, expected_error_snippet):
    """Same cases as above, written as one data-driven test instead of five separate functions."""
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(username, password)

    assert expected_error_snippet in login_page.get_error_text()
