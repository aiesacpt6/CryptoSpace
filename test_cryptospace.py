# test_cryptospace.py
"""
Tests for CryptoSpace module.
"""

import unittest
from cryptospace import CryptoSpace

class TestCryptoSpace(unittest.TestCase):
    """Test cases for CryptoSpace class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoSpace()
        self.assertIsInstance(instance, CryptoSpace)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoSpace()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
