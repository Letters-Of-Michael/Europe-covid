import streamlit as st
import pandas as pd
from IPython.display import IFrame
from PIL import Image
import matplotlib.pyplot as plt

header = st.container()
background = st.container()
dataset = st.container()
question = st.container()
Data_Development = st.container()
visualization = st.container()
copywright = st.container()


with header:
	st.title('Europe Covid Analysis')
	st.write('A detailed analysis to provide general insights about the raging pandermic in 2020. The data analyzed the effects and influence of the pandemic on each country in europe, it further gave insights on the level of mortality and fatality and extensively the rate of recovery and tests: this shows the level of work put in by the medical services for each country and also the strength of the health sector and other policies')

	with background:
		st.header("PANDEMIC BACKGROUND")
		st.write('Covid are important human and animal pathogens. In 2019, a novel coronavirus was identified as the cause of a cluster pneumonia cases in Wuhan, China. It spread rapidly followed by a global pandemic. In Feb, 2020, the WHO designated the disease the COVID_19 which stands for coronovirus disease 2019.')

	with dataset:
		st.header("Data gathered from the Kaggle.")
		st.write('Here, the dataset contains about 48 countries in europe with their recorded cases, recovery rates, deaths. This data was collected over the period of time while the pandemic ravaged in 2020.')

		covid_data = pd.read_csv('./image/europe_covid.csv')
		st.write(covid_data.head())

	with question:
		st.header('Analysis Background')
		st.write('In this section, I provided more insights on some important questions that could arise during and after the pandemic. This insights will be a guide to our analysis and visualization as a whole.')


		st.markdown('* **first:** How each country were affected: the death rate, recovery rate, active cases left in relation to the number of tests recorded per country and these were put into consideration according to the population density for each country.')
		st.markdown('* **second:** The occurence and effect of the pandemic in relation and comparison to other countries in that continent and within the geographical location.')


	with Data_Development:
		st.header('Data Development')
		st.write("I downloaded the dataset from kaggle and thereafter, I used excel for the data cleaning process and to get the general overview of our dataset: removed unwanted columns, calculated the per 1 million relationship for each country, then imported our data into microsoft powerbi for visualization and to answer our questions and guide our analysis.")



	with visualization:
		st.header('Time to visualize our data!')
		st.write('#CovidAnalysis, #DataAnalysis, #Analysis, #Data, #DataVisualization, #PowerBi')

		sel_col, disp_col = st.columns(2)

		#Dashboard = IFrame(src" ", width = 1000, height = 600)
		#display(Dashboard)

		img = Image.open("./image/4.jpg")
		st.image(img)

		url = 'To view the interactive live dashboard on powerbi service, click  [Dashboard](https://app.powerbi.com/view?r=eyJrIjoiOGYzOWQ0MTAtN2Q3NS00Mzg5LTgwMDEtNjM4NDhmYmZjYTgzIiwidCI6IjhlOTVjNGQxLWRiZmQtNGFmNS1iODA2LTIwMGJkZDY2ZDJjZSJ9)'
		st.markdown(url,unsafe_allow_html=True)

		
	with copywright:
		st.text('By Oluwaseyi Michael')




