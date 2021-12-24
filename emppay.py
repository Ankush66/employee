#program for generating pay slip of an employee
#emppay.py
eno=int(input("enter employee number:"))
ename=input("enter employee name:")
dsg=input("enter employee designation:")
basicsal=float(input("enter employee basic salary:"))
#calculation
if (basicsal>=10000):
	da=basicsal*(20/100)
	ta=basicsal*(15/100)
	hra=basicsal*(20/100)
	ma=basicsal*(5/100)
else:
	da=basicsal*(25/100)
	ta=basicsal*(20/100)
	hra=basicsal*(25/100)
	ma=basicsal*(10/100)
netasl=basicsal=da+ta+hra+ma
#display employee pay slip
print("="*50)
print("employee number:{}".format(eno))
print("employee name:{}".format(ename))
print("employee designation:{}".format(dsg))
print("employee basic salary:{}".format(basicsal))
print("employee da:{}".format(da))
print("employee ta:{}".format(ta))
print("employee hra:{}".format(hra))
print("employee ma:{}".format(ma))
print("-"*50)
print("empoyee net salary:{}".format(natsal))
print("*"*50)


