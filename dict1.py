
dict = {"apple":100, "orange":50, "melon":1000}

print dict["apple"], dict["orange"], dict["melon"]

dict["banana"] = 200
print dict["banana"]
print dict.keys()
del dict["melon"]

print dict.keys()
