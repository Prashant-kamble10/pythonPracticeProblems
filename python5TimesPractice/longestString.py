


def sample(str):
    arr = str.split(" ")
    print(arr)
   
    longestWord = ""
    for word in arr:
        if len(word) > len(longestWord):
            longestWord = word
    
    print(longestWord)


sample("my name is prashant kamble")