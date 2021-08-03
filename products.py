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