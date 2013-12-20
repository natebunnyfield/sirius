#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Item:

    def __init__(self, sku, weight, is_irregular=False, height=0, width=0, depth=0):
        self.sku = sku
        self.weight = weight
        self.is_irregular = is_irregular
        self.height = height
        self.width = width
        self.depth = depth

    def __str__(self):
        return self.sku

    def __repr__(self):
        return "Item({})".format(self.sku)


class Box:

    def __init__(self):
        self.items = []
        self.shipping_method = None
        self.shipping_cost = 0.0

    def __str__(self):
        return "Box({})".format(', '.join(str(item) for item in self.items))

    def __repr__(self):
        return self.__str__()

    @property
    def weight(self):
        return sum([item.weight for item in self.items])

    @property
    def volume(self):
        return sum([item.height * item.width * item.depth for item in self.items])

    def to_json(self):
        output = {
            'cost': self.shipping_cost,
            'method': self.shipping_method,
        }
        items = {}
        for item in self.items:
            items.setdefault(item.sku, 0)
            items[item.sku] += 1
        output['items'] = [{'sku': sku, 'qty': qty} for sku, qty in items.iteritems()]
        return output


class Order:

    def __init__(self):
        self.boxes = []

    def __str__(self):
        return "Order({})".format(', '.join([str(box) for box in self.boxes]))

    def __repr__(self):
        return self.__str__()

    @property
    def shipping_cost(self):
        return sum([box.shipping_cost for box in self.boxes])

    def to_json(self):
        return {
            'boxes': [box.to_json() for box in self.boxes],
            'cost': self.shipping_cost
        }
