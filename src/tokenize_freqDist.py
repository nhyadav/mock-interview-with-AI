import nltk
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from EDA import get_parameter
from nltk import FreqDist
import warnings
warnings.filterwarnings('ignore')


token = nltk.tokenize.word_tokenize

def tokenize_data(x):
    data = token(x)
    return data
    # for i in range(len(data)):
    #     data_text = data['Resume_str'][i] 
    #     if data_text:
    #         text = token(data_text)
    #     else:
    #         print('The text to be tokenized is a None type. Defaulting to blank string.')
    #         text = ''
    #     data['Resume_str'][i] = text
    
    # return data



def freqdist_data(data,path, title):
    fig = plt.figure(figsize=(20,10))
    freq_dist = FreqDist(data)
    plt.ion()
    freq_dist.plot(50,title=title,cumulative=False)
    plt.savefig(path)
    plt.ioff()
    plt.show()


def tokenize_freqdist_data(path):
    param = get_parameter(path)
    data = pd.read_csv(param['eda']['processed_lemmatized'])
    data.replace({'INFORMATION-TECHNOLOGY':'INFORMATION_TECHNOLOGY','BUSINESS-DEVELOPMENT':'BUSINESS_DEVELOPMENT',
                  'DIGITAL-MEDIA':'DIGITAL_MEDIA','PUBLIC-RELATIONS':'PUBLIC_RELATIONS'},inplace=True)
    data.dropna(axis=0,inplace=True)
    # print(data.isnull().sum())
    # print(data.columns)
    data['tokenize_data'] = data.lemmatize_data.apply(lambda x:tokenize_data(x))
    data.to_csv(param['eda']['processed_tokenized'], index=False)
    
    # split the individual resume category data
    # load_data = pd.read_csv(param['eda']['processed_tokenized'])
    resume_categories = param['base']['resume_category']
    for category_class in resume_categories:
        data = data.loc[(data.Category==category_class)]
        print(data['tokenize_data'])
        raw_text = []
        for i in range(len(data)):
            raw_text = raw_text+data['tokenize_data'][i]
        print(raw_text)
        joblib.dump(raw_text,param['eda']['data_'+category_class])
    
    #################################################################
    ##########plot the frequency distribution########################
    # for category in resume_categories:
        # t_data = joblib.load(param['eda']['data_'+category])
        # path = param['plot']['eda_freq_dist_'+category]
        # freqdist_data(t_data,path,category)

if __name__ == "__main__":
    path = 'params.yaml'
    tokenize_freqdist_data(path)

    
    







