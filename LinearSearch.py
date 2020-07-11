def linearSearch(arr,n,x):
    for i in range(0,n):
        if (arr[i]==x):
            return i;
    return -1;
arr=[2,3,8,5,10,6,1];
x = 8;
n = len(arr);
results = linearSearch(arr,n,x);
if(results==-1):
    print("Element are not present in the array");
else:
    print ("Element are present in index", results);
    
