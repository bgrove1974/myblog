import unittest
from cards import Card, AceCard, FaceCard


class TestCard(unitttest.TestCase):

    def setUp(self):
        self.aceClubs = AceCard(Card.Ace, Card.Clubs)
        self.twoClubs = Card(2, Card.Clubs)
        self.tenClubs = Card(10, Card.Clubs)
        self.kingClubs = FaceCard(Card.King, Card.Clubs)
        self.aceDiamonds = AceCard(Card.Ace, Card.Diamonds)

    def testString(self):
        def testString(self):
        self.assertEqual(" A♣", str(self.aceClubs))
        self.assertEqual(" 2♣", str(self.twoClubs))
        self.assertEqual("10♣", str(self.tenClubs))
        self.assertEqual(" K♣", str(self.kingClubs))
        self.assertEqual(" A♢", str(self.aceDiamonds))


    def testOrder(self):
        self.assertTrue(self.tenClubs < self.kingClubs)
        self.assertFalse(self.tenClubs >= self.kingClubs)
        self.assertTrue(self.kingClubs < self.AceClubs)
        self.assertTrue(self.aceClubs == self.aceDiamonds)

    def testImage(self):
            self.assertEqual("🃑", self.aceClubs.image)
            self.assertEqual("🃒", self.twoClubs.image)
            self.assertEqual("🃚", self.tenClubs.image)
            self.assertEqual("🃞", self.kingClubs.image)
            self.assertEqual("🃁", self.aceDiamonds.image)


if __name__ == '__main__':
    unittest.main()
