#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests:

    items               qty         weight                          dest            irregular
    -----------------------------------------------------------------------------------------
0   single              1           < 1 lb                          normal
1                                   1 < lbs < 5                     normal
2                                   > 5 lbs                         normal
3                                   < 1 lb                          hi/ak
4                                   1 < lbs < 5                     hi/ak
5                                   > 5 lbs                         hi/ak
6                                   < 1 lb                          normal          true
7                                   1 < lbs < 5                     normal          true
8                                   > 5 lbs                         normal          true
9                                   < 1 lb                          hi/ak           true
10                                  1 < lbs < 5                     hi/ak           true
11                                  > 5 lbs                         hi/ak           true

    items               qty         weight                          dest            irregular
-----------------------------------------------------------------------------------------
12  single              > 1         ind < 1 lb, total > 1 lbs       normal
13                                  ind < 1 lb, total < 1 lb        normal
14                                  1 < ind lbs < 5, total < 5      normal
15                                  1 < ind lbs < 5, total > 5      normal
16                                  ind > 5 lbs                     normal
17                                  ind < 1 lb, total > 1 lbs       hi/ak
18                                  ind < 1 lb, total < 1 lb        hi/ak
19                                  1 < ind lbs < 5, total < 5      hi/ak
20                                  1 < ind lbs < 5, total > 5      hi/ak
21                                  ind > 5 lbs                     hi/ak
22                                  ind < 1 lb, total > 1 lbs       normal          true
23                                  ind < 1 lb, total < 1 lb        normal          true
24                                  1 < ind lbs < 5, total < 5      normal          true
25                                  1 < ind lbs < 5, total > 5      normal          true
26                                  ind > 5 lbs                     normal          true
27                                  ind < 1 lb, total > 1 lbs       hi/ak           true
28                                  ind < 1 lb, total < 1 lb        hi/ak           true
29                                  1 < ind lbs < 5, total < 5      hi/ak           true
30                                  1 < ind lbs < 5, total > 5      hi/ak           true
31                                  ind > 5 lbs                     hi/ak           true

    items               qty         weight                          dest            irregular
-----------------------------------------------------------------------------------------
32  multiple            1 ea        ind < 1 lb, total > 1 lbs       normal
33                                  ind < 1 lb, total < 1 lb        normal
34                                  1 < ind lbs < 5, total < 5      normal
35                                  1 < ind lbs < 5, total > 5      normal
36                                  ind > 5 lbs                     normal
37                                  ind < 1 lb, total > 1 lbs       hi/ak
38                                  ind < 1 lb, total < 1 lb        hi/ak
39                                  1 < ind lbs < 5, total < 5      hi/ak
40                                  1 < ind lbs < 5, total > 5      hi/ak
41                                  ind > 5 lbs                     hi/ak
42                                  ind < 1 lb, total > 1 lbs       normal          true
43                                  ind < 1 lb, total < 1 lb        normal          true
44                                  1 < ind lbs < 5, total < 5      normal          true
45                                  1 < ind lbs < 5, total > 5      normal          true
46                                  ind > 5 lbs                     normal          true
47                                  ind < 1 lb, total > 1 lbs       hi/ak           true
48                                  ind < 1 lb, total < 1 lb        hi/ak           true
49                                  1 < ind lbs < 5, total < 5      hi/ak           true
50                                  1 < ind lbs < 5, total > 5      hi/ak           true
51                                  ind > 5 lbs                     hi/ak           true
52                                  ind < 1 lb, total > 1 lbs       normal          mix
53                                  ind < 1 lb, total < 1 lb        normal          mix
54                                  1 < ind lbs < 5, total < 5      normal          mix
55                                  1 < ind lbs < 5, total > 5      normal          mix
56                                  ind > 5 lbs                     normal          mix
57                                  ind < 1 lb, total > 1 lbs       hi/ak           mix
58                                  ind < 1 lb, total < 1 lb        hi/ak           mix
59                                  1 < ind lbs < 5, total < 5      hi/ak           mix
60                                  1 < ind lbs < 5, total > 5      hi/ak           mix
61                                  ind > 5 lbs                     hi/ak           mix

    items               qty         weight                          dest            irregular
    -----------------------------------------------------------------------------------------
