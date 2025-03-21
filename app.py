# Pyramid Pattern in Python

rows = 5    # Number of rows

# Generate the pyramid

for i in range(1, rows + 1):    #ye loop 1 se 5 tak chalega aur 1 ka increment hoga
    
    # Calculate number of spaces
    spaces = rows - i   #Agar i = 1 (pehli row), to spaces = 5 - 1 = 4

    # Calculate number of stars
    stars = 2 * i - 1    # Agar i = 1 (pehli row), to stars = 2 * 1 - 1 = 1
    
   # Har row ke liye spaces aur stars ko mila ke print karta hai.
    print(" " * spaces + "*" * stars)  
