
class string_funcs:
    def __init__(self, s, separator=" "):
        self.separator = separator
        self.s = s
        self.string = " ".join(((self.s).replace(separator, " ")).split())
        self.stringSpace = " ".join(((self.s).replace(separator, " ")).split())+" "
    def len_last_word(self):
        """Replaces separator with spaces and gets rid of unnecessary whitespace and Returns the length of the last word.

           Ex. print((string_funcs("Hello world", separator=" ").len_last_word()))
           Output:
           5
        """
       
        lastspace=-1
        for indexvalue in range(len((self.string))):
            if self.string[indexvalue] == " ":
                lastspace =indexvalue
        return len(self.string) - (lastspace+1)
    def len_First_Word(self):
        """Replaces separator with spaces and gets rid of unnecessary whitespace 
           Returns the length of the First Word in a string as a int 

           Ex. print(StringFunctions.string_funcs.Len_Of_Last_Word("This is a Example"," "))

           Output:
           4
        """
        iterations=0
        while self.string[iterations]!=" ":
             iterations+=1
        return iterations
    def get_last_word(self):
            """ Replaces separator with spaces and gets rid of unnecessary whitespace
            Gets the last word in a in a string. Omits Non-alphabetical characters unless they are inside the word.
                Returns last word as a string slice. Returns None if there is less than two words.

                Ex. print((string_funcs("This is a Ex3mp1e str1ng!", separator=" ").get_last_word()))
                Output: str1ng

            """
            AlphaR= -1
            AlphaL= 1
            for indexvalue in range(len((self.string))-1, 0, -1):  
                if self.string[indexvalue] == " ":
                    while self.string[AlphaR].isalpha()==False:
                        AlphaR-=1
                    while self.string[indexvalue+AlphaL].isalpha()==False:
                        AlphaL+=1
                    return self.string[(indexvalue+AlphaL):len(self.string)+AlphaR+1]          
    def get_last_chars(self):
        """ Replaces separator with spaces and gets rid of unnecessary whitespace
            Gets last characters in a string. Returns a string slice of the last charcters. Does NOT omit non-alphabetical characters.
            Returns a string slice.

            Ex. (string_funcs("This.is.a.Testing.String.3Cool3", separator=".")).get_last_chars()

            Output:
            3Cool3
        """
        for indexvalue in range(len((self.string))-1, 0, -1):
             if self.string[indexvalue] == " ":
                  return self.string[(indexvalue+1):len(self.string)]
    def chars_as_list(self):
        """ Replaces separator with spaces and gets rid of unnecessary whitespace ands a extra space at the end of the string.
            Returns characters as a list. Does NOT omit non-alphabetical characters.

            Ex. print((string_funcs("This.is.a.Testing.String.3Cool3", separator=".")).chars_as_list())

            Output: 
            ['This', 'is', 'a', 'Testing', 'String', '3Cool3']
        """
        list1 =[]
        lastspace=0
        for indexvalue in range(0,len(self.stringSpace)):
                if self.stringSpace[indexvalue]==" " and indexvalue:
                    list1.append((self.stringSpace[lastspace:indexvalue]).strip())
                    lastspace = indexvalue
        return list1
if __name__ == "__main__":
    print((string_funcs("Hello World!!!", separator=" ")).get_last_word())
 
