import pandas as pd


# import titles for all services
amazon_titles = pd.read_csv(r'C:\Users\akles\OneDrive\Desktop\streaming_project\amazonPrime\amazonTitles.csv')
apple_titles = pd.read_csv(r'C:\Users\akles\OneDrive\Desktop\streaming_project\appletv+\titles.csv')
disney_titles = pd.read_csv(r'C:\Users\akles\OneDrive\Desktop\streaming_project\disney+\disneyTitles.csv')
hbo_titles = pd.read_csv(r'C:\Users\akles\OneDrive\Desktop\streaming_project\hboMax\hboTitles.csv')
netflix_titles = pd.read_csv(r'C:\Users\akles\OneDrive\Desktop\streaming_project\netflix\netflixTitles.csv')
paramount_titles = pd.read_csv(r'C:\Users\akles\OneDrive\Desktop\streaming_project\paramount+\paramountTitles.csv')

# remove unnecessary columns and add service column amazon
amazon_titles.columns
amazon_titles.drop(['production_countries', 'seasons'],1, inplace=True)
amazon_titles['service'] = 'amazon'

# remove unnecessary columns and add service column apple
apple_titles.columns
for column in apple_titles:
    if column not in(amazon_titles):
        apple_titles.drop(column, axis='columns', inplace=True)
apple_titles['service'] = 'apple'

# remove unnecessary columns and add service column disney
disney_titles.columns
for column in disney_titles:
    if column not in(amazon_titles):
        disney_titles.drop(column, axis='columns', inplace=True)
disney_titles['service'] = 'disney'

# remove unnecessary columns and add service column hbo
hbo_titles.columns
for column in hbo_titles:
    if column not in(amazon_titles):
        hbo_titles.drop(column,axis='columns', inplace=True)
hbo_titles['service'] = 'hbo'

# remove unnecessary columns and add service column netflix
netflix_titles.columns
for column in netflix_titles:
    if column not in(amazon_titles):
        netflix_titles.drop(column, axis='columns', inplace=True)
netflix_titles['service'] = 'netflix'

# remove unnecessary columns and add service column paramount
paramount_titles.columns
for column in paramount_titles:
    if column not in(amazon_titles):
        paramount_titles.drop(column, axis='columns', inplace=True)
paramount_titles['service'] = 'paramount'
        

all_titles = pd.concat((paramount_titles, netflix_titles, hbo_titles, disney_titles, apple_titles, amazon_titles))

