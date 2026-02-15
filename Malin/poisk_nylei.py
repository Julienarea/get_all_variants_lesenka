# 1.1
a = [3, 4, 0, 5, 6, 0 ,7, 8]
p1,p2 = -1,-1
for i in range(len(a)):
    if a[i] == 0:
        p1 = i
        break
for j in range(len(a)):
    if a[j] == 0:
        p2 = j

print(p1,p2)

#1.2
a = [3, 4, 0, 5, 6, 0 ,7, 8]
p1,p2 = -1,-1

for i in range(len(a)):
    if a[i] == 0:
        if p1 == -1:
            p1 = i
        else:
            p2 = i
    
print(p1,p2)


#2
