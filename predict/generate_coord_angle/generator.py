###WARNING: This code is not tested without intercepts
import os
import sys
import pandas as pd
import numpy as np
import itertools
path = os.getcwd()
#print(path)
####USER INPUT: FILE NAME
fweight_csv = "Weights_of_Pose_Name.csv"
flabel_csv = "labels_of_Pose_Name.csv"
####Determine number of features
flag_intercept = True
file_weight = os.path.join(path,fweight_csv)
file_label = os.path.join(flabel_csv)
df_weight = pd.read_csv(file_weight, header=None)
df_label = pd.read_csv(file_label, header=None)
#print(len(df_weight))
list_weight = df_weight.values.tolist()
list_label = df_label.iloc[:,0].values.tolist()
n_labels = len(list_label)
#print(len(list_label))

####USER INPUT: NUMBER OF FEATURES
# Use 8 for angles
#USER INPUT FOR NUMBER OF UNIQUE FEATURES (LHA,RHA etc etc)
#Use 5 for PCA
n_input_features = 8
n_features = len(list_weight[0])
#####USER INPUT: USING INTERCEPT
#Input True if you want to use intercept else False
flag_intercept = True

if flag_intercept == True:
    n_features = len(list_weight[0])
else:
    list_weight[0].pop(0)
    n_features = len(list_weight[0])
#print(n_features)
#print(list_weight[0])    
#print(len(df.index))



#######Reading Weights#####################

file = "top_constant.txt"
fname1 = os.path.join(path,file)
file3 = "bottom_constant.txt"
fname3 = os.path.join(path,file3)
file4 = "between_constant.txt"
fname4 = os.path.join(path,file4)
fname_gen = "predict_gen.java"
fname2 = os.path.join(path,fname_gen)
gen_file = open(fname2)

########Input Test Files##################
test_file = "Sorted_Warrior_3.csv"
fname_test = os.path.join(path,test_file)
test_file_coord = "Sorted_Warrior_3.txt"
fname_test_coord = os.path.join(path,test_file_coord)

index = 0
with open(fname1) as f1:
    with open(fname2,"w") as f2:
        for line in f1:
            index += 1
            f2.write(line)
    f2.close()
f1.close()

###Load test data
df_test = pd.read_csv(fname_test)
RHA_list = df_test["RHA"].values.tolist()
LHA_list = df_test["LHA"].values.tolist()
REA_list = df_test["REA"].values.tolist()
LEA_list = df_test["LEA"].values.tolist()
RKA_list = df_test["RKA"].values.tolist()
LKA_list = df_test["LKA"].values.tolist()
RSA_list = df_test["RSA"].values.tolist()
LSA_list = df_test["LSA"].values.tolist()
#print("Number of images are:")
#print(len(REA_list))

####Load coordinate data
RHip_X = []
RHip_Y = []
Rknee_X =[]
Rknee_Y = []
RAnkle_X =[]
RAnkle_Y=[]
RElbow_X=[]
RElbow_Y=[]
RWrist_X=[]
RWrist_Y=[]
Lhip_X=[]
Lhip_Y=[]
LKnee_X=[]
LKnee_Y=[]
LAnkle_X=[]
LAnkle_Y=[]
LElbow_X=[]
LElbow_Y=[]
LWrist_X=[]
LWrist_Y=[]
Rshoulder_X=[]
Rshoulder_Y=[]
Lshoulder_X=[]
Lshoulder_Y=[]
Reye_X=[]
Reye_Y=[]
Leye_X=[]
Leye_Y=[]
file_coords = open(fname_test_coord,'r')
Lines_coords = file_coords.readlines()
List_Names_coords = ["RHip_X","RHip_Y","Rknee_X","Rknee_Y","RAnkle_X","RAnkle_Y","RElbow_X","RElbow_Y","RWrist_X","RWrist_Y","Lhip_X","Lhip_Y","LKnee_X","LKnee_Y","LAnkle_X","LAnkle_Y","LElbow_X","LElbow_Y","LWrist_X","LWrist_Y","Rshoulder_X","Rshoulder_Y","Lshoulder_X", "Lshoulder_Y","Reye_X","Reye_Y","Leye_X","Leye_Y"]

