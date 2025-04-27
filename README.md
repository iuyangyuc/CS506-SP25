# Final Report

> Final Presentation Link: 

## Install Dependencies

```
# Terminal
pip install -r requirements.txt

# MacOS
chmod +x install.sh
./install.sh

# Windows
# double click install.bat
```

## Project Structure

```
CS506-SP25/
│
├── README.md               
├── requirements.txt        
│
├── code/       
│   ├── q1.ipynb	# ipynb files run all the visualizations for specific questions
│   ├── q2_4.ipynb
│   ├── q3_5.ipynb
│   ├── q6_7.ipynb
│   ├── process.py	# store functions to preprocess data
│   ├── regression.py	# store functions for machine learning
│
├── data/       
│   ├── Overtime/
│   ├── budget/
│   ├── earning/
```

We organized all data visualization functions and analysis code into separate Jupyter Notebook files corresponding to each specific question. To improve code reusability and maintainability, we encapsulated all common data loading and preprocessing routines into standalone Python modules, which are imported and reused across different notebooks.

## How To Run

```
cd code
# Run All Cells In Notebooks: Kernel -> Restart & Run All
# If you have jupyter in your environment, you can run the following scripts to run notebooks automatically and save the outputs to ./output

# MacOS
./run.sh

# Windows
#Double click run.bat
```

## **Project Description**

The project aims to conduct a thorough analysis of the Boston Police Department (BPD)’s budget. Given the significant operating budget of over $4.6 billion allocated to the BPD, understanding how funds are spent, particularly in the context of overtime, is crucial for ensuring accountability and transparency. The project will involve cleaning, analyzing, and visualizing overtime data to answer key questions regarding shifts in budget, patterns in overtime pay, and potential inequities within the department.

## **Clear Goals**
1. Analyze how the BPD budget has changed in 2011-2024, and identify trends in funding growth or shrinkage across departments.
2. Analyze patterns in overtime pay, comparing it to regular pay and against non-BPD city employees.
3. Use previous overtime data in 2011-2024 to predict overtime pay for the upcoming year, and compare it to the allocated budget.
4. Determine how much of BPD’s total payroll comes from injury pay and the percentage of officers receiving it annually.
5. Track annual financial trends of overtime hours paid compared to overtime hours worked and any discrimination in that trend.
6. Determine whether specific demographics (e.g., senior, male, high-ranking, long-tenured officers) are more likely to have lower worked-to-paid overtime ratios.
7. Analyze the distribution of overtime worked versus paid ratios and identify outliers.

## **Dataset Collection**
The following datasets are collected and utilized:

**Earnings**: Employee Earnings Report dataset (2011-2024). Each year, the City of Boston publishes payroll data for employees. This dataset contains employee names, department names, job details, and earnings information including base salary, overtime, and total earnings, etc.

**Budget**: The FY25 Adopted Operating Budget totals \$4.64 billion and represents an increase of \$345 million, or 8.0%, over FY24. The adopted version reflects the finalized budget accepted by the City Council. The City's budget is planned and built on the program level for each department. This dataset contains expense categories of appropriations to each department and program from the City's General Fund for the year starting July 1, 2024 and ending June 30, 2025.

**Overtime**:Overtime dataset(2012-2020). This dataset contains employee rank, employee hours worked,  employee hours paid and etc.

## **Data Modeling:**
Linear model: Using the scikit-learn library, a linear model was developed to forecast overtime pay trends across various departments. Despite the model's current simplicity, it is projected that overtime pay will continue to increase.

## **Data Processing:**
**Tools**: Pandas, Re, Numpy

For the Earning dataset in the CSV file, many data fields need to be standardized. For example, remove the dollar sign ($) from salary values, unify the representation of missing values in the table, and use Pandas for format conversion, such as applying regular expressions for batch processing. 

Handle outliers by replacing them with the mean or mode, perform data type conversions (e.g., converting between date formats and integers), and convert string data to floating-point numbers to facilitate computation.



## **Data Visualization:**

*Please run the notebooks to reproduce the visualizations and interact with some interactive plots.*

**Tools**: Matplotlib, Seaborn, Plotly

1. **Line plot**: We used line plots to visualize the change of BPD paycheck and changes of ratios of overtime paid hours. (See the section below for details).

   It is also used to visualize the trend of the overtime pay for several departments. And the show the result of the preliminary result of the linear model of question3.

2. **Box plot**: We used box plot to visualize the distribution of Overtime Worked/Paid Ratio and Injured Pay ratio. It can help us analyze spread, central tendency and outliers of the data.Also it can help us compare difference between groups of data.

   ![1](./img/1.png)

   We also use it to visualize the distribution of Overtime Worked/Paid Ratio in 2020,    which can help us to find the outlier in these dataset-values that are significantly higher or lower than the rest of the data.

   ![2](./img/2.png)

