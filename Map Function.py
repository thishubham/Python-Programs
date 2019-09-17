items =[
    ('Product1', 10),
    ('Product2', 90),
    ('Product3', 40),
]


price = []
for item in items:
    price.append(item[1])
    #  price.sort()

map(lambda item: item[1], items)

print(price)