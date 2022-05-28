import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import seaborn as sns



diabetes = pd.read_csv('diabetes.csv')
diabetes.rename(columns={'DiabetesPedigreeFunction':'Pedigree','BloodPressure':'BP','SkinThickness':'Skin'},inplace=True)
corr = diabetes.corr()
print(corr)
heatmap = sns.heatmap(corr, 
         xticklabels=corr.columns, 
         yticklabels=corr.columns)
plt.xlabel
plt.show()

average_glucose = diabetes["Glucose"].mean()
average_insulin = diabetes['Insulin'].mean()
average_dpf = diabetes['Pedigree'].mean()

print(f'Average glucose : {average_glucose}')
print(f'Average insulin : {average_insulin}')
print(f'Average DPF : {average_dpf}')

#Eliminating first row

X = diabetes.loc[:,diabetes.columns != 'Outcome']
X_train, X_Test, y_train,y_test = train_test_split(X,diabetes['Outcome'],stratify=diabetes['Outcome'],test_size=0.28,random_state=66)
#X_train,X_Test,y_train,y_test=train_test_split(X,y,test_size=0.28,random_state=0)


from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression(max_iter=1000)
logreg.fit(X_train,y_train)
print(f'Accuracy of Logistic Regression classifier on training set:{logreg.score(X_train, y_train)}')
print(f'Accuracy of Logistic Regression  classifier on test set:{logreg.score(X_Test, y_test)}')




from sklearn.neighbors import KNeighborsClassifier

training_accuracy = []
test_accuracy = []

#trying n neighbors from 1 to 10
neighbors = range(1,10)

for n_neighbors in neighbors:
    
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(X_train,y_train)
    
    training_accuracy.append(knn.score(X_train,y_train))
    test_accuracy.append(knn.score(X_Test,y_test))

plt.plot(neighbors, training_accuracy, label="training accuracy")
plt.plot(neighbors, test_accuracy, label="test accuracy")
plt.ylabel("Accuracy")
plt.xlabel("n_neighbors")
plt.legend()
plt.savefig('knn_compare_model')
plt.show()

knn = KNeighborsClassifier(n_neighbors=9)
knn.fit(X_train,y_train)
print(f'Accuracy of K-NN classifier on training set:{knn.score(X_train, y_train)}')
print(f'Accuracy of K-NN classifier on test set:{knn.score(X_Test, y_test)}')

from sklearn.tree import DecisionTreeClassifier
tree = DecisionTreeClassifier(random_state=0)
tree.fit(X_train, y_train)
print(f'Accuracy of Decision Tree Classifier on training set:{tree.score(X_train, y_train)}')
print(f'Accuracy of Decision Tree Classifier on test set:{tree.score(X_Test, y_test)}')

dt_training_accuracy = tree.score(X_train, y_train)
dt_test_accuracy = tree.score(X_Test, y_test)




from sklearn.ensemble import RandomForestClassifier
forest = RandomForestClassifier(n_estimators=100, random_state=0)
forest.fit(X_train, y_train)
print(f'Accuracy of Random Forest Classifier on training set:{forest.score(X_train, y_train)}')
print(f'Accuracy of Random Forest Classifier on test set:{forest.score(X_Test, y_test)}')

from sklearn.tree import plot_tree

fig = plt.figure(figsize=(15, 10))
plot_tree(forest.estimators_[0], 
          feature_names=diabetes.columns,
         
          filled=True, impurity=True, 
          rounded=True)
plt.show()








from sklearn.ensemble import GradientBoostingClassifier
gb = GradientBoostingClassifier(random_state=0)
gb.fit(X_train, y_train)

print(f'Accuracy of Random Forest Classifier on training set:{gb.score(X_train, y_train)}')
print(f'Accuracy of Random Forest Classifier on test set:{gb.score(X_Test, y_test)}')

from sklearn import linear_model
lr = linear_model.LinearRegression()


lr.fit(X_train, y_train)
# Predict
yhat = lr.predict(X_Test)


# Calculate error
mse_ols = np.mean((y_test - yhat) ** 2)
mse_ols2 = np.dot((y_test - yhat).T, (y_test - yhat)) / y_test.shape[0]
mae_ols = np.mean(np.fabs(y_test - yhat))
print("Mean y_test: %f" % np.mean(y_test))
print("MSE1: %f" % mse_ols)
print("MSE2: %f" % mse_ols2)
print("RMSE: %f" % (np.sqrt(mse_ols)))
print("MAE: %f" % (mae_ols))


# Vector w=[w_1, w_2, ..., w_p]
print(lr.coef_)

print("Plot prediction vs actual, for last feature only")
plt.plot(X_Test['BMI'], y_test, 'bo')
plt.plot(X_Test["BMI"], yhat, 'rx')
plt.grid()
plt.show()


plt.plot(X_Test['Glucose'], y_test, 'bo')
plt.plot(X_Test["Glucose"], yhat, 'rx')
plt.grid()
plt.show()