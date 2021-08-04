
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

#寫檔
with open('products.csv', 'w', encoding='utf-8') as f:        #csv可用ecxel打開 用逗點可以隔開   encoding修正編碼中文亂碼問題 
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')

