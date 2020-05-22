import re
print("Our Magical Calculetor")
print("Type 'quit' to exit\n")

previous = 0 # set defulat values : 0
run = True # set value for while loop

def preformath(): # define function performath
    global run # use global on run for if type quit run values change into false
    equation = input("enter eqution:")
    if equation == "quit": # if type quit run values change into fals
        run = False
    else:
        equation = re.sub('[a-zA-Z]','',equation) # text does not matter using re function
        previous = eval(equation)
        print("result is", previous)

while run: # use while loop for preformat repeat again and again hoewver run value equal True
    preformath()
