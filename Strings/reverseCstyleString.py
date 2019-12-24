#Note, Python strings are immutable.
#This means that they can never be changed.
#You can make new strings that are assigned to the same variable name,
#but the in-memory image for a given strings will never change.
#Thus, the notion of "reverse a string in place" can not happen in Python.
original = "abc\0"
finish_correct = "cba\0"
answer = original[:-1]  # remove final null
answer = answer[::-1]  # reverse string
# Extended slice syntax:  [begin:end:step]
# So, [::-1] means take whole string, but in reverse.

#Algorithm
void reverse(char *str) {
    char * end = str;
    char tmp;
    if (str) {
        while (*end) {
            ++end;
         }
         --end;
         while (str < end) {
            tmp = *str;
            *str++ = *end;
            *end-- = tmp;
        }
    }
}
