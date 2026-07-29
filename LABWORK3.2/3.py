'''Create a list and a tuple both containing the same 3 items.

Try changing the first item of each.

Discuss the error (in case of tuple) and explain why it happens.'''


lst = ["abc","def","ghi"]
tpl = ("abc","def","ghi")

lst[0] = "jkl"
print("updated list:",lst)

tpl[0] = "jkl"
print("updated tuple:",tpl)