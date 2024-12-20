'''#1.
sentence="To change the overall look of your document.To change the look availablein the gallery"
words=sentence.split()#split sentence into words
word_count={}

for word in words:
    word=word.lower().strip('.').strip(',')#removing punctuation and converting into lower case

    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1

print("Word counts:")
for word,count in word_count.items():
    print(word ," = occur in ", count,"times")#printing word with count



#2.
string="\nBest \nDeeptech \nPython \nTraining \n"
string=string.replace('\n','')#replace newline with space

print("String without newline :",string)#printing string without newline
                      


#3.
string="Deeptech Python Training"
words=string.split()#split string into words

reversed_string=''.join(reversed(words))#reversing the list of words and join them back
print("Reversed string :",reversed_string)


#4.

string="Welcome to Python Training"
vowels="aeiou"
vowels_count=0

for char in string:
    if char.lower() in vowels:
        vowels_count+=1

print("Number of vovels :",vowels_count)








#1
input_string = "P@#yn26at^&i5ve"
chars = 0
digits = 0
symbols = 0

for char in input_string:
    if char.isalpha():  # Check if the character is a letter
        chars += 1
    elif char.isdigit():  # Check if the character is a digit
        digits += 1
    else:  # Else, it's considered a special symbol
        symbols += 1

print("Chars =", chars)
print("Digits =", digits)
print("Symbol =", symbols)




#2.
input_string = "String and String Function"
result = ''

for char in input_string:
    if char not in result:
        result += char

print("String without duplicates:", result)

#3
input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
uppercase = lowercase = digits = special = 0

for char in input_string:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
    elif char.isdigit():
        digits += 1
    else:
        special += 1

print("UpperCase:", uppercase)
print("LowerCase:", lowercase)
print("NumberCase:", digits)
print("SpecialCase:", special)




#4.
input_string = "Welcome to Python Assignment"
vowels = "aeiou"
vowel_count = 0

for char in input_string:
    if char.lower() in vowels:
        vowel_count += 1

print("Vowel count:", vowel_count)

'''

#1.

my_list = [1, 2, 3, 4, 5]
total = 0

for item in my_list:
    total += item  # Add each item to the total

print("Sum of all items:", total)





#2
my_list = [3, 1, 4, 1, 5, 9, 2, 6]
largest = smallest = my_list[0]  # Start by assuming the first item is both the largest and smallest

for number in my_list:
    if number > largest:
        largest = number  # Update largest if a bigger number is found
    if number < smallest:
        smallest = number  # Update smallest if a smaller number is found

print("Largest number:", largest)
print("Smallest number:", smallest)




#3
my_list = [1, 2, 3, 4, 5, 1, 2, 6]
duplicates = []

for item in my_list:
    if my_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)  # Add the item to duplicates if it occurs more than once

print("Duplicate values:", duplicates)


#4
original_list = [1, 1, 2, 3, 4, 4, 5, 1]
length_first_part = 3

first_part = original_list[:length_first_part]  # Get the first part of the list
second_part = original_list[length_first_part:]  # Get the second part of the list

print("Splitted lists:", first_part, second_part)


#5
my_list = ['red', 'green', 'white', 'black']

print("Traverse the list in reverse order:")
for i in range(len(my_list) - 1, -1, -1):  # Start from the last element
    print(my_list[i])  # Print each item in reverse order