count = 1
for i in range(0,len(REA_list)):
    RHip_X.append(Lines_coords[count])
    RHip_Y.append(Lines_coords[count+1])
    Rknee_X.append(Lines_coords[count+3])
    Rknee_Y.append(Lines_coords[count+4])
    RAnkle_X.append(Lines_coords[count+6])
    RAnkle_Y.append(Lines_coords[count+7])
    RElbow_X.append(Lines_coords[count+9])
    RElbow_Y.append(Lines_coords[count+10])
    RWrist_X.append(Lines_coords[count+12])
    RWrist_Y.append(Lines_coords[count+13])
    Lhip_X.append(Lines_coords[count+15])
    Lhip_Y.append(Lines_coords[count+16])
    LKnee_X.append(Lines_coords[count+18])
    LKnee_Y.append(Lines_coords[count+19])
    LAnkle_X.append(Lines_coords[count+21])
    LAnkle_Y.append(Lines_coords[count+22])
    LElbow_X.append(Lines_coords[count+24])
    LElbow_Y.append(Lines_coords[count+25])
    LWrist_X.append(Lines_coords[count+27])
    LWrist_Y.append(Lines_coords[count+28])
    Rshoulder_X.append(Lines_coords[count+30])
    Rshoulder_Y.append(Lines_coords[count+31])
    Lshoulder_X.append(Lines_coords[count+33])
    Lshoulder_Y.append(Lines_coords[count+34])
    Reye_X.append(Lines_coords[count+36])
    Reye_Y.append(Lines_coords[count+37])
    Leye_X.append(Lines_coords[count+39])
    Leye_Y.append(Lines_coords[count+40])
    count += 42

Coords_1d = itertools.chain(RHip_X,RHip_Y,Rknee_X,Rknee_Y,RAnkle_X,RAnkle_Y,RElbow_X,RElbow_Y,RWrist_X,RWrist_Y,Lhip_X,Lhip_Y,LKnee_X,LKnee_Y,LAnkle_X,LAnkle_Y,LElbow_X,LElbow_Y,LWrist_X,LWrist_Y,Rshoulder_X,Rshoulder_Y,Lshoulder_X,Lshoulder_Y,Reye_X,Reye_Y,Leye_X,Leye_Y)
Coords_1d_list = list(Coords_1d)
#print(Coords_1d_list[0])
with open(fname2, "a") as f2:
    f2.write("\n")
    k = 0
    for list_names in List_Names_coords:
        count = 0
        f2.write("A_")
        f2.write(str(list_names))
        f2.write("=new double[]{")
        for i in range(0,len(RHA_list)):
            if i<=len(RHA_list)-2:
                f2.write(str.rstrip(Coords_1d_list[k]))
                f2.write(",")
            else:
                f2.write(str.rstrip(Coords_1d_list[k]))
            k = k+1
        f2.write("};")
        f2.write("\n")

    '''
for list_names in List_Names_coords:
    count = 0
    print(list_names,"=new double[]{")

    for j in range(RHA_list)):
        if j<=len(RHA_list)-2:
            print(str(Coords_2d_list[j])+",")
        else:
            print(str(Coords_2d_list[j]))
    print("};")
    print("\n")
    count = count +1
'''


