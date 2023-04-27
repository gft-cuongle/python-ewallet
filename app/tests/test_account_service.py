import unittest
from unittest.mock import Mock

from app.common.account_type import AccountType
from app.service import account_service


class AccountServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.mock_repository = Mock()
        self.mock_db = Mock()
        account_service.account_repository = self.mock_repository

    def test_create_account(self):
        # Mock the behavior of account_repository.create_account
        self.mock_repository.create_account.return_value = None

        # Perform the test
        result = account_service.create_account(AccountType.PERSONAL.value)

        # Assertions
        self.assertIsNotNone(result)
        self.assertEqual(result["accountType"], AccountType.PERSONAL.value)
        self.assertEqual(result["balance"], 0)
        self.mock_repository.create_account.assert_called_once_with(result)

    def test_topup_account(self):
        # Mock the behavior of account_repository.get_account_by_id
        self.mock_repository.get_account_by_id.side_effect = [
            {"accountId": "receiver_id", "balance": 100},
            {"accountId": "issuer_id", "balance": 200}
        ]

        # Perform the test
        account_service.topup_account("receiver_id", "issuer_id", 50)

        # Assertions
        self.mock_repository.update_account_balance.assert_any_call("receiver_id", 150)
        self.mock_repository.update_account_balance.assert_any_call("issuer_id", 150)
