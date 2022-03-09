import pickle
from xgboost import XGBClassifier
from EDA import get_parameter
from sklearn.metrics import accuracy_score
from sklearn.multiclass import OneVsRestClassifier
import json


def model_training(model,features, targets, model_path):
    onevsmodel = OneVsRestClassifier(eval(model))
    # model_svc = eval(model+".fit(features, targets)")
    model_svc = onevsmodel.fit(features, targets)
    with open(model_path, 'wb') as res:
        pickle.dump(model_svc, res)
    

def model_test(model, test_data):
    data = model.predict(test_data)
    return data


def model_building(path):
    print("Starting...............................")
    params = get_parameter(path)
    model = params['model_building']['model_name']
    X_train_path = params['feature_engineering']['X_train']
    X_test_path = params['feature_engineering']['X_test']
    y_train_path = params['feature_engineering']['y_train']
    y_test_path = params['feature_engineering']['y_test']
    with open(X_train_path, 'rb') as res:
        X_train = pickle.load(res)
    with open(X_test_path, 'rb') as res:
        X_test = pickle.load(res)
    with open(y_train_path, 'rb') as res:
        y_train = pickle.load(res)
    with open(y_test_path, 'rb') as res:
        y_test = pickle.load(res)
    model_path = params['model_building']['model_path']
    model_svc = model_training(model, X_train, y_train, model_path)
    with open(model_path, 'rb') as res:
        model = pickle.load(res)
    train_prediction_path = params['model_building']['model_train_prediction']
    test_prediction_path = params['model_building']['model_test_prediction']
    train_pred = model_test(model, X_train)
    test_pred = model_test(model, X_test)
    with open(train_prediction_path, 'wb') as res:
        pickle.dump(train_pred, res)
    with open(test_prediction_path, 'wb') as res:
        pickle.dump(test_pred, res)
    training_accuracy = accuracy_score(y_train, train_pred)
    testing_accuracy = accuracy_score(y_test, test_pred)
    print("Training Accuracy:", training_accuracy)
    print("testing Accuracy:", testing_accuracy)
    report_path = params['model_evaluate']['evalution_matrics']
    with open(report_path, 'w') as res:
        score = {
            "Training Accuracy:": training_accuracy,
            "Testing Accuracy:": testing_accuracy
        }
        json.dump(score, res, indent=4)
    print("Stoping................................")

if __name__ == '__main__':
    path = "params.yaml"
    model_building(path)