#!/usr/bin/env python3
"""Independently check synthetic lab business rules from CSVs (no SQL engine)."""
from collections import Counter
from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parents[1]
def load(name):
    with (ROOT / 'data' / name).open(encoding='utf-8',newline='') as f:
        return list(csv.DictReader(f))

customers, orders, items = load('customers.csv'), load('orders.csv'), load('order_items.csv')
expected = json.loads((ROOT / 'data/expected_results.json').read_text(encoding='utf-8'))
assert len(customers) == 12 and len(orders) == 34 and len(items) == 44, 'Unexpected dataset sizes'
assert len({c['customer_id'] for c in customers}) == 12
assert len({o['order_id'] for o in orders}) == 34
assert len({i['order_item_id'] for i in items}) == 44
customers_by_id = {c['customer_id']: c for c in customers}
orders_by_id = {o['order_id']: o for o in orders}
assert all(o['customer_id'] in customers_by_id for o in orders)
assert all(i['order_id'] in orders_by_id for i in items)
assert all(int(i['quantity']) > 0 and int(i['unit_price_inr']) >= 0 for i in items)

status_counts = Counter(o['status'] for o in orders)
assert status_counts == {'completed':29,'cancelled':2,'pending':3}
assert [[k,status_counts[k]] for k in sorted(status_counts)] == expected['b02_orders_by_status.sql']

ordered_customer_ids = {o['customer_id'] for o in orders}
never_ordered = [[c['customer_id'],c['customer_name']] for c in customers if c['customer_id'] not in ordered_customer_ids]
assert never_ordered == expected['i02_customers_without_orders.sql']

regions,products = Counter(),Counter()
for line in items:
    order = orders_by_id[line['order_id']]
    if order['status'] != 'completed':
        continue
    amount = int(line['quantity']) * int(line['unit_price_inr'])
    regions[customers_by_id[order['customer_id']]['region']] += amount
    products[line['product']] += amount
assert sum(regions.values()) == 65580
assert [[k,v] for k,v in sorted(regions.items(),key=lambda p:(-p[1],p[0]))] == expected['i01_completed_revenue_by_region.sql']
assert [[k,v] for k,v in sorted(products.items(),key=lambda p:(-p[1],p[0]))[:3]] == expected['i03_top_three_products.sql']

complete_ids = {o['order_id'] for o in orders if o['status']=='completed'}
ids_with_items = {i['order_id'] for i in items}
exceptions = sorted(complete_ids - ids_with_items)
assert exceptions == ['O1029']
assert expected['a04_completed_orders_missing_items.sql'] == [['O1029','C004','completed']]
print('PASS independent CSV audit: 12 customers, 34 orders, 44 line items, ₹65,580 completed revenue, 1 missing-items exception.')
