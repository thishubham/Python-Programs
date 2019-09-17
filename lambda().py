items = [
    ('Product1', 10),   # product name and price tuple
    ('Product2', 5),    # product name and price tuple
    ('Product3', 80),   # product name and price tuple
]


items.sort(key=lambda items:items[1])  # parameters:expression
print(items)