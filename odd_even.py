def oddeven(*args):
    evenlist = [n for n in args if n%2==0]
    oddlist = [n for n in args if n%2==1]
    return f'evennumbers: {evenlist}\noddnumbers: {oddlist}'

inputvalues = oddeven(1,2,3,4,5,6,7,8,9,10)
print(inputvalues)