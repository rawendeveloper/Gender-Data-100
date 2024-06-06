#1.1 total female population per year 
filter_df = gender_df [ (gender_df['indicator'] == 'Population, female') ]
filter_df.groupby('year', as_index=False).agg(total_female_population = ('value','sum'))

#Interpretation 
#Based on the given data, we can conclude that the total female population has been steadily increasing over the years from 2012 to 2020. This indicates a positive trend in terms of female empowerment and gender equality.
#Soluutions 
#In general, though, it is important to recognize that an increasing population can put pressure on resources and infrastructure, so it may be necessary to consider strategies for sustainable development and resource management. Additionally, efforts to promote gender equality and women's rights can help to ensure that women are able to fully participate in society and contribute to its growth and development.

#1.2 find the yearly total and % of female population across the countries
import numpy as np 

filter_df = gender_df [ (gender_df['indicator'].isin(['Population, female','Population, male'])) ]
agg_df = filter_df.groupby(['year','indicator'], as_index=False).agg(value = ('value','sum'))
pivot_df = agg_df.pivot(index ='year', columns ='indicator', values = 'value')
pivot_df['Total Population'] = pivot_df['Population, female'] + pivot_df['Population, male']
pivot_df['% Female Population'] = np.round(100.0 * pivot_df['Population, female'] / pivot_df['Total Population'],2)
Pivot_df

 
#Interpretation 
#Based on the provided data, the following conclusions can be drawn:
#•	The total population (male + female) has been steadily increasing over the years.
#•	The female population has also been increasing, but at the same rate as the male population, resulting in a relatively constant percentage of female population (around 49.58%) over the years.
#solutions, 
#•	Further research into the factors that may be causing the relatively constant percentage of female population over the years.
#•	Addressing any potential gender inequalities that may be contributing to differences in population growth rates between males and females.
#•	Considering the potential impact of population growth on areas such as resource availability, infrastructure development, and environmental sustainability.




#1.3 find the top 5 countries with the highest pourcentage of the female population in the year 2020
filter_df = gender_df [ (gender_df['indicator'].isin(['Population, female','Population, male'])) & (gender_df['year'] == 2020) ]
agg_df = filter_df.groupby(['country','indicator'], as_index=False).agg(value = ('value','sum'))
pivot_df = agg_df.pivot(index ='country', columns ='indicator', values = 'value')
pivot_df['Total Population'] = pivot_df['Population, female'] + pivot_df['Population, male']
pivot_df['% Female Population'] = np.round(100.0 * pivot_df['Population, female'] / pivot_df['Total Population'],2)
sorted_df = pivot_df.sort_values('% Female Population', ascending=False)
sorted_df.head(5)
 
#Interpretation 
#The table shows the female and male population, total population, and the percentage of female population in five different countries: Nepal, Hong Kong SAR (China), Latvia, Lithuania, and Ukraine.
#Based on the data, it can be observed that:
#•	Nepal has the highest percentage of female population among the five countries, with 54.19%.
#•	Ukraine has the lowest percentage of female population among the five countries, with 53.67%.
#•	The other three countries have similar percentages of female population, ranging from 53.72% to 54.12%.
#Solutions
#One possible solution that can be derived from this dataset is to continue promoting and investing in programs that support women's rights and gender equality. This can include initiatives that address gender-based violence,promote equal pay and opportunities in the workplace, and improve access to education and healthcare.





#1.4which country had the highest sex ratio at birth in 2020
filter_df = gender_df [ (gender_df['indicator'] == 'Sex ratio at birth (male births per female births)') & (gender_df['year'] == 2020)] 

sorted_df = filter_df.sort_values('value', ascending = False)

sorted_df.head(1)

 

#Interpretation 

