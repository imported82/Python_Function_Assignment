def func_1(n):
    if (n==2):
        return False
    elif (n==4):
        return True;
    else:
        for x in range(4,n):
             if(n % x==0):
                  return False
        return True
print(func_1(7))