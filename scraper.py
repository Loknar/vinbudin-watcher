#!/usr/bin/python
# -*- coding: utf-8 -*-
# import datetime
import json

import lxml.etree
import requests

import utils

def get_vinbudin_product_data(product_id):
    '''
    Desc:   Fetches information on product (by id) from vinbudin.is
    Before: @product_id is an id of an existing vinbudin product
    After:  returns fancy object filled with data
    '''
    product_data = {
        'name': '',
        'img_url': '',
        'price': '',  # in ISK
        'stock': []  # ,
        # 'timestamp': ''
    }
    url = (
        'http://www.vinbudin.is'
        '/heim/vorur/stoek-vara.aspx/?productid={product_id}/'
    ).format(product_id=product_id)
    res = requests.get(url)
    res.raise_for_status()
    html = lxml.etree.fromstring(
        res.content, lxml.etree.HTMLParser(encoding='utf-8')
    )
    product_name = html.find(
        './/*[@id="ctl01_ctl01_Label_ProductName"]'
    ).text
    product_image = html.find('.//*[@class="MagicZoomPlus"]').get('href')
    product_price = html.find(
        './/*[@id="ctl01_ctl01_Label_ProductPrice"]'
    ).text
    # product_info_timestamp_text = html.find(
    #     './/*[@id="ctl01_ctl01_span_stockStatusLastUpdated"]'
    # ).text.strip()
    # product_info_timestamp = datetime.datetime.strptime(
    #     '%s %s' % (
    #         product_info_timestamp_text.split()[-3],
    #         product_info_timestamp_text.split()[-1]
    #     ),
    #     '%d.%m.%Y %H:%M.'
    # ).strftime('%Y-%m-%d %H:%M')
    product_image = 'https://www.vinbudin.is%s' % (product_image, )
    product_data['name'] = product_name
    product_data['img_url'] = product_image
    product_data['price_isk'] = product_price
    # product_data['timestamp'] = product_info_timestamp
    product_stock_table = html.find('.//*[@id="div-stock-status"]')
    for table in product_stock_table.findall('.//table'):
        for row in table.findall('.//tr'):
            for rowtype in ('oddRow', 'evenRow'):  # html stupidity
                if row.find('.//td[@class="%s store"]' % (rowtype, )) is None:
                    # skip header like rows
                    continue
                store_name = row.find(
                    './/td[@class="%s store"]' % (rowtype, )
                ).text
                store_stock = row.find(
                    './/td[@class="%s stockstatus"]' % (rowtype, )
                ).text
                product_data['stock'].append({
                    'name': store_name,
                    'stock': store_stock
                })
    return product_data

if __name__ == '__main__':
    # import pdb
    product_data = get_vinbudin_product_data(22837)
    print json.dumps(
        utils.bytify(product_data),
        indent=4,
        ensure_ascii=False,
        sort_keys=True
    )
    # pdb.set_trace()
