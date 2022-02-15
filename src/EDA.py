import numpy as np
import pandas as pd
import os
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt
import seaborn as sns
import yaml
import joblib
import warnings
import re
warnings.filterwarnings("ignore")
from wordcloud import WordCloud

token = nltk.tokenize.word_tokenize
lemmatizer = WordNetLemmatizer()
# for other theme, please run: mpl.pyplot.style.available
PLOT_PALETTE = 'tableau-colorblind10'
# for other color map, please run: mpl.pyplot.colormaps()
WORDCLOUD_COLOR_MAP = 'tab10_r'




def wordcloud(df):
    txt = ' '.join(txt for txt in df['lemmatize_data'])
    wordcloud = WordCloud(
        height=2000,
        width=4000,
        colormap=WORDCLOUD_COLOR_MAP
    ).generate(txt)
    return wordcloud


def wordfreq(df):
    count = df['lemmatize_data'].str.split(expand=True).stack().value_counts().reset_index()
    count.columns = ['Word', 'Frequency']
    return count.head(30)


# get the required parameter from param
def get_parameter(path):
    with open(path,) as param:
        yaml_param = yaml.safe_load(param)
    return yaml_param


def remove_punction(data):
    resumedata = data.lower()
    cleanr = re.compile('<.*?>')
    resumedata = re.sub(cleanr, ' ', resumedata)
    resumedata = re.sub(r"http\S+"," ",resumedata)
    resumedata = re.sub(r"www\S+"," ",resumedata)
    resumedata = re.sub(r'[^A-Za-z]',' ', resumedata)
    # resumedata = re.sub('[0-9]+', ' ', resumedata)
    # resumedata = re.sub("http+$"," ",resumedata)
    # resumedata = re.sub('RT|cc', ' ', resumedata)  # remove RT and cc
    # resumedata = re.sub('#S+', ' ', resumedata)  # remove hashtags
    # resumedata = re.sub('@S+', ' ', resumedata)  # remove mentions
    # resumedata = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[]^_`{|}~"""), ' ', resumedata)  # remove punctuations
    # resumedata = re.sub(r'[^x00-x7f]', ' ', resumedata) 
    resumedata = re.sub("\s+\Z"," ", resumedata)
    return resumedata



def remove_stopwords(x):
    data = x.split()
    data = [lemmatizer.lemmatize(word) for word in data if word not in set(stopwords.words('english'))]
    return ' '.join(data)

def tokenize_data(x):
    data = token(x)
    return data

def exploar_data_analysis(path):
    param = get_parameter(path )
    data = pd.read_csv(param['data_source']['data'])
    figure = plt.figure(figsize=(20,20))
    sns.countplot(y='Category', data=data)  #plot the count plot with the help of seaborn
    plt.savefig(param['plot']['eda_count_plot'])   #save the count plot 
    data['cleaned_resume'] = data.Resume_str.apply(lambda x: remove_punction(x))
    print("remove unusual text done.......")

    data['lemmatize_data'] = data.cleaned_resume.apply(lambda x:remove_stopwords(x))
    print("Remove stopword done...............")
    data['tokenize_data'] = data.lemmatize_data.apply(lambda x:tokenize_data(x))
    print("tokenize done................")
    processed_data = data.drop(['Resume_html'], axis=1)
    
    # data.to_csv(param['eda']['processed_data'], index=False)
    #################wordcloud###############################
    data.replace({'INFORMATION-TECHNOLOGY':'INFORMATION_TECHNOLOGY','BUSINESS-DEVELOPMENT':'BUSINESS_DEVELOPMENT',
                  'DIGITAL-MEDIA':'DIGITAL_MEDIA','PUBLIC-RELATIONS':'PUBLIC_RELATIONS'},inplace=True)
    categories = param['base']['resume_category']
    df_categories = [data[data['Category'] == category].loc[:, ['lemmatize_data', 'Category']] for category in categories]
    processed_data.to_csv(param['eda']['processed_data'], index=False)
    
    ###################seperate each categories resume
    dt_categories = [data[data['Category'] == category].loc[:, ['tokenize_data', 'Category','lemmatize_data','Resume_str']] for category in categories]
    for i,cat in enumerate(categories):
        dt_categories[i].to_csv(param['eda']['data_'+cat])
    ###################################################
    # plt.figure(figsize=(32, 28))
    for i, category in enumerate(categories):
        wc = wordcloud(df_categories[i])
        # plt.subplot(6, 4, i + 1).set_title(category)
        plt.title(category+" wordcloud")
        plt.imshow(wc)
        plt.axis('off')
        plt.plot()
        plt.savefig(param['plot']['eda_wordcloud_'+category])
        plt.show()
    plt.close()

    #####################wordfrequency##########################
    # fig = plt.figure(figsize=(32, 64))
    for i, category in enumerate(categories):
        wf = wordfreq(df_categories[i])
        # fig.add_subplot(12, 2, i + 1).set_title(category)
        plt.title(category+" word count")
        plt.plot(wf['Word'], wf['Frequency'])
        plt.ylim(0, 3000)
        plt.xticks(rotation=70)
        plt.savefig(param['plot']['eda_freq_dist_'+category])
        plt.show()
    plt.close()


    

if __name__ == "__main__":
    path = "params.yaml"
    exploar_data_analysis(path)