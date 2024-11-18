import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def testticketprice(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)

    # Add your additional test cases here.
    
    def test_ticket_priceC1b1(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "ERROR")

    def test_ticket_priceC1b2(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)

    def test_ticket_priceC1b3(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_ticket_priceC1b4(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)

    def test_ticket_priceC1b5(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

if __name__ == '__main__':
    unittest.main()