def print_statistics(arr):
    n=len(arr)
    if n==0:
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        return
    print(n)
    avg=0
    min=arr[0]
    max=arr[0]
    for a in arr:
        avg += a
        if a > max:
            max=a
    if a < min:
        min=a
    avg=avg/n
    print(avg)
    print(min)
    print(max)
    tmp=sorted(arr)
    if n%2==0:
        med=0.5*(tmp[n//2-1]+tmp[n//2])
    else:
        med=tmp[n//2]
    print(med)