arr=[1,2,3,4,5]
#prefix sum
ps_arr=[]
#prefix multiplication
pm_arr=[]
ps_arr.append(arr[0])
pm_arr.append(arr[0])
for i in range(1,len(arr)):
    ps_arr.append(ps_arr[i-1]+arr[i])
for i in range(1,len(arr)):
    pm_arr.append(pm_arr[i-1]*arr[i])
print(ps_arr)
print(pm_arr)