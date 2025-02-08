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

1. Use linear methods like linear regression to model the trend of budget and overtime pay and predict for upcoming year. 
2. Train a Decision Tree using features like rank, tenure, age, gender, and race to determine which groups are more likely to have low worked-to-paid ratios.
3. Use Z-score analysis to compute the ratio of overtime paid vs. actual hours worked and detect extreme values


## **Data Visualization:**

Tools: Matplotlib, Seaborn, PowerBI

1. Line charts - Show how BPD’s budget has changed over the years.
2. Stacked Bar Chart – Displays how budget allocation has shifted among departments over time
3. Boxplot – Compares BPD salaries vs. other city employees to show salary distribution.
4. Pie Chart – Illustrates the proportion of BPD salaries coming from injury pay.
5. Scatter Plot – Shows the relationship between overtime hours worked vs. overtime hours paid.
6. Decision Tree Diagram – If the Decision Tree model is used, we will visualize it.


## **Test Plan:**



1. Data Splitting: 20% of the dataset is withheld as a test set, while 80% is used for training, ensuring that both training and testing sets represent the demographic diversity of the workforce.
2. Sequential Testing: Train models using historical data from the past years (e.g., 2011-2022) and validate the forecasting model with the most recent data from 2023.
3. Cross-Validation: Implement k-fold cross-validation on the training set to ensure model robustness and minimize overfitting.
4. Cross-Testing Through Different Models: Each model’s performance will be evaluated on the test set, comparing results across metrics.
