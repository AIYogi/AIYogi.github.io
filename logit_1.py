import pandas as pd
import os
from sklearn.linear_model import LogisticRegression
from collections import Counter
from sklearn.datasets import make_classification
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

home_path = os.getcwd()
#print("home",home_path)
file1 = "Combined_sorted_datasets_all"
folder_name = "try_data"
filename = file1+".csv"
fname = os.path.join(home_path,folder_name,filename)
data=pd.read_csv(fname)
filename_test = "test.csv"
fname_test = os.path.join(home_path,folder_name,filename_test)

#print(data['Pose Name'])
Labels = data['Pose Name']
Features = data[['RHA',	'LHA',	'REA',	'LEA',	'RKA',	'LKA',	'RSA',	'LSA'
]]
Features_train, Features_test,Labels_train, Labels_test = train_test_split(Features, Labels, test_size=0.33)
#print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
#Features_test = pd.read_csv(fname_test)
lr = LogisticRegression(solver='liblinear')
lr.fit(Features_train,Labels_train)
#print(lr.predict(Features_test))
Labels_predict = lr.predict(Features_test)
#score = lr.score(Labels_test_predict,Labels_test)
#print(score)
from sklearn import metrics
cnf_matrix = metrics.confusion_matrix(Labels_test, Labels_predict)
print(cnf_matrix)
class_names=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24] # name  of classes
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
# create heatmap
sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()
print("Accuracy:",metrics.accuracy_score(Labels_test, Labels_predict))

#clf = LogisticRegression(fit_intercept=True, C = 1e15)
#clf.fit(features,labels)

#print (clf.intercept_, clf.coef_)
#print (weights)