####Write Test Data 
with open(fname2, "a") as f2:
    f2.write("\n")
    f2.write("RHA= new double[]{ ")
    for j in range(len(RHA_list)):
        if j<=len(RHA_list)-2:
            f2.write(str(RHA_list[j])+",")
        else:
            f2.write(str(RHA_list[j]))
    f2.write("};")
    f2.write("\n")
    f2.write("LHA= new double[]{ ")
    for j in range(len(LHA_list)):
        if j<=len(LHA_list)-2:
            f2.write(str(LHA_list[j])+",")
        else:
            f2.write(str(LHA_list[j]))
    f2.write("};")
    f2.write("\n")
    f2.write("REA= new double[]{ ")
    for j in range(len(REA_list)):
        if j<=len(REA_list)-2:
            f2.write(str(REA_list[j])+",")
        else:
            f2.write(str(REA_list[j]))
    f2.write("};")
    f2.write("\n")
    f2.write("LEA= new double[]{ ")
    for j in range(len(LEA_list)):
        if j<=len(LEA_list)-2:
            f2.write(str(LEA_list[j])+",")
        else:
            f2.write(str(LEA_list[j]))
    f2.write("};")
    f2.write("\n")
    f2.write("RKA= new double[]{ ")
    for j in range(len(RKA_list)):
        if j<=len(RKA_list)-2:
            f2.write(str(RKA_list[j])+",")
        else:
            f2.write(str(RKA_list[j]))
    f2.write("};")
    f2.write("\n")
    f2.write("LKA= new double[]{ ")
    for j in range(len(LKA_list)):
        if j<=len(LKA_list)-2:
            f2.write(str(LKA_list[j])+",")
        else:
            f2.write(str(LKA_list[j]))
    f2.write("};")
    f2.write("\n")
    f2.write("RSA= new double[]{ ")
    for j in range(len(RSA_list)):
        if j<=len(RSA_list)-2:
            f2.write(str(RSA_list[j])+",")
        else:
            f2.write(str(RSA_list[j]))
    f2.write("};")
    f2.write("\n")
    f2.write("LSA= new double[]{ ")
    for j in range(len(LSA_list)):
        if j<=len(LSA_list)-2:
            f2.write(str(LSA_list[j])+",")
        else:
            f2.write(str(LSA_list[j]))
    f2.write("};")
    f2.write("\n")
    

    f2.write("int test_image = 0;")
    f2.write("\n")
    f2.write("do{")
    f2.write("\n")
    f2.write("righthip = RHA[test_image];")
    f2.write("\n")
    f2.write("lefthip = LHA[test_image];")
    f2.write("\n")
    f2.write("rightelbow = REA[test_image];")
    f2.write("\n")
    f2.write("leftelbow = LEA[test_image];")
    f2.write("\n")
    f2.write("rightknee = RKA[test_image];")
    f2.write("\n")
    f2.write("leftknee = LKA[test_image];")
    f2.write("\n")
    f2.write("rightshoulder = RSA[test_image];")
    f2.write("\n")
    f2.write("leftshoulder = LSA[test_image];")
    f2.write("\n")
    for list_names in List_Names_coords:
        count = 0
        f2.write(str(list_names))
        f2.write(" = ")
        f2.write("A_")
        f2.write(str(list_names))
        f2.write("[test_image];")
        f2.write("\n")
    f2.close()


with open(fname2,"a") as f2:
    f2.write("\n")
    f2.write("int numPoses="+str(n_labels)+";")
    f2.write("\n")
    f2.write("beta = new double[numPoses]["+str(n_features)+"];")
    f2.close()

with open(fname2,"a") as f2:
    f2.write("\n")
    for i in range(len(list_label)):
        f2.write("    double[] "+list_label[i]+";")
        f2.write("\n")
    f2.close()

if flag_intercept == True:
    with open(fname2,"a") as f2:
        i_w = 0
        for i in range(len(list_label)):
            i_w = 0
            f2.write("    "+list_label[i]+" = new double[]{")
            for j in range(len(list_weight[0])):
                if j <= len(list_weight[0])-2:
                    f2.write(str(list_weight[i][i_w])+"d,")
                else:
                    f2.write(str(list_weight[i][i_w])+"d")
                i_w += 1
            f2.write("};")
            f2.write("\n")
            
else:
    with open(fname2,"a") as f2:
        i_w = 1
        for i in range(len(list_label)):
            
            f2.write("    "+list_label[i]+" = new double[]{")
            for j in range(len(list_weight[0])):
                if j <= len(list_weight[0])-2:
                    f2.write(str(list_weight[i][i_w])+"d,")
                else:
                    f2.write(str(list_weight[i][i_w])+"d")
                i_w += 1
            i_w = 1
            i_w += 1
            f2.write("};")
            f2.write("\n")


        #f2.write(weight[i_w])#weight of intercepts
with open(fname2,"a") as f2:
    f2.write("\n")    
    f2.write("//Densify the beta matrix")
    f2.write("\n")   
    f2.write("for (int i = 0; i <= "+str(list_label[0])+".length - 1; i++)")
    f2.write("\n")
    f2.write("{")
    f2.write("\n")
    for j in range(len(list_label)):
        f2.write("      beta["+str(j)+"][i] = "+str(list_label[j])+"[i];")
        f2.write("\n")
    f2.write("\n")
    f2.write("}")
    f2.write("\n")
    f2.close()

input_features = ["righthip", "lefthip", "rightelbow", "leftelbow", "rightknee", "leftknee", "rightshoulder", "leftshoulder"]
#input_features = ["x0","x1","x2","x3","x4","x5","x6","x7"]
Features_series_1 = list(itertools.combinations_with_replacement(input_features,1))
Features_series_2 = list(itertools.combinations_with_replacement(input_features,2))
Features = Features_series_1 + Features_series_2
#print(len(Features))
#print(Features[0])

