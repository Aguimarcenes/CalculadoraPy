word = "string"
list_words = [w for w in word]
print(list_words)

y = 100
list_2 = [str(x**2 + y) for x in range(50) if x % 2 == 0]
print(list_2)