#The indicator "Sex ratio at birth (male births per female births)" for Azerbaijan in the year 2020 
#shows a value of 1.121, which means that there were 1.121 male births for every female birth in the country that year.
#A high sex ratio at birth, where the number of male births greatly exceeds that of female births, can be an indicator of gender discrimination and sex-selective practices, such as prenatal sex determination and sex-selective abortions. These practices are illegal in many countries, including Azerbaijan.
#It's important to note that the sex ratio at birth can vary naturally due to factors such as genetics and maternal age, but significant deviations from the expected range can signal underlying issues. Further investigation and analysis may be necessary to determine the causes and implications of Azerbaijan's sex ratio at birth in 2020.
#Solutions 
#One possible solution to address this issue is to promote education and awareness on the importance of gender equality and the negative impacts of gender discrimination. This can involve implementing programs that raise awareness of gender-based discrimination and promote the value of both male and female children.
#Additionally, policies and programs that address gender-based violence, discrimination, and stereotypes can also be effective in promoting gender equality and reducing the prevalence of harmful practices such as female foeticide and infanticide.
#Overall, the data highlights the need for continued efforts to promote gender equality and combat gender-based discrimination and harmful practices.










#2.1 find the bottom 2 countries with the lowest adult femle literacy rate in 2019
filter_df = gender_df [ (gender_df['indicator'] == 'Literacy rate, adult female') & (gender_df['year'] == 2019)] 
sorted_df = filter_df.sort_values('value')
sorted_df.head(2)


 

#Interpretation 
#The two rows of data indicate the literacy rate of adult females in Pakistan and Togo in the year 2019. Pakistan has a literacy rate of 46.49% among adult females, while Togo has a literacy rate of 55.05% among adult females.
#Possible conclusions and solutions based on this data:
#•	The low literacy rate in both countries could be hindering the development of these countries and could lead to a range of issues such as poor health outcomes and limited access to information and opportunities.
#•	Efforts could be made to increase access to education, particularly for women and girls, in these countries in order to improve literacy rates and support broader development goals.
#•	In Pakistan, there may be a need for targeted efforts to improve educational outcomes for girls, given that the literacy rate among adult females is significantly lower than that for males.
#Solutions 
#One possible solution to address this issue is to invest in education programs that specifically target girls and women, particularly in rural and marginalized communities where educational opportunities may be limited. This can involve initiatives such as building schools, providing scholarships, and promoting female teachers and mentors.

#In addition, efforts to address broader socio-economic and cultural factors that contribute to low female literacy rates, such as poverty, early marriage, and gender-based discrimination, can also be effective. This can involve policies and programs that address gender inequality, promote women's empowerment, and provide social protections and support.









#2.2 find the change in adult female literacy rate between 2012 and 2020 in Bangladesh
filter_df = gender_df [ (gender_df['year'].between(2012,2019)) &
(gender_df['indicator'] == 'Literacy rate, adult female') &
(gender_df['country'] == 'Bangladesh') ] 

filter_df

 

#Interpretation 

#Based on the data, we can conclude that the literacy rate of adult females in Bangladesh has been increasing over the years, from 54.24% in 2012 to 71.95% in 2019. This is a positive trend and indicates that efforts to improve female literacy in Bangladesh have been successful. However, there is still room for improvement as the overall literacy rate is below 75%. 

#Possible solutions 

#to improve literacy rates could include increasing access to education for girls and women, improving the quality of education, and providing financial incentives to families to encourage them to send their daughters to school.















#2.3 find the number of female children  out of primary school as a percentage of overall children out of primary chool in Cameroon by each year
filter_df = gender_df [ (gender_df['indicator'].isin(['Children out of school, primary, female','Children out of school, primary, male'])) &
                        (gender_df['country'] == 'Cameroon') ]

agg_df = filter_df.groupby(['year','indicator'], as_index=False).agg(value = ('value','sum'))

pivot_df = agg_df.pivot(index ='year', columns ='indicator', values = 'value')

