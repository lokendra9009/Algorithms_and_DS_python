#Anagram solution

# Program check if the given input strings are anagram of each other

def anagram_check(str1,str2):
    str1=str1.strip()
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()
    str2=str2.strip()
    return sorted(str1)==sorted(str2)


print anagram_check("dog","god")
    
