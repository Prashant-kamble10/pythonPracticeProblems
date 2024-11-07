#  find the largest number in python

arr = [1,2,11,3,4,5,]

def sample(num):
   
   res = num[0]
   for i in num:
      if i > res:
         res = i
      
   print(res)


sample(arr)

# palindrome

name = "radar"

def sample(str):
   revStr = str[::-1]

   if revStr == str:
      print("true") 
   else:
      print("false")

sample(name)    