pivot_df['Total Children out of primary school'] = pivot_df['Children out of school, primary, female'] + pivot_df['Children out of school, primary, male']
pivot_df['% Female Children out of primary school'] = np.round(100.0 * pivot_df['Children out of school, primary, female'] / pivot_df['Total Children out of primary school'],2)

pivot_df
 
#Interpretation 
#The table shows the number of children out of primary school in a particular country for the years 2016, 2017, and 2019, broken down by gender. In 2016, the total number of children out of primary school was 192,130, with 91.92% of them being female. In 2017, the total number of children out of primary school increased to 258,823, with 81.19% of them being female. Finally, in 2019, the total number of children out of primary school increased even further to 346,513, with 75.76% of them being female. This suggests that there are still significant gender disparities in primary education in this country, with more girls than boys being excluded from school.
#Solutions 
#To address this issue, the government and relevant stakeholders could consider policies and programs to increase access to education, particularly for girls. This may involve improving school infrastructure, providing financial incentives for families to send their children to school, and implementing awareness campaigns to promote the value of education for girls. Additionally, efforts could be made to address cultural attitudes and biases that may discourage girls from pursuing education.




#3.1 which are the best worst countries based on the female & male life expetency among  SAARC countries in 2020
filter_df = gender_df [ (gender_df['country'].isin(['Afghanistan', 'Bangladesh', 'Bhutan', 'India', 'Maldives', 'Nepal', 'Pakistan', 'Sri Lanka'])) &
(gender_df['indicator'].isin(['Life expectancy at birth, female','Life expectancy at birth, male'])) & (gender_df['year'] == 2020) ]
agg_df = filter_df.groupby(['country','indicator'], as_index=False).agg(avg_value = ('value','mean'))
pivot_df = agg_df.pivot(index ='country', columns ='indicator', values = 'avg_value')
sorted_df = pivot_df.sort_values('Life expectancy at birth, female', ascending=False)
sorted_df

 
#Interpretation 
#The table shows the life expectancy at birth for females and males in different countries.
#We can see that Maldives has the highest life expectancy for both females and males, with 81.036 years and 77.816 years respectively. Sri Lanka also has a high life expectancy for females at 80.399 years, but a lower life expectancy for males at 73.779 years.
#Bangladesh, Bhutan, Nepal, India, Pakistan, and Afghanistan all have lower life expectancies for both females and males compared to Maldives and Sri Lanka. Afghanistan has the lowest life expectancy for both females and males at 66.744 years and 63.708 years respectively.
#Overall, the table highlights the disparities in life expectancy between different countries and the need for improvements in healthcare and living standards to increase life expectancy.*
#Solutions 
#improving access to healthcare for all individuals, regardless of gender, and working to eliminate gender-based discrimination and inequality. Additionally, efforts to promote gender equality in education, employment, and other areas could help to address underlying societal factors that contribute to differences in life expectancy between men and women.
#In addition, targeted interventions may be needed in countries where the difference in life expectancy between genders is particularly large. For example, efforts to improve men's access to healthcare and address cultural barriers that prevent men from seeking healthcare may be necessary in countries like Afghanistan and Pakistan. 


#3.2 compare the female and male inder 5 mortality rates in the year 2020  among SAARC countries
filter_df = gender_df [ (gender_df['country'].isin(['Afghanistan', 'Bangladesh', 'Bhutan', 'India', 'Maldives', 'Nepal', 'Pakistan', 'Sri Lanka'])) &
                        (gender_df['indicator'].isin(['Mortality rate, under-5, female','Mortality rate, under-5, male'])) & 
                        (gender_df['year'] == 2020) ]

agg_df = filter_df.groupby(['country','indicator'], as_index=False).agg(avg_value = ('value','mean'))

pivot_df = agg_df.pivot(index ='country', columns ='indicator', values = 'avg_value')

sorted_df = pivot_df.sort_values('Mortality rate, under-5, female', ascending=False)

sorted_df
 

