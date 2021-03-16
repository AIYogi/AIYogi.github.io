###WARNING: This code is not tested without intercepts
import os
import sys
import pandas as pd
import numpy as np
import itertools
path = os.getcwd()
print(path)
####USER INPUT: FILE NAME
fweight_csv = "Weights_of_Pose_Name.csv"
flabel_csv = "labels_of_Pose_Name.csv"
####Determine number of features
flag_intercept = True
file_weight = os.path.join(path,fweight_csv)
file_label = os.path.join(flabel_csv)
df_weight = pd.read_csv(file_weight, header=None)
df_label = pd.read_csv(file_label, header=None)
print(len(df_weight))
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
print(len(Features))
print(Features[0])

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
    f2.write("System.out.println(pose);")
    f2.write("\n")
    f2.write("}}")
    f2.close()

