#zip make pairs of data from two or more different or same king of iterables


user_name = ["Jake_79","Mike45","Mira_online","Alex_dope"]
passwords = ("Akbne21Ha","LcE$$345Kn","f^eVaeQ","Jfn^&9kM:L")
login_date = ["1/1/2022","1/2/2022","3/2/2022","4/2/2022"]


users = zip(user_name,passwords,login_date)            #zip to a tuple
#users = list(zip(user_name,passwords))     #zip to a list
#users = dict(zip(user_name,passwords))     #zip to a dictionary
print(type(users))
for user_name,pw,login_date in users:   #Or you can give single iteration like 'i' to print whole thing
    print("----------------------")
    print(f"User: {user_name}\nPassword: {pw}\nLogin: {login_date}")