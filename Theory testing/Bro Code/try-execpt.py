while True:
    try:
        value = int(input("Enter Numbers to divide : "))
        divide_by = int(input("Enter Number to divide by : "))
        division = value/divide_by
        cv = f"{value} divide by {divide_by} is {division} "

    except ZeroDivisionError:
        print("Can't divide by zero !!!")
    except ValueError as e:
        print(e,end = "")
        print(" -Different types of values are not acceptable !!!")
    except Exception as e: #You can just leave 'except:' without any specification if you want
        print(e,end = "")
        print(" -Something went wrong !!! ")
    else: #If theres no exception matches given above,will execute this line 
        print(cv)
    finally: #Will execute at the end no matter what
        print("Successful")