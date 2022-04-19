import numpy as np


def adjust_students_data(data_input):
    data = data_input.dropna()
    columns_to_use = ['gender', 'group A', 'group B', 'group C', 'group D', 'degree', 'lunch', 'course',
                      'math score', 'reading score', 'writing score']
    degree_map = {"bachelor's degree": 4, 'some high school': 1, 'some college': 3, "associate's degree": 5,
                  'high school': 2, "master's degree": 6}

    data['gender'] = data['gender'].map({'female': 1, 'male': 0})
    data['group A'] = data.apply(lambda row: 1 if row['race/ethnicity'] == 'group A' else 0, axis=1)
    data['group B'] = data.apply(lambda row: 1 if row['race/ethnicity'] == 'group B' else 0, axis=1)
    data['group C'] = data.apply(lambda row: 1 if row['race/ethnicity'] == 'group C' else 0, axis=1)
    data['group D'] = data.apply(lambda row: 1 if row['race/ethnicity'] == 'group D' else 0, axis=1)
    data['lunch'] = data.apply(lambda row: 1 if row['lunch'] == 'standard' else 0, axis=1)
    data['course'] = data.apply(lambda row: 1 if row['test preparation course'] == 'completed' else 0, axis=1)
    data['degree'] = data['parental level of education'].map(degree_map)

    return data[columns_to_use]


def adjust_games_data(data_input):
    data = data_input.dropna()
    columns_to_use = ['Platform', 'Year', 'Genre', 'NA_Sales', 'EU_Sales',
                      'JP_Sales', 'Other_Sales', 'Global_Sales']

    return data


def mahalanobis_metric(x, y, cov):
    if not type(x).__module__ == np.__name__:
        x = np.array(x)
    if not type(y).__module__ == np.__name__:
        y = np.array(y)
    inv_cov = np.linalg.inv(cov)
    vec = x - y
    return np.sqrt(vec.T @ inv_cov @ vec)
