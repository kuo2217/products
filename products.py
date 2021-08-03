#二維清單

products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入價格: ')
    p = []
    p.append(name)
    p.append(price)
    #可直接寫成 p = [name, price] or products.append([name, price])
    products.append(p)
print(products)


#印出小清單
for p in products:
    print(p)

#印出小清單的第一項(物品)
for p in products:
    print(p[0])
