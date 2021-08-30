import os #載入作業系統

#讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f:    #讀取檔案
        for line in f:
            if '商品,價格' in line:
                continue    #使用continue不會跳出迴圈 但會略過下面兩行(不執行) 重新做迴圈
            name, price = line.strip().split(',')     #strip()分割/n(換行) 因為用逗點分割 所以可以儲存到兩個變數中
            products.append([name, price])
    print(products)
    return products

#二維清單 讓使用者輸入
def user_input(products):
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
    return products

#印出清單
def print_list(products):
    for p in products:
        print(p[0], '價格是', p[1])

#寫檔
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:        #csv可用ecxel打開 用逗點可以隔開   encoding修正編碼中文亂碼問題 
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')

def main():
    filename = 'products.csv'   
    if os.path.isfile(filename): #先用os模組檢查檔案是否存在
        print('找到檔案')
        products = read_file(filename)
    else:
        print('找不到檔案')

    products = user_input(products)
    print_list(products)
    write_file('products.csv', products)

main()