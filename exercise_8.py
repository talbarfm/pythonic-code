def process_data(data):
    total = 0
    num_items = len(data)
    for item in data:
        qty = item['qty']
        price = item['price']
        amt = qty * price
        total += amt
    avg = total / num_items
    min_item = min(data, key=lambda x: x['price'])
    max_item = max(data, key=lambda x: x['price'])
    return {
        'total': total,
        'average': avg,
        'min_item': min_item,
        'max_item': max_item
    }
