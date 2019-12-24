#Approach 1
#Use new string
def replaceSpace(str):
    if (str is None):
        return str
    num_spaces = 0

    for i in range(len(str)):
        if str[i] == " ":
            num_spaces+=1

    if (num_spaces == 0):
        return(str)

    new_length= len(str)+ 2 * num_spaces
    str_to_return=""
    for i in range(len(str)):
        if (str[i] == " "):
            str_to_return+="%"
            str_to_return+="2"
            str_to_return+= "0"
        else:
            str_to_return+=str[i]
            #i = i-2
    return str_to_return

#Approach 2
# Use the same string and we shift the characters
# 1. Count the number of spaces during the first scan of the string.
# 2. Parse the string again from the end and for each character:
# If a space is encountered, store “%20”.
# Else, store the character as it is in the newly shifted location.
#1 public static void ReplaceFun(char[] str, int length) {
#    int spaceCount = 0, newLength, i = 0;
#   for (i = 0; i < length; i++) {
#       if (str[i] == ‘ ‘) {
#           spaceCount++;
#        }
#   }
#   newLength = length + spaceCount * 2;
#   str[newLength] = ‘\0’;
#   for (i = length - 1; i >= 0; i--) {
#       if (str[i] == ‘ ‘) {
#           str[newLength - 1] = ‘0’;
#           str[newLength - 2] = ‘2’;
#           str[newLength - 3] = ‘%’;
#           newLength = newLength - 3;
#       } else {
#           str[newLength - 1] = str[i];
#           newLength = newLength - 1;
#       }
#   }

print(replaceSpace("a b"))
