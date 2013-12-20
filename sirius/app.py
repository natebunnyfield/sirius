#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import combinations
import json
from pprint import pprint

from flask import Flask, request

from matrices import get_cheapest_option
from models import Item, Box, Order


app = Flask(__name__)


@app.route('/optimize_shipping/', methods=['POST'])
def optimize_shipping():
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

    # get posted json
    data = json.loads(request.data)

    # pull zipcode
    zipcode = data['zip']

    # create items
    items = []
    for item in data['items']:
        qty = item['qty']
        del item['qty']
        for __ in xrange(qty):
            items.append(Item(**item))

    # create orders/bundles from items combinations
    orders = []
    for combination in make_combinations(items):  # full tuple of tuples of items. ex: ( (one,two), (three,) )
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
        # add order to list of all possible combinations
        orders.append(order)

    # get the cheapest order combination
    cheapest = min(orders, key=lambda o: o.shipping_cost)

    # respond
    return str(cheapest.to_json())


if __name__ == '__main__':
    app.run(debug=True)
