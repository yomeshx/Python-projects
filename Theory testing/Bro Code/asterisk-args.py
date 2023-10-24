# when you make a function you can give *argument as a parameter ,
# When you give *args as parameter,you can give infinite amount of positional arguments and it will pack all of them to a tuple


def add(*inputs): #You can give any name to the parameter after the *    Ex : *numbers ,*values
    _sum = 0
    for i in inputs:
        _sum += i
    return _sum

print(add(10,20,30,40,50))