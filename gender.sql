1.1 total female population per year indicator names female population
SELECT
year,
SUM(value) AS total_female_population
FROM
career_nub.gender_data
WHERE
indicator = 'Population, female'
GROUP BY 1
ORDER BY 1

interpretation
From the data provided, we can see that the total female population has been steadily increasing every year from 2012 to 2020. This is a positive trend as it indicates that there is a growing number of women in the world.


solutions
In general, though, it is important to recognize that an increasing population can put pressure on resources and infrastructure, so it may be necessary to consider strategies for sustainable development and resource management. Additionally, efforts to promote gender equality and women's rights can help to ensure that women are able to fully participate in society and contribute to its growth and development.






1.2 find the yearly total and % of female population across the countries 
SELECT
  year,
  SUM(CASE WHEN indicator = 'Population, female' THEN value END) AS female_population,
  SUM(value) AS total_population,
  100.0 * SUM(CASE WHEN indicator = 'Population, female' THEN value END) / SUM(value) AS perc_female_population
FROM 
  career_nub.gender_data 
WHERE
  indicator IN ('Population, female', 'Population, male')  
GROUP BY 1
ORDER BY 1;
 
interpretation
From this dataset, we can see that the percentage of the total population that is female has remained relatively constant over the years, hovering around 49.5-49.6%. However, it is worth noting that the absolute number of females has been increasing each year, indicating an overall growth in the female population.
Solutions
To continue promoting gender equality and empowering women in all aspects of society, including education, healthcare, and employment opportunities. By providing equal opportunities for women and men, we can ensure that both genders can contribute to society and achieve their full potential.
Additionally, efforts to improve access to family planning and reproductive health services can help to ensure that women are able to make informed choices about their reproductive health, including the decision to have a child. This can also help to reduce the prevalence of female foeticide and other harmful practices that discriminate against women
1.3 find the top 5 countries with the highest pourcentage of the female population in the year 2020 
SELECT
  country,
  SUM(CASE WHEN indicator = 'Population, female' THEN value END) AS female_population,
  SUM(value) AS total_population,
  100.0 * SUM(CASE WHEN indicator = 'Population, female' THEN value END) / SUM(value) AS perc_female_population
FROM 
  career_nub.gender_data 
WHERE
  year = 2020
  AND indicator IN ('Population, female', 'Population, male')
GROUP BY 1
ORDER BY 4 DESC
LIMIT 5;

 
interpretation
From this dataset, we can see that the countries listed have a higher percentage of female population than the global average, with percentages ranging from 53.7% to 54.2%. This indicates that these countries may have made progress towards gender equality and empowering women.
Solutions 
One possible solution that can be derived from this dataset is to continue promoting and investing in programs that support women's rights and gender equality. This can include initiatives that address gender-based violence, promote equal pay and opportunities in the workplace, and improve access to education and healthcare.





1.4 which country had the highest sex ratio at birth in 2020 
SELECT
  *
FROM 
  career_nub.gender_data  
WHERE
  indicator = 'Sex ratio at birth (male births per female births)'
  AND year = '2020'
ORDER BY value DESC
LIMIT 1

 
Interpretation 
From this dataset, we can see that the sex ratio at birth in Azerbaijan in 2020 was 1.121, indicating that there were more male births than female births. This suggests that there may be a cultural preference for male children in Azerbaijan.
Solutions 
One possible solution to address this issue is to promote education and awareness on the importance of gender equality and the negative impacts of gender discrimination. This can involve implementing programs that raise awareness of gender-based discrimination and promote the value of both male and female children.
Additionally, policies and programs that address gender-based violence, discrimination, and stereotypes can also be effective in promoting gender equality and reducing the prevalence of harmful practices such as female foeticide and infanticide.
Overall, the data highlights the need for continued efforts to promote gender equality and combat gender-based discrimination and harmful practices.







2.1 find the bottom 2 countries with the lowest adult femle literacy rate in 2019 
SELECT
  *
