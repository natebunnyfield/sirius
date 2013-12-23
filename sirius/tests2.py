#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests:

items               qty         weight                          dest            irregular
-----------------------------------------------------------------------------------------
single              1           < 1 lb                          normal
                                1 < lbs < 5                     normal
                                > 5 lbs                         normal
                                < 1 lb                          hi/ak
                                1 < lbs < 5                     hi/ak
                                > 5 lbs                         hi/ak
                                < 1 lb                          normal          true
                                1 < lbs < 5                     normal          true
                                > 5 lbs                         normal          true
                                < 1 lb                          hi/ak           true
                                1 < lbs < 5                     hi/ak           true
                                > 5 lbs                         hi/ak           true

items               qty         weight                          dest            irregular
-----------------------------------------------------------------------------------------
single              > 1         ind < 1 lb, total > 1 lbs       normal
                                ind < 1 lb, total < 1 lb        normal
                                1 < ind lbs < 5, total < 5      normal
                                1 < ind lbs < 5, total > 5      normal
                                ind > 5 lbs                     normal
                                ind < 1 lb, total > 1 lbs       hi/ak
                                ind < 1 lb, total < 1 lb        hi/ak
                                1 < ind lbs < 5, total < 5      hi/ak
                                1 < ind lbs < 5, total > 5      hi/ak
                                ind > 5 lbs                     hi/ak
                                ind < 1 lb, total > 1 lbs       normal          true
                                ind < 1 lb, total < 1 lb        normal          true
                                1 < ind lbs < 5, total < 5      normal          true
                                1 < ind lbs < 5, total > 5      normal          true
                                ind > 5 lbs                     normal          true
                                ind < 1 lb, total > 1 lbs       hi/ak           true
                                ind < 1 lb, total < 1 lb        hi/ak           true
                                1 < ind lbs < 5, total < 5      hi/ak           true
                                1 < ind lbs < 5, total > 5      hi/ak           true
                                ind > 5 lbs                     hi/ak           true

items               qty         weight                          dest            irregular
-----------------------------------------------------------------------------------------
multiple            1 ea        ind < 1 lb, total > 1 lbs       normal
                                ind < 1 lb, total < 1 lb        normal
                                1 < ind lbs < 5, total < 5      normal
                                1 < ind lbs < 5, total > 5      normal
                                ind > 5 lbs                     normal
                                ind < 1 lb, total > 1 lbs       hi/ak
                                ind < 1 lb, total < 1 lb        hi/ak
                                1 < ind lbs < 5, total < 5      hi/ak
                                1 < ind lbs < 5, total > 5      hi/ak
                                ind > 5 lbs                     hi/ak
                                ind < 1 lb, total > 1 lbs       normal          true
                                ind < 1 lb, total < 1 lb        normal          true
                                1 < ind lbs < 5, total < 5      normal          true
                                1 < ind lbs < 5, total > 5      normal          true
                                ind > 5 lbs                     normal          true
                                ind < 1 lb, total > 1 lbs       hi/ak           true
                                ind < 1 lb, total < 1 lb        hi/ak           true
                                1 < ind lbs < 5, total < 5      hi/ak           true
                                1 < ind lbs < 5, total > 5      hi/ak           true
                                ind > 5 lbs                     hi/ak           true

items               qty         weight                          dest            irregular
-----------------------------------------------------------------------------------------
multiple            > 1 ea      ind < 1 lb, total > 1 lbs       normal
                                ind < 1 lb, total < 1 lb        normal
                                1 < ind lbs < 5, total < 5      normal
                                1 < ind lbs < 5, total > 5      normal
                                ind > 5 lbs                     normal
                                ind < 1 lb, total > 1 lbs       hi/ak
                                ind < 1 lb, total < 1 lb        hi/ak
                                1 < ind lbs < 5, total < 5      hi/ak
                                1 < ind lbs < 5, total > 5      hi/ak
                                ind > 5 lbs                     hi/ak
                                ind < 1 lb, total > 1 lbs       normal          true
                                ind < 1 lb, total < 1 lb        normal          true
                                1 < ind lbs < 5, total < 5      normal          true
                                1 < ind lbs < 5, total > 5      normal          true
                                ind > 5 lbs                     normal          true
                                ind < 1 lb, total > 1 lbs       hi/ak           true
                                ind < 1 lb, total < 1 lb        hi/ak           true
                                1 < ind lbs < 5, total < 5      hi/ak           true
                                1 < ind lbs < 5, total > 5      hi/ak           true
                                ind > 5 lbs                     hi/ak           true

items               qty         weight                          dest            irregular
-----------------------------------------------------------------------------------------
multiple            mix         ind < 1 lb, total > 1 lbs       normal
                                ind < 1 lb, total < 1 lb        normal
                                1 < ind lbs < 5, total < 5      normal
                                1 < ind lbs < 5, total > 5      normal
                                ind > 5 lbs                     normal
                                ind < 1 lb, total > 1 lbs       hi/ak
                                ind < 1 lb, total < 1 lb        hi/ak
                                1 < ind lbs < 5, total < 5      hi/ak
                                1 < ind lbs < 5, total > 5      hi/ak
                                ind > 5 lbs                     hi/ak
                                ind < 1 lb, total > 1 lbs       normal          true
                                ind < 1 lb, total < 1 lb        normal          true
                                1 < ind lbs < 5, total < 5      normal          true
                                1 < ind lbs < 5, total > 5      normal          true
                                ind > 5 lbs                     normal          true
                                ind < 1 lb, total > 1 lbs       hi/ak           true
                                ind < 1 lb, total < 1 lb        hi/ak           true
                                1 < ind lbs < 5, total < 5      hi/ak           true
                                1 < ind lbs < 5, total > 5      hi/ak           true
                                ind > 5 lbs                     hi/ak           true

"""

from itertools import combinations
import unittest

from matrices import get_cheapest_option, get_irregular_price
from models import Item, Box, Order


class TestOptimizer(unittest.TestCase):

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

    def test_00(self):
        input_data = {"zip": "", "items": [{"sku": "", "weight": 0, "qty": 0}]}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_01(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_02(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_03(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_04(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_05(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_06(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_07(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_08(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_09(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_10(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_11(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_12(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_13(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_14(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_15(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_16(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_17(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_18(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_19(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_20(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_21(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_22(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_23(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_24(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_25(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_26(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_27(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_28(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_29(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_30(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_31(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_32(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_33(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_34(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_35(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_36(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_37(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_38(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_39(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_40(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_41(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_42(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_43(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_44(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_45(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_46(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_47(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_48(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_49(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_50(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_51(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_52(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_53(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_54(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_55(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_56(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_57(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_58(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_59(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_60(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_61(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_62(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_63(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_64(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_65(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_66(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_67(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_68(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_69(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_70(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_71(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_72(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_73(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_74(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_75(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_76(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_77(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_78(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_79(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_80(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_81(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_82(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_83(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_84(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_85(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_86(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_87(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_88(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_89(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_90(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_91(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_92(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_93(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)

    def test_94(self):
        input_data = {}
        expected = {"boxes": [{"items": [{"sku": "", "qty": 0}], "cost": 0, "method": ""}], "cost": 0}
        response = self.optimize_shipping(input_data)
        self.assertEqual(expected, response)
