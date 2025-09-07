buttons = list(map(int, input().split()))
target = input()
n = buttons[0]
buttons = set(buttons[1:])
res = 0
closest_num = ""
for char in target:
    num = int(char)
    if num not in buttons:
        closest_num += char
        continue
    

print(res)

