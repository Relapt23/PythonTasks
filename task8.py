# Дан набор точек на координатной плоскости. Необходимо подсчитать и вывести количество точек, лежащих в каждой координатной четверти.
count1 = 0
count2 = 0
count3 = 0
count4 = 0
for i in range(int(input())):
    a = [int(i) for i in input().split()]
    x, y = a[0], a[1]
    if x > 0 and y > 0:
        count1 += 1
    elif x > 0 and y < 0:
        count4 += 1
    elif x < 0 and y < 0:
        count3 += 1
    elif x < 0 and y > 0:
        count2 += 1
    else:
        continue

print(f"Первая четверть: {count1}")
print(f"Вторая четверть: {count2}")
print(f"Третья четверть: {count3}")
print(f"Четвертая четверть: {count4}")    
