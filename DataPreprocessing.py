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
    # Set parameters
    min_year = 2006
    big_publisher = ['Nintendo', 'Microsoft Game Studios', 'Activision',
                     'Take-Two Interactive', 'Sony Computer Entertainment',
                     'Ubisoft', 'Bethesda Softworks', 'Electronic Arts']
    columns_to_use = ['NA_Sales', 'EU_Sales', 'JP_Sales',
                      'Other_Sales', 'Global_Sales']

    # Filter data
    data = data_input.dropna()
    data = data[data['Year'] >= min_year]

    # Adjust Publisher column
    data.loc[~data["Publisher"].isin(big_publisher), "Publisher"] = "Other"
    for publisher in big_publisher:
        data[publisher] = data.apply(
            lambda row: 1 if row['Publisher'] == publisher else 0, axis=1)

    # Adjust Platform Column
    platforms = set(data['Platform']) - {'3DS'}
    for platform in platforms:
        data[platform] = data.apply(
            lambda row: 1 if row['Platform'] == platform else 0, axis=1)

    # Adjust Platform Column
    genres = set(data['Genre']) - {'Puzzle'}
    for genre in genres:
        data[genre] = data.apply(
            lambda row: 1 if row['Genre'] == genre else 0, axis=1)

    return data[columns_to_use + big_publisher + list(genres) + list(platforms)]
