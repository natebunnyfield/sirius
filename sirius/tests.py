#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import combinations
import unittest

from matrices import get_cheapest_option, get_irregular_price
from models import Item, Box, Order


class TestOptimizer(unittest.TestCase):
    """
    Tests:

    1. single item, under a pound, normal zone
    2. single item, 3 pounds, normal zone
    3. multiple items, all under a pound, normal zone
    4. multiple items, mixed weight, normal zone
    5. irregular item, normal zone
    6. mixed type items, mixed weight, normal zone
    7. regular item, under a pound, ak/hi zone

    Order Input Data:

    Test No | Item      | Qty   | Weight    | Zipcode   | Irregular
    ===============================================================
    1       | stick     | 1     | 4         | 60631     | false
    ---------------------------------------------------------------
    2       | stick     | 2     | 48        | 50172     | false
    ---------------------------------------------------------------
    3       | stick     | 1     | 4         | 00243     | false
            | ball      | 1     | 3         |           | false
    ---------------------------------------------------------------
    4       | treat     | 3     | 20        | 90210     | false
            | pizzle    | 1     | 16        |           | false
            | ball      | 5     | 2         |           | false
    ---------------------------------------------------------------
    5       | antler    | 1     | 24        | 44987     | true
    ---------------------------------------------------------------
    6       | antler    | 2     | 24        | 67098     | true
            | treat     | 3     | 20        |           | false
            | pizzle    | 1     | 16        |           | false
            | ball      | 5     | 2         |           | false
    ---------------------------------------------------------------
    7       | ball      | 1     | 6         | 96718     | false
    
    """

    # copy of view - modified to just return dictionary
    def optimize_shipping(self, data):
        """
        """

        def make_combinations(items):
            """
            makes all possible combinations to the length of the origin input
            """

            def inner(items, r):
                """
                recursively yields partitioned remainders of original partition lists
                """
                items = set(items)
                if not len(items):
                    yield ()
                    return
                first = next(iter(items))
                remainder = items.difference((first, ))
                for combination in combinations(remainder, r-1):
                    first_subset = (first, ) + combination
                    for partition in inner(remainder.difference(combination), r):
                        yield (first_subset, ) + partition

            def outter(items, r):
                """
                combines partition lists
                """
                items = set(items)
                for i in range(len(items), -1, -r):
                    if i == 0:
                        for partition in inner(items, r):
                            yield partition
                    elif i != r:
                        for combination in combinations(items, i):
                            for partition in inner(items.difference(combination), r):
                                yield partition + (combination, )

            # step through length of origin combination partitions to ensure full list
            for i in range(1, len(items)):
                gen = outter(items, i)
                for row in gen:
                    yield row

        # pull zipcode
        zipcode = data['zip']

        # create items
        regular, irregular = [], []
        for item in data['items']:
            qty = item['qty']
            del item['qty']
            for __ in xrange(qty):
                if 'is_irregular' in item:
                    if item['is_irregular']:
                        irregular.append(Item(**item))
                    else:
                        regular.append(Item(**item))
                else:
                    regular.append(Item(**item))

        # process irregular items
        irregular_boxes = []
        for item in irregular:
            box = Box()
            box.items.append(item)
            cost = get_irregular_price(zipcode, box.weight)
            box.shipping_method = 'UPS Ground'
            box.shipping_cost = cost
            irregular_boxes.append(box)

        # process regular items
        if len(regular):
            if len(regular) == 1:
                box = Box()
                box.items.extend(regular)
                method, cost = get_cheapest_option(zipcode, box.weight)
                box.shipping_method = method
                box.shipping_cost = cost
                order = Order()
                order.boxes.append(box)
                # add irregular boxes to order
                order.boxes.extend(irregular_boxes)
                return order.to_json()

            else:  # create orders/bundles from items combinations
                orders = []
                for combination in make_combinations(regular):  # full tuple of tuples of items. ex: ( (one,two), (three,) )
                    order = Order()
                    for grouping in combination:  # tuple of items. ex (one,two) from above
                        box = Box()
                        # add items to the box
                        box.items.extend(grouping)
                        # get cheapest shipping option for this box
                        method, cost = get_cheapest_option(zipcode, box.weight)
                        box.shipping_method = method
                        box.shipping_cost = cost
                        # add box to order
                        order.boxes.append(box)
                    # add irregular boxes to order
                    order.boxes.extend(irregular_boxes)
                    # add order to list of all possible combinations
                    orders.append(order)

                # get the cheapest order combination
                cheapest = min(orders, key=lambda o: o.shipping_cost)
                cheapest.shipping_cost = round(cheapest.shipping_cost, 2)

                # respond
                return cheapest.to_json()

        # no regular items:
        else:
            order = Order()
            order.boxes.extend(irregular_boxes)
            return order.to_json()

    def test_1(self):
        data = {
            'zip': 60631,
            'items': [
                {
                    'sku': 'stick',
                    'qty': 1,
                    'weight': 4
                }
            ]
        }
        expected = {
            'boxes': [
                {
                    'items': [
                        {
                            'sku': 'stick',
                            'qty': 1
                        }
                    ],
                    'cost': 1.7,
                    'method': 'UPS Mail Innovations'
                }
            ],
            'cost': 1.7
        }
        response = self.optimize_shipping(data)
        self.assertEqual(expected, response)

    def test_2(self):
        data = {
            'zip': 50172,
            'items': [
                {
                    'sku': 'stick',
                    'qty': 2,
                    'weight': 48
                }
            ]
        }
        expected = {
            'boxes': [
                {
                    'items': [
                        {
                            'sku': 'stick',
                            'qty': 2
                        }
                    ],
                    'cost': 8.88,
                    'method': 'UPS Ground'
                }
            ],
            'cost': 8.88
        }
        response = self.optimize_shipping(data)
        self.assertEqual(expected, response)

    def test_3(self):
        data = {
            'zip': 00243,
            'items': [
                {
                    'sku': 'stick',
                    'qty': 1,
                    'weight': 4
                },
                {
                    'sku': 'ball',
                    'qty': 1,
                    'weight': 3
                }
            ]
        }
        expected = {
            'boxes': [
                {
                    'items': [
                        {
                            'sku': 'ball',
                            'qty': 1
                        },
                        {
                            'sku': 'stick',
                            'qty': 1
                        }
                    ],
                    'cost': 2.05,
                    'method': 'UPS Mail Innovations'
                }
            ],
            'cost': 2.05
        }
        response = self.optimize_shipping(data)
        self.assertEqual(expected, response)

    def test_4(self):
        data = {
            'zip': 90210,
            'items': [
                {
                    'sku': 'treat',
                    'qty': 3,
                    'weight': 20
                },
                {
                    'sku': 'pizzle',
                    'qty': 1,
                    'weight': 16
                },
                {
                    'sku': 'ball',
                    'qty': 5,
                    'weight': 2
                }
            ]
        }
        expected = {
            'boxes':
                [
                    {
                        'items': [
                            {
                                'sku': 'ball',
                                'qty': 5
                            },
                            {
                                'sku': 'treat',
                                'qty': 3
                            },
                            {
                                'sku': 'pizzle',
                                'qty': 1
                            }
                        ],
                        'cost': 10.67,
                        'method': 'UPS Ground'
                    }
                ],
            'cost': 10.67
        }
        response = self.optimize_shipping(data)
        self.assertEqual(expected, response)

    def test_5(self):
        data = {
            'zip': 44987,
            'items': [
                {
                    'sku': 'antler',
                    'qty': 1,
                    'weight': 24,
                    'is_irregular': True
                }
            ]
        }
        expected = {
            'boxes': [
                {
                    'items': [
                        {
                            'sku': 'antler',
                            'qty': 1
                        }
                    ],
                    'cost': 8.64,
                    'method': 'UPS Ground'
                }
            ],
            'cost': 8.64
        }
        response = self.optimize_shipping(data)
        self.assertEqual(expected, response)

    def test_6(self):
        data = {
            'zip': 67098,
            'items': [
                {
                    'sku': 'antler',
                    'qty': 2,
                    'weight': 24,
                    'is_irregular': True
                },
                {
                    'sku': 'treat',
                    'qty': 3,
                    'weight': 20
                },
                {
                    'sku': 'pizzle',
                    'qty': 1,
                    'weight': 16
                },
                {
                    'sku': 'ball',
                    'qty': 5,
                    'weight': 2
                }
            ]
        }
        expected = {
            'boxes': [
                {
                    'items': [
                        {
                            'sku': 'ball',
                            'qty': 5
                        },
                        {
                            'sku': 'treat',
                            'qty': 3
                        },
                        {
                            'sku': 'pizzle',
                            'qty': 1
                        }
                    ],
                    'cost': 9.68,
                    'method': 'UPS Ground'
                },
                {
                    'items': [
                        {
                            'sku': 'antler',
                            'qty': 1
                        }
                    ],
                    'cost': 8.88,
                    'method': 'UPS Ground'
                },
                {
                    'items': [
                        {
                            'sku': 'antler',
                            'qty': 1
                        }
                    ],
                    'cost': 8.88,
                    'method': 'UPS Ground'
                }
            ],
            'cost': 27.44
        }
        response = self.optimize_shipping(data)
        self.assertEqual(expected, response)

    def test_7(self):
        data = {
            'zip': 96718,
            'items': [
                {
                    'sku': 'ball',
                    'qty': 1,
                    'weight': 6
                }
            ]
        }
        expected = {
            'boxes': [
                {
                    'items': [
                        {
                            'sku': 'ball',
                            'qty': 1
                        }
                    ],
                    'cost': 1.9,
                    'method': 'UPS Mail Innovations'
                }
            ],
            'cost': 1.9
        }
        response = self.optimize_shipping(data)
        self.assertEqual(expected, response)


if __name__ == '__main__':
    unittest.main()
