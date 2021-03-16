import os
home_path = os.getcwd()
# input file name
file1 = "Sorted_Cobra"
# file_name = sorted+posename
# need to assign 2 more columns: col 1:posename col 2 : standing/sitting col 3: straight/
pose_class = ["Standing","Sitting", "Balancing", "Inverted","Reclining","Wheel"]
pose_Standing = ["Straight","Forward_bend","Side_bend","Others"]
pose_Standing_breaks = [3,8,15,20]
pose_Sitting = ["Normal1","Normal2","Split","Forward_bend","Twist"]
pose_Sitting_breaks = [25,29,31,35,38]
pose_Balancing = ["Front","Side"]
pose_Balancing_breaks = [43,46]
pose_Inverted = ["Legs_straight_up","Legs_bend"]
pose_Inverted_breaks = [51,53]
pose_Reclining = ["Up_facing","Down_facing","Side_facing","Plank_balance"]
pose_Reclining_breaks = [61,66,68,72]
pose_Wheel = ["Up_facing","Down_facing","Others"]
pose_Wheel_breaks = [79,80,82]
pose_Name = ["Eagle","Tree","Chair","Standing_forward_bend","Wide_legged_forward_bend","Dolphin","Downward_dog","Intense_side_stretch","Half_moon","Extended_triangle","Extended_side_angle","Gate","Warrior_1","Reverse_warrior","Low_lunges","Warrior_2","Warrior_3","Lord_of_dance","Standing_big_toe_hold","Standing_split","Easy_sitting","Cobbler","Garland","Staff","Noose","Cow_face","Hero_and_thunderbolt","Bharadwajas_twist","Half_lord_of_the_fishes","Split","Wide_angle_seated_forward_bend","Head_to_knee","Revolved_head_to_knee","Seated_forward_bend","Tortoise_pose","Shooting_bow","Heron","King_pigeon","Crane_crow","Shoulder_pressing","Cockerel","Scale","Firefly","Side_crane_crow","Eight_angle","Sage_koundaniya","Handstand","Headstand","Shoulder_stand","Feather_peacock","Legs_up_to_wall","Plow","Scorpion","Corpse","Fish","Happy_baby","Reclining_hand_to_big_toe","Wind_relieving","Reclining_cobbler","Reclining_hero","Yogic_sleep","Cobra","Frog","Locust","Child","Extended_puppy","Side_reclining_leg_lift","Side_plank","Dolphin_plank","Low_plank","Plank","Peacock","Upward_bow","Upward_facing_two_foot_staff","Upward_plank","Pigeon","Bridge","Wild_things","Camel","Cat-cow","Boat","Bow"]
pose_breaks = [3,8,15,20,25,29,31,35,38,43,46,51,53,61,66,68,72,79,80,82]
pose_class_breaks = [0,20,38,46,53,72,82]
pose_sub_class = []
pose_sub_class_breaks =[]
file_search = file1[7:]
index = pose_Name.index(file_search)+1
j = 0

length_pose = len(pose_class)
while (j<=len(pose_class)-1):
    X_class = pose_class_breaks[j]+1
    Y_class = pose_class_breaks[j+1]
    
    if index in range(X_class,Y_class+1):
        class_identify = pose_class[j]
        class_number = j
        pose_number = index
        if j == 0:
            pose_sub_class = ["Straight","Forward_bend","Side_bend","Others"]
            pose_sub_class_breaks = [0,3,8,15,20]
        elif j == 1:
            pose_sub_class = ["Normal1","Normal2","Split","Forward_bend","Twist"]
            pose_sub_class_breaks = [20,25,29,31,35,38]
        elif j  == 2:
            pose_sub_class = ["Front","Side"]
            pose_sub_class_breaks = [38,43,46]
        elif j == 3:
            pose_sub_class = ["Legs_straight_up","Legs_bend"]
            pose_sub_class_breaks = [46,51,53]
        elif j == 4:
            pose_sub_class = ["Up_facing","Down_facing","Side_facing","Plank_balance"]
            pose_sub_class_breaks = [53,61,66,68,72]
        elif j == 5:
            pose_sub_class = ["Up_facing","Down_facing","Others"]
            pose_sub_class_breaks = [72,79,80,82]

        break
        
    
    j = j+1





