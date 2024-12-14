# scopes and namespaces are same

# ghar mein bahare ke cheeze annadar aaa sahkti hain,but annadar ke cheeze bahar nahi jaa shakti

username = "prashant"

def test():
    username = "kamble"      # kamble
    print(username)

print(username)            # prashant
test()
#----------------------------------------------------------      
x = 99

def test2(y):
    z = x + y
    return z

result = test2(1)
print(result)       # 100
#----------------------------------------------------------  









