import yaml
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
from EDA import get_parameter

# remove noise word and stop word.
def textpreprocessing(data):
    resumedata = data.lower()
    resumedata = re.sub("https+$"," ",resumedata)
    resumedata = re.sub("http+$"," ",resumedata)
    resumedata = re.sub('RT|cc', ' ', resumedata)  # remove RT and cc
    resumedata = re.sub('#S+', '', resumedata)  # remove hashtags
    resumedata = re.sub('@S+', '  ', resumedata)  # remove mentions
    resumedata = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[]^_`{|}~"""), ' ', resumedata)  # remove punctuations
    resumedata = re.sub(r'[^x00-x7f]',r' ', resumedata) 
    resumedata = re.sub("\s+\Z"," ", resumedata)
    return resumedata
    


def eda(path):
    param = get_parameter(path )
    data = pd.read_csv(param['data_source']['data'])
    figure = plt.figure(figsize=(20,20))
    sns.countplot(y='Category', data=data)  #plot the count plot with the help of seaborn
    plt.savefig(param['plot']['eda_count_plot'])   #save the count plot 
    data['cleaned_resume'] = data.Resume_str.apply(lambda x: textpreprocessing(x))
    data_path = param['eda']['processed_punc']
    processed_data =data.loc[:,['ID','Category','cleaned_resume']]
    processed_data.to_csv(data_path,index=False)


if __name__ == "__main__":
    path = 'params.yaml'
    eda(path)



