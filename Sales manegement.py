items = {
    100: "Buns",
    101: "Bread",
    102: "Coffee",
    103: "Ice Coffee",
    104: "Juice",
    105:"Chocolate",
    106:"Milk",
    107:"Tea",
    108:"Pizza"
}
price = {
    100: 30,
    101: 100,
    102: 50,
    103: 70,
    104: 120,
    105: 50,
    106: 40,
    107: 20,
    108: 500
}
#------------------------------------------------------------------------------------
cart =[]
#------------------------------------------------------------------------------------
discount_gen(sub_total):
    if sub_total > 10000:#if total is greater then 10000 discount will be 30%
        pay = int(sub_total - (sub_total*30/100))
    elif sub_total > 5000:#if total is greater then 5000 discount will be 20%
        pay = int(sub_total - (sub_total*20/100))
    elif sub_total > 3000:#if total is greater then 3000 discount will be 10%
        pay = int(sub_total - (sub_total*10/100))
    return pay
#------------------------------------------------------------------------------------
main():
    while True:
        item_code=input("Item Code: ")
        quantity =input("Quantity: ")
        if item_code.isdigit() and quantity.isdigit(): #int Validation
            cart.append([int(item_code),int(quantity)]) #appending itemCode and Quantity to the list
        else:
            break
        
        