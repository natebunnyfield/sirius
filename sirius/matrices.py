#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import ceil
import os

import yaml


CONFIG_DIR = os.path.abspath(os.path.join(__file__, '..', 'shipping_configs'))

# ups ground
UPS_GROUND_ZIP_TO_ZONE = yaml.load(open(os.path.join(CONFIG_DIR, 'ups_ground_zip_to_zone.yaml'), 'r'))
UPS_GROUND_ZONE_WEIGHT_PRICE = yaml.load(open(os.path.join(CONFIG_DIR, 'ups_ground_zone_weight_price.yaml'), 'r'))
UPS_GROUND_ZONE_44 = [int(line.rstrip()) for line in open(os.path.join(CONFIG_DIR, 'zone44.txt'))]
UPS_GROUND_ZONE_46 = [int(line.rstrip()) for line in open(os.path.join(CONFIG_DIR, 'zone46.txt'))]

# ups mail innovations
UPS_MI_RATES_OZ = yaml.load(open(os.path.join(CONFIG_DIR, 'ups_mi_rates_oz.yaml')))
UPS_MI_RATES_LBS = yaml.load(open(os.path.join(CONFIG_DIR, 'ups_mi_rates_lbs.yaml')))


def get_cheapest_option(zipcode, weight):
    """
    gets the cheapest price for a box
    """
    # weights come in ounces - if it's less than a pound - send it via mail innovations
    if weight <= 16:
        for tier in sorted(UPS_MI_RATES_OZ):
            if ceil(weight) <= tier:
                return 'UPS Mail Innovations', UPS_MI_RATES_OZ[tier]

    # over a pound? that gets tricky. convert to pounds
    weight = ceil(float(weight) / 16)

    # check if the zipcode is in the 44/46 lists (hawaii or alaska)
    if zipcode in UPS_GROUND_ZONE_44:
        zone = '044'
    elif zipcode in UPS_GROUND_ZONE_46:
        zone = '046'
    else:  # it's in the lower 48
        zipcode = str(zipcode)[:3]  # ups only uses the first three digits
        zone = UPS_GROUND_ZIP_TO_ZONE[zipcode]

    # check weights
    options = []    # ups mail innovations
    for tier in sorted(UPS_MI_RATES_LBS):
        if weight <= tier:
            options.append(('UPS Mail Innovations', UPS_MI_RATES_LBS[tier]))
            break
    # ups ground
    for tier in sorted(UPS_GROUND_ZONE_WEIGHT_PRICE[zone]):
        if weight <= tier:
            options.append(('UPS Ground', UPS_GROUND_ZONE_WEIGHT_PRICE[zone][tier]))
            break

    # get cheapest option
    return min(options, key=lambda x: x[1])


def get_irregular_price(zipcode, weight):
    """
    does much of the same as `get_cheapest_option`, but skips all MI
    """
    weight = ceil(float(weight) / 16)
    if zipcode in UPS_GROUND_ZONE_44:
        zone = '044'
    elif zipcode in UPS_GROUND_ZONE_46:
        zone = '046'
    else:  # it's in the lower 48
        zipcode = str(zipcode)[:3]  # ups only uses the first three digits
        zone = UPS_GROUND_ZIP_TO_ZONE[zipcode]
    for tier in sorted(UPS_GROUND_ZONE_WEIGHT_PRICE[zone]):
        if weight <= tier:
            return UPS_GROUND_ZONE_WEIGHT_PRICE[zone][tier]
