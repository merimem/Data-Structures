#Approach 0
#We create a hash table and we go through the string and
#we add the chars in the hash table
#if it exists in the hash table then we
def is_unique(str):
    dict = {}
    for i in range(len(str)):
        if str[i] in dict:
            return False
        else:
            dict[str[i]]= True
    return True
#Approach 1
def unique_chars(str):
    for i in range(len(str)):
        for j in range(i+1,len(str)):
            if (str[i] == str[j]):
                return False
    return True
# Time Complexity: O(n2)

#Approach 2 – Sorting: Using sorting based on ASCII values of characters
#Time Complexity: O(n log n)
str = "abcdef"
print(is_unique(str))
