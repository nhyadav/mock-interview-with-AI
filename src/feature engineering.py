import pickle
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from EDA import get_parameter
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split




def encode_target(target):
    lblencoder = LabelEncoder()
    return lblencoder.fit_transform(target)

def create_dictonary(data, path):
    data = data[['Category','target_data']].drop_duplicates(keep='first').sort_values('target_data')
    target_dict = {key:value for key, value in zip(data['target_data'], data['Category'])}
    with open(path, 'wb') as res:
        pickle.dump(target_dict, res)

def train_test_split_data(features, targets, test_size):
    X_train, X_test, y_train, y_test = train_test_split(features, targets, test_size=test_size, random_state=42, shuffle=True, stratify=targets)
    return [X_train, X_test, y_train, y_test]



def vectorize_data(x_train, x_test,tfidf_path):
    tfidf = TfidfVectorizer(stop_words='english', max_features=2000)
    X_train = tfidf.fit_transform(x_train)
    X_test = tfidf.transform(x_test)
    with open(tfidf_path, 'wb') as res:
        pickle.dump(tfidf, res)
    return [X_train, X_test]


def feature_engineering(path):
    print("start.............................")
    params = get_parameter(path)
    data_path = params['eda']['processed_data']
    data = pd.read_csv(data_path)
    data.dropna(inplace=True)
    features_data = data['lemmatize_data'].values
    target_dict_path = params['feature_engineering']['target_dict']
    data['target_data'] = encode_target(data['Category'])
    target = data['target_data'].values
    create_dictonary(data, target_dict_path)
    test_size_path = params['feature_engineering']['test_size']
    X_train_path = params['feature_engineering']['X_train']
    X_test_path = params['feature_engineering']['X_test']
    y_train_path = params['feature_engineering']['y_train']
    y_test_path = params['feature_engineering']['y_test']
    X_train, X_test, y_train, y_test = train_test_split_data(features_data, target, test_size_path)
    tfidf_path = params['feature_engineering']['tfidf']
    X_train_vectorized, X_test_vectorized = vectorize_data(X_train,X_test, tfidf_path)
    with open(X_train_path, 'wb') as res:
        pickle.dump(X_train_vectorized, res)
    with open(X_test_path, 'wb') as res:
        pickle.dump(X_test_vectorized, res)
    with open(y_train_path, 'wb') as res:
        pickle.dump(y_train, res)
    with open(y_test_path, 'wb') as res:
        pickle.dump(y_test, res)
    print("Done.............................")


if __name__ == '__main__':
    path = "params.yaml"
    feature_engineering(path)
