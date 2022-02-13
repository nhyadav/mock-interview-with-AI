import pandas as pd
from  EDA import get_parameter
import warnings
warnings.filterwarnings("ignore")
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()





# tokenize the sentances.
# pre_data['tokenize_data'] = pre_data.cleaned_resume.apply(lambda x:tokenize(x))



# pre_data['tokenize_data'].head()
# stopwords.words('english')

def removestopword(x):
    data = x.split()
    data = [lemmatizer.lemmatize(word) for word in data if word not in set(stopwords.words('english'))]
    return ' '.join(data)

def lemmatized_data(path):
    param = get_parameter(path)
    data_path = param['eda']['processed_punc']
    data = pd.read_csv(data_path)
    data['lemmatize_data'] = data.cleaned_resume.apply(lambda x:removestopword(x))
    data.to_csv(param['eda']['processed_lemmatized'],index=False)







# token = nltk.tokenize.word_tokenize
# def tokenize(x):
#     data = token(x)
#     return data


# pre_data['tokenize_data'] = pre_data.lemmatize_data.apply(lambda x:tokenize(x))






if __name__ == "__main__":
    path = "params.yaml"
    lemmatized_data(path)
















