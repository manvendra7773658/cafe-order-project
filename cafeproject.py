menu={
    'pizza':100,
    'pasta':80,
    'burger':40,
    'salad':60,
    'cold coffee':30,
}
print("welcome to our pip cafe")
print("pizza:100\npasta:80\nburger:40\nsalad:60\ncold coffee:30")
order_total = 0
item1 = input("enter your order please= ")
if item1 in menu:
    order_total+= menu[item1]
    print(f"your item {item1} is added to your order")
else:
    print(f"ordered item {item1} is not available yet")

anotheritem = input("do you want to add another item (yes/no)")
if anotheritem == "yes":
    item2 = input("enter your  second order please= ")
    if item2 in menu:
     order_total+= menu[item2]
     print(f"your item {item2} is added to your order")
    else:
       print(f"ordered item {item2} is not available yet")

print(f"the total amount of item  to pay is{order_total}")