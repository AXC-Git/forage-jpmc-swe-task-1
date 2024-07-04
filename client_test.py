import unittest
from client3 import getDataPoint


class ClientTest(unittest.TestCase):

  def test_getDataPoint_calculatePrice(self):
    quotes = [{
        'top_ask': {
            'price': 121.2,
            'size': 36
        },
        'timestamp': '2019-02-11 22:06:30.572453',
        'top_bid': {
            'price': 120.48,
            'size': 109
        },
        'id': '0.109974697771',
        'stock': 'ABC'
    }, {
        'top_ask': {
            'price': 121.68,
            'size': 4
        },
        'timestamp': '2019-02-11 22:06:30.572453',
        'top_bid': {
            'price': 117.87,
            'size': 81
        },
        'id': '0.109974697771',
        'stock': 'DEF'
    }]
    for quote in quotes:
      self.assertEqual(
          getDataPoint(quote),
          (quote['stock'], quote['top_ask']['price'],
           quote['top_bid']['price'],
           (quote['top_ask']['price'] + quote['top_bid']['price']) / 2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [{
        'top_ask': {
            'price': 119.2,
            'size': 36
        },
        'timestamp': '2019-02-11 22:06:30.572453',
        'top_bid': {
            'price': 120.48,
            'size': 109
        },
        'id': '0.109974697771',
        'stock': 'ABC'
    }, {
        'top_ask': {
            'price': 121.68,
            'size': 4
        },
        'timestamp': '2019-02-11 22:06:30.572453',
        'top_bid': {
            'price': 117.87,
            'size': 81
        },
        'id': '0.109974697771',
        'stock': 'DEF'
    }]
    for quote in quotes:
      self.assertEqual(
          getDataPoint(quote),
          (quote['stock'], quote['top_ask']['price'],
           quote['top_bid']['price'],
           (quote['top_ask']['price'] + quote['top_bid']['price']) / 2))

  def test_getDataPoint_singleQuote(self):
    quote = {
        'top_ask': {
            'price': 121.2,
            'size': 36
        },
        'timestamp': '2019-02-11 22:06:30.572453',
        'top_bid': {
            'price': 120.48,
            'size': 109
        },
        'id': '0.109974697771',
        'stock': 'ABC'
    }
    self.assertEqual(
        getDataPoint(quote),
        (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
         (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  def test_getDataPoint_emptyQuote(self):
    quote = {}
    with self.assertRaises(KeyError):
      getDataPoint(quote)

  def test_getDataPoint_bidPriceEqualToAskPrice(self):
    quotes = [{
        'top_ask': {
            'price': 121.2,
            'size': 36
        },
        'timestamp': '2019-02-11 22:06:30.572453',
        'top_bid': {
            'price': 121.2,
            'size': 109
        },
        'id': '0.109974697771',
        'stock': 'DEF'
    }, {
        'top_ask': {
            'price': 120.0,
            'size': 36
        },
        'timestamp': '2019-02-11 22:06:30.572453',
        'top_bid': {
            'price': 120.0,
            'size': 109
        },
        'id': '0.109974697771',
        'stock': 'ABC'
    }]
    for quote in quotes:
      self.assertEqual(
          getDataPoint(quote),
          (quote['stock'], quote['top_bid']['price'],
           quote['top_ask']['price'],
           (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  def test_getDataPoint_zeroBidPrice(self):
    quote = {
        'top_ask': {
            'price': 121.2,
            'size': 36
        },
        'timestamp': '2019-02-11 22:06:30.572453',
        'top_bid': {
            'price': 0.0,
            'size': 109
        },
        'id': '0.109974697771',
        'stock': 'ABC'
    }
    self.assertEqual(
        getDataPoint(quote),
        (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
         (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  def test_getDataPoint_zeroAskPrice(self):
    quote = {
        'top_ask': {
            'price': 0.0,
            'size': 36
        },
        'timestamp': '2019-02-11 22:06:30.572453',
        'top_bid': {
            'price': 120.48,
            'size': 109
        },
        'id': '0.109974697771',
        'stock': 'ABC'
    }
    self.assertEqual(
        getDataPoint(quote),
        (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
         (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  def test_getDataPoint_zeroPrice(self):
    quotes = [{
        'top_ask': {
            'price': 0.0,
            'size': 36
        },
        'timestamp': '2019-02-11 22:06:30.572453',
        'top_bid': {
            'price': 0.0,
            'size': 109
        },
        'id': '0.109974697771',
        'stock': 'ABC'
    }, {
        'top_ask': {
            'price': 0.0,
            'size': 4
        },
        'timestamp': '2019-02-11 22:06:30.572453',
        'top_bid': {
            'price': 0.0,
            'size': 81
        },
        'id': '0.109974697771',
        'stock': 'DEF'
    }]
    for quote in quotes:
      self.assertEqual(
          getDataPoint(quote),
          (quote['stock'], quote['top_bid']['price'],
           quote['top_ask']['price'],
           (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))


if __name__ == '__main__':
  unittest.main()
