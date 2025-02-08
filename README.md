## **Project Description:**

The project aims to conduct a thorough analysis of the Boston Police Department (BPD)’s budget, specifically focusing on overtime expenditures. Given the significant operating budget of over $400 million allocated to the BPD, understanding how funds are spent, particularly in the context of overtime, is crucial for ensuring accountability and transparency. The project will involve cleaning, analyzing, and visualizing overtime data to answer key questions regarding shifts in budget, patterns in overtime pay, and potential inequities within the department.


## **Clear Goals:**



1. Analyze how the BPD budget has changed in 2011-2023, and identify trends in funding growth or shrinkage across departments.
2. Analyze patterns in overtime pay, comparing it to regular pay and against non-BPD city employees.
3. Use previous overtime data in 2011-2023 to predict overtime pay for the upcoming year, and compare it to the allocated budget.
4. Determine how much of BPD’s total payroll comes from injury pay and the percentage of officers receiving it annually.
5. Track annual financial trends of overtime hours paid compared to overtime hours worked and any discrimination in that trend.
6. Determine whether specific demographics (e.g., senior, male, high-ranking, long-tenured officers) are more likely to have lower worked-to-paid overtime ratios.
7. Analyze the distribution of overtime worked versus paid ratios and identify outliers.


## **Data Collection:**

The following datasets will be collected and utilized:



1. Employee basic Data: Access payroll data from 2011-2023, including job title, name, department name, regular pay.
2. Overtime Data: Collect comprehensive overtime records from 2012-2022, including Records overtime pay and special duty pay to analyze work patterns and additional compensation.
3. Injury compensation Data: Includes injury pay to assess the financial impact of work-related injuries.
4. Quinn Education Incentive: Captures Quinn education payments, reflecting additional earnings from continued education.
5. Total Earnings: Represents the sum of all earnings, allowing for salary comparisons across different roles and individuals.



## **Data Modeling:**


## **Data Visualization:**

The visualization strategy will include:



1. Interactive Dashboards: Utilize Power BI to create comprehensive dashboards showcasing budget shifts, overtime patterns, and demographic comparisons.
2. Visualizations:
    * Time Series Plots: To show changes in budget allocations over the years.
    * Bar Charts: To compare average overtime pay versus regular pay.
    * Scatter Plots: To illustrate correlations between demographics and overtime worked-to-paid ratios.
3. Geospatial Analysis: Use ArcGIS to map overtime distribution and field activities geographically.
4. Correlation Chart: To visualize relationships between key variables, identifying trends and dependencies.


## **Test Plan:**



1. Data Splitting: 20% of the dataset is withheld as a test set, while 80% is used for training, ensuring that both training and testing sets represent the demographic diversity of the workforce.
2. Sequential Testing: Train models using historical data from the past years (e.g., 2011-2022) and validate the forecasting model with the most recent data from 2023.
3. Cross-Validation: Implement k-fold cross-validation on the training set to ensure model robustness and minimize overfitting.
4. Cross-Testing Through Different Models: Each model’s performance will be evaluated on the test set, comparing results across metrics.
