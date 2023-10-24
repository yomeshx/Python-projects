import time
#----------------------------------------------------------------------------------------------------
print(time.ctime(0))    #converts a time expressed in seconds since epoch to a readable string
#                       epoch = when your computer thinks time began (reference point)
#----------------------------------------------------------------------------------------------------

print(time.time())                  #return current seconds since epoch
#----------------------------------------------------------------------------------------------------

print(time.ctime(time.time()))      #return time since epoch in a readable way using time.ctime

#------------|Local time/UTC time(GMT)|--------------------------------------------------------------------

#A time object Local or GMT (UTC) made of 9 key words arguments
#ex: year,month,date ,current hour,current minute,current sec and more...

time_object = time.localtime()
print(f"Local Time - {time_object}")

#UTC time - Coordinated Universal Time (UTC is the primary time standard by which world regulates clocks and time)
time_object = time.gmtime()
print(f"UTC Time - {time_object}")

# UTC is precisely the same imaginary line defined by GMT at the Prime Meridian,
#  located in the Royal Observatory in Greenwich. 
# Nevertheless, many people still use GMT as the time standard for all countries worldwide 
# - for example, GMT+12:00 for New Zealand

#--------------| strftime (directives , time_object)|-------------

#'strftime' use to make local time or UTC time to a more readable format that you can understand .
#strftime takes two arguments one of which called directives("special symbolic characters to format in different ways")
# and the second argument is thing you want to format itself 
local_time = time.strftime("%B %d %Y %H:%M:%S",time_object)
print(local_time)
# %B - Month name
# %d - Day of the month as a decimal number 01 - 31
# %Y - Year with century as a decimal number ex: 2022
# %H - Hour (24 hour clock) as a decimal number
# %M - Minute as a decimal number 00 - 59
# %S - Second as a decimal number 00 - 61

#Checkout under strftime on ' docs.python.org/3/library/time.html ' to see all the symbols and their meanings

#----| time.strptime(time_string,directives) |---------------------------------------------------------------------------------------

#strptime will convert string representation of date or time to a time object 
# -by assign them to key word arguments as given order
time_string = "20 April, 2020"
time_object = time.strptime(time_string, "%d %B, %Y")
print(time_object)

#----|time.acstime(time_tuple)|----------------------------------------------------------------------------------------------

#acstime will convert tuple representation of time in to a date or time object to a readable string
#tuple must containing 9 elements because struct_time objects contains 9 elements
time_tuple = (2022, 7 , 14 , 16 , 53 , 30 , 0, 0 ,0)
time_string = time.asctime(time_tuple)
print(time_string)



#-----|time.mktime(time_tuple)|----------------------------------------------------------------------------------------------

#mktime will take argument as time object
#mktime() method of Time module is used to convert a time. struct_time object or a tuple containing 9 elements corresponding to time.
#converts time object to time in seconds passed since epoch in local time

time_tuple = (2022, 7 , 14 , 16 , 53 , 30 , 0, 0 ,0)
time_string = time.mktime(time_tuple)
print(time_string)