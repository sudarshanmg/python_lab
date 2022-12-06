# Write your code here :-)
def ph_no(string):
    if ( string[3] == "-" and string[7] == "-" and len(string) == 12):
        return True
    return False
print(ph_no("122-122-1222"))