k = 0


length_sub_class = len(pose_sub_class)
print(len(pose_sub_class))
while (k<=len(pose_sub_class)-1):
    X_sub_class = pose_sub_class_breaks[k]+1
    Y_sub_class = pose_sub_class_breaks[k+1]
    
    if  pose_number in range(X_sub_class,Y_sub_class+1):
        print("Entered loop")
        sub_class_identify = pose_sub_class[k]
        sub_class_number = k
        break
        #list_identify = "pose_"+class_identify
        #list_identify_breaks = list_identify+"_breaks"
       
    k = k+1

head_sub_head = class_identify+"_"+sub_class_identify
head_sub_head_number = str(class_number+1)+"."+str(sub_class_number+1)
head_sub_head_pose_number = str(class_number+1)+"."+str(sub_class_number+1) + "."+str(pose_number)





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
column_0x = []
column_pose_number = []
column_class_number = []
column_sub_class_number = []
column_combo_number = []
column_01 = []
column_02 = []
column_1 = []
column_Lh=[]
column_RE=[]
column_LE=[]
column_Ls=[]
column_Rs=[]
column_LK=[]
column_Rk=[]
column_RH=[]
column_Lhz=[]
column_REz=[]
column_LEz=[]
column_Lsz=[]
column_Rsz=[]
column_LKz=[]
column_Rkz=[]
column_RHz=[]
column_status = []
#print(len(identifiers_list_image))
p = 0
#print(len(list_image))
while p<(len(list_image)):
        column_0.append(file1)
        column_combo_number.append(head_sub_head_pose_number)
        column_0x.append(head_sub_head)
        column_pose_number.append(pose_number)
        column_01.append(class_identify)
        column_class_number.append(class_number+1)
        column_02.append(sub_class_identify)
        column_sub_class_number.append(sub_class_number+1)
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
#calculate mean
mean_Lh = sum(map(float,column_Lh))/len(column_Lh)
mean_RE = sum(map(float,column_RE))/len(column_RE)
mean_LE = sum(map(float,column_LE))/len(column_LE)
mean_Ls = sum(map(float,column_Ls))/len(column_Ls)
mean_Rs = sum(map(float,column_Rs))/len(column_Rs)
mean_LK = sum(map(float,column_LK))/len(column_LK)
mean_Rk = sum(map(float,column_Rk))/len(column_Rk)
mean_RH = sum(map(float,column_RH))/len(column_RH)
#SD
sq = 0.0
for j in range(0,len(column_Lh)):
    sq += ((float(column_Lh[j])) - mean_Lh)**2
    sd_Lh = (sq/len(column_Lh))**0.5
sq = 0.0
for col_RE in column_RE:
    sq += (float(col_RE) - mean_RE)**2
    sd_RE = (sq/len(column_RE))**0.5
sq = 0.0
for col_LE in column_LE:
    sq += (float(col_LE) - mean_LE)**2
    sd_LE = (sq/len(column_LE))**0.5
sq = 0.0
for col_Ls in column_Ls:
    sq += (float(col_Ls) - mean_Ls)**2
    sd_Ls = (sq/len(column_Ls))**0.5
sq = 0.0
for col_Rs in column_Rs:
    sq += (float(col_Rs) - mean_Rs)**2
    sd_Rs = (sq/len(column_Rs))**0.5
sq = 0.0
for col_LK in column_LK:
    sq += (float(col_LK) - mean_LK)**2
    sd_LK = (sq/len(column_LK))**0.5
sq = 0.0
for col_Rk in column_Rk:
    sq += (float(col_Rk) - mean_Rk)**2
    sd_Rk = (sq/len(column_Rk))**0.5
