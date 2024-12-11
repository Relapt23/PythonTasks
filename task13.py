a = []
ans = "НЕТ"
for i in range(int(input())):
    a.append(int(input()))
res = int(input())
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] * a[j] == res and i != j:
            ans = "ДА"
print(ans)
