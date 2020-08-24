#functions for model inference

#Checking for favorite artists in list
def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    if not lst3:
        print("There are no common artists")
        return False
    else:
        return True

lst1 = ['Ram', 'Nadal', 'Djokovic']
lst2 = ['Ram']
print(intersection(lst1,lst2))