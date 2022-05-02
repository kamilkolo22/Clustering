import pandas as pd
from copy import deepcopy


def adjust_students_data(data_input):
    """Prepare data, get dummies for qualitative data and normalize values"""
    data = deepcopy(data_input)
    columns_to_use = ['gender', 'group A', 'group B', 'group C', 'group D',
                      'degree', 'lunch', 'course', 'AvgScore']
    degree_map = {"bachelor's degree": 3/5, 'some high school': 0,
                  'some college': 2/5, "associate's degree": 4/5,
                  'high school': 1/5, "master's degree": 1}

    data['gender'] = data['gender'].map({'female': 1, 'male': 0})
    data['group A'] = data.apply(
        lambda row: 1 if row['race/ethnicity'] == 'group A' else 0, axis=1)
    data['group B'] = data.apply(
        lambda row: 1 if row['race/ethnicity'] == 'group B' else 0, axis=1)
    data['group C'] = data.apply(
        lambda row: 1 if row['race/ethnicity'] == 'group C' else 0, axis=1)
    data['group D'] = data.apply(
        lambda row: 1 if row['race/ethnicity'] == 'group D' else 0, axis=1)
    data['lunch'] = data.apply(
        lambda row: 1 if row['lunch'] == 'standard' else 0, axis=1)
    data['course'] = data.apply(
        lambda row: 1 if row['test preparation course'] == 'completed' else 0,
        axis=1)
    data['degree'] = data['parental level of education'].map(degree_map)
    data['AvgScore'] = data.apply(lambda row: (row['math score'] +
                                               row['reading score'] +
                                               row['writing score']) / 3,
                                  axis=1)
    max_v = max(data['AvgScore'])
    min_v = min(data['AvgScore'])
    data['AvgScore'] = data.apply(lambda row: (row['AvgScore'] - min_v) /
                                              (max_v - min_v),
                                  axis=1)
    return data[columns_to_use]


def adjust_games_data(data_input):
    """Prepare games data for further analysis and clustering algorithm"""
    # Set parameters
    big_publisher = ['Nintendo', 'Microsoft Game Studios', 'Activision',
                     'Take-Two Interactive', 'Sony Computer Entertainment',
                     'Ubisoft', 'Bethesda Softworks', 'Electronic Arts']
    # relevant_platforms = ['PC', 'PS3', 'XOne', 'PSP', 'Wii', 'DS', 'X360']
    columns_to_use = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']
    data = deepcopy(data_input)

    # Adjust Publisher column
    data.loc[~data["Publisher"].isin(big_publisher), "Publisher"] = "Other"
    for publisher in big_publisher:
        data[publisher] = data.apply(
            lambda row: 1 if row['Publisher'] == publisher else 0, axis=1)

    # Adjust Platform Column
    # data.loc[~data["Platform"].isin(relevant_platforms), "Platform"] = "Other"
    platforms = set(data['Platform']) - {'3DS'}
    for platform in platforms:
        data[platform] = data.apply(
            lambda row: 1 if row['Platform'] == platform else 0, axis=1)

    # Adjust Platform Column
    genres = set(data['Genre']) - {'Platform'}
    for genre in genres:
        data[genre] = data.apply(
            lambda row: 1 if row['Genre'] == genre else 0, axis=1)

    return data[columns_to_use + big_publisher + list(genres) + list(platforms)]


def read_data(path, typ):
    """Read data from file path and drop na values"""
    data = pd.read_csv(path, na_values='no data')
    # Filter data
    data = data.dropna()
    if typ == 'games':
        data = data[data['Year'] >= 2006]
    data = data.reset_index(drop=True)

    return data


def read_excel(path):
    """Read excel file with games data stats"""
    data = pd.read_excel(path, index_col=[0, 1, 2], header=[0, 1])
    return data


def adjust_to_plot(data_input):
    """Prepare games data for plots"""
    data = deepcopy(data_input)
    # Set parameters
    big_publisher = ['Nintendo', 'Microsoft Game Studios', 'Activision',
                     'Take-Two Interactive', 'Sony Computer Entertainment',
                     'Ubisoft', 'Bethesda Softworks', 'Electronic Arts']
    # relevant_platforms = ['PC', 'PS3', 'XOne', 'PSP', 'Wii', 'DS', 'X360']
    columns_to_use = ['NA_Sales', 'EU_Sales', 'JP_Sales',
                      'Other_Sales',
                      'Publisher', 'Genre', 'Platform']

    # Adjust Publisher column
    data.loc[~data["Publisher"].isin(big_publisher), "Publisher"] = "Other"
    # Adjust Platform Column
    # data.loc[~data["Platform"].isin(relevant_platforms), "Platform"] = "Other"

    data = data[columns_to_use]
    data = data.melt(id_vars=['Publisher', 'Genre', 'Platform'],
                     var_name='Region', value_name='Sales')

    return data
