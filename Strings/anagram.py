#Approach 0
# We can sort the two strings
# and then sorted_1 == sorted_2

#Approach1
#We use the hashtables
def is_anagram (str_1, str_2):
    #delete white spaces
    str_1 = str_1.replace(" ","")
    str_2 = str_2.replace(" ","")

    if len(str_1) != len (str_2):
        return False

    #deal with lowercases
    str_1 = str_1.lower
    str_2 = str_2.lower

    #use hash tables
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    dict_1 = dict.fromkeys(list(alphabet), 0)
    dict_2 = dict.fromkeys(list(alphabet), 0)

    for i in range(len(str_1)):
        dict_1[str_1[i]] += 1
        dict_2[str_2[i]] += 1

    return dict_1 == dict_2
