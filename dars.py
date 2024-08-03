# 1-topshiriq
with open('product_material.txt', 'r') as file:
    data = [line.strip().split(',') for line in file]

header = data.pop(0)

eligible_products = [
    (id_, material)
    for id_, product, material, price, is_available in data
    if 500 <= float(price) <= 1000 and bool(int(is_available))
]

print("1-topshiriq natijasi:")
for id_, material in eligible_products:
    print(f"ID: {id_}, Material: {material}")
print()

user_material = input("Mahsulot materialni kiriting: ")

available_products = [
    (price,)
    for id_, product, material, price, is_available in data
    if material == user_material and bool(int(is_available))
]

available_products.sort()

print("2-topshiriq natijasi:")
for price, in available_products:
    print(f"Narxi: ${price}")
print()

unavailable_cheap_products = [
    material
    for id_, product, material, price, is_available in data
    if float(price) < 1000 and not bool(int(is_available))
]

print("3-topshiriq natijasi:")
for material in set(unavailable_cheap_products):
    print(f"Material: {material}")