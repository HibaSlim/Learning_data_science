import plotly.express as px
import pandas as pd

df= pd.read_csv('clean_histogram_data.csv')
figure = px.bar(df,x='Area (ft.)',y='Price', color='Price')
figure.update_traces(marker=dict(color='red',opacity=0.7,line=dict(color='blue',width=0.5)))
figure.update_layout(coloraxis_colorbar=dict(title='Price'))
figure.show()