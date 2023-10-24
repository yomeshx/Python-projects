n_list = ["kaputu","kaak","kaak","kaak","basil","basil","basil","basil","kaputu","kaak","kaak","kaak","basil","basil","basil","basil"]

n_dic = dict()

for name in n_list :
    if not name in n_dic:
        n_dic[name] = 1
    else:
        n_dic[name] += 1

print(n_dic)