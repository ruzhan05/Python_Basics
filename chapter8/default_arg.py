def goodDay(name, ending = "Thank you"):
    print("Good Day, " + name)
    print(ending)
    return "done"

goodDay("Harry")  #Thank you gets printed even though not given in the function call
# If any other argument is passed in the function call, then that one is executed. The default one is executed only when there is no value given in the function call.