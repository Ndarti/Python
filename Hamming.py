a="12_34"
b="12336"
i=0
count=0
while i<len(a):
    if a[i]!=b[i]:count=count+1
    i=i+1
print(count)