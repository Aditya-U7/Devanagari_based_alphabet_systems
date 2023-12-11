"""
Author: Aditya Upadhye

"""

def print_vowels():

    for i in range(5, 21):                    
        
        if i in [12, 13, 14, 17, 18]:
            continue
        
        print(chr(0x0900 + i), " ", end="")
     
    print(chr(0x0902), chr(0x0905), sep="", end=" ")
    print(chr(0x0905), chr(0x0903), sep="")    
        

def print_consonants():
    
    for i in range(5, 42):                   
        
        if i in [25, 33, 35, 36]:
            continue

        x = chr(0x0910 + i)

        print(x," ", end="")

        if ((i+1) % 5 == 0 and i < 29) or (i == 30) or (i == 37):
            
            print()        


def print_hindi_varnamala():
   
    print_vowels()
    
    print()
    
    print_consonants()
    
    print()

#####################

print_hindi_varnamala()
  
