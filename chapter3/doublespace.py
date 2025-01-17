str = input("Enter your text her: ")

hasDS = str.find("  ")
if(hasDS != -1):
    print("Double space has been detected in your message.\nWe are correcting it for you.....")
    newstr = str.replace("  ", " ")
    print(newstr)
else:
    print("No double spacing detected.")
    