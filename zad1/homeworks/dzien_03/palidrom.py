texts = ["php", "w3r", "Python", "abcd", "Java", "aaa"]
print("Orginal list of strings:")
print(texts)
result = list(filter(lambda x: (x==x[::-1], texts))
print("\nList of palindromes:")
print(result)
