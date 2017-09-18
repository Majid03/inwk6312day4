# This opens a file
my_file = open("words.txt")
# This creates a empty list
word_list = []

# for each line in my file do
for line in my_file:
    #append the stripped word to the wordlist
    word_list.append(line.strip())

print (len(word_list))

