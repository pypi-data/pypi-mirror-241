import os
import matplotlib.pyplot as plt
from pathlib import Path
from mlutils.dataimporters import MLUtilsDataLoader
from mlutils.featuresengine import impute_data, box_cox_data_transform
from mlutils.config import ROOT_DIR, DATA_DIR

if __name__ == '__main__':

    print(ROOT_DIR)
    print(DATA_DIR)
    # print(os.path.dirname(__file__))
    # load the data
    data = MLUtilsDataLoader.load_covid_flu()

    print(data.head(n=5))

    # which columns are qualitative and which quantitative
    print(data.info())

    # check percentage of nulls per column
    print(data.isnull().mean())


    # let's the counts for every class. This is
    # a binary classification problem so two classes should be present
    class_counts = data['Diagnosis'].value_counts(normalize=True)

    print(f"Class counts are: ")
    print(class_counts)

    # Our most common category is H1N1, with just over 72% of our response
    # variable belonging to that category. Our null accuracy is 72%—the accuracy
    # of a classification model that just guesses the most common category
    # over and over again. Our absolute baseline for our machine learning
    # pipeline will have to be beating the null accuracy.
    # If our model just guessed H1N1 for every person coming in,
    # technically, that model would be accurate 72% of the time, even
    # though it isn’t really doing anything. But hey, even a guessing ML model is right 72% of the time.

    numeric_types = ['float16', 'float32', 'float64', 'int16', 'int32', 'int64']

    numerical_columns = data.select_dtypes(include=numeric_types).columns.tolist()

    print(numerical_columns)

    imputed_lymphocytes = impute_data(data[['lymphocytes']], strategy='mean')
    print(imputed_lymphocytes[:5])

    # another imputation approach is to use an arbitrary value
    # for the missing data
    arbitrary_imputer = impute_data(data[['lymphocytes']], strategy='constant', **{'fill_value': 999})
    print(arbitrary_imputer[:5])

    eof_imputer = impute_data(data[['lymphocytes']], strategy='end-of-tail')
    eof_imputer.plot(title='Lymphocytes (Imputed)', kind='hist', xlabel='cells/μL')
    plt.show()


    # categorical data
    categorical_types = ['O']  # The "object" type in pandas
    categorical_columns = data.select_dtypes(
        include=categorical_types).columns.tolist()
    categorical_columns.remove('Diagnosis')
    for categorical_column in categorical_columns:
        print('=======')
        print(categorical_column)
        print('=======')
        print(data[categorical_column].value_counts(dropna=False))

    data['Female'] = data['Sex'] == 'F'
    del data['Sex']

    data = data.replace({'Yes': True, 'No': False})

    box_cox_data_transform(data[['lymphocytes']], **{'standardize': False})