3. **Bar plot**: We used bar plot to show comparisons between different categories like the budget by expense category and earnings of different job titles.
    It is also used to visualize the earnings differences between ranks within the same department.(See the section below for details)


## **Result**
### 1. How has the BPD budget changed year-over-year?
#### Assumptions

1. Budget Categories Are Consistent:
2. Budget Growth Reflects Real Increases, Not Inflation Alone:
3. Minimal Reallocation Between Categories:is calculated using the **mean of TOTAL_GROSS** per department per year.
4. Which positions within a police department have the highest salaries? What is the primary salary structure?
5. What were the trends in police department budgets and compensation from 2020 to 2024?
6. How does the police department's compensation compare to that of other municipal departments?
7. Are there departments where employees receive additional compensation, such as disability pay, due to high-risk job roles?


#### Observations
  To identify where there was financial excess in BPD spending we first looked at how the BPD budget had changed year over year. We looked at data from 2022-2025 as this was available to us from the City Of Boston. The overall budget was broken up into seven categories: Contractual Services, Current Charges & Obligation, Equipment, Fixed Expenses, Other Expenses, Personnel Services, and Supplies and Materials. To determine how the budget has changed between these categories, we looked at the percent each category made up of the total budget.From the graph, it is evident that Personnel Services consistently accounted for the largest portion of the total budget across all fiscal years from 2022 to 2025. This category highlights the significant costs associated with salaries and benefits, which dominate the overall spending. Year over year, while other categories such as Contractual Services, Current Charges & Obligations, and Supplies & Materials show relatively minimal changes in their share of the budget, the increasing trend in Other Expenses and Fixed Expenses suggests growing commitments or new initiatives that demanded additional funding. Notably, Equipment and Supplies & Materials remain the smallest contributors to the budget each year, indicating these areas are less prioritized. Despite these being essential for operations, their consistent low allocation reflects that BPD likely focuses resources on personnel-related and operational necessities rather than physical assets or materials. By 2025, the overall budget shows a consistent increase compared to previous years, with the largest growth occurring in Personnel Services and Other Expenses. This trend points to potential financial excess in staffing costs and operational overhead.

![3](./img/3.png)

  Analyzing the top ten highest-earning police department occupations from 2020 to 2024 reveals that Policy Officer consistently holds the top spot in total income. This is unsurprising, given the large proportion of officers in this role. Almost all occupations experienced relatively stable earnings from 2020 to 2023, with an increase in 2024, likely reflecting the increased Total Budget shown in the figure above.

![4](./img/4.png)

  Lastly we looked at the changes in funding between departments. To do this we looked at earnings data from 2012-2022. From this we were able to see which departments received the highest salaries and therefore the most budget for that category, focusing on the top 10 departments.As the image shows, the police department has consistently been the highest-earning department between 2020 and 2024, with a significant increase in 2024. While other departments have remained relatively stable, this suggests a budget increase for the police department in 2024.

![5](./img/5.png)

To better analyze the variations in revenue growth, we created a detailed revenue and expenditure analysis for the top ten departments in total revenue for both 2020 and 2024, as shown in the image below.

![14](./img/14.png)
![15](./img/15.png)

The charts indicate that the Boston Police Department and Boston Fire Department have the highest regular salaries, likely due to the inherent risks of their work. Overtime pay data confirms frequent overtime in these departments, and they also exhibit the highest rates of injury and associated compensation, unlike other departments which report almost no injuries. Additionally, the Boston Police Department's involvement in education and training contributes to their comparatively higher salaries.

Next, we compared the 2020 and 2024 income data within the Boston Police Department.

![16](./img/16.png)

Based on our previous analysis, we know that the total revenue in 2024 is greater than that in 2020. Comparing the charts, we observe an increase in regular wages and overtime pay in 2024 compared to 2020, while other income components remained relatively stable. This indicates that the company increased compensation for employees' regular and overtime hours in 2024, reflecting a greater recognition of employee labor value and enhanced incentives. The stability in other income items (such as bonuses and allowances) suggests a consistent policy in these areas. Therefore, the increase in total revenue in 2024 is primarily attributed to the growth in regular wages and overtime pay.

