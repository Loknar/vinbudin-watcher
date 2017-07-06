#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

import scraper
import utils

PRODUCTS = [  # http://www.vinbudin.is/heim/vorur/vorur.aspx/?text=Grevens
    '22006',
    '22837',
    '23282',
    '22004'
]

if __name__ == '__main__':
    print 'Working ...'
    directory = 'products/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    for product_id in PRODUCTS:
        print 'Fetching data for product %s ...' % (product_id, )
        product_data = scraper.get_vinbudin_product_data(product_id)
        print 'Writing data to file ...'
        utils.save_to_json(
            '%s%s.json' % (directory, product_id),
            product_data,
            pretty=True
        )
        print 'Done.'
    print 'All done.'
