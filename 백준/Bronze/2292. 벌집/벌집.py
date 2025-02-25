n = int(input())

layer = 1 
count = 1  

while n > count:
    count += 6 * layer
    layer += 1

print(layer)