FROM 
  career_nub.gender_data
WHERE 
  indicator in ('Literacy rate, adult female')
  AND year = 2019
ORDER BY value
LIMIT 2;
 
interpretation
From this dataset, we can see that the adult female literacy rates in Pakistan and Togo in 2019 were 46.49% and 55.05%, respectively. These rates suggest that a significant portion of adult women in these countries may not have the basic reading and writing skills necessary to fully participate in society and access important information.
Solutions 
One possible solution to address this issue is to invest in education programs that specifically target girls and women, particularly in rural and marginalized communities where educational opportunities may be limited. This can involve initiatives such as building schools, providing scholarships, and promoting female teachers and mentors.

In addition, efforts to address broader socio-economic and cultural factors that contribute to low female literacy rates, such as poverty, early marriage, and gender-based discrimination, can also be effective. This can involve policies and programs that address gender inequality, promote women's empowerment, and provide social protections and support.






2.2 find the change in adult female literacy rate between 2012 and 2020 in Bangladesh 
SELECT
  *
FROM career_nub.gender_data
WHERE 
  year BETWEEN 2012 AND 2019
  AND indicator='Literacy rate, adult female'
  AND country = 'Bangladesh'
ORDER BY year;

 
Interpreation 
From this dataset on literacy rate, adult female in Bangladesh, we can draw the following conclusions:
1.	The literacy rate for adult females in Bangladesh has been increasing steadily over the years from 2012 to 2019.
2.	In 2019, the literacy rate for adult females in Bangladesh was around 72%.
3.	While the progress in literacy rate is encouraging, there is still a significant gender gap in education, with male literacy rates being higher than female literacy rates.
Solutions 
1.	Addressing cultural barriers: Some communities in Bangladesh may not prioritize education for females due to cultural norms and beliefs. Educating communities about the benefits of education for females can help change this mindset.
2.	Improving access to education: Access to education can be improved by building more schools in rural areas, increasing the availability of textbooks and learning materials, and providing transportation for students who have to travel long distances to attend school.
3.	Providing incentives for female education: Providing scholarships or other incentives to girls who attend school can encourage families to prioritize education for their daughters.
2.3 find the number of female children  out of primary school as a percentage of overall children out of primary chool in Cameroon by each year 
SELECT
  year,
  SUM(CASE WHEN indicator = 'Children out of school, primary, female' THEN value END) AS     female_OutOfPrimarySchool_population,
  SUM(value) AS total_children_OutOfPrimarySchool_population,
  100.0 * SUM(CASE WHEN indicator = 'Children out of school, primary, female' THEN value END) / SUM(value) AS perc_female_OutOfPrimarySchool_population
FROM 
  career_nub.gender_data 
WHERE
  indicator IN ('Children out of school, primary, female', 'Children out of school, primary, male')  
  AND country = 'Cameroon'
GROUP BY 1;

 
Interpretation 
From the data provided, we can see that the number of females out of primary school has increased from 2016 to 2019, whereas the total number of children out of primary school has decreased during the same period. Additionally, the percentage of females out of primary school has also decreased over time.
Solutions 
To address this issue, potential solutions could include increasing funding for girls' education programs, providing safe transportation for girls to attend school, addressing cultural and social norms that prioritize boys' education over girls', and providing support and resources for families who may face economic barriers to educating their daughters. Additionally, efforts to improve overall primary school enrollment and reduce dropout rates should continue to be a priority, as this will likely have a positive impact on girls' access to education as well.




 3.1 which are the best worst countries based on the female & male life expetency among  SAARC countries in 2020 
SELECT
  country,
  AVG(CASE WHEN indicator = 'Life expectancy at birth, female' THEN value END) AS "Life expectancy at birth for females",
  AVG(CASE WHEN indicator = 'Life expectancy at birth, male' THEN value END) AS "Life expectancy at birth for males"
FROM 
  career_nub.gender_data 
