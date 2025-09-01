# Getting text from 'raw_text.txt'
with open("raw_text.txt") as f:
    text = f.read()

# Creating lists of all letters
a_to_m = []
n_to_z = []
A_to_M = []
N_to_Z = []

# Encrypted text variable
encrypted_text = ""
decrypted_text = ""

# Adding all letters to their corresponding list
for char in range(ord("a"), ord("m") + 1):     
    a_to_m.append(chr(char))                   
for char in range(ord("n"), ord("z") + 1):     
    n_to_z.append(chr(char))                   
for char in range(ord("A"), ord("M") + 1):     
    A_to_M.append(chr(char))                   
for char in range(ord("N"), ord("Z") + 1):     
    N_to_Z.append(chr(char))                   

# Encryption Function
def encryption(shift1, shift2):
    global encrypted_text
    # Going through each character within
    for c in text:
        temp_num = ord(c)

        if c in a_to_m:
            temp_num = temp_num + (shift1 * shift2)
            while temp_num > ord("m"):
                temp_num -= 13
        elif c in n_to_z:
            temp_num = temp_num - (shift1 + shift2)
            while temp_num < ord("n"):
                temp_num += 13
        elif c in A_to_M:
            temp_num = temp_num - shift1
            while temp_num < ord("A"):
                temp_num += 13
        elif c in N_to_Z:
            temp_num = temp_num + shift2 ** 2
            while temp_num > ord("Z"):
                temp_num -= 13
        encrypted_text += chr(temp_num)

# Decryption Function
def decryption(shift1, shift2):
    global decrypted_text
    for c in text_back:
        temp_num = ord(c)

        if c in a_to_m:
            temp_num = temp_num - (shift1 * shift2)
            while temp_num < ord("a"):
                temp_num += 13
        elif c in n_to_z:
            temp_num = temp_num + (shift1 + shift2)
            while temp_num > ord("z"):
                temp_num -= 13
        elif c in A_to_M:
            temp_num = temp_num + shift1
            while temp_num > ord("M"):
                temp_num -= 13
        elif c in N_to_Z:
            temp_num = temp_num - shift2 ** 2
            while temp_num < ord("N"):
                temp_num += 13
        decrypted_text += chr(temp_num)  

# Verification Function
def verification():
    with open("decrypted_text.txt") as f:
        final_decryption = f.read()

    if final_decryption == text:
        print("The decryption was successful!")
    else:
        print("The decryption was unsuccessful.")

# These loops are to receive an integer input from the user, to be utilised as the shifting encryption values
while True:
        try:                                                   
            val1 = int(input("Enter the first encryption number: "))    
            if int (val1) < 0:                                 
                val1=print("Please enter a positive integer")  
                continue
            else:                                               
                break
        except ValueError:                                      
                val1=print("Please enter a positive integer")

while True:
        try:                                                   
            val2 = int(input("Enter the second encryption number: "))    
            if int (val2) < 0:                                 
                val2=print("Please enter a positive integer")  
                continue
            else:                                               
                break
        except ValueError:                                      
                val2=print("Please enter a positive integer")

print("\nLoading...\n")

# Calling the encryption function
encryption(val1, val2)

# Getting text from 'raw_text.txt'
with open("encrypted_text.txt", "w") as f:
    f.write(encrypted_text)

print("Done! The encrypted text should be in the text file.")

with open("encrypted_text.txt") as f:
    text_back = f.read()

print("\nDecrypting...\n")

decryption(val1, val2)

with open("decrypted_text.txt", "w") as f:
    f.write(decrypted_text)

print("Done! The decrypted text should be in the text file.")

verification()