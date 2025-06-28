import sys


def open_file_and_read():
    with open("Date.txt","r") as file:##open file and save the object of the file in "file"
         read2 = file.read() ###read the file(strig)
         return read2##return all the word
         
 
            
def to_sort_the_text(read):#
    read = read.split()
    every_word_apper_one_time = set(read)###  in set() dont have doplicate of words!
    # print(every_word_apper_one_time)
    Dictionary = {}##make some Dictionary
    for word in every_word_apper_one_time:##creat kewand value for evry word in Dictionary and restart him to zero 
     Dictionary[word] = 0

    for word in every_word_apper_one_time:### here he work on list witout doplicate
        for another_word in read:### here he work on list that have all the word in the story/message
            if word == another_word:# if the word  in the list without doplicate and see in the big list same word she add one look down
                Dictionary[word] +=1#because of thets mean the word appers in the big list and the loop count how much time she is appears
            
    Dictionary = list(Dictionary.items())##convert to list because it is easier to sort  list then Dictionary
    Dictionary= sorted(Dictionary,key = lambda item:item[1],reverse= True)### sort from the big to the small
    return dict(Dictionary)###convert to Dictionary agein because its easier to printing the key and the value from Dictionary
    


# Dictionary = dict(sorted(Dictionary.items(),key = lambda item: item[1], reverse= True)) להתעלם להתעלם להתעלם להתעלם

def Printing_the_n_word_thats_apear_inthe_text(d,n):###printing the bigest word in the list
    count =0
    while n > count:
        z =d.copy()# i do doplicate for d (Dictionary)  
        z =list(z)# and after that convart the doplicate to list because it is much easier to get key from list 
        f = z[count]
        print("the word -",f,"- apper" ,d[f])###get the word from list and the value(how much time word is in the ,message) from Dictionary
        count+=1###stop until the first (n) will printing





r = open_file_and_read()
sortdictionary =to_sort_the_text(r)
if len(sys.argv) >1:
    Printing_the_n_word_thats_apear_inthe_text(sortdictionary,int(sys.argv[1]))
else:
    print("you need more parameter")


