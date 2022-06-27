sequence = [0]          #Initialise empty list

def fibonacci (x):      # First 2 numbers, set count to 0
    n1 = 0
    n2 = 1
    count = 0

    if x <=0:           # Validate input for 1 and below:
        return ("Please enter a positive integer.")
    elif x == 1:
        return (sequence)

    else:               #Generate fibonacci sequence
        while count < x-1:
            sequence.append(n2)
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            count += 1
        else:
            return (sequence)

x= int(input("How many items in the sequence would you like to see? "))
fibonacci (x)
print (sequence)