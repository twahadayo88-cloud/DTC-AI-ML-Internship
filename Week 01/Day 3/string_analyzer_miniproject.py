#//program for string analysis
text = input("Enter your text here: ")
print("The text is:", text)
character_count = len(text)  #// counting the number of characters in the text
word_count = len(text.split())  #// counting the number of words in the text
print("The number of characters in the text is:", character_count)
print("The number of words in the text is:", word_count)
print ("The text in uppercase is:", text.upper())  #// converting the text to uppercase
print ("The text in lowercase is:", text.lower())  #// converting the text to lowercase
print ("The text capitalized is:", text.capitalize())  #// capitalizing the first letter of the text
print ("The text with title case is:", text.title())  #// converting the text to title case
print("First Character in capitalize form:", text[0].upper()) #// capitalizing the first character of the text
print("Last Character in capitalize form:", text[-1].upper()) #// capitalizing the last character of the text
