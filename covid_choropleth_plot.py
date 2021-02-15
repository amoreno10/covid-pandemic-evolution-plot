# For this practical example we will need the following libraries
import pandas as pd
import plotly.express as px

# from plotly.offline import init_notebook_mode
# init_notebook_mode(connected=True)

# Import dataset and first exploratory analysis
path = './data/covid_19_data.csv'
raw_data = pd.read_csv(path)
print(raw_data)

# Check if the dataset has null values, and the types of the columns
print(raw_data.info())

# Data manipulation
data = raw_data.rename(columns={'ObservationDate': 'Date', 'Country/Region': 'Country'})
# Change Date type to datetime to sort in ascending way
data['Date'] = pd.to_datetime(data['Date'])
df_country_timeline = data[data['Confirmed'] > 0]
df_country_timeline = df_country_timeline.groupby(['Country', 'Date']).sum().sort_values(by='Date', ascending=True)
df_country_timeline = df_country_timeline.reset_index()
df_country_timeline['Date'] = df_country_timeline['Date'].apply(lambda x: x.strftime('%Y-%m-%d'))

# Create the choropleth plot using Plotly.
fig = px.choropleth(df_country_timeline, locations='Country', locationmode='country names',
                    color='Confirmed', hover_name='Country', animation_frame='Date',
                    color_continuous_scale='orrd')

fig.update_layout(title={'text': '<b>Global Spread of Coronavirus</b>',
                         'x': 0.5, 'font': {'size': 25, 'color': 'black'}},
                  geo=dict(showframe=False, showcoastlines=False))

# Display plot
fig.show()
