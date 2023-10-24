#You can give infinite amount of 'keyword arguments' when you call the function , **parameter_name 
#   ex:  def add(**kwargs):
            #########
            #######
        #add(name ="nah",game="PUBG",call="hello")

#Parameter that will pack all the arguments into a 'dictionary'

def hello (**names):
    print("Hello",end = " ")
    for k,v in names.items():
        print(v,end=" ")

hello(fname = "Yasintha",lname ="Yomesh")