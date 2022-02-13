import pandas as pd
from  EDA import get_parameter
import warnings
warnings.filterwarnings("ignore")
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()


def remove_stopword(x):
    data = x.split()
    data = [lemmatizer.lemmatize(word) for word in data if word not in set(stopwords.words('english'))]
    return ' '.join(data)




def lemmatized_data(path):
    param = get_parameter(path)
    data_path = param['eda']['processed_punc']
    data = pd.read_csv(data_path)
    data['lemmatize_data'] = data.cleaned_resume.apply(lambda x:remove_stopword(x))
    data.to_csv(param['eda']['processed_lemmatized'],index=False)
    



if __name__ == "__main__":
    path = "params.yaml"
    lemmatized_data(path)
