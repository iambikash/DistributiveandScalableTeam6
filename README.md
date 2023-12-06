# DistributiveandScalableTeam6

Abstract 
Predicting house prices involves accounting for multiple factors beyond traditional 
aspects like size and location. This project aimed to develop a robust House Price 
Prediction model incorporating socio-economic and environmental variables, utilizing 
the XGBoost algorithm. Our methodology involved exploratory data analysis, feature 
engineering, and model selection to enhance predictive accuracy. Transitioning to AWS, 
we deployed our model using EC2, enabling user interaction through a comprehensive 
front-end. The model's performance surpassed market standards, providing valuable 
insights into crime rates, proximity to hospitals/schools, and detailed housing cost 
breakdowns by state, establishing it as an advanced tool for commercial applications in 
real estate decision-making

Exploratory Data Analysis
Our initial approach to this problem was to obtain the data we felt was needed to solve
the problem. We found datasets that provided information such as proximity to schools, 
hospitals, and the prevailing crime rate in the area, as well as their overall costs during 
different time periods. We also obtained information such as number of floors, amenities
per household, and so on.
Initially, our analysis centered on evaluating school data alongside the corresponding 
crime rates. Recognizing the presence of Canadian data within the dataset intended for 
American statistics, we meticulously excluded this information to ensure the accuracy of 
our insights. Utilizing geopandas, we visually represented the geographical distribution 
of schools and hospitals.
To refine our analysis, we recalculated the crime rates, diligently addressing any 
missing values by employing a method that substituted them with median values. 
Subsequently, a comprehensive merge of the hospital, crime, and school datasets was 
conducted, organizing the information based on the respective US states they 
originated from.
Our exploration extended beyond the immediate data sets, encompassing the 
examination of the Average Sales Price per Unit Square (ASPUS) from 1963 to 2020. 
Our visualization revealed a substantial increase in ASPUS over time, notably observing 
a rise from 19300 in 1963 to 323000 in 2020. Further examination, focusing specifically 
on the years 1990, 1995, 2000, and 2023, unveiled significant spikes in the ASPUS for 
the latter year.
Due to the excessive number of available columns, delving deeply into each was 
impractical. To streamline our analysis, we opted to narrow our focus by selecting 
specific features and conducting a correlation analysis. Notably, the analysis revealed 
that the most pronounced correlation with the output was observed in the overall quality 
of the house, closely followed by the variables indicating the year built and remodels.
Given our objective of fitting the data into a machine learning model, we encountered 
non-numeric values within certain fields. To address this, we employed the label 
encoder from the sklearn library. This transformation facilitated the conversion of non- numeric values into a numeric format, enabling seamless integration into our model.
Our initial phase involved feature engineering, primarily focusing on scaling among 
other techniques. To assess the dataset's predictive capabilities, we experimented with 
a range of models including random forest, logistic regression, nearest neighbor, 
decision tree, bagging and boosting regressors, and the xgb regressor. Across these 
models, the mean absolute error consistently ranged between 16000 to 33000.
However, upon rigorous evaluation, the gradient boosting model exhibited the most 
promising performance, yielding the minimum Mean Squared Error (MSE) of 16000. 
Given this superior performance, we concluded that the gradient boosting model was 
the most suitable choice for our predictive task. Finally, we serialized the output of the 
XGBoost model using the pickle functionality.
Front End
For our final project, necessitating diverse operations such as user input processing and 
result prediction, we provisioned a new EC2 instance, opting for a t2 medium type. This 
choice facilitated the multitude of tasks crucial for our project's execution.
Transitioning from local host to AWS services was driven by a paramount concern for 
security. Primarily, we embarked on this transition by uploading the serialized pickle file 
onto the EC2 instance. Simultaneously, recognizing the size constraints of our files, we 
stored the necessary data files for analysis in an S3 bucket.
Leveraging boto3, we seamlessly interacted with the files housed in the S3 bucket, 
ensuring smooth access and retrieval of the essential data. Establishing the application 
structure, we crafted 'app.py', 'index.html', and 'result.html' files to facilitate the user 
interaction and prediction process.
