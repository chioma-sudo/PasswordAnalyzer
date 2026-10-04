import unittest
from main import (
    check_length,
    check_uppercase,
    check_lowercase,
    check_number,
    check_special,
    check_repetition,
    normalize_password,
    load_common_passwords,
    check_common_password,
    get_strength,
    hash_password,
    verify_password 
)


class TestPasswordAnalyzer(unittest.TestCase):
    def test_check_length(self):
        self.assertTrue(check_length("password123"))
        self.assertFalse(check_length("pass"))

    def test_empty_password(self):
        self.assertFalse(check_length(""))

    def test_length_boundary(self):
        self.assertFalse(check_length("1234567"))
        self.assertTrue(check_length("12345678"))

    def test_long_password(self):
        self.assertTrue(check_length("A" * 100))

    def test_whitespace_password(self):
        self.assertTrue(check_length("        "))

    def test_check_uppercase(self):
        self.assertTrue(check_uppercase("Password"))
        self.assertFalse(check_uppercase("password"))

    def test_check_lowercase(self):
        self.assertTrue(check_lowercase("password"))
        self.assertFalse(check_lowercase("PASSWORD"))

    def test_check_number(self):
        self.assertTrue(check_number("Password123"))
        self.assertFalse(check_number("Password"))

    def test_check_special(self):
        self.assertTrue(check_special("Password!"))
        self.assertFalse(check_special("Password123"))

    def test_check_repetition(self):
        # Repeated character
        self.assertTrue(
            check_repetition("aaaaaaaa")
        )

        # Repeated number
        self.assertTrue(
            check_repetition("11111111")
        )

        # Repeated pattern
        self.assertTrue(
            check_repetition("abcabc")
        )

        # Normal password
        self.assertFalse(
            check_repetition("PurpleTiger42!")
        )

        # Different characters and no repeated pattern
        self.assertFalse(
            check_repetition("Password123!")
        )

    def test_normalize_password(self):
        self.assertEqual(
            normalize_password("Password123!"),
            "password123"
    )

        self.assertEqual(
            normalize_password("QWERTY!"),
            "qwerty"
    )

    def test_load_common_passwords(self):
        common_passwords = load_common_passwords()

        self.assertIn("password", common_passwords)
        self.assertIn("123456", common_passwords)
        self.assertIn("qwerty", common_passwords)

        self.assertNotIn("", common_passwords)
    def test_check_common_password(self):
        common_passwords = load_common_passwords()

        self.assertTrue(
            check_common_password("password", common_passwords)
        )

        self.assertTrue(
            check_common_password("Password123!", common_passwords)
        )

        self.assertTrue(
            check_common_password("P@ssword1", common_passwords)
        )

        self.assertTrue(
            check_common_password("k1ller", common_passwords)
        )

        self.assertTrue(
            check_common_password("pass2word2@", common_passwords)
        )

        self.assertFalse(
            check_common_password("PurpleTiger42!", common_passwords)
        )

        self.assertFalse(
            check_common_password(
            "purpl3tig3r 241!",
            common_passwords
        )
    )

    def test_get_strength(self):
        # Less than 8 characters = Weak
        self.assertEqual(
            get_strength("pass", False),
            "Weak"
        )

        # 8+ characters but poor composition = Weak
        self.assertEqual(
            get_strength("abcdefgh", False),
            "Weak"
        )

        # 8–13 characters with some complexity = Moderate
        self.assertEqual(
            get_strength("Password", False),
            "Moderate"
        )

        self.assertEqual(
            get_strength("Password1", False),
            "Moderate"
        )

        self.assertEqual(
            get_strength("PurpleTiger!", False),
            "Moderate"
        )

        # 14+ characters with all character types = Strong
        self.assertEqual(
            get_strength("PurpleTiger42!", False),
            "Strong"
        )

        # Common passwords should always be Weak
        self.assertEqual(
            get_strength("Password123!", True),
            "Weak"
        )
            # Repeated characters or patterns = Weak
        self.assertEqual(
            get_strength("aaaaaaaa", False),
            "Weak"
        )

        self.assertEqual(
            get_strength("abcabcabcabc", False),
            "Weak"
        )

    def test_password_verification_edge_cases(self):
        password = "Password123!"
    
        salt1, hash1 = hash_password(password)
        salt2, hash2 = hash_password(password)
    
        # Same password should produce different salts and hashes
        self.assertNotEqual(salt1, salt2)
        self.assertNotEqual(hash1, hash2)
    
        # Correct password should verify
        self.assertTrue(
            verify_password(password, salt1, hash1)
        )
    
        # Wrong password should not verify
        self.assertFalse(
            verify_password("WrongPassword!", salt1, hash1)
        )
    
    def test_password_verification_with_modified_hash(self):
        password = "Password123!"

        salt, stored_hash = hash_password(password)

        modified_hash = bytearray(stored_hash)
        modified_hash[0] ^= 1
        modified_hash = bytes(modified_hash)

        self.assertFalse(
            verify_password(password, salt, modified_hash)
    )

    
if __name__ == "__main__":
    unittest.main()