num_list = list()
while True:
    in_ =input("Enter Value : ")
    if in_ == "done":
        break
    in_=float(in_)
    num_list.append(in_)
avg = sum(num_list) / len(num_list)
print("Average is : ",avg)
