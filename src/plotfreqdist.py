import pandas as pd
import joblib
import pickle
import nltk
import matplotlib.pyplot as plt
from EDA import get_parameter
import warnings
warnings.filterwarnings('ignore')
from nltk import FreqDist
token = nltk.tokenize.word_tokenize
# text_daat = joblib.

# total_resume_category = text_data['Category'].unique() 
# text_data.replace({'INFORMATION-TECHNOLOGY':'INFORMATION_TECHNOLOGY','BUSINESS-DEVELOPMENT':'BUSINESS_DEVELOPMENT',
#                   'DIGITAL-MEDIA':'DIGITAL_MEDIA','PUBLIC-RELATIONS':'PUBLIC_RELATIONS'},inplace=True)




# for category_class in total_resume_category:
#     data = text_data.loc[(text_data.Category==category_class)]
#     raw_text = []
#     for i in range(len(data)):
#         raw_text = raw_text+text_data['tokenize_data'][i]
#     globals()[category_class] = raw_text
    
def tokenize_data(x):
    data = token(x)
    return data


#plot the each category resume frequency data.
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
    data['tokenize_data'] = data.lemmatize_data.apply(lambda x:tokenize_data(x))
    data.to_csv(param['eda']['processed_tokenized'], index=False)
    text_data = pd.read_csv(param['eda']['processed_tokenized'])
    resume_category = text_data['Category'].unique()
    for category_class in resume_category:
        text = text_data.loc[(text_data.Category==category_class)]
        raw_text = []
        lt_data = list(text['tokenize_data'])
        for i in range(len(text)):
            raw_text.extend(lt_data[i])
        joblib.dump(raw_text,param['eda']['data_'+category_class])
    for category in resume_category:
        t_data = joblib.load(param['eda']['data_'+category])
        path = param['plot']['eda_freq_dist_'+category]
        freqdist_data(t_data,path,category)
    

if __name__ == "__main__":
    path = "params.yaml"
    tokenize_freqdist_data(path)