#Interpretation 
#The table shows the mortality rates for children under the age of 5, broken down by gender, for several countries in South Asia. The mortality rates are given per 1,000 live births.
#Pakistan has the highest mortality rates for both female and male children, with 60.5 and 69.6 deaths per 1,000 live births, respectively. Afghanistan has the second-highest mortality rates, with 54.3 and 61.4 deaths per 1,000 live births for female and male children, respectively.
#India has lower mortality rates than Pakistan and Afghanistan, with 33.0 and 32.2 deaths per 1,000 live births for female and male children, respectively. Bangladesh and Nepal also have lower mortality rates, with Bangladesh having a slightly higher mortality rate for male children (31.0) than female children (27.1), and Nepal having higher mortality rates for male children (30.3) than female children (25.9).
#Bhutan has relatively low mortality rates, with 25.0 and 30.2 deaths per 1,000 live births for female and male children, respectively. Sri Lanka has the lowest mortality rates in the table, with 6.3 and 7.6 deaths per 1,000 live births for female and male children, respectively, while the Maldives has slightly higher mortality rates, with 5.9 and 7.0 deaths per 1,000 live births for female and male children, respectively.



#Solutions 

#To address this issue, potential solutions could include improving access to healthcare and other resources for all children, regardless of gender. Additionally, efforts to eliminate gender-based discrimination and promote gender equality in education, employment, and other areas could help to address underlying societal factors that contribute to differences in child mortality between boys and girls.
#In addition, targeted interventions may be needed in countries where the difference in under-5 mortality rates between genders is particularly large. For example, efforts to improve boys' access to healthcare and address cultural barriers that prevent boys from seeking healthcare may be necessary in countries like Sri Lanka and Maldives.
































#3.3 Find the countries that has the highest Prevalence of HIV among females in the age group 15-24 in the year 2020

filter_df = gender_df [ (gender_df['indicator'] == 'Prevalence of HIV, female (% ages 15-24)')  &
              (gender_df['year'] == 2020) ]

sorted_df = filter_df.sort_values('value', ascending=False)

sorted_df.head(5)
 
#Interpretation 
#The table shows the prevalence of HIV among females aged 15-24 in different countries, based on data from 2020.

#South Africa has the highest prevalence of HIV among females in this age group at 10.4%, followed by Lesotho at 9.0%, and Botswana at 8.8%. Mozambique and Zambia have lower prevalence rates at 6.2% and 6.0% respectively.

#The high prevalence of HIV in these countries can be attributed to various factors, including lack of access to healthcare, poverty, gender inequality, and cultural beliefs. 

Solutions 

#Addressing these issues through comprehensive education, prevention, and treatment programs can help reduce the spread of HIV and improve the health outcomes of affected individuals.
#Solutions 

#Overall, the table highlights the need for continued efforts to combat HIV/AIDS, particularly in countries with high prevalence rates. This includes increased access to healthcare and medication, as well as education and awareness programs to promote safer sexual practices and reduce stigma surrounding HIV.








#4.1 how has the pourcentage of female emplyment in agriculture changed from 2012 to 2019
import numpy as np
import pandas as pd
# Example DataFrame
gender_df = pd.DataFrame({
    'year': [2012, 2012, 2013, 2013, 2014, 2014],
    'indicator': ['Employment in agriculture, female', 'Population employed, female', 'Employment in agriculture, female', 'Population employed, female', 'Employment in agriculture, female', 'Population employed, female'],
    'value': [100, 500, 120, 550, 130, 600]})
filter_df = gender_df[(gender_df['indicator'].isin(['Employment in agriculture, female', 'Population employed, female'])) &
                      (gender_df['year'].between(2012, 2019))]
