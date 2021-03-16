import os
import sys
import pandas as pd
import numpy as np
path = os.getcwd()
print(path)
####USER INPUT: FILE NAME (s)
fname_csv = "modelclasssubclass125.csv"
fname1_csv = "modelclass125.csv"
####USER INPUT: NUMBER OF FEATURES
# Use 8 for angles
#Use 5 for PCA
n_features = 8
#####USER INPUT: USING INTERCEPT
#Input True if you want to use intercept else False
flag_intercept = True
flag_intercept_1 = True

file_csv = os.path.join(path,fname_csv)
df = pd.read_csv(file_csv)

file_csv_1 = os.path.join(path,fname1_csv)
df_1 = pd.read_csv(file_csv_1)

#######Reading Labels#####################
label_list = df["y.level"].values.tolist()
#print(label_list)#[:2])
label_array = np.array(label_list)
label_unique_array = np.unique(label_array)
list_labels = label_unique_array.tolist()
#print(list_labels)
n_labels = len(list_labels)

label_list_1 = df_1["y.level"].values.tolist()
#print(label_list)#[:2])
label_array_1 = np.array(label_list_1)
label_unique_array_1 = np.unique(label_array_1)
list_labels_1 = label_unique_array_1.tolist()
#print(list_labels)
n_labels_1 = len(list_labels_1)

#######Reading Features#####################
feature_list = df["term"].values.tolist()
#print(feature_list)#[:2])
feature_array = np.array(feature_list)
feature_unique_array = np.unique(feature_array)
list_features = feature_unique_array.tolist()
#print(list_features)
if flag_intercept == True:
    n_features = len(list_features)
else:
    list_features.pop(0)
    n_features = len(list_features)
print(n_features)
print(list_features)    
#print(len(df.index))
if flag_intercept == True:
    if n_labels * n_features == len(df.index) :
        print("Checked") 
    else: 
        print("Check inputs")
else:
    if n_labels * (n_features+1) == len(df.index) :
        print("Checked") 
    else: 
        print("Check inputs")

feature_list_1 = df_1["term"].values.tolist()
#print(feature_list)#[:2])
feature_array_1 = np.array(feature_list_1)
feature_unique_array_1 = np.unique(feature_array_1)
list_features_1 = feature_unique_array_1.tolist()
#print(list_features)
if flag_intercept_1 == True:
    n_features_1 = len(list_features_1)
else:
    list_features_1.pop(0)
    n_features_1 = len(list_features_1)
print(n_features_1)
print(list_features_1)    
#print(len(df.index))
if flag_intercept == True:
    if n_labels_1 * n_features_1 == len(df_1.index) :
        print("Checked") 
    else: 
        print("Check inputs")
else:
    if n_labels_1 * (n_features_1+1) == len(df_1.index) :
        print("Checked") 
    else: 
        print("Check inputs")


#######Reading Weights#####################
weight_list = df["estimate"].values.tolist()
print(weight_list)

weight_list_1 = df_1["estimate"].values.tolist()
print(weight_list_1)


file = "top_constant_1.txt"
fname1 = os.path.join(path,file)
file3 = "bottom_constant.txt"
fname3 = os.path.join(path,file3)
file4 = "between_constant.txt"
fname4 = os.path.join(path,file4)
file4_1 = "between_constant_1.txt"
fname4_1 = os.path.join(path,file4_1)
fname_gen = "PoseGraphic_1.java"
fname2 = os.path.join(path,fname_gen)
gen_file = open(fname2)

index = 0
with open(fname1) as f1:
    with open(fname2,"w") as f2:
        for line in f1:
            index += 1
            f2.write(line)
    f2.close()
f1.close()


with open(fname2,"a") as f2:
    f2.write("\n")
    f2.write("int numPoses="+str(n_labels)+";")
    f2.write("\n")
    f2.write("int numPoses_1="+str(n_labels_1)+";")
    f2.write("\n")
    
    f2.write("beta = new double[numPoses]["+str(n_features)+"];")
    f2.write("\n")
    f2.write("beta_1 = new double[numPoses_1]["+str(n_features_1)+"];")
    f2.close()
    
    f2.close()

with open(fname2,"a") as f2:
    f2.write("\n")
    for i in range(len(list_labels)):
        f2.write("    double[] "+list_labels[i]+";")
        f2.write("\n")
    f2.close()
with open(fname2,"a") as f2:
    f2.write("\n")
    for i in range(len(list_labels_1)):
        f2.write("    double[] "+list_labels_1[i]+";")
        f2.write("\n")
    f2.close()

if flag_intercept == True:
    with open(fname2,"a") as f2:
        i_w = 0
        for i in range(len(list_labels)):
            f2.write("    "+list_labels[i]+" = new double[]{")
            for j in range(len(list_features)):
                if j <= len(list_features)-2:
                    f2.write(str(weight_list[i_w])+"d,")
                else:
                    f2.write(str(weight_list[i_w])+"d")
                i_w += 1
            f2.write("};")
            f2.write("\n")
