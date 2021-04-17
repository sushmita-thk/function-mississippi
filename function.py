def prCharWithFreq(str):
 
    # Store all characters and their frequencies
    # in dictionary
    d = {}
    for i in str:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
     
    # Print characters and their frequencies in
    # same order of their appearance
    for i in str:
 
        # Print only if this character is not printed
        # before. 
        if d[i] != 0:
            print("{}{}".format(i,d[i]), end =" ")
            d[i] = 0
      
     
# Driver Code
if __name__ == "__main__" :
     
    str = "Mississippi";
    prCharWithFreq(str);
     