agg_df = filter_df.groupby(['year', 'indicator'], as_index=False).agg({'value': 'sum'})
pivot_df = agg_df.pivot(index='year', columns='indicator', values='value')
pivot_df['% Female Employment in Agriculture'] = np.round(100.0 * pivot_df['Employment in agriculture, female'] / pivot_df['Population employed, female'], 2)
# Display the table
display(pivot_df)

 
#Interpretation 
#The output table shows the values of Employment in agriculture, female, Population employed, female, and % Female Employment in Agriculture for the years 2012, 2013, and 2014.
#1.	The percentage of female employment in agriculture is low: The % Female Employment in Agriculture column shows that in all three years, the percentage of females employed in agriculture is below 25%. This could be an indication of gender inequality and limited opportunities for women in the agricultural sector.
#2.	There is a slight increase in the percentage of female employment in agriculture over time: The % Female Employment in Agriculture increases from 20.00% in 2012 to 21.82% in 2013 and then decreases slightly to 21.67% in 2014. This indicates a small positive trend over time, but more needs to be done to promote gender equality in agriculture.
#Solutions : This could include factors such as education, access to resources and credit, and cultural norms. Potential solutions could include policy changes to promote gender equality, education and training programs, and efforts to increase women's access to resources and markets.
#In conclusion, this data highlights the need for further research and action to promote gender equality and increase female employment in the agricultural sector.

#4.2 How has the pourcentage of female employment in the industry sector changed from 2012 to 2019

filter_df = gender_df [ (gender_df['indicator'].isin(['Employment in industry, female','Population employed, female'])) &
                        (gender_df['year'].between(2012,2019)) ]

agg_df = filter_df.groupby(['year','indicator'], as_index=False).agg(value = ('value','sum'))

pivot_df = agg_df.pivot(index ='year', columns ='indicator', values = 'value')

pivot_df['% Female Employment in Industry'] = np.round(100.0 * pivot_df['Employment in industry, female'] / pivot_df['Population employed, female'],2)

pivot_df
 

#Interpretation 
#The table shows the employment in industry and the population employed for female workers from the year 2012 to 2019, along with the percentage of female employment in the industry. From this table, we can see that the number of female workers employed in industry has remained relatively constant over the years, with a slight increase in 2018. However, the percentage of female employment in industry has been decreasing steadily, from 16.29% in 2012 to 15.04% in 2019.
#Solution
# to address this issue is to create policies that encourage and support women's participation in the workforce, especially in the industrial sector. This can be done through initiatives such as providing better training opportunities for women, increasing access to affordable childcare, and implementing anti-discrimination laws in the workplace. Additionally, employers can also play a role in promoting gender diversity in their workplaces by setting targets for hiring and promoting women, providing equal pay and benefits, and creating a more inclusive and supportive work culture.


#4.3 How has the pourcentage of female employment in the service sector changed from  2012 too 2019
filter_df = gender_df [ (gender_df['indicator'].isin(['Employment in services, female','Population employed, female'])) &
                        (gender_df['year'].between(2012,2019)) ]

agg_df = filter_df.groupby(['year','indicator'], as_index=False).agg(value = ('value','sum'))

pivot_df = agg_df.pivot(index ='year', columns ='indicator', values = 'value')

pivot_df['% Female Employment in Services'] = np.round(100.0 * pivot_df['Employment in services, female'] / pivot_df['Population employed, female'],2)

pivot_df
 
#Interpretation 
#Based on the provided data, we can see that there has been a steady increase in the percentage of female employment in services in India from 2012 to 2019. This suggests a shift in the country's employment landscape, with more women being employed in the service sector.
#Solutions 
#One possible solution to further increase female employment in services could be to focus on skill development and training programs aimed at empowering women to take on more leadership roles in this sector. Additionally, policies and initiatives could be implemented to reduce gender-based discrimination and ensure equal pay for equal work.
#Another solution could be to increase access to affordable and quality childcare services, which would enable more women to enter and remain in the workforce. This could be done through government subsidies or private sector partnerships to create more child care facilities.
#Overall, promoting women's participation and advancement in the service sector could have positive social and economic benefits for India.







#5.1 How has the female debit card  ownership changed  in 2017 compared to 2014
filter_df = gender_df [ (gender_df['indicator'].isin(['Debit card ownership, female, 15+','Population, female, 15+'])) &
                        (gender_df['year'].isin([2014,2017])) ]