WHERE 
  country IN ('Afghanistan', 'Bangladesh', 'Bhutan', 'India', 'Maldives', 'Nepal', 'Pakistan', 'Sri Lanka')
  AND year = 2020
GROUP BY 1
ORDER BY 2 DESC;

 
interpretation
From the data provided, we can see that in general, females have a higher life expectancy at birth than males in all of the countries listed. However, there is variation in the difference between female and male life expectancy across countries. For example, the difference is smaller in Maldives and Sri Lanka, and larger in Afghanistan and Pakistan.
solutions
improving access to healthcare for all individuals, regardless of gender, and working to eliminate gender-based discrimination and inequality. Additionally, efforts to promote gender equality in education, employment, and other areas could help to address underlying societal factors that contribute to differences in life expectancy between men and women.
In addition, targeted interventions may be needed in countries where the difference in life expectancy between genders is particularly large. For example, efforts to improve men's access to healthcare and address cultural barriers that prevent men from seeking healthcare may be necessary in countries like Afghanistan and Pakistan. 
3.2 compare the female and male inder 5 mortality rates in the year 2020  among SAARC countries 
SELECT
  country,
  AVG(CASE WHEN indicator = 'Mortality rate, under-5, female' THEN value END) AS "Average under-5 mortality rate for females ",
  AVG(CASE WHEN indicator = 'Mortality rate, under-5, male' THEN value END) AS "Average under-5 mortality rate for males "
FROM 
  career_nub.gender_data 
WHERE 
  country IN ('Afghanistan', 'Bangladesh', 'Bhutan', 'India', 'Maldives', 'Nepal', 'Pakistan', 'Sri Lanka')
  AND year = 2020
GROUP BY 1
ORDER BY 2 DESC;

 
interpretation
From the data provided, we can see that in general, under-5 mortality rates for males are higher than for females in all countries listed. However, there is variation in the difference between male and female under-5 mortality rates across countries. For example, the difference is relatively small in Pakistan and Afghanistan, and larger in Sri Lanka and Maldives.
solution
To address this issue, potential solutions could include improving access to healthcare and other resources for all children, regardless of gender. Additionally, efforts to eliminate gender-based discrimination and promote gender equality in education, employment, and other areas could help to address underlying societal factors that contribute to differences in child mortality between boys and girls.
In addition, targeted interventions may be needed in countries where the difference in under-5 mortality rates between genders is particularly large. For example, efforts to improve boys' access to healthcare and address cultural barriers that prevent boys from seeking healthcare may be necessary in countries like Sri Lanka and Maldives. 

3.3 Find the countries that has the highest Prevalence of HIV among females in the age group 15-24 in the year 2020 
SELECT
  country,
  indicator,
  value
FROM 
  career_nub.gender_data 
WHERE
  indicator = 'Prevalence of HIV, female (% ages 15-24)'
  AND year = 2020
ORDER BY value DESC
LIMIT 5;
 
interpretation
From the data provided, we can see that the prevalence of HIV among females aged 15-24 is particularly high in some African countries, including South Africa, Lesotho, Botswana, Mozambique, and Zambia. This is a concerning trend as young women are particularly vulnerable to HIV infection.
solutions
To address this issue, potential solutions could include improving access to comprehensive sexual and reproductive health services, including HIV prevention, testing, and treatment. This could involve increasing funding for public health initiatives and programs that target young women, as well as increasing awareness about HIV and reducing stigma surrounding the disease.
In addition, efforts to promote gender equality and empower young women could help to address underlying societal factors that contribute to the high prevalence of HIV among this group. This could involve improving access to education and economic opportunities, as well as challenging social norms and attitudes that perpetuate gender inequality and limit young women's ability to protect themselves from HIV infection.



