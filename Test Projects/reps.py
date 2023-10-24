#-----------------------------------------------
def rep_count (starting_reps,end_Reps):
    x = starting_reps
    total_reps = 0
    no_of_sets = 0
    while not x == end_Reps:
        no_of_sets += 1
        total_reps += x
        x -= 1
    print("---------------")

    print(f"Total Reps: {total_reps}")
    print(f"Total Sets: {no_of_sets}")
    
    print("---------------")

#-----------------------------------------------
def re_try():
    re_calculate = input("To Try Again: Y or N: ").upper()
    if re_calculate == "Y":
        return True
    else:
        return False
#-----------------------------------------------
print()
starting_reps = int(input("Enter Starting Reps: "))
end_Reps = int(input("Enter Ending Reps: "))

rep_count(starting_reps,end_Reps)
while re_try() is True:
    starting_reps = int(input("Enter Starting Reps: "))
    end_Reps = int(input("Enter Ending Reps: "))
    rep_count(starting_reps,end_Reps)