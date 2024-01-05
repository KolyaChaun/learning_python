import pytest
from thirteenth_lesson_practice_oop import CurrentAccount, CreditAccount, Client


@pytest.fixture(scope="class")
def current_account() -> CurrentAccount:
    instance = CurrentAccount()
    return instance


@pytest.fixture(scope="class")
def credit_account() -> CreditAccount:
    instance = CreditAccount(limit=-20000)
    return instance


@pytest.fixture(scope="class")
def client() -> Client:
    instance = Client(name="Alex")
    return instance


@pytest.fixture(scope="class")
def another_client() -> Client:
    instance = Client(name="Bob")
    return instance


@pytest.fixture(scope="class")
def first_current_account_for_another_client() -> CurrentAccount:
    instance = CurrentAccount()
    return instance


@pytest.fixture(scope="class")
def second_current_account_for_another_client() -> CurrentAccount:
    instance = CurrentAccount()
    return instance


@pytest.fixture(scope="class")
def first_credit_account_for_another_client() -> CreditAccount:
    instance = CreditAccount(limit=-5000)
    return instance


@pytest.fixture(scope="class")
def second_credit_account_for_another_client() -> CreditAccount:
    instance = CreditAccount(limit=-10000)
    return instance
