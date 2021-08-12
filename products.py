#讀取檔案
products = []
with open('products.csv', 'r') as f:
    for line in f:
        if '商品,價格' in line:
            continue        #使用continue不會跳出迴圈 但會略過7 8行(不執行) 重新做迴圈
        name, price = line.strip().split(',')     #strip()分割/n(換行) 因為用逗點分割 所以可以儲存到兩個變數中
        products.append([name, price])
print(products)





#二維清單


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