Another interesting point is that the number of INJURED in 2020 is slightly higher than in 2024. We calculated the average, maximum, and variance of INJURED for both 2020 and 2024. The data is as follows:
2020 Injured - Max: 25272021.09, Mean: 4231181.3149999995, Variance: 80574886206358.27 
2024 Injured - Max: 20552550.44, Mean: 4105282.082, Variance: 68899807503967.93
Based on the data, the number of extremely high injury compensation cases decreased significantly from 2020 to 2024, and the overall distribution became more compact and equitable. This may be due to policy adjustments, improved management practices, or stricter subsidy reviews.
* Since the killing of George Floyd in 2020, social movements calling for police reform and defunding the police have put pressure on budget allocations. These protests spurred audits and discussions of police budgets by city governments. Despite intentions to cut police spending, the actual result has been increased budgets. Many discussions have suggested shifting some police funding to [public health and community safety programs](https://baystatebanner.com/2024/09/19/boston-police-to-reach-record-breaking-100-million-overtime-budget/).
* Personnel costs consistently account for the largest portion of the BPD's budget, primarily due to rising salaries and benefits. Analysis indicates that the BPD's budget increased by $9.88 million in 2024, mainly to recruit and retain officers, reflecting a continued need for increased recruitment and training of new officers, for example, to [mitigate attrition](https://data.aclum.org/2023/05/05/analyzing-fy24-boston-police-department-budget-recommendation/).
* The BPD's overtime costs are steadily rising. The high-risk nature of police work contributes to relatively high salaries and overtime pay, which significantly impacts overall expenditures, especially during periods of [economic constraint](https://www.baystatebanner.com/2024/09/19/boston-police-to-reach-record-breaking-100-million-overtime-budget/).
* The wage increase for injured workers may be due to increased compensation amounts resulting from rising workplace [health and safety standards](https://www.bostonglobe.com/metro/2016/07/04/boston-police-officers-injured-duty-collect-big-paychecks/BF6J6tyHgCPPY6nYcWkFbJ/story.html).

### 2. How have BPD paychecks changed year-over-year? Both the average amount, as compared with non-BPD Boston city.

#### Assumptions

1. Only non-BPD departments that **exist in all years** from 2011 to 2024 are included in the comparison.
2. Among those non-BPD departments, only the **top 10 by employee count** are selected.
3. Average gross pay is calculated using the **mean of TOTAL_GROSS** per department per year.

![6](img/6.png)

#### Observations

This chart shows that all non-BPD departments except Boston Fire Department (BPD)—including Human Resources, City Council, Libraries, Youth Services, and Budget Management—consistently earn much lower average pay than BPD and BFD, generally between \$40,000 and \$90,000.

* BFD leads in pay across almost all years. The Boston Fire Department consistently has the highest average gross pay from 2011 to 2024, except for 2017, where BPD briefly overtook it. In 2024, the BFD average salary exceeds $180,000, maintaining its top position despite BPD’s rapid growth.
* BPD is a strong second, with a sharp spike in 2024. Despite this surge, BPD still remains second to BFD in 2024, but the gap narrows significantly.
* In 2024, both BPD and BFD experienced substantial spikes in average gross pay, likely due to a combination of new collective bargaining agreements, increased overtime from high-profile events (e.g., the Emerson College protests), and retroactive pay. For BPD, this [retroactive compensation](https://www.wbur.org/news/2025/03/12/boston-police-salaries-city-employee#:~:text=In%20Boston%2C%20the,2024%27s%20pay) stemmed from a newly ratified five-year contract that covered wages dating back to 2020, while BFD’s increase followed a similar contract adjustment retroactive to 2021. These factors collectively contributed to sharp year-over-year earnings growth, particularly among frontline public safety personnel.

### 3. Given previous overtime data, predict the amount of overtime paid for the next year. How does this compare with the budget allocation for the BPD?

#### Assumptions
* Data for over time payment are gathered from overtime databased. 
* Department summary are caluated to decided the top 5 department 

#### Observations

* The timing of the FY2016 overtime reduction suggests a connection to City actions taken in response to the FY2015 overspending crisis, specifically initiatives aimed at controlling Police overtime.
* The COVID-19 pandemic significantly influenced BPD operations and overtime throughout FY2021, both reducing traditional overtime needs and creating new pandemic-related ones.

##### FY2016
* Data indicates a reduction in actual BPD overtime spending between FY2015 and FY2016. Expenditures decreased by $2.4 million (4%), falling from $59.9 million to $57.5 million.
This decrease followed FY2015, a year marked by exceptionally high overtime overspending where the department exceeded its budget by $24.9 million (70.9%), the largest deficit in a decade.
Consequently, the $57.5 million spent in FY2016, though lower than the previous year's peak, was still substantial. Given the historical pattern of overspending, it is highly probable that this amount exceeded the specific budget allocated for FY2016 (the exact FY2016 budget figure and deficit are not provided in the source material).
The reduction in FY2016 appears to represent a partial pullback from an extreme outlier year due to increased scrutiny, rather than a sustainable shift towards meeting budgeted spending levels.

##### FY2021:

* Despite a significant reduction in the overtime budget for FY2021, the department's actual overtime spending, while lower than the previous year, far exceeded this new budget target.
* Actual overtime expenditures in FY2021 decreased by approximately $6.48 million compared to the $74 million spent in FY2020, resulting in actual FY2021 spending of around $67.5 million. Some sources report total incurred overtime was slightly higher, exceeding $68.2 million.
 


![7](./img/7.png)

### 4. How much BPD officer pay came from injury pay? What percentage of officers took injury pay in a given year?

#### Assumptions

1. Officers with non-null “Injured” pay values are considered to have received injury compensation.
2. The injury pay ratio is defined as: (Injury Pay) / (Total Gross) per officer.
3. Average injury pay ratios are computed on a per-year basis.
4. The proportion of injured officers each year is: (Number of officers with injury pay) / (Total number of officers that year).

![8](./img/8.png)



![9](./img/9.png)

#### Observations

The charts show the percentage of total gross pay that came from injury compensation for BPD officers and the percentage of BPD officers who received injury pay each year from 2011 to 2024. On average, around 17% of BPD officers received injury compensation annually. The data reveals significant spikes in the injury rate among Boston Police Department (BPD) officers in the years 2014, 2020, 2021, and 2024. These spikes are accompanied by notable fluctuations in the injury pay ratio—sharp increases in 2020–2022 and notably low ratios in 2014 and 2024

- In 2014, the percentage of injured officers spiked to over 25%, while the injury pay ratio remained unusually low. In this year, national protests following the deaths of [Michael Brown](https://en.wikipedia.org/wiki/Killing_of_Michael_Brown) and [Eric Garner](https://en.wikipedia.org/wiki/Killing_of_Eric_Garner) led to large-scale demonstrations in Boston. This suggests that a large number of officers may received minor injury compensation during large-scale public protests, which could explain the low injury pay ratio. 
- In 2020 and 2021, both injury participation and average injury pay ratio increased significantly, likely due to the [George Floyd protests in Boston](https://en.wikipedia.org/wiki/George_Floyd_protests_in_Massachusetts) and continued pandemic-related stress and enforcement duties. A [high-risk standoff in Dorchester](https://www.wgbh.org/news/politics/2021-11-11/wu-calls-tuesdays-police-shooting-an-example-of-large-systemic-failure?utm_source=chatgpt.com) also contributed to officer injuries in 2021. 
- Most recently, in 2024, the proportion of injured officers reached a record high (over 30%), but the average injury pay ratio dropped sharply.  This suggests widespread but minor injuries, likely associated with the [pro-Palestinian encampment removal at Emerson College](https://www.wcvb.com/article/boston-police-arrest-protesters-clear-pro-palestinian-encampment-at-emerson-college/60600586?utm_source=chatgpt.com), where over 100 arrests were made and several officers were hurt. 

These observations suggest that surges in injury rates may be closely tied to periods of civil unrest and intense policing demands.

### 5. How do overtime hours paid compare to overtime hours worked? What does the discrepancy financially amount to, year after year?

#### Assumptions
* Overtime is gathered form overtime dataset. 
* Calculated by subtracted 8 from total hours worked.

#### Observations
* Fiscal Year 2020 (FY20): The BPD was budgeted $60.8 million for overtime but ultimately spent $74.7 million, exceeding the allocation by $13.9 million or 23%.14  This overspending occurred despite the cancellation of many large public events due to the COVID-19 pandemic, which might have been expected to reduce overtime needs.10
* Fiscal Year 2021 (FY21): Amid calls for police reform, the City reallocated funds, resulting in a nominal overtime budget "cut" from $60 million to $48 million.5  However, projections early in the fiscal year indicated spending was on track to significantly exceed this reduced budget.5  Actual incurred overtime spending for FY21 totaled $68.2 million, surpassing the budget by $19.4 million.


![8](./img/19.png)

### 6. Are certain officers (e.g., white, old, male, long tenure, high ranking title) more likely than others to have lower worked-to-paid ratios?

#### Assumptions

1.  Since we lack certain demographic and employment details for some officers—such as race, age, and tenure—this analysis focuses specifically on the relationship between rank and worked-to-paid overtime ratios.
2. the numerical rank values (e.g., 3, 4, 8, 9) consistently represent levels of authority or seniority, where higher numbers denote higher-ranking officers.
3. The worked-to-paid ratio is defined as: (worked hour) / (paid hour) per officer. 
4. The analysis assumes that the absence of demographic and employment variables (like race, tenure, or age) does not substantially confound the observed relationship between rank and overtime ratios. 

   ![10](./img/10.png)

#### Observations

The data suggests a clear trend: higher-ranking officers tend to have lower worked-to-paid overtime ratios. In other words, they are typically paid for significantly more overtime hours than they report working.
- As shown in the chart, officers with higher ranks (e.g., 8 and 9) have the lowest average ratios, while those with lower ranks (e.g., 3 and 4) show higher ratios, indicating that their reported worked hours are more closely aligned with the overtime hours paid.

- One possible reason for this discrepancy is that higher-ranking officers may have more discretion or administrative authority in approving overtime, which could lead to less standardized documentation of their actual work hours.

In conclusion, officers with higher-ranking titles appear more likely to receive overtime pay disproportionate to their reported work hours, highlighting potential disparities in how overtime is allocated or documented across ranks.

### 7. **What is the distribution of ratios of overtime worked vs. overtime paid? Are there any outliers? (Hours Worked/WRKDHRS vs Hours Paid/OTHOURS in the court OT database).**

#### Assumptions

1. The worked-to-paid ratio is defined as: (worked hour) / (paid hour) per officer. 

   ![11](./img/11.png)

#### Observations

* The distribution of the ratios of overtime paid hours to court worked hours is right-skewed, with a large number of observations clustered at lower ratios (0.1 to 0.3). And there are smaller peaks near 0.5 and 0.95–1.0, indicating some officers are being paid overtime that closely aligns with, or nearly equals, the number of hours worked.

- The worked-to-paid ratio has shown a consistent decline from 2014 to 2020, dropping from about 0.55 to 0.37. This trend indicates that over time, employees are being paid for more overtime hours than they report working on average. 
- The drop between 2018 and 2020 is especially sharp, which may point to policy shifts, systemic inefficiencies, or underreporting of actual hours worked.
  
- The sharp drop in the ratio in 2020 was very likely related to the COVID-19 pandemic.That year, Boston experienced multiple lockdowns, leading to reduced public activity and shifts in police deployment, which disrupted the usual structure of overtime work.

- It’s also possible that opportunities for reporting overtime changed, or that some officers received overtime compensation without actually working additional hours — for example, through special allowances or standby duty. From the [Local news](https://baystatebanner.com/2021/05/05/councilors-struggle-to-rein-in-police-overtime/), this article provides concrete evidence that the drop in the overtime “worked hours/paid hours” ratio in 2020 was likely influenced by structural compensation rules, civil unrest, and pandemic disruptions — all of which inflated paid hours without necessarily increasing actual work time.

- For the question of are there any outliers, since the drop in 2020 is significantly larger than the gradual changes observed in previous years.
  We draw the box plot of 2020 data and set the threshold to 0.1, as we believe extremely low ratio values may be skewing the mean distribution in 2020. ![12](./img/12.png) The outliers are shown in the following figure, which are lower than 0.1.

![13](./img/13.png)


## Further Question:
### 1.  Are there systemic inequalities ingrained in the policing system?

#### Assumptions

1. For this problem, we're starting with postal codes to explore whether overtime pay is fair across different regions. Our plan is to analyze the ratio of overtime pay to total earnings. Below is the distribution of this ratio across different regions
2. The postal code and location type are as an indicator for judging the region.
3. Overtime ratio is defined as (total oveertime / total gross)
4. The WRKDHRS / OTHOURS is defined as: (worked hour) / (paid hour) per officer. 


#### Observations
![17](./img/17.png)
- We've observed significant variations in overtime pay rates across different regions. Some zip codes show rates exceeding 0.35, while others are below 0.10. The proportion of overtime earnings by zip code reveals clear regional disparities within the police system.
- This indicates that overtime income is not being distributed equally or fairly across different areas. While this data alone doesn't definitively prove inequality, it does reflect inequitable distribution. Further multi-factor analysis (e.g., demographics, local policies, crime rates) would help determine the underlying causes of these differences.
![18](./img/18.png)
- The chart visualizes the average WRKDHRS / OTHOURS ratio across different locations.
From the distribution, we observe substantial variation across areas:
- Some locations exhibit significantly higher overtime ratios (closer to 0.8), indicating a tighter correspondence between hours worked and overtime compensated. Other locations (less than 0.4) show noticeably lower ratios, suggesting discrepancies between actual working hours and overtime payment.
- The clear gradient in the chart suggests that the overtime compensation practices are not uniform across locations. Instead, there appear to be systematic regional differences in how overtime hours are credited relative to actual work performed.