62  multiple            > 1 ea      ind < 1 lb, total > 1 lbs       normal
63                                  ind < 1 lb, total < 1 lb        normal
64                                  1 < ind lbs < 5, total < 5      normal
65                                  1 < ind lbs < 5, total > 5      normal
66                                  ind > 5 lbs                     normal
67                                  ind < 1 lb, total > 1 lbs       hi/ak
68                                  ind < 1 lb, total < 1 lb        hi/ak
69                                  1 < ind lbs < 5, total < 5      hi/ak
70                                  1 < ind lbs < 5, total > 5      hi/ak
71                                  ind > 5 lbs                     hi/ak
72                                  ind < 1 lb, total > 1 lbs       normal          true
73                                  ind < 1 lb, total < 1 lb        normal          true
74                                  1 < ind lbs < 5, total < 5      normal          true
75                                  1 < ind lbs < 5, total > 5      normal          true
76                                  ind > 5 lbs                     normal          true
77                                  ind < 1 lb, total > 1 lbs       hi/ak           true
78                                  ind < 1 lb, total < 1 lb        hi/ak           true
79                                  1 < ind lbs < 5, total < 5      hi/ak           true
80                                  1 < ind lbs < 5, total > 5      hi/ak           true
81                                  ind > 5 lbs                     hi/ak           true
82                                  ind < 1 lb, total > 1 lbs       normal          mix
83                                  ind < 1 lb, total < 1 lb        normal          mix
84                                  1 < ind lbs < 5, total < 5      normal          mix
85                                  1 < ind lbs < 5, total > 5      normal          mix
86                                  ind > 5 lbs                     normal          mix
87                                  ind < 1 lb, total > 1 lbs       hi/ak           mix
88                                  ind < 1 lb, total < 1 lb        hi/ak           mix
99                                  1 < ind lbs < 5, total < 5      hi/ak           mix
90                                  1 < ind lbs < 5, total > 5      hi/ak           mix
91                                  ind > 5 lbs                     hi/ak           mix

    items               qty         weight                          dest            irregular
    -----------------------------------------------------------------------------------------
92  multiple            mix         ind < 1 lb, total > 1 lbs       normal
93                                  ind < 1 lb, total < 1 lb        normal
94                                  1 < ind lbs < 5, total < 5      normal
95                                  1 < ind lbs < 5, total > 5      normal
96                                  ind > 5 lbs                     normal
97                                  ind < 1 lb, total > 1 lbs       hi/ak
98                                  ind < 1 lb, total < 1 lb        hi/ak
99                                  1 < ind lbs < 5, total < 5      hi/ak
100                                 1 < ind lbs < 5, total > 5      hi/ak
101                                 ind > 5 lbs                     hi/ak
102                                 ind < 1 lb, total > 1 lbs       normal          true
103                                 ind < 1 lb, total < 1 lb        normal          true
104                                 1 < ind lbs < 5, total < 5      normal          true
105                                 1 < ind lbs < 5, total > 5      normal          true
106                                 ind > 5 lbs                     normal          true
107                                 ind < 1 lb, total > 1 lbs       hi/ak           true
108                                 ind < 1 lb, total < 1 lb        hi/ak           true
109                                 1 < ind lbs < 5, total < 5      hi/ak           true
110                                 1 < ind lbs < 5, total > 5      hi/ak           true
111                                 ind > 5 lbs                     hi/ak           true
112                                 ind < 1 lb, total > 1 lbs       normal          mix
113                                 ind < 1 lb, total < 1 lb        normal          mix
114                                 1 < ind lbs < 5, total < 5      normal          mix
115                                 1 < ind lbs < 5, total > 5      normal          mix
116                                 ind > 5 lbs                     normal          mix
117                                 ind < 1 lb, total > 1 lbs       hi/ak           mix
118                                 ind < 1 lb, total < 1 lb        hi/ak           mix
119                                 1 < ind lbs < 5, total < 5      hi/ak           mix
120                                 1 < ind lbs < 5, total > 5      hi/ak           mix
121                                 ind > 5 lbs                     hi/ak           mix

