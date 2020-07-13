def BinarySearch(arr,l,r,x):
    if(r>=l):
      mid=l+(r-l);
      if(arr[mid]==x):
        return mid;
      elif(arr[mid]>x):
        return BinarySearch(arr,l,mid-1,x);
      else:
        return BinarySearch(arr,mid+1,r,x);
    else:
      return -1;
arr = [2,5,7,9,12,17];
x=7;
n=len(arr);
result = BinarySearch(arr,0,n-1,x);
if(result!=-1):
  print("Elements are present in the index at:", result);
else:
  print ("Elements are not present");