else:
    with open(fname2,"a") as f2:
        i_w = 1
        for i in range(len(list_labels)):
            f2.write("    "+list_labels[i]+" = new double[]{")
            for j in range(len(list_features)):
                if j <= len(list_features)-2:
                    f2.write(str(weight_list[i_w])+"d,")
                else:
                    f2.write(str(weight_list[i_w])+"d")
                i_w += 1
            i_w += 1
            f2.write("};")
            f2.write("\n")

if flag_intercept_1 == True:
    with open(fname2,"a") as f2:
        i_w = 0
        for i in range(len(list_labels_1)):
            f2.write("    "+list_labels_1[i]+" = new double[]{")
            for j in range(len(list_features_1)):
                if j <= len(list_features_1)-2:
                    f2.write(str(weight_list_1[i_w])+"d,")
                else:
                    f2.write(str(weight_list_1[i_w])+"d")
                i_w += 1
            f2.write("};")
            f2.write("\n")
else:
    with open(fname2,"a") as f2:
        i_w = 1
        for i in range(len(list_labels_1)):
            f2.write("    "+list_labels_1[i]+" = new double[]{")
            for j in range(len(list_features_1)):
                if j <= len(list_features_1)-2:
                    f2.write(str(weight_list_1[i_w])+"d,")
                else:
                    f2.write(str(weight_list_1[i_w])+"d")
                i_w += 1
            i_w += 1
            f2.write("};")
            f2.write("\n")


        #f2.write(weight[i_w])#weight of intercepts
with open(fname2,"a") as f2:
    f2.write("\n")    
    f2.write("//Densify the beta matrix")
    f2.write("\n")   
    f2.write("for (int i = 0; i <= "+str(list_labels[0])+".length - 1; i++)")
    f2.write("\n")
    f2.write("{")
    f2.write("\n")
    for j in range(len(list_labels)):
        f2.write("      beta["+str(j)+"][i] = "+str(list_labels[j])+"[i];")
        f2.write("\n")
    f2.write("\n")
    f2.write("}")
    f2.write("\n")
    f2.close()
###REPEAT
with open(fname2,"a") as f2:
    f2.write("\n")    
    f2.write("//Densify the beta_1 matrix")
    f2.write("\n")   
    f2.write("for (int i = 0; i <= "+str(list_labels_1[0])+".length - 1; i++)")
    f2.write("\n")
    f2.write("{")
    f2.write("\n")
    for j in range(len(list_labels_1)):
        f2.write("      beta_1["+str(j)+"][i] = "+str(list_labels_1[j])+"[i];")
        f2.write("\n")
    f2.write("\n")
    f2.write("}")
    f2.write("\n")
    f2.close()

if flag_intercept == True:
    with open(fname2,"a") as f2:
        f2.write("\n")  
        f2.write("    yPo = new double[numPoses + 1];")
        f2.write("\n")
        for j in range(len(list_labels)):
            f2.write("yPo["+str(j)+"] = beta["+str(j)+"][0];")
            f2.write("\n")
        f2.write("for (int i = 1; i <= "+str(list_labels[0])+".length - 1; i++)")
        f2.write("\n")
        f2.write("{")
        f2.write("\n")
        for j in range(len(list_labels)):
            f2.write("  yPo["+str(j)+"] = yPo["+str(j)+"] + beta["+str(j)+"][i] * Features[i-1];")
            f2.write("\n")
        f2.write("\n")
        f2.write("}")
        

else:
    with open(fname2,"a") as f2:
        f2.write("\n")  
        f2.write("    yPo = new double[numPoses+1];")
        f2.write("\n")
        for j in range(len(list_labels)):
            f2.write("yPo["+str(j)+"] = 0")
            f2.write("\n")
        f2.write("for (int i = 0; i <= "+str(list_labels[0])+".length - 1; i++)")
        f2.write("\n")
        f2.write("{")
        f2.write("\n")
        for j in range(len(list_labels)):
            f2.write("  yPo["+str(j)+"] = yPo["+str(j)+"] + beta["+str(j)+"][i] * Features[i];")
            f2.write("\n")
        f2.write("\n")
        f2.write("}")
###REPEAT yPo
if flag_intercept_1 == True:
    with open(fname2,"a") as f2:
        f2.write("\n")  
        f2.write("    yPo_1 = new double[numPoses_1 + 1];")
        f2.write("\n")
        for j in range(len(list_labels_1)):
            f2.write("yPo_1["+str(j)+"] = beta_1["+str(j)+"][0];")
            f2.write("\n")
        f2.write("for (int i = 1; i <= "+str(list_labels_1[0])+".length - 1; i++)")
        f2.write("\n")
        f2.write("{")
        f2.write("\n")
        for j in range(len(list_labels)):
            f2.write("  yPo_1["+str(j)+"] = yPo_1["+str(j)+"] + beta_1["+str(j)+"][i] * Features[i-1];")
            f2.write("\n")
        f2.write("\n")
        f2.write("}")
        