"""

from itertools import combinations
import unittest

from matrices import get_cheapest_option, get_irregular_price
from models import Item, Box, Order


class TestOptimizer(unittest.TestCase):

    # copy of view - modified to just return order object
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
                return order

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

                # get the cheapest order combination; respond
                return min(orders, key=lambda o: o.shipping_cost)

        # no regular items:
        else:
            order = Order()
            order.boxes.extend(irregular_boxes)
            return order

    # single item, qty = 1
    def test_0(self):
        input_data = {"zip": "60084", "items": [{"sku": "sample bull sticks", "weight": 4, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Mail Innovations')

    def test_1(self):
        input_data = {"zip": "60084", "items": [{"sku": "bag bully sticks", "weight": 30, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Mail Innovations')

    def test_2(self):
        input_data = {"zip": "60084", "items": [{"sku": "bulk bully sticks", "weight": 180, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Ground')

    def test_3(self):
        input_data = {"zip": "96810", "items": [{"sku": "sample bull sticks", "weight": 4, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Mail Innovations')

    def test_4(self):
        input_data = {"zip": "96810", "items": [{"sku": "bag bully sticks", "weight": 30, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Mail Innovations')

    def test_5(self):
        input_data = {"zip": "96810", "items": [{"sku": "bulk bully sticks", "weight": 180, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Ground')

    def test_6(self):
        input_data = {"zip": "60084", "items": [{"sku": "sample bull sticks", "weight": 4, "qty": 1, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Ground')

    def test_7(self):
        input_data = {"zip": "60084", "items": [{"sku": "bag bully sticks", "weight": 30, "qty": 1, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Ground')

    def test_8(self):
        input_data = {"zip": "60084", "items": [{"sku": "bulk bully sticks", "weight": 180, "qty": 1, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Ground')

    def test_9(self):
        input_data = {"zip": "96810", "items": [{"sku": "sample bull sticks", "weight": 4, "qty": 1, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Ground')

    def test_10(self):
        input_data = {"zip": "96810", "items": [{"sku": "bag bully sticks", "weight": 30, "qty": 1, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Ground')

    def test_11(self):
        input_data = {"zip": "96810", "items": [{"sku": "bulk bully sticks", "weight": 180, "qty": 1, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Ground')

    # single item, qty > 1
    def test_12(self):
        input_data = {"zip": "02345", "items": [{"sku": "bag bull sticks", "weight": 10, "qty": 2}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Mail Innovations')
        self.assertEqual(response.boxes[1].shipping_method, 'UPS Mail Innovations')

    def test_13(self):
        input_data = {"zip": "21432", "items": [{"sku": "sample bully sticks", "weight": 6, "qty": 2}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Mail Innovations')

    def test_14(self):
        input_data = {"zip": "54093", "items": [{"sku": "big bag bully sticks", "weight": 20, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Mail Innovations')

    def test_15(self):
        input_data = {"zip": "60631", "items": [{"sku": "bulk bully sticks", "weight": 150, "qty": 4}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Ground')

    def test_16(self):
        input_data = {"zip": "45455", "items": [{"sku": "bulk bull sticks", "weight": 160, "qty": 2}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Ground')

    def test_17(self):
        input_data = {"zip": "99701", "items": [{"sku": "bag bull sticks", "weight": 10, "qty": 2}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        for box in response.boxes:
            self.assertEqual(box.shipping_method, 'UPS Mail Innovations')

    def test_18(self):
        input_data = {"zip": "99701", "items": [{"sku": "sample bully sticks", "weight": 6, "qty": 2}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Mail Innovations')

    def test_19(self):
        input_data = {"zip": "99701", "items": [{"sku": "big bag bully sticks", "weight": 20, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Mail Innovations')

    def test_20(self):
        input_data = {"zip": "99701", "items": [{"sku": "bulk bully sticks", "weight": 150, "qty": 4}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Ground')

    def test_21(self):
        input_data = {"zip": "99701", "items": [{"sku": "bulk bull sticks", "weight": 160, "qty": 2}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Ground')

    def test_22(self):
        input_data = {"zip": "02345", "items": [{"sku": "bag bull sticks", "weight": 10, "qty": 2, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Ground')

    def test_23(self):
        input_data = {"zip": "21432", "items": [{"sku": "sample bully sticks", "weight": 6, "qty": 2, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Ground')

    def test_24(self):
        input_data = {"zip": "54093", "items": [{"sku": "big bag bully sticks", "weight": 20, "qty": 3, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 3)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Ground')

    def test_25(self):
        input_data = {"zip": "60631", "items": [{"sku": "bulk bully sticks", "weight": 150, "qty": 4, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 4)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Ground')

    def test_26(self):
        input_data = {"zip": "45455", "items": [{"sku": "bulk bull sticks", "weight": 160, "qty": 2, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Ground')

    def test_27(self):
        input_data = {"zip": "99701", "items": [{"sku": "bag bull sticks", "weight": 10, "qty": 2, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Ground')

    def test_28(self):
        input_data = {"zip": "99701", "items": [{"sku": "sample bully sticks", "weight": 6, "qty": 2, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Ground')

    def test_29(self):
        input_data = {"zip": "99701", "items": [{"sku": "big bag bully sticks", "weight": 20, "qty": 3, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 3)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Ground')

    def test_30(self):
        input_data = {"zip": "99701", "items": [{"sku": "bulk bully sticks", "weight": 150, "qty": 4, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 4)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Ground')

    def test_31(self):
        input_data = {"zip": "99701", "items": [{"sku": "bulk bull sticks", "weight": 160, "qty": 2, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Ground')

    # multiple, 1 ea
    def test_32(self):
        input_data = {"zip": "64231", "items": [{"sku": "bag bully sticks", "weight": 10, "qty": 1}, {"sku": "big bag bully sticks", "weight": 14, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        for box in response.boxes:
            self.assertEqual(box.shipping_method, 'UPS Mail Innovations')

    def test_33(self):
        input_data = {"zip": "64231", "items": [{"sku": "bag bully sticks", "weight": 8, "qty": 1}, {"sku": "sample bully sticks", "weight": 6, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Mail Innovations')

    def test_34(self):
        input_data = {"zip": "64231", "items": [{"sku": "kong filler", "weight": 32, "qty": 1}, {"sku": "bigger bag bully sticks", "weight": 32, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Mail Innovations')

    def test_35(self):
        input_data = {"zip": "64231", "items": [{"sku": "bulk bully sticks", "weight": 72, "qty": 1}, {"sku": "bulk kong filler", "weight": 72, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Ground')

    def test_36(self):
        input_data = {"zip": "64231", "items": [{"sku": "massive bulk bully sticks", "weight": 160, "qty": 1}, {"sku": "massive bulk kong filler", "weight": 160, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Ground')

    def test_37(self):
        input_data = {"zip": "99701", "items": [{"sku": "bag bully sticks", "weight": 10, "qty": 1}, {"sku": "big bag bully sticks", "weight": 14, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        for box in response.boxes:
            self.assertEqual(box.shipping_method, 'UPS Mail Innovations')

    def test_38(self):
        input_data = {"zip": "99701", "items": [{"sku": "bag bully sticks", "weight": 8, "qty": 1}, {"sku": "sample bully sticks", "weight": 6, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Mail Innovations')

    def test_39(self):
        input_data = {"zip": "99701", "items": [{"sku": "kong filler", "weight": 32, "qty": 1}, {"sku": "bigger bag bully sticks", "weight": 32, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Mail Innovations')

    def test_40(self):
        input_data = {"zip": "99701", "items": [{"sku": "bulk bully sticks", "weight": 72, "qty": 1}, {"sku": "bulk kong filler", "weight": 72, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        for box in response.boxes:
            self.assertEqual(box.shipping_method, 'UPS Mail Innovations')

    def test_41(self):
        input_data = {"zip": "99701", "items": [{"sku": "massive bulk bully sticks", "weight": 160, "qty": 1}, {"sku": "massive bulk kong filler", "weight": 160, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Ground')

    def test_42(self):
        input_data = {"zip": "64231", "items": [{"sku": "bag bully sticks", "weight": 10, "qty": 1, "is_irregular": True}, {"sku": "big bag bully sticks", "weight": 14, "qty": 1, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        for box in response.boxes:
            self.assertEqual(box.shipping_method, 'UPS Ground')

    def test_43(self):
        input_data = {"zip": "64231", "items": [{"sku": "bag bully sticks", "weight": 8, "qty": 1, "is_irregular": True}, {"sku": "sample bully sticks", "weight": 6, "qty": 1, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        for box in response.boxes:
            self.assertEqual(box.shipping_method, 'UPS Ground')

    def test_44(self):
        input_data = {"zip": "64231", "items": [{"sku": "kong filler", "weight": 32, "qty": 1, "is_irregular": True}, {"sku": "bigger bag bully sticks", "weight": 32, "qty": 1, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        for box in response.boxes:
            self.assertEqual(box.shipping_method, 'UPS Ground')

    def test_45(self):
        input_data = {"zip": "64231", "items": [{"sku": "bulk bully sticks", "weight": 72, "qty": 1, "is_irregular": True}, {"sku": "bulk kong filler", "weight": 72, "qty": 1, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        for box in response.boxes:
            self.assertEqual(box.shipping_method, 'UPS Ground')

    def test_46(self):
        input_data = {"zip": "64231", "items": [{"sku": "massive bulk bully sticks", "weight": 160, "qty": 1, "is_irregular": True}, {"sku": "massive bulk kong filler", "weight": 160, "qty": 1, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        for box in response.boxes:
            self.assertEqual(box.shipping_method, 'UPS Ground')

    def test_47(self):
        input_data = {"zip": "99701", "items": [{"sku": "bag bully sticks", "weight": 10, "qty": 1, "is_irregular": True}, {"sku": "big bag bully sticks", "weight": 14, "qty": 1, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        for box in response.boxes:
            self.assertEqual(box.shipping_method, 'UPS Ground')

    def test_48(self):
        input_data = {"zip": "99701", "items": [{"sku": "bag bully sticks", "weight": 8, "qty": 1, "is_irregular": True}, {"sku": "sample bully sticks", "weight": 6, "qty": 1, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        for box in response.boxes:
            self.assertEqual(box.shipping_method, 'UPS Ground')

    def test_49(self):
        input_data = {"zip": "99701", "items": [{"sku": "kong filler", "weight": 32, "qty": 1, "is_irregular": True}, {"sku": "bigger bag bully sticks", "weight": 32, "qty": 1, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        for box in response.boxes:
            self.assertEqual(box.shipping_method, 'UPS Ground')

    def test_50(self):
        input_data = {"zip": "99701", "items": [{"sku": "bulk bully sticks", "weight": 72, "qty": 1, "is_irregular": True}, {"sku": "bulk kong filler", "weight": 72, "qty": 1, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        for box in response.boxes:
            self.assertEqual(box.shipping_method, 'UPS Ground')

    def test_51(self):
        input_data = {"zip": "99701", "items": [{"sku": "massive bulk bully sticks", "weight": 160, "qty": 1, "is_irregular": True}, {"sku": "massive bulk kong filler", "weight": 160, "qty": 1, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        for box in response.boxes:
            self.assertEqual(box.shipping_method, 'UPS Ground')

    def test_52(self):
        input_data = {"zip": "64231", "items": [{"sku": "bag bully sticks", "weight": 10, "qty": 1, "is_irregular": True}, {"sku": "big bag bully sticks", "weight": 14, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        self.assertEqual(len([box for box in response.boxes if box.shipping_method == 'UPS Ground']), 1)
        self.assertEqual(len([box for box in response.boxes if box.shipping_method == 'UPS Mail Innovations']), 1)

    def test_53(self):
        input_data = {"zip": "64231", "items": [{"sku": "bag bully sticks", "weight": 8, "qty": 1, "is_irregular": True}, {"sku": "sample bully sticks", "weight": 6, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        self.assertEqual(len([box for box in response.boxes if box.shipping_method == 'UPS Ground']), 1)
        self.assertEqual(len([box for box in response.boxes if box.shipping_method == 'UPS Mail Innovations']), 1)

    def test_54(self):
        input_data = {"zip": "64231", "items": [{"sku": "kong filler", "weight": 32, "qty": 1, "is_irregular": True}, {"sku": "bigger bag bully sticks", "weight": 32, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        self.assertEqual(len([box for box in response.boxes if box.shipping_method == 'UPS Ground']), 1)
        self.assertEqual(len([box for box in response.boxes if box.shipping_method == 'UPS Mail Innovations']), 1)

    def test_55(self):
        input_data = {"zip": "64231", "items": [{"sku": "bulk bully sticks", "weight": 72, "qty": 1, "is_irregular": True}, {"sku": "bulk kong filler", "weight": 72, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        self.assertEqual(len([box for box in response.boxes if box.shipping_method == 'UPS Ground']), 2)
        self.assertEqual(len([box for box in response.boxes if box.shipping_method == 'UPS Mail Innovations']), 0)

    def test_56(self):
        input_data = {"zip": "64231", "items": [{"sku": "massive bulk bully sticks", "weight": 160, "qty": 1, "is_irregular": True}, {"sku": "massive bulk kong filler", "weight": 160, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        self.assertEqual(len([box for box in response.boxes if box.shipping_method == 'UPS Ground']), 2)
        self.assertEqual(len([box for box in response.boxes if box.shipping_method == 'UPS Mail Innovations']), 0)

    def test_57(self):
        input_data = {"zip": "99701", "items": [{"sku": "bag bully sticks", "weight": 10, "qty": 1, "is_irregular": True}, {"sku": "big bag bully sticks", "weight": 14, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        self.assertEqual(len([box for box in response.boxes if box.shipping_method == 'UPS Ground']), 1)
        self.assertEqual(len([box for box in response.boxes if box.shipping_method == 'UPS Mail Innovations']), 1)

    def test_58(self):
        input_data = {"zip": "99701", "items": [{"sku": "bag bully sticks", "weight": 8, "qty": 1, "is_irregular": True}, {"sku": "sample bully sticks", "weight": 6, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        self.assertEqual(len([box for box in response.boxes if box.shipping_method == 'UPS Ground']), 1)
        self.assertEqual(len([box for box in response.boxes if box.shipping_method == 'UPS Mail Innovations']), 1)

    def test_59(self):
        input_data = {"zip": "99701", "items": [{"sku": "kong filler", "weight": 32, "qty": 1, "is_irregular": True}, {"sku": "bigger bag bully sticks", "weight": 32, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        self.assertEqual(len([box for box in response.boxes if box.shipping_method == 'UPS Ground']), 1)
        self.assertEqual(len([box for box in response.boxes if box.shipping_method == 'UPS Mail Innovations']), 1)

    def test_60(self):
        input_data = {"zip": "99701", "items": [{"sku": "bulk bully sticks", "weight": 72, "qty": 1, "is_irregular": True}, {"sku": "bulk kong filler", "weight": 72, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        self.assertEqual(len([box for box in response.boxes if box.shipping_method == 'UPS Ground']), 1)
        self.assertEqual(len([box for box in response.boxes if box.shipping_method == 'UPS Mail Innovations']), 1)

    def test_61(self):
        input_data = {"zip": "99701", "items": [{"sku": "massive bulk bully sticks", "weight": 160, "qty": 1, "is_irregular": True}, {"sku": "massive bulk kong filler", "weight": 160, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 2)
        self.assertEqual(len([box for box in response.boxes if box.shipping_method == 'UPS Ground']), 2)
        self.assertEqual(len([box for box in response.boxes if box.shipping_method == 'UPS Mail Innovations']), 0)

    # multiple items, >1 ea
    def test_62(self):
        input_data = {"zip": "64231", "items": [{"sku": "bag bully sticks", "weight": 10, "qty": 3}, {"sku": "big bag bully sticks", "weight": 14, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Ground')

    def test_63(self):
        input_data = {"zip": "64231", "items": [{"sku": "bag bully sticks", "weight": 8, "qty": 3}, {"sku": "sample bully sticks", "weight": 6, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Mail Innovations')

    def test_64(self):
        input_data = {"zip": "64231", "items": [{"sku": "kong filler", "weight": 32, "qty": 3}, {"sku": "bigger bag bully sticks", "weight": 32, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Ground')

    def test_65(self):
        input_data = {"zip": "64231", "items": [{"sku": "bulk bully sticks", "weight": 72, "qty": 3}, {"sku": "bulk kong filler", "weight": 72, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Ground')

    def test_66(self):
        input_data = {"zip": "64231", "items": [{"sku": "massive bulk bully sticks", "weight": 160, "qty": 3}, {"sku": "massive bulk kong filler", "weight": 160, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Ground')

    def test_67(self):
        input_data = {"zip": "99701", "items": [{"sku": "bag bully sticks", "weight": 10, "qty": 3}, {"sku": "big bag bully sticks", "weight": 14, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Mail Innovations')

    def test_68(self):
        input_data = {"zip": "99701", "items": [{"sku": "bag bully sticks", "weight": 8, "qty": 3}, {"sku": "sample bully sticks", "weight": 6, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Mail Innovations')

    def test_69(self):
        input_data = {"zip": "99701", "items": [{"sku": "kong filler", "weight": 32, "qty": 3}, {"sku": "bigger bag bully sticks", "weight": 32, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 3)
        for box in response.boxes:
            self.assertEqual(box.shipping_method, 'UPS Mail Innovations')

    def test_70(self):
        input_data = {"zip": "99701", "items": [{"sku": "bulk bully sticks", "weight": 72, "qty": 3}, {"sku": "bulk kong filler", "weight": 72, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 6)
        for box in response.boxes:
            self.assertEqual(box.shipping_method, 'UPS Mail Innovations')

    def test_71(self):
        input_data = {"zip": "99701", "items": [{"sku": "massive bulk bully sticks", "weight": 160, "qty": 3}, {"sku": "massive bulk kong filler", "weight": 160, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 1)
        self.assertEqual(response.boxes[0].shipping_method, 'UPS Ground')

    def test_72(self):
        input_data = {"zip": "64231", "items": [{"sku": "bag bully sticks", "weight": 10, "qty": 3, "is_irregular": True}, {"sku": "big bag bully sticks", "weight": 14, "qty": 3, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 6)
        for box in response.boxes:
            self.assertEqual(box.shipping_method, 'UPS Ground')

    def test_73(self):
        input_data = {"zip": "64231", "items": [{"sku": "bag bully sticks", "weight": 8, "qty": 3, "is_irregular": True}, {"sku": "sample bully sticks", "weight": 6, "qty": 3, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 6)
        for box in response.boxes:
            self.assertEqual(box.shipping_method, 'UPS Ground')

    def test_74(self):
        input_data = {"zip": "64231", "items": [{"sku": "kong filler", "weight": 32, "qty": 3, "is_irregular": True}, {"sku": "bigger bag bully sticks", "weight": 32, "qty": 3, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 6)
        for box in response.boxes:
            self.assertEqual(box.shipping_method, 'UPS Ground')

    def test_75(self):
        input_data = {"zip": "64231", "items": [{"sku": "bulk bully sticks", "weight": 72, "qty": 3, "is_irregular": True}, {"sku": "bulk kong filler", "weight": 72, "qty": 3, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 6)
        for box in response.boxes:
            self.assertEqual(box.shipping_method, 'UPS Ground')

    def test_76(self):
        input_data = {"zip": "64231", "items": [{"sku": "massive bulk bully sticks", "weight": 160, "qty": 3, "is_irregular": True}, {"sku": "massive bulk kong filler", "weight": 160, "qty": 3, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 6)
        for box in response.boxes:
            self.assertEqual(box.shipping_method, 'UPS Ground')

    def test_77(self):
        input_data = {"zip": "99701", "items": [{"sku": "bag bully sticks", "weight": 10, "qty": 3, "is_irregular": True}, {"sku": "big bag bully sticks", "weight": 14, "qty": 3, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 6)
        for box in response.boxes:
            self.assertEqual(box.shipping_method, 'UPS Ground')

    def test_78(self):
        input_data = {"zip": "99701", "items": [{"sku": "bag bully sticks", "weight": 8, "qty": 3, "is_irregular": True}, {"sku": "sample bully sticks", "weight": 6, "qty": 3, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 6)
        for box in response.boxes:
            self.assertEqual(box.shipping_method, 'UPS Ground')

    def test_79(self):
        input_data = {"zip": "99701", "items": [{"sku": "kong filler", "weight": 32, "qty": 3, "is_irregular": True}, {"sku": "bigger bag bully sticks", "weight": 32, "qty": 3, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 6)
        for box in response.boxes:
            self.assertEqual(box.shipping_method, 'UPS Ground')

    def test_80(self):
        input_data = {"zip": "99701", "items": [{"sku": "bulk bully sticks", "weight": 72, "qty": 3, "is_irregular": True}, {"sku": "bulk kong filler", "weight": 72, "qty": 3, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 6)
        for box in response.boxes:
            self.assertEqual(box.shipping_method, 'UPS Ground')

    def test_81(self):
        input_data = {"zip": "99701", "items": [{"sku": "massive bulk bully sticks", "weight": 160, "qty": 3, "is_irregular": True}, {"sku": "massive bulk kong filler", "weight": 160, "qty": 3, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 6)
        for box in response.boxes:
            self.assertEqual(box.shipping_method, 'UPS Ground')

    def test_82(self):
        input_data = {"zip": "64231", "items": [{"sku": "bag bully sticks", "weight": 10, "qty": 3, "is_irregular": True}, {"sku": "big bag bully sticks", "weight": 14, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 4)
        self.assertEqual(len([box for box in response.boxes if box.shipping_method == 'UPS Ground']), 3)
        self.assertEqual(len([box for box in response.boxes if box.shipping_method == 'UPS Mail Innovations']), 1)

    def test_83(self):
        input_data = {"zip": "64231", "items": [{"sku": "bag bully sticks", "weight": 8, "qty": 3, "is_irregular": True}, {"sku": "sample bully sticks", "weight": 6, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 5)
        self.assertEqual(len([box for box in response.boxes if box.shipping_method == 'UPS Ground']), 3)
        self.assertEqual(len([box for box in response.boxes if box.shipping_method == 'UPS Mail Innovations']), 2)

    def test_84(self):
        input_data = {"zip": "64231", "items": [{"sku": "kong filler", "weight": 32, "qty": 3, "is_irregular": True}, {"sku": "bigger bag bully sticks", "weight": 32, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)
        self.assertEqual(len(response.boxes), 4)
        self.assertEqual(len([box for box in response.boxes if box.shipping_method == 'UPS Ground']), 4)
        self.assertEqual(len([box for box in response.boxes if box.shipping_method == 'UPS Mail Innovations']), 0)

    def test_85(self):
        input_data = {"zip": "64231", "items": [{"sku": "bulk bully sticks", "weight": 72, "qty": 3, "is_irregular": True}, {"sku": "bulk kong filler", "weight": 72, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_86(self):
        input_data = {"zip": "64231", "items": [{"sku": "massive bulk bully sticks", "weight": 160, "qty": 3, "is_irregular": True}, {"sku": "massive bulk kong filler", "weight": 160, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_87(self):
        input_data = {"zip": "99701", "items": [{"sku": "bag bully sticks", "weight": 10, "qty": 3, "is_irregular": True}, {"sku": "big bag bully sticks", "weight": 14, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_88(self):
        input_data = {"zip": "99701", "items": [{"sku": "bag bully sticks", "weight": 8, "qty": 3, "is_irregular": True}, {"sku": "sample bully sticks", "weight": 6, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_89(self):
        input_data = {"zip": "99701", "items": [{"sku": "kong filler", "weight": 32, "qty": 3, "is_irregular": True}, {"sku": "bigger bag bully sticks", "weight": 32, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_90(self):
        input_data = {"zip": "99701", "items": [{"sku": "bulk bully sticks", "weight": 72, "qty": 3, "is_irregular": True}, {"sku": "bulk kong filler", "weight": 72, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_91(self):
        input_data = {"zip": "99701", "items": [{"sku": "massive bulk bully sticks", "weight": 160, "qty": 3, "is_irregular": True}, {"sku": "massive bulk kong filler", "weight": 160, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    # multiple items, mix qty
    def test_92(self):
        input_data = {"zip": "64231", "items": [{"sku": "bag bully sticks", "weight": 10, "qty": 1}, {"sku": "big bag bully sticks", "weight": 14, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_93(self):
        input_data = {"zip": "64231", "items": [{"sku": "bag bully sticks", "weight": 8, "qty": 1}, {"sku": "sample bully sticks", "weight": 6, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_94(self):
        input_data = {"zip": "64231", "items": [{"sku": "kong filler", "weight": 32, "qty": 3}, {"sku": "bigger bag bully sticks", "weight": 32, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_95(self):
        input_data = {"zip": "64231", "items": [{"sku": "bulk bully sticks", "weight": 72, "qty": 3}, {"sku": "bulk kong filler", "weight": 72, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_96(self):
        input_data = {"zip": "64231", "items": [{"sku": "massive bulk bully sticks", "weight": 160, "qty": 1}, {"sku": "massive bulk kong filler", "weight": 160, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_97(self):
        input_data = {"zip": "99701", "items": [{"sku": "bag bully sticks", "weight": 10, "qty": 3}, {"sku": "big bag bully sticks", "weight": 14, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_98(self):
        input_data = {"zip": "99701", "items": [{"sku": "bag bully sticks", "weight": 8, "qty": 1}, {"sku": "sample bully sticks", "weight": 6, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_99(self):
        input_data = {"zip": "99701", "items": [{"sku": "kong filler", "weight": 32, "qty": 3}, {"sku": "bigger bag bully sticks", "weight": 32, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_100(self):
        input_data = {"zip": "99701", "items": [{"sku": "bulk bully sticks", "weight": 72, "qty": 1}, {"sku": "bulk kong filler", "weight": 72, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_101(self):
        input_data = {"zip": "99701", "items": [{"sku": "massive bulk bully sticks", "weight": 160, "qty": 3}, {"sku": "massive bulk kong filler", "weight": 160, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_102(self):
        input_data = {"zip": "64231", "items": [{"sku": "bag bully sticks", "weight": 10, "qty": 1, "is_irregular": True}, {"sku": "big bag bully sticks", "weight": 14, "qty": 3, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_103(self):
        input_data = {"zip": "64231", "items": [{"sku": "bag bully sticks", "weight": 8, "qty": 3, "is_irregular": True}, {"sku": "sample bully sticks", "weight": 6, "qty": 1, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_104(self):
        input_data = {"zip": "64231", "items": [{"sku": "kong filler", "weight": 32, "qty": 1, "is_irregular": True}, {"sku": "bigger bag bully sticks", "weight": 32, "qty": 3, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_105(self):
        input_data = {"zip": "64231", "items": [{"sku": "bulk bully sticks", "weight": 72, "qty": 3, "is_irregular": True}, {"sku": "bulk kong filler", "weight": 72, "qty": 1, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_106(self):
        input_data = {"zip": "64231", "items": [{"sku": "massive bulk bully sticks", "weight": 160, "qty": 1, "is_irregular": True}, {"sku": "massive bulk kong filler", "weight": 160, "qty": 3, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_107(self):
        input_data = {"zip": "99701", "items": [{"sku": "bag bully sticks", "weight": 10, "qty": 3, "is_irregular": True}, {"sku": "big bag bully sticks", "weight": 14, "qty": 1, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_108(self):
        input_data = {"zip": "99701", "items": [{"sku": "bag bully sticks", "weight": 8, "qty": 1, "is_irregular": True}, {"sku": "sample bully sticks", "weight": 6, "qty": 3, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_109(self):
        input_data = {"zip": "99701", "items": [{"sku": "kong filler", "weight": 32, "qty": 3, "is_irregular": True}, {"sku": "bigger bag bully sticks", "weight": 32, "qty": 1, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_110(self):
        input_data = {"zip": "99701", "items": [{"sku": "bulk bully sticks", "weight": 72, "qty": 1, "is_irregular": True}, {"sku": "bulk kong filler", "weight": 72, "qty": 3, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_111(self):
        input_data = {"zip": "99701", "items": [{"sku": "massive bulk bully sticks", "weight": 160, "qty": 3, "is_irregular": True}, {"sku": "massive bulk kong filler", "weight": 160, "qty": 1, "is_irregular": True}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_112(self):
        input_data = {"zip": "64231", "items": [{"sku": "bag bully sticks", "weight": 10, "qty": 1, "is_irregular": True}, {"sku": "big bag bully sticks", "weight": 14, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_113(self):
        input_data = {"zip": "64231", "items": [{"sku": "bag bully sticks", "weight": 8, "qty": 3, "is_irregular": True}, {"sku": "sample bully sticks", "weight": 6, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_114(self):
        input_data = {"zip": "64231", "items": [{"sku": "kong filler", "weight": 32, "qty": 1, "is_irregular": True}, {"sku": "bigger bag bully sticks", "weight": 32, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_115(self):
        input_data = {"zip": "64231", "items": [{"sku": "bulk bully sticks", "weight": 72, "qty": 3, "is_irregular": True}, {"sku": "bulk kong filler", "weight": 72, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_116(self):
        input_data = {"zip": "64231", "items": [{"sku": "massive bulk bully sticks", "weight": 160, "qty": 1, "is_irregular": True}, {"sku": "massive bulk kong filler", "weight": 160, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_117(self):
        input_data = {"zip": "99701", "items": [{"sku": "bag bully sticks", "weight": 10, "qty": 3, "is_irregular": True}, {"sku": "big bag bully sticks", "weight": 14, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_118(self):
        input_data = {"zip": "99701", "items": [{"sku": "bag bully sticks", "weight": 8, "qty": 1, "is_irregular": True}, {"sku": "sample bully sticks", "weight": 6, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_119(self):
        input_data = {"zip": "99701", "items": [{"sku": "kong filler", "weight": 32, "qty": 3, "is_irregular": True}, {"sku": "bigger bag bully sticks", "weight": 32, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_120(self):
        input_data = {"zip": "99701", "items": [{"sku": "bulk bully sticks", "weight": 72, "qty": 1, "is_irregular": True}, {"sku": "bulk kong filler", "weight": 72, "qty": 3}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)

    def test_121(self):
        input_data = {"zip": "99701", "items": [{"sku": "massive bulk bully sticks", "weight": 160, "qty": 3, "is_irregular": True}, {"sku": "massive bulk kong filler", "weight": 160, "qty": 1}]}
        response = self.optimize_shipping(input_data)
        self.assertIsInstance(response, Order)


if __name__ == '__main__':
    unittest.main()
