word = input().lower()
count = {}

for char in word:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

max_count = max(count.values())
max_chars = []

for char in count:
    if count[char] == max_count:
        max_chars.append(char)

if len(max_chars) == 1:
    print(max_chars[0].upper())
else:
    print("?")
