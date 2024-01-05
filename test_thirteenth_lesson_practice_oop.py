import random

from thirteenth_lesson_practice_oop import CurrentAccount, CreditAccount


class TestDepositFunds:
    def test_add_account_to_client(self, client, current_account):
        client.accounts.append(current_account)
        assert client.accounts

    def test_add_credit_account(self, client, credit_account):
        client.accounts.append(credit_account)
        assert len(client.accounts) == 2
        print(client.accounts)
        random.shuffle(client.accounts)

    def test_add_first_account_to_another_client(
        self, another_client, first_current_account_for_another_client
    ):
        another_client.accounts.append(first_current_account_for_another_client)
        assert another_client.accounts

    def test_add_second_account_to_another_client(
        self, another_client, second_current_account_for_another_client
    ):
        another_client.accounts.append(second_current_account_for_another_client)
        assert another_client.accounts

    def test_add_first_credit_account_to_another_client(
        self, another_client, first_credit_account_for_another_client
    ):
        another_client.accounts.append(first_credit_account_for_another_client)
        assert another_client.accounts

    def test_add_second_credit_account_to_another_client(
        self, another_client, second_credit_account_for_another_client
    ):
        another_client.accounts.append(second_credit_account_for_another_client)
        assert len(another_client.accounts) == 4

    def test_deposit_on_current_on_1560(self, client):
        for account in client.accounts:
            if isinstance(account, CurrentAccount):
                account.deposit_money(1560)
                assert account.balance == 1560
                break

    def test_withdraw_money_from_current_on_500(self, client):
        for account in client.accounts:
            if isinstance(account, CurrentAccount):
                account.withdraw_money(500)
                assert account.balance == 1060
                break

    def test_transfer_from_credit_to_debit(self, client):
        for account in client.accounts:
            if isinstance(account, CurrentAccount):
                cur_acc = account
                break
        for account in client.accounts:
            if isinstance(account, CreditAccount):
                cred_acc = account
                break

        cred_acc.make_transaction(cur_acc, 700)
        assert cur_acc.balance == 1760
        assert cred_acc.balance == (-700 - (700 * CreditAccount.percent_commission))

    def test_unsuccessful_withdraw_money_from_current_acc(
        self, another_client, first_current_account_for_another_client
    ):
        for account in another_client.accounts:
            if isinstance(account, CurrentAccount):
                balance_before = first_current_account_for_another_client.balance
                account.withdraw_money(1000000000)
                assert account.balance == balance_before

    def test_unsuccessful_from_current_account(self, current_account, credit_account):
        print(current_account.__dict__)
        balance_before = current_account.balance
        current_account.make_transaction(credit_account, 50000000000)
        assert current_account.balance == balance_before

    def test_transfer_from_client_credit_to_another_client_current(
        self, client, another_client
    ):
        for account in client.accounts:
            if isinstance(account, CreditAccount):
                client_cred_acc = account
                break
        for account in another_client.accounts:
            if isinstance(account, CurrentAccount):
                another_client_cur_acc = account
                break

        client_cred_balance_before = client_cred_acc.balance

        client_cred_acc.make_transaction(another_client_cur_acc, 1.33)
        assert another_client_cur_acc.balance == 1.33
        assert client_cred_acc.balance == client_cred_balance_before + (
            -1.33 - (1.33 * CreditAccount.percent_commission)
        )

    def test_get_account_information_positive_balance(self, client):
        for account in client.accounts:
            if isinstance(account, CreditAccount):
                account.deposit_money(5000)
        assert client.is_positive_balance() is True

    def test_get_account_information_negative_balance(self, client):
        for account in client.accounts:
            if isinstance(account, CreditAccount):
                account.withdraw_money(10000)
                assert client.is_positive_balance() is False
