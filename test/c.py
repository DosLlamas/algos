# numOfWords = input()
# dictionary = {}
# for i in range(int(numOfWords)):
#     word = input()
#     dictionary[word] = word

# numOfTestWords = input()
# yes = 0
# res = []
# for i in range(int(numOfTestWords)):
#     word = input()
#     if word in dictionary:
#         res.append(1)
#         yes = 1
#     else:
#         test = ""
#         test2 = ""
#         for j in range(len(word)):
#             test += word[j]
#             if test in dictionary: 
#                 for k in range(j+1, len(word) -1):
#                     test2 += word[k]
#                     if test2 in dictionary:
#                         res.append(2)
#                         yes = 2
#     if yes == 0:
#         res.append(0)
#     yes = 0
# for r in res:
#     print(r)

n = int(input())
dictionary = set()

for _ in range(n):
    dictionary.add(input())

m = int(input())
results = []

for _ in range(m):
    word = input()
    if word in dictionary:
        results.append(1)
        continue

    found = False
    for i in range(1, len(word)):  # split at every position
        first = word[:i]
        second = word[i:]
        if first in dictionary and second in dictionary:
            results.append(2)
            found = True
            break

    if not found:
        results.append(0)

for r in results:
    print(r)