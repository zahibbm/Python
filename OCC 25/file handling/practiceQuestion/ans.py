#2nd question
def nextID():
    sales = open('sales.txt','r')
    lines = sales.readlines()
    sales.close()
    return len(lines)
#4th question
def calculatePrice(itemCode,type,quantity):
    if type=='WH':
        priceList=open('wholesalePrice.txt','r')
    else:
        priceList=open('retailPrice.txt','r')
    for line in priceList:
        item,price=line.split('\t')
        if item==itemCode:break
    total=int(price)*quantity
    priceList.close()
    return total
#last question
totalPrice=0
type = input('Type: ')
while True:
    itemCode = input('Item Code: ')
    if not(itemCode):break
    quantity = int(input('Quantity: '))
    price = calculatePrice(itemCode,type,quantity)
    totalPrice += price
    # print(price)
# itemCode = input('Item Code: ')
# while itemCode:
#     quantity = int(input('Quantity: '))
#     price = calculatePrice(itemCode,type,quantity)
#     totalPrice += price
#     # print(price)
#     itemCode = input('Item Code: ')
# print('Total Price :',totalPrice)
sale = open('sales.txt','a')
print(nextID(),type,totalPrice,file=sale,sep='\t')
sale.close()