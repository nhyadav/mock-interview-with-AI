import numpy as numpy
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import yaml
import joblib
import warnings
import re
warnings.filterwarnings("ignore")


# get the required parameter from param
def get_parameter(path):
    with open(path,) as param:
        yaml_param = yaml.safe_load(param)
    return yaml_param


def remove_punction(data):
    resumedata = data.lower()
    resumedata = re.sub("https+$"," ",resumedata)
    resumedata = re.sub('RT|cc', ' ', resumedata)  # remove RT and cc
    resumedata = re.sub('#S+', '', resumedata)  # remove hashtags
    resumedata = re.sub('@S+', '  ', resumedata)  # remove mentions
    resumedata = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[]^_`{|}~"""), ' ', resumedata)  # remove punctuations
    resumedata = re.sub(r'[^x00-x7f]',r' ', resumedata) 
    resumedata = re.sub("\s+\Z"," ", resumedata)
    return resumedata


def exploar_data_analysis(path):
    param = get_parameter(path )
    data = pd.read_csv(param['data_source']['data'])
    figure = plt.figure(figsize=(20,20))
    sns.countplot(y='Category', data=data)  #plot the count plot with the help of seaborn
    plt.savefig(param['plot']['eda_count_plot'])   #save the count plot 
    data['cleaned_resume'] = data.Resume_str.apply(lambda x: remove_punction(x))
    data_path = param['eda']['processed_punc']
    processed_data = data.drop(['Resume_html'], axis=1)
    processed_data.to_csv(data_path,index=False)
    


if __name__ == "__main__":
    path = "params.yaml"
    exploar_data_analysis(path)