# initialize bottle variable
bottle = 0

# describe functions of program
print("This is a program that prints out the lyrics to 100 Bottles of Beer using a variable number of bottles input by the user.")

# get bottle input and check for number
y = true
while y == true:
    bottle = input("Please input number of bottles: ")
    try:
        bottle = int(bottle);
        y = false
    except:
        print:("Please input a whole numerical value.")
        
# run lyrical loop
while bottle >= 1
    if bottle == 1
        print(bottle, " bottle of beer on the wall, ", bottle, " bottle of beer...")
    else
        print(bottle, " bottles of beer on the wall, ", bottle, " bottles of beer...")
    
    print("Take one down and pass it around, ", bottle, "bottle(s) of beer on the wall.")
    
# report out of bottles
print("No more bottles of beer. It may be time to get some more.")