4.1 how has the pourcentage of female emplyment in agriculture changed from 2012 to 2019 
SELECT
  year,
  SUM(CASE WHEN indicator = 'Employment in agriculture, female' THEN value END) AS "Females Employed in Agriculture",
  SUM(CASE WHEN indicator = 'Population employed, female' THEN value END) AS "Total females employed",
  100*SUM(CASE WHEN indicator = 'Employment in agriculture, female' THEN value END) / SUM(CASE WHEN indicator = 'Population employed, female' THEN value END) AS "% Female Employment in Agriculture"
FROM 
  career_nub.gender_data
WHERE 
  year BETWEEN 2012 AND 2019  
GROUP BY 1
ORDER BY 1;

 
interpretation
From the data provided, we can see that a significant proportion of females are employed in the agricultural sector. While the percentage of female employment in agriculture has decreased slightly over the years, it still remains relatively high.
solutions
One solution to ensure that women working in the agricultural sector are not left behind is to prioritize gender-responsive agricultural policies and programs. These policies and programs should recognize and address the unique challenges faced by women in agriculture, such as limited access to land, finance, and technology, as well as discrimination and social norms that limit their participation and decision-making power.
Additionally, efforts to improve access to education and training opportunities for women in agriculture could help to promote their skills and knowledge, and enhance their productivity and competitiveness. This could involve initiatives to improve literacy and numeracy skills, as well as training in agricultural practices, marketing, and entrepreneurship.

4.2 How has the pourcentage of female employment in the industry sector changed from 2012 to 2019 
SELECT
  year,
  SUM(CASE WHEN indicator = 'Employment in industry, female' THEN value END) AS "Females Employed in Industry",
  SUM(CASE WHEN indicator = 'Population employed, female' THEN value END) AS "Total females employed",
  100*SUM(CASE WHEN indicator = 'Employment in industry, female' THEN value END) / SUM(CASE WHEN indicator = 'Population employed, female' THEN value END) AS "% Female Employment in Industry"
FROM 
  career_nub.gender_data
WHERE 
  year BETWEEN 2012 AND 2019  
GROUP BY 1
ORDER BY 1;

 
interpretation
The data shows the percentage of females employed in industry out of the total female employment, and how it has changed from 2012 to 2019. Here are some conclusions and solutions that can be derived from this data:There has been a slight decline in the percentage of female employment in industry from 2012 to 2019, which may suggest that fewer women are pursuing careers in the industrial sector.
Solutions 
Governments and organizations can  provide incentives for companies to hire and promote women in industrial fields, and create policies that support work-life balance and the advancement of women in the workforce.
Additionally, efforts to promote and celebrate female role models and success stories in industrial fields can help to break down stereotypes and encourage more women to pursue careers in these areas.

4.3 How has the pourcentage of female employment in the service sector changed from  2012 too 2019 
SELECT
  year,
  SUM(CASE WHEN indicator = 'Employment in services, female' THEN value END) AS "Females Employed in Services",
  SUM(CASE WHEN indicator = 'Population employed, female' THEN value END) AS "Total females employed",
  100*SUM(CASE WHEN indicator = 'Employment in services, female' THEN value END) / SUM(CASE WHEN indicator = 'Population employed, female' THEN value END) AS "% Female Employment in Services"
FROM 
  career_nub.gender_data
WHERE 
  year BETWEEN 2012 AND 2019  
GROUP BY 1
ORDER BY 1;
 
intrpretation
Based on the data provided, we can conclude that the percentage of female employment in the services sector has been consistently increasing over the years. In 2012, it was around 51%, and by 2019, it had increased to almost 57%.
Solutions 
to providing vocational training and skill development programs to women, particularly in the areas of technology and finance. Encouraging entrepreneurship among women could also help them take advantage of opportunities in the services sector.
Governments and private organizations could also create policies and initiatives to improve the work environment for women, such as promoting work-life balance, providing maternity and childcare benefits, and implementing measures to prevent harassment and discrimination in the workplace. This could encourage more women to join the services sector and continue working in it, leading to greater gender equality and economic growth.


