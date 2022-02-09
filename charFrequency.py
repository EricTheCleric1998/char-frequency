# Eric Hillmeyer
# Fall 2019
# CS105L Section 007

# A function that locates the max value within the char_dict, list seen later
def maxInFile(dictionary):
    
    maximum = 0
    max_number = 0

    for i in dictionary:
        if dictionary[i] > max_number:
            max_number = dictionary[i]
            maximum = i

    return (maximum)

contents = ""
badInput = True

while badInput:
    try:
        user_file = input('Please enter the name of the file you wish to read from: ')

        f = open(user_file, "r")
        contents = f.readlines()
        f.close()

        break

    except:
        print('Please enter a valid text file.')


# Opening a dictionary to store characters
char_dict = dict()

# A for loop for iterating over each line in the readlines()
for line in contents:

    # The final for loop to iterate over each character and create a dictionary denoting all instances of that specific character
    for j in line:
        if j in char_dict:
            char_dict[j] += 1
        else:
            char_dict[j] = 1

ignore = input('Do you wish to ignore any characters? y/n ')

if ignore == 'y':

    file_contents = ""
    badInput = True
    while badInput:
        try:
            ignore_file = input('Please enter the name of the file containing the characters to ignore: ')
            
            g = open(ignore_file, "r")
            file_contents = g.readlines()
            g.close()

            break

        except:
            print('Please enter a valid text file.')
    
    file_contents = str(file_contents)

    for i in char_dict:
        if i == file_contents:
            char_dict.pop(i)
            
    maximum = maxInFile(char_dict)
    instance = char_dict[maximum]
    print('The character that appears the most frequently is ', maximum, ' with ', instance, ' instances.')
else:
    maximum = maxInFile(char_dict)
    instance = char_dict[maximum]
    print('The character that appears the most frequently is ', maximum, ' with ', instance, ' instances.')