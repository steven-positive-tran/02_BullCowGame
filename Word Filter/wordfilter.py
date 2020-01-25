
file = open("words_alpha_new.txt","r")

def if_isogram(word):
    letter_list = []

    for letter in word:
        if letter in letter_list:
            return False
        letter_list.append(letter)
    
    return True

filenew = open("words_alpha_new2.txt","w")

for x in file: 
    word = file.readline()
    isogram = if_isogram(word)
    if isogram == True:
        if len(word) > 4:
            filenew.write(word)
    

file.close()
filenew.close()
        
    

file.close()



    