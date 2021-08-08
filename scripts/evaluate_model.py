import numpy as np
import pandas as pd
from sklearn.model_selection import RepeatedStratifiedKFold, cross_validate
from sklearn.metrics import accuracy_score, classification_report, plot_confusion_matrix
import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')  

def train_evaluate_classifier(clf, x, y, x_train, y_train, x_test, y_test, skip_fit = False):
    np.random.seed(73246)
    cv = RepeatedStratifiedKFold(n_splits=5, n_repeats=10)
    if not skip_fit:
        clf.fit(x_train, y_train)
    results = cross_validate(clf, x, y, cv=cv, scoring='f1', return_train_score=True, n_jobs=-1)
    y_predict = clf.predict(x_test)
    auc_medio = np.mean(results['test_score'])
    print(f'F1: {auc_medio}')
    print(format_classification_report(y_test, y_predict))
    plot_confusion_matrix(clf, x_test, y_test)
    return clf

def format_classification_report(test, predict):
    df_cr = pd.DataFrame(classification_report(test, predict, output_dict=True)).T
    df_cr['precision']['accuracy'] = ''
    df_cr['recall']['accuracy'] = ''
    df_cr['support']['accuracy'] = df_cr['support']['macro avg']
    df_cr['support'] = df_cr['support'].astype('int32')
    return df_cr