5.1 How has the female debit card  ownership changed in 2017 compared to 2014 
SELECT
  year,
  SUM(CASE WHEN indicator = 'Debit card ownership, female, 15+' THEN value END) AS "Females who own a debit card",
  SUM(CASE WHEN indicator = 'Population, female, 15+' THEN value END) AS "Adult female population",
  100*SUM(CASE WHEN indicator = 'Debit card ownership, female, 15+' THEN value END) / SUM(CASE WHEN indicator = 'Population, female, 15+' THEN value END) AS "% Females who own a debit card"
FROM 
  career_nub.gender_data
WHERE 
  year IN (2014,2017)
GROUP BY 1
ORDER BY 1;

 
Interpretation
From the given data, we can conclude that there has been a significant increase in the percentage of adult females who own a debit card between 2014 and 2017. In 2014, only 35.79% of adult females owned a debit card, while in 2017, this percentage increased to 42.73%.
solutions
To increase the percentage of females who own a debit card, governments and financial institutions can work on providing financial education to women, especially in rural areas.
 They can also work on reducing the gender gap in financial inclusion by promoting women's access to financial services, including access to savings and credit facilities.
 Finally, increasing the number of bank branches and ATMs in rural areas can also help to increase the number of females who own a debit card.





5.2 Find the five countries with the lowest female debit card ownership in 2017 
SELECT
  country,
  indicator,
  value
FROM 
  career_nub.gender_data 
WHERE
  indicator = 'Debit card ownership, female (% age 15+)'
  AND year = 2017
ORDER BY value
LIMIT 5;

 
Interpretation 
The data suggests that the percentage of females who own a debit card is quite low in these countries. This could be due to a lack of access to banking services, financial education, or cultural and societal factors that limit women's financial independence.
Solutions 
To improve the situation, governments and financial institutions could work to increase access to banking services in these countries, particularly in rural areas. 
Providing financial education to women could also be beneficial, as it would help them better understand how to use and manage financial tools like debit cards.
 Cultural and societal barriers may require a longer-term approach, such as promoting gender equality and empowering women through education and economic opportunities.





6.1 How has the capital human index for females in india changed from 2017 to 2020 
SELECT
  *
FROM 
  career_nub.gender_data
WHERE indicator = 'Human Capital Index (HCI), Female'
  AND country = 'India'
  AND year IN (2017, 2020);
 
interpretation
The Human Capital Index (HCI) measures the knowledge, skills, and health that individuals accumulate over their lifetime, and how productive they can be with those assets. The increase in the HCI value from 2017 to 2020 for females in India suggests that there has been progress in improving access to education and healthcare, which are key components of human capital. However, the HCI value for females in India still remains low, indicating that there is still a lot of work to be done in terms of improving access to education and healthcare for women in the country.
Solutions 
Some potential solutions to improve the HCI for females in India could include:
1.	Improving access to education: This could involve increasing the number of schools and colleges, providing scholarships and financial assistance, and implementing policies to encourage girls to attend and complete school.
2.	Improving access to healthcare: This could involve increasing the number of healthcare facilities, training more healthcare professionals, and implementing policies to improve the quality of healthcare.
3.	Addressing cultural and social barriers: Many girls in India face barriers to education and healthcare due to cultural and social norms. Addressing these barriers could involve working with community leaders and stakeholders to change attitudes and behaviors towards women and girls.
4.	Increasing female participation in the workforce: Encouraging more women to participate in the workforce can improve their access to education and healthcare, as well as increase their earning potential and overall economic empowerment. This could involve implementing policies to promote gender equality in the workplace, providing training and support to female entrepreneurs, and increasing access to financial services

6.2 which are the best 5 countries based on Human Capital Index for females in 2020 
SELECT
  country,
  indicator,
  value
FROM 
  career_nub.gender_data
WHERE
  indicator = 'Human Capital Index (HCI), Female'
  AND year = 2020