else:
    with open(fname2,"a") as f2:
        f2.write("\n")  
        f2.write("    yPo_1 = new double[numPoses_1+1];")
        f2.write("\n")
        for j in range(len(list_labels)):
            f2.write("yPo_1["+str(j)+"] = 0")
            f2.write("\n")
        f2.write("for (int i = 0; i <= "+str(list_labels_1[0])+".length - 1; i++)")
        f2.write("\n")
        f2.write("{")
        f2.write("\n")
        for j in range(len(list_labels_1)):
            f2.write("  yPo_1["+str(j)+"] = yPo_1["+str(j)+"] + beta_1["+str(j)+"][i] * Features[i];")
            f2.write("\n")
        f2.write("\n")
        f2.write("}")



with open(fname2,"a") as f2:
    f2.write("\n")
    f2.write("double[] zPo = new double[]{")
    for j in range(len(list_labels)):
        if j <= len(list_labels)-2:
            f2.write("yPo["+str(j)+"],")
        else:
            f2.write("yPo["+str(j)+"]};")
    f2.write("\n")
    f2.write("double[] numEr = new double[]{")
    for j in range(len(list_labels)):
        if j <= len(list_labels)-2:
            f2.write("0.0d"+",")
        else:
            f2.write("0.0d};")
    f2.write("\n")
    f2.write("double[] softMax = new double[]{")
    for j in range(len(list_labels)):
        if j <= len(list_labels)-2:
            f2.write("0.0d"+",")
        else:
            f2.write("0.0d};")
    f2.write("\n")

###REPEAT declarations
with open(fname2,"a") as f2:
    f2.write("\n")
    f2.write("double[] zPo_1 = new double[]{")
    for j in range(len(list_labels_1)):
        if j <= len(list_labels_1)-2:
            f2.write("yPo_1["+str(j)+"],")
        else:
            f2.write("yPo_1["+str(j)+"]};")
    f2.write("\n")
    f2.write("double[] numEr_1 = new double[]{")
    for j in range(len(list_labels_1)):
        if j <= len(list_labels_1)-2:
            f2.write("0.0d"+",")
        else:
            f2.write("0.0d};")
    f2.write("\n")
    f2.write("double[] softMax_1 = new double[]{")
    for j in range(len(list_labels_1)):
        if j <= len(list_labels_1)-2:
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

###REPEAT between constant
with open(fname4_1) as f1:
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
    for j in range(len(list_labels)):
        f2.write("      case "+str(j+1)+":")
        f2.write("\n")
        f2.write("          pose=\""+str(list_labels[j])+"\";")
        f2.write("\n")
        f2.write("          Log.d(\"Posename\", \"This is "+str(list_labels[j]))
        f2.write("\");")
        f2.write("\n")
        f2.write("          break;")
        f2.write("\n")
    f2.write("      default:")
    f2.write("\n")
    f2.write("           Log.d(\"Posename\", \"NA\");")
    f2.write("\n")
    f2.write("           break;")
    f2.write("\n")
    f2.write("}")

###REPEAT switch
with open(fname2,"a") as f2:
    f2.write("\n")
    f2.write("    String pose_1=\"no pose\";")
    f2.write("\n")
    f2.write("switch (maxPos_1 + 1) {")
    f2.write("\n")
    for j in range(len(list_labels_1)):
        f2.write("      case "+str(j+1)+":")
        f2.write("\n")
        f2.write("          pose_1=\""+str(list_labels_1[j])+"\";")
        f2.write("\n")
        f2.write("          Log.d(\"Posename_1\", \"This is "+str(list_labels_1[j]))
        f2.write("\");")
        f2.write("\n")
        f2.write("          break;")
        f2.write("\n")
    f2.write("      default:")
    f2.write("\n")
    f2.write("           Log.d(\"Posename_1\", \"NA\");")
    f2.write("\n")
    f2.write("           break;")
    f2.write("\n")
    f2.write("}")
    
with open(fname3) as f1:
    with open(fname2,"a") as f2:
        f2.write("\n")
        for line in f1:
            index += 1
            f2.write(line)
    f2.close()
f1.close()


'''
f2.write("Features = new double[]{")
if flag_intercept == True:
    #if index > 130:
    for i in range(len(list_features)):
        if i <= len(list_features)-2:
            if list_features[i] == "(Intercept)" or i==0:
                f2.write("INTERCEPT"+",")
            else:
                f2.write(list_features[i]+", ")
        else:
            f2.write(list_features[i])#righthip, lefthip, rightelbow, leftelbow, rightknee, leftknee, rightshoulder, leftshoulder};)
    f2.write("};")
else:
    for i in range(len(list_features)-1):
        if i <= len(list_features)-3:
            f2.write(list_features[i+1]+", ")
        else:
            f2.write(list_features[i+1])#righthip, lefthip, rightelbow, leftelbow, rightknee, leftknee, rightshoulder, leftshoulder};)
    f2.write("};")
    '''