with open(fname2,"a") as f2:
    f2.write("\n")
    f2.write("//Generate Feature")
    f2.write("\n")
    f2.write("Features= new double[]{ ")
    for j in range(len(Features)):
        if j<=n_input_features-1:
            f2.write(str(Features[j][0])+",")
        elif j<=n_features-3:
            f2.write(str(Features[j][0])+"*"+str(Features[j][1])+",")
        else:
            f2.write(str(Features[j][0]+"*"+str(Features[j][1])))
    f2.write("};")
    f2.write("\n")
    f2.close()






if flag_intercept == True:
    with open(fname2,"a") as f2:
        f2.write("\n")  
        f2.write("    yPo = new double[numPoses + 1];")
        f2.write("\n")
        for j in range(len(list_label)):
            f2.write("yPo["+str(j)+"] = beta["+str(j)+"][0];")
            f2.write("\n")
        f2.write("for (int i = 1; i <= "+str(list_label[0])+".length - 1; i++)")
        f2.write("\n")
        f2.write("{")
        f2.write("\n")
        for j in range(len(list_label)):
            f2.write("  yPo["+str(j)+"] = yPo["+str(j)+"] + beta["+str(j)+"][i] * Features[i-1];")
            f2.write("\n")
        f2.write("\n")
        f2.write("}")
        

else:
    with open(fname2,"a") as f2:
        f2.write("\n")  
        f2.write("    yPo = new double[numPoses+1];")
        f2.write("\n")
        for j in range(len(list_label)):
            f2.write("yPo["+str(j)+"] = 0")
            f2.write("\n")
        f2.write("for (int i = 0; i <= "+str(list_label[0])+".length - 1; i++)")
        f2.write("\n")
        f2.write("{")
        f2.write("\n")
        for j in range(len(list_labels)):
            f2.write("  yPo["+str(j)+"] = yPo["+str(j)+"] + beta["+str(j)+"][i] * Features[i];")
            f2.write("\n")
        f2.write("\n")
        f2.write("}")
with open(fname2,"a") as f2:
    f2.write("\n")
    f2.write("double[] zPo = new double[]{")
    for j in range(len(list_label)):
        if j <= len(list_label)-2:
            f2.write("yPo["+str(j)+"],")
        else:
            f2.write("yPo["+str(j)+"]};")
    f2.write("\n")
    f2.write("double[] numEr = new double[]{")
    for j in range(len(list_label)):
        if j <= len(list_label)-2:
            f2.write("0.0d"+",")
        else:
            f2.write("0.0d};")
    f2.write("\n")
    f2.write("double[] softMax = new double[]{")
    for j in range(len(list_label)):
        if j <= len(list_label)-2:
            f2.write("0.0d"+",")
        else:
            f2.write("0.0d};")
    f2.write("\n")

with open(fname4) as f1:
    with open(fname2,"a") as f2:
        f2.write("\n")
        for line in f1:
            index += 1
            f2.write(line)
    f2.close()
f1.close()

with open(fname2,"a") as f2:
    f2.write("\n")
    f2.write("    String pose=\"no pose\";")
    f2.write("\n")
    f2.write("switch (maxPos + 1) {")
    f2.write("\n")
    for j in range(len(list_label)):
        f2.write("      case "+str(j+1)+":")
        f2.write("\n")
        f2.write("          pose=\""+str(list_label[j])+"\";")
        f2.write("\n")
        #f2.write("          Log.d(\"Posename\", \"This is "+str(list_label[j]))
        #f2.write("\");")
        f2.write("\n")
        f2.write("          break;")
        f2.write("\n")
    f2.write("      default:")
    f2.write("\n")
    f2.write("          pose=\""+"BS"+"\";")
    #f2.write("           Log.d(\"Posename\", \"NA\");")
    f2.write("\n")
    f2.write("           break;")
    f2.write("\n")
    f2.write("}")
    f2.write("\n")
    f2.write("System.out.print(test_image);")
    f2.write("\n")
    f2.write("System.out.print(\":\");")
    f2.write("\n")
    f2.write("System.out.println(pose);")
    f2.write("\n")
    f2.write("test_image = test_image + 1;")
    f2.write("\n")
    f2.write("}while(test_image<=RHA.length-1);")
    f2.write("}}")
    f2.close()

