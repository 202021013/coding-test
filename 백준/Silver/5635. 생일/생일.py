import sys

n = int(sys.stdin.readline().strip())
student_list = []

for _ in range(n):
    name, day, month, year = sys.stdin.readline().split()
    b_date = int(year + month.zfill(2) + day.zfill(2))
    student_list.append((name,b_date))

sorted_list = sorted(student_list, key = lambda x : x[1])

print(sorted_list[-1][0])
print(sorted_list[0][0])