sq = 0.0
for col_RH in column_RH:
    sq += (float(col_RH) - mean_RH)**2
    sd_RH = (sq/len(column_RH))**0.5
# Z score
for col_Lh in column_Lh:
    z_Lh = (float(col_Lh) - mean_Lh)/sd_Lh
    column_Lhz.append(z_Lh)
for col_RE in column_RE:
    z_RE = (float(col_RE) - mean_RE)/sd_RE
    column_REz.append(z_RE)
for col_LE in column_LE:
    z_LE = (float(col_LE) - mean_LE)/sd_LE
    column_LEz.append(z_LE)
for col_Ls in column_Ls:
    z_Ls = (float(col_Ls) - mean_Ls)/sd_Ls
    column_Lsz.append(z_Ls)
for col_Rs in column_Rs:
    z_Rs = (float(col_Rs) - mean_Rs)/sd_Rs
    column_Rsz.append(z_Rs)
for col_LK in column_LK:
    z_LK = (float(col_LK) - mean_LK)/sd_LK
    column_LKz.append(z_LK)
for col_Rk in column_Rk:
    z_Rk = (float(col_Rk) - mean_Rk)/sd_Rk
    column_Rkz.append(z_Rk)
for col_RH in column_RH:
    z_RH = (float(col_RH) - mean_RH)/sd_RH
    column_RHz.append(z_RH)

for row_index in range(0,len(column_Lh)):
    count_Z = 0
    count_Lhz  = count_REz  = count_LEz = count_Lsz = count_Rsz = count_LKz = count_Rkz = count_RHz = 0
    if(abs(float(column_Lhz[row_index]))>2):
        count_Lhz += 1
    if(abs(float(column_REz[row_index]))>2):
        count_REz += 1
    if(abs(float(column_LEz[row_index]))>2):
        count_LEz += 1
    if(abs(float(column_Lsz[row_index]))>2):
        count_Lsz += 1
    if(abs(float(column_Rsz[row_index]))>2):
        count_Rsz += 1
    if(abs(float(column_LKz[row_index]))>2):
        count_LKz += 1
    if(abs(float(column_Rkz[row_index]))>2):
        count_Rkz += 1
    if(abs(float(column_RHz[row_index]))>2):
        count_RHz += 1
    countZ = count_Lhz + count_REz + count_LEz + count_Lsz + count_Rsz + count_LKz + count_Rkz + count_RHz
    if countZ >=3:
        column_status.append("Fail")
    else:
        column_status.append("Pass")

        #print("Delete "+str(column_1_stripped[row_index])+"at "+str(row_index+2))



#print(column_1_stripped)
import csv
from itertools import zip_longest
d = [column_pose_number, column_0, column_0x, column_01, column_class_number, column_02, column_sub_class_number, column_combo_number, column_1_stripped, column_status, column_RH, column_RHz, column_Lh, column_Lhz, column_RE, column_REz, column_LE,column_LEz, column_Rk, column_Rkz, column_LK, column_LKz, column_Rs, column_Rsz, column_Ls, column_Lsz]
export_data = zip_longest(*d, fillvalue = '')
file_export = file1+"ver_Jan17"+".csv" 
with open(file_export, 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Pose Number","Pose Name","Class_sub_class","Pose_Class","Class Number","Pose_Sub_Class","Sub Class Number","Standard Pose Number","Image Name", "Status","RHA","RHAZ", "LHA","LHAZ", "REA","REAZ", "LEA","LEAZ", "RKA","RKAZ", "LKA","LKAZ","RSA","RSAZ","LSA","LSAZ"))
      wr.writerows(export_data)
      #wr.writerow("Delete "+str(column_1_stripped[row_index])+"at "+str(row_index+2))
      #wr.writerows(export_data)      
myfile.close()      
#print(column_1)    
#print(column_Lh)
#print(len(column_Lh))
#Image	RHA	RKA	REA	LHA	LKnee	Lhip	LKnee	LElbow	Rshoulder	Lshoulder









