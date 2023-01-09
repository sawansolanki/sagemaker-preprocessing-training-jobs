import os

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib

if __name__ == "__main__":
    training_data_directory = "/opt/ml/input/data/train"
    train_features_data = os.path.join(training_data_directory, "train_features.csv")
    train_labels_data = os.path.join(training_data_directory, "train_labels.csv")
    print("Reading input data")
    X_train = pd.read_csv(train_features_data, header=None)
    y_train = pd.read_csv(train_labels_data, header=None)
    

    model = LogisticRegression(class_weight="balanced", solver="lbfgs")
    print("Training LR model")
    model.fit(X_train, y_train)
    model_output_directory = os.path.join("/opt/ml/model", "model.joblib")
    print("Saving model to {}".format(model_output_directory))
    joblib.dump(model, model_output_directory)
    
    print("Loading test input data")
    
    test_features_data = os.path.join("/opt/ml/input/data/test", "test_features.csv")
    test_labels_data = os.path.join("/opt/ml/input/data/test", "test_labels.csv")
    X_test = pd.read_csv(test_features_data, header=None)
    y_test = pd.read_csv(test_labels_data, header=None)
    predictions = model.predict(X_test)
    print("Creating classification evaluation report")
    report_dict = classification_report(y_test, predictions, output_dict=True)
    report_dict["accuracy"] = accuracy_score(y_test, predictions)
    report_dict["roc_auc"] = roc_auc_score(y_test, predictions)

    print("Classification report:\n{}".format(report_dict))
    
    with open('details.txt', 'w') as outfile:
    outfile.write(report_dict)
