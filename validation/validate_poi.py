#!/usr/bin/python


"""
    starter code for the validation mini-project
    the first step toward building your POI identifier!

    start by loading/formatting the data

    after that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, classification_report

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### it's all yours from here forward!
from sklearn import cross_validation

train_features, test_features, train_labels, test_labels = cross_validation.train_test_split(features, labels, test_size =0.3, random_state=42)

from sklearn.tree import DecisionTreeClassifier


clf = DecisionTreeClassifier()
clf.fit(train_features,train_labels)
pred = clf.predict(test_features)

print "accuracy::",accuracy_score(test_labels,pred)


kf = cross_validation.KFold(len(features), n_folds = 10)

for train_index, test_index in kf:
        train_features = [features[ii] for ii in train_index]
        test_features = [features[ii] for ii in test_index]
        train_labels = [labels[ii] for ii in train_index]
        test_labels = [labels[ii] for ii in test_index]
        
        clf = DecisionTreeClassifier()
        clf.fit(train_features,train_labels)
        pred = clf.predict(test_features)

#        print "Accuracy::",accuracy_score(test_labels, pred)    
#        print "Confusion matrix::", confusion_matrix(test_labels, pred)
#        print "Classification Report::",classification_report(test_labels, pred)
        print "Precision::",precision_score(test_labels, pred)
        print "Recall::",recall_score(test_labels, pred)