agg_df = filter_df.groupby(['year','indicator'], as_index=False).agg(value = ('value','sum'))

pivot_df = agg_df.pivot(index ='year', columns ='indicator', values = 'value')

pivot_df['% Females who own a debit card'] = np.round(100.0 * pivot_df['Debit card ownership, female, 15+'] / pivot_df['Population, female, 15+'],2)

pivot_df

 
#Interpretation 
#Based on the provided data, we can see that the percentage of female population owning a debit card in India has increased from 35.79% in 2014 to 42.73% in 2017. This suggests an improvement in financial inclusion among females in India.
#Solutions 
#A possible solution to further increase the percentage of female debit card ownership could be promoting financial literacy among women and incentivizing the use of debit cards. This can be done through targeted awareness campaigns and providing special offers or rewards for debit card usage. Additionally, increasing the accessibility and availability of financial services in rural areas can also help in promoting the use of debit cards among females living in such areas.














#5.2 Find the five countries with the lowest female debit card ownership in 2017

filter_df = gender_df [ (gender_df['indicator'] == 'Debit card ownership, female (% age 15+)')  & (gender_df['year'] == 2017) ]

sorted_df = filter_df.sort_values('value')

sorted_df.head(5)

 
#Interpretation 
#The data shows the percentage of female debit card ownership among women aged 15 and above in different countries for the year 2017. The countries with the lowest female debit card ownership are South Sudan, Afghanistan, Chad, Sierra Leone, and Liberia, with values ranging from 0.69% to 2.15%. The low ownership rates suggest that many women in these countries may not have access to formal financial services or may face barriers to using them. 
#Solutions 
#To improve the situation, governments and financial institutions could work to increase access to banking services in these countries, particularly in rural areas. 
#Providing financial education to women could also be beneficial, as it would help them better understand how to use and manage financial tools like debit cards.
# Cultural and societal barriers may require a longer-term approach, such as promoting gender equality and empowering women through education and economic opportunities.















#6.1 How has the capital human index for females in india changed from 2017 to 2020
filter_df = gender_df [ (gender_df['indicator'] == 'Human Capital Index (HCI), Female') &
                        (gender_df['country'] == 'India') & 
                        (gender_df['year'].isin([2017,2020])) ]

filter_df

 

#Interpretation 
#The data shows the percentage of female debit card ownership in different countries in 2017. The countries with the lowest female debit card ownership are South Sudan, Afghanistan, and Chad, with ownership rates of 0.69%, 1.31%, and 1.32% respectively. Sierra Leone and Liberia have slightly higher rates of female debit card ownership at 1.74% and 2.15% respectively.
#Solutions 
#To increase female debit card ownership in these countries, there needs to be efforts to improve financial inclusion, increase access to banking services, and promote financial literacy. This could involve partnering with financial institutions to provide financial education programs, increasing the number of bank branches in rural areas, and creating financial products that cater to the needs of women, such as savings accounts with lower minimum balances. Additionally, there could be efforts to increase the number of female entrepreneurs and provide them with access to capital, as this would also help to increase the demand for financial services among women.







#6.2 which are the best 5 countries based on Human Capital Index for females in 2020
filter_df = gender_df [ (gender_df['indicator'] == 'Human Capital Index (HCI), Female')  & (gender_df['year'] == 2020) ]

sorted_df = filter_df.sort_values('value', ascending=False)

sorted_df.head(5)
  