ORDER BY value DESC
LIMIT 5;

 
Interpretation 
The Human Capital Index (HCI) measures the knowledge, skills, and health that people accumulate over their lives. A higher HCI score indicates that a country's population is more productive and has the potential to contribute more to economic growth.
From the given data, we can conclude that the female population of Singapore has the highest HCI score (0.8899) among the selected countries, which indicates that they have better access to education, health services, and job opportunities. Hong Kong SAR, China, Finland, Korea, Rep., and Estonia also have relatively high HCI scores for females, indicating that their female populations have good access to education and health services.
Solutions 
To improve the HCI score for females in other countries, the government and relevant organizations can focus on initiatives that promote equal access to education and healthcare services, reduce gender-based discrimination in the workplace, and increase female labor force participation. These efforts can include policies such as improving infrastructure, providing financial incentives for female education, promoting gender equality in the workplace, and creating more job opportunities for women.


6.3 which are the worst five countries based on the human capital index (HCI) for females in 2020 
SELECT
  country,
  indicator,
  value
FROM 
  career_nub.gender_data
WHERE
  indicator = 'Human Capital Index (HCI), Female'
  AND year = 2020
ORDER BY value
LIMIT 5;

 
Interpretation 
The Human Capital Index (HCI) measures the human capital that a child born today can expect to attain by age 18, given the risks of poor health and poor education that prevail in the country where she lives. It combines indicators of health, education, and learning to create a composite score that reflects the productivity of the next generation of workers.
Looking at the values provided for these countries, we can conclude that the HCI for females is low in these countries, indicating that there are significant challenges in providing access to quality education and healthcare for girls and women. This can result in a large portion of the female population being underutilized in the labor market, which can negatively impact economic growth and development.
Solutions 
To address this issue, there needs to be a focus on improving access to education and healthcare for girls and women. This can include initiatives to increase enrollment and retention of girls in schools, improve the quality of education, and provide access to healthcare services that are specifically tailored to the needs of women and girls. Investing in human capital development for girls and women can have significant long-term benefits for individuals, communities, and countries as a whole.

6.4 Find the number of the countries each year where a woman cannot get a job the same way a man can 
SELECT
  year,
  COUNT(CASE WHEN value = 0 THEN country END) AS "Countries where women cannot get job same way as a man",
  COUNT(country) AS "Total Countries"
FROM 
  career_nub.gender_data 
WHERE
  indicator = 'A woman can get a job in the same way as a man (1=yes; 0=no)'
GROUP BY 1
ORDER BY 1;

 
Interpretation 
Based on the data provided, we can conclude that there has been a gradual decrease in the number of countries where women cannot get a job the same way as a man from 2012 to 2020. In 2012, the number of countries where this was the case was 23 out of 181, while in 2020, it decreased to 17 out of 181. This indicates that there is some progress being made towards gender equality in the workplace, but there is still a long way to go.
Solutions 
Possible solutions to further improve gender equality in the workplace include implementing policies and programs to eliminate gender bias in recruitment, promotions, and pay, promoting and encouraging women's education and training opportunities, and increasing women's representation in leadership positions. Additionally, raising awareness and challenging gender stereotypes and biases can also contribute to creating a more inclusive and equitable workplace for women.



6.5 List all countries where all of this still happen 
SELECT
  year,
  country,
  indicator,
  value
FROM 
  career_nub.gender_data 
WHERE
  indicator = 'A woman can open a bank account in the same way as a man (1=yes; 0=no)'
  AND year = 2020
  AND value = 0;

 
Interpretation 
The data provided shows that in 2020, in some countries such as Bhutan, Equatorial Guinea, Guinea-Bissau, Kenya, and Suriname, women are not able to open a bank account in the same way as men. This can have negative implications for women's financial inclusion and their ability to access financial services, which are important for economic empowerment.
Solutions 
To address this issue, governments and financial institutions can take steps to promote women's financial inclusion, such as implementing policies to ensure equal access to financial services and products, increasing financial literacy and education for women, and improving infrastructure for financial services in underserved areas. Additionally, efforts can be made to address cultural and societal barriers that may prevent women from accessing financial services.
