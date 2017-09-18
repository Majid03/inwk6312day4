#import my own file
import task

# This opens a file
my_file = open("words.txt")

# This creates a empty list
word_list = []

# for each line in my file do
for line in my_file:
    #append the stripped word to the wordlist
    word_list.append(line.strip())

# Create dict 
word_count = {}
for index in range(len(word_list)):
    word_count = task.hist(word_list[index],word_count)

# Print the count
task.print_hist(word_count)
    
    