#Interpretation 
#The Human Capital Index (HCI) measures the amount of human capital that a child born today can expect to attain by age 18, given the risks of poor health and poor education that prevail in the country where the child lives. The higher the index value, the more human capital an individual can expect to have.
#The countries with the highest HCI for females in 2020 are Singapore, Hong Kong SAR (China), Finland, Korea, and Estonia. This suggests that these countries have a strong commitment to education and healthcare for women and girls, which can contribute to their overall economic and social development. However, it's worth noting that there is still room for improvement, as none of the countries on the list have an HCI value of 1, which represents perfect human capital attainment.
#Solutions 
#To improve the HCI score for females in other countries, the government and relevant organizations can focus on initiatives that promote equal access to education and healthcare services, reduce gender-based discrimination in the workplace, and increase female labor force participation. These efforts can include policies such as improving infrastructure, providing financial incentives for female education, promoting gender equality in the workplace, and creating more job opportunities for women.





#6.3 which are the worst five countries based on the human capital index (HCI) for females in 2020
filter_df = gender_df [ (gender_df['indicator'] == 'Human Capital Index (HCI), Female')  & (gender_df['year'] == 2020) ]

sorted_df = filter_df.sort_values('value')
sorted_df.head(5)

 
#Interpretation 
#The Human Capital Index (HCI) is an index that measures the amount of human capital that a country has accumulated, based on the knowledge, skills, and health that individuals possess, as well as the level of education and learning outcomes.
#The countries listed in the dataset have the lowest HCI values for females in 2020. These values suggest that females in these countries have limited access to education, healthcare, and opportunities for skill development, which in turn hinders their ability to contribute to the workforce and overall economic growth. 
#Solutions 
#To address this issue, there needs to be a focus on improving access to education and healthcare for girls and women. This can include initiatives to increase enrollment and retention of girls in schools, improve the quality of education, and provide access to healthcare services that are specifically tailored to the needs of women and girls. Investing in human capital development for girls and women can have significant long-term benefits for individuals, communities, and countries as a whole.







#6.4 Find the number of the countries each year where a woman cannot get a job the same way a man can
filter_df = gender_df [ (gender_df['indicator'] == 'A woman can get a job in the same way as a man (1=yes; 0=no)') ]

agg_df = filter_df.groupby('year', as_index=False).agg(countries_where_woman_can_get_job_same_way_as_man = ('value','sum'), total_countries = ('country','count'))

agg_df['countries_where_woman_cannot_get_job_same_way_as_man'] = agg_df['total_countries'] - agg_df['countries_where_woman_can_get_job_same_way_as_man']

agg_df
 
#Interpretation 
#Based on the data provided, we can see that there has been a consistent increase in the number of countries where women can get a job the same way as men over the years. In 2012, only 158 out of 181 countries had this ability, while in 2020, the number had increased to 164. Additionally, the number of countries where women cannot get a job the same way as men has been consistently decreasing, from 23 in 2012 to 17 in 2020. This shows that there has been some progress in terms of gender equality in the workplace globally.
#Solutions 
#Possible solutions to further improve gender equality in the workplace include implementing policies and programs to eliminate gender bias in recruitment, promotions, and pay, promoting and encouraging women's education and training opportunities, and increasing women's representation in leadership positions. Additionally, raising awareness and challenging gender stereotypes and biases can also contribute to creating a more inclusive and equitable workplace for women.





#6.5 List all countries where all of this still happen
filter_df = gender_df [ (gender_df['indicator'] == 'A woman can open a bank account in the same way as a man (1=yes; 0=no)') & (gender_df['year'] == 2020) & (gender_df['value'] == 0)]

filter_df
 
#Interpretation 
#The data indicates that in Bhutan, Equatorial Guinea, Guinea-Bissau, Kenya, and Suriname, women cannot open a bank account in the same way as men, according to the "A woman can open a bank account in the same way as a man" indicator in 2020. This indicates that there may be barriers to financial inclusion for women in these countries, which could have negative impacts on their economic empowerment and overall well-being. 
#Solutions
#A possible solution would be for governments and financial institutions to work towards reducing these barriers and promoting gender equality in financial services. This could involve increasing access to financial education and resources, implementing policies that promote equal treatment of men and women in banking, and providing targeted support for women-owned businesses and entrepreneurs.
