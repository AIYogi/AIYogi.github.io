import os
home_path = os.getcwd()
file1 = "Sorted_warrior_1"
filename = file1+".txt"
fname = os.path.join(home_path,filename)
f = open(fname,"r")
Lines = f.readlines()
#count = 0
list_image = []
list_angle = []
list_marker = []
for count in range(len(Lines)):
    #print("Testing line",Lines[count],"at count",count)
    if count % 2 == 0:
        #print("Inside loop")
        list_image.append(Lines[count][-11:])
        marker = Lines[count][0:2]
        #print("marker",marker) 
        list_marker.append(marker)
    else:
        list_angle.append(Lines[count])
    #count += 1

#print("List_image")
#print(list_image)
identifiers_list_marker = list(set(list_marker))
identifiers_list_image = list(set(list_image))
column_0 = []
column_1 = []
column_Lh=[]
column_RE=[]
column_LE=[]
column_Ls=[]
column_Rs=[]
column_LK=[]
column_Rk=[]
column_RH=[]
#print(len(identifiers_list_image))
p = 0
print(len(list_image))
while p<(len(list_image)):
        column_0.append(file1)
        column_1.append((list_image[p]))
        p+=8
#print(list_image)
#print(column_1)
i = 0
for i in range(len(list_image)):
    
    if list_marker[i]=='Lh':
        column_Lh.append(list_angle[i])
    elif list_marker[i]=='RE':
        column_RE.append(list_angle[i])
    elif list_marker[i]=='LE':
        column_LE.append(list_angle[i])
    elif list_marker[i]=='Ls':
        column_Ls.append(list_angle[i])
    elif list_marker[i]=='Rs':
        column_Rs.append(list_angle[i])
    elif list_marker[i]=='LK':
        column_LK.append(list_angle[i])
    elif list_marker[i]=='Rk':
        column_Rk.append(list_angle[i])
    elif list_marker[i]=='RH':
        column_RH.append(list_angle[i])
    else:
        continue

column_1_stripped =list(map(str.strip,column_1))
print(column_1_stripped)
import csv
from itertools import zip_longest
d = [column_0, column_1_stripped, column_RH,column_Lh,column_RE,column_LE,column_Rk,column_LK,column_Rs,column_Ls]
export_data = zip_longest(*d, fillvalue = '')
file_export = file1+".csv" 
with open(file_export, 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Pose Name","Image Name", "RHA", "LHA", "REA", "LEA", "RKA", "LKA","RSA","LSA"))
      wr.writerows(export_data)
myfile.close()      
#print(column_1)    
#print(column_Lh)
#print(len(column_Lh))
#Image	RHA	RKA	REA	LHA	LKnee	Lhip	LKnee	LElbow	Rshoulder	Lshoulder









