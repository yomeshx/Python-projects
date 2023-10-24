import os
os.chdir("D:\P\Programing\Python\My Learning Projects\Challenge_ME_SELF_")

user_in = input("Input the 'Name of the Text file'\n------->|: ")
dic_word_co= dict()
lst_of_wds = list()
f_handle = open(user_in)
#p = f_handle.read()
# print(p)                        #TEST 1

for line in f_handle:
    line = line.rstrip()
    line_l = line.split() #now line is a list

    for word in line_l:
        # if word in dic_word_co.keys():
        #     dic_word_co[word] = dic_word_co[word]+1       #Standard method @Q 1.(I)
        # else:
        #     dic_word_co[word] = 1
       dic_word_co[word] = dic_word_co.get(word,0)+1        #Get method @Q 1.(II)
# print(dic_word_co)              #TETS 2
for wd in dic_word_co.keys():
    if wd not in lst_of_wds:
        lst_of_wds.append(wd)                               #@Q 2
    else:
        continue
#print(lst_of_wds)               #TEST 3
temp_list = list()
for k,v in dic_word_co.items():
    temp_list.append((v,k))

# print("temp_list is : ",temp_list)     #TEST 4    making sure that temp list is been created.
sort_temp_list_min2mx = sorted(temp_list)
sort_temp_list_mx2min = sorted(temp_list,reverse = True)
print(f"\nMin2Max : {sort_temp_list_min2mx}\n")   #TEST 5     list of tuples that sorted by min value 2 max 
print(f"\nMax2Min : {sort_temp_list_mx2min}\n")   #TEST 6     list of tuples that sorted by max value 2 min 

conv_temp_lst = list()
for v,k in sort_temp_list_mx2min:
    conv_temp_lst.append((k,v))
# print(conv_temp_lst)                          #TEST 7 Swapped back to key-value order list of tuples

mx2mn_sorted_dic = dict(conv_temp_lst)                      #@Q 3
print(mx2mn_sorted_dic)

print(f"\nBEFORE : {lst_of_wds} ") #the normal order
sort_lst_of_wds = sorted(lst_of_wds) #sorting by the value of the string        #@Q 4
print(f"\nAFTER : {sort_lst_of_wds}")

most_com_10_wds = conv_temp_lst[:10]
most_com_wd = conv_temp_lst[0:1]
most_com_wd_len =len(most_com_wd)



# def mst_com(para):
#     n_list = conv_temp_lst[0:para]           #Don't get how to use a function to show most common words yet
#     for mst_com_w in n_list:
#         print(most_com_wd)
# x = mst_com(10)
# mst_com(10)


# print(f"Most common 10 words are :\n{most_com_10_wds}")
# print(f"Most common word is :\n{most_com_wd} it's length is {most_com_wd_len} characters.")
# # except OSError:
# #     print("\nFile Not Found !!!\n")