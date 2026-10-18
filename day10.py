#wap to input eid, name, bs, doj of employee and print their salary slip
'''
IF BS>=30000 THEN
TA=BS*40/100
DA=BS*60/100
HRA=BS*40/100
ELSE
TA=BS*20/100
DA=BS*40/100
HRA=BS*30/100
--------------------------------------------------
              salary slip of <employeename>
---------------------------------------------------
EID     BS     TA    DA   HRA   GS   TDS   NS
H101   20000  
---------------------------------------------------
              SALARY SLIP OF AUG-26
----------------------------------------------------
'''
name=input("ENTER YOUR NAME : ")
eid=input("ENTER YOUR EID : ")
bs=int(input("ENTER YOUR BASE SALARY : "))
doj=input("ENTER DATE OF JOINING (dd/mm/yyyy) : ")

if bs>=30000:
    ta=bs*40/100
    da=bs*60/100
    hra=bs*50/100
elif bs>=25000:
    ta=bs*30/100
    da=bs*50/100
    hra=bs*40/100
else:
    ta=bs*20/100
    da=bs*40/100
    hra=bs*30/100

print('-'*100)
print(' '*30,"SALARY SLIP OF ",name)
print('-'*100)
print("\tEID\t\tBS\t\tTA\t\tDA\t\tHRA\t\tGS\t\tTDS\t\tNS\t\t")
print("\t",eid,"\t",ta,"\t",da,"\t",hra,"\t",ta+da+hra,"\t",(ta+da+hra)/10,"\t",(ta+da+hra)-(ta+da+hra)/10)
print('-'*100)
print(' '*30,"SALARY SLIP OF AUG-2026")
print('-'*100)