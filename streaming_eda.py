import pandas as pd

# import titles for all services
amazon_titles = pd.read_csv(r'C:\Users\akles\OneDrive\Desktop\streaming_project\amazonPrime\amazonTitles.csv')
apple_titles = pd.read_csv(r'C:\Users\akles\OneDrive\Desktop\streaming_project\appletv+\titles.csv')
disney_titles = pd.read_csv(r'C:\Users\akles\OneDrive\Desktop\streaming_project\disney+\disneyTitles.csv')
hbo_titles = pd.read_csv(r'C:\Users\akles\OneDrive\Desktop\streaming_project\hboMax\hboTitles.csv')
netflix_titles = pd.read_csv(r'C:\Users\akles\OneDrive\Desktop\streaming_project\netflix\netflixTitles.csv')
paramount_titles = pd.read_csv(r'C:\Users\akles\OneDrive\Desktop\streaming_project\paramount+\paramountTitles.csv')

# remove unneccesary columns amazon
amazon_titles.columns
amazon_titles.drop(['production_countries', 'seasons'],1, inplace=True)

# remove unneccesary columns apple
apple_titles.columns
for column in apple_titles:
    if column not in(amazon_titles):
        apple_titles.drop(column, axis='columns', inplace=True)

# remove unneccessary columns disney
disney_titles.columns
for column in disney_titles:
    if column not in(amazon_titles):
        disney_titles.drop(column, axis='columns', inplace=True)

# remove unnecessary columns hbo
hbo_titles.columns
for column in hbo_titles:
    if column not in(amazon_titles):
        hbo_titles.drop(column,axis='columns', inplace=True)

# remove unneccesary columns netflix
netflix_titles.columns
for column in netflix_titles:
    if column not in(amazon_titles):
        netflix_titles.drop(column, axis='columns', inplace=True)

# remove unneccary columns paramount
paramount_titles.columns
for column in paramount_titles:
    if column not in(amazon_titles):
        paramount_titles.drop(column, axis='columns', inplace=True)