numbers = [3, 848, 23, 56, 65]
numbers.sort(reverse=True)  # it sorts the original list in reveres order
print(sorted(numbers))  # it do not change original list, but creates a new one
print(numbers)

items = [
    ('Product1', 10),   # product name and price tuple
    ('Product2', 5),    # product name and price tuple
    ('Product3', 80),   # product name and price tuple
]


def sort_item(item):
    return item[1]      # sorts the list by index 2 (i.e. by price)


items.sort(key=sort_item)
print(items)

