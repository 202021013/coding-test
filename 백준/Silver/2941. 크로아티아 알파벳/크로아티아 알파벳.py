word = input()
alphas = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count_values = 0

for alpha in alphas:
    word = word.replace(alpha, "1")
    
for i in word:
    count_values += 1

print(count_values)
