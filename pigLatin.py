import datetime

# A list containing vowels (I would've used a tuple if it is up to me, but the question asked for a list)
vowels = ['a','A', 'e','E', 'i','I', 'o','O', 'u','U','y','Y']

# The function that takes a string (an english word) and converts it into pigLatin then returns it
def pigLatin(inputStr):
    foundFlag = False
    
    if inputStr == "" or not inputStr.isalpha(): # Input validation
        return "Invalid input .. Try again"
    elif inputStr[0] in vowels: # Checks if the first character is a vowl
        return inputStr + "way"
    else:
        for char in inputStr: # Loops to find the position of the first vowl
            if char in vowels:
                vowlPos = inputStr.index(char) # Stores the position of the vowl
                foundFlag = True
                break
        # Where the magic happens .. 
        # using string manupulation to convert and return the pigLatin word  
        if foundFlag:  # If a vowel was found
            return "".join(inputStr[vowlPos:] + inputStr[:vowlPos] + "ay") 
        else:
            return inputStr + "ay"
def main():
    
    inpString = input("Please enter a word to convert to pigLatin: ")
    
    result = pigLatin(inpString)
    
    timestamp = datetime.datetime.now()  # Get the current date and time

    dt_string = timestamp.strftime("%d/%m/%Y %H:%M") # Formats the current date and time

    if result == "Invalid input .. Try again":
        print("Invalid input .. Try again")
    else:
        print(f"{inpString} in PigLatin is: {result}")  # Outputs the converted PigLatin word
        try: # Opens the history file (if it exists) to retrive the last converted word
            f = open("history.txt","r")
            preSession = f.readline()
            print(f"Last generated word was: {preSession}")
            f.write(f"{result} @ {dt_string}")
            f.close()
        except: # Writes the new converted word to file
            f = open("history.txt","w")
            f.write(f"{result} @ {dt_string}")
            f.close()
    
    
if __name__ == "__main__":
    main()