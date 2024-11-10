# Insurance Cost Prediction

**Project Overview**
This project aims to predict the insurance premiums for individuals based on various health, demographic, and personal factors. Accurate premium prediction helps insurance companies offer fair pricing while managing risk effectively. This project explores and models the factors affecting premium costs using machine learning techniques, and the model is deployed to facilitate real-time premium predictions.

---

**Problem Statement**
Insurance companies need to determine appropriate premium costs for individuals based on several risk factors. This involves assessing the likelihood of high-value claims for each applicant, often challenging due to various influencing factors. By predicting Premium Price, insurers can better manage their portfolios, ensuring fair and effective pricing.

---

**Target Metric**
The key metric for this regression problem is the R-squared (R²) score on both the training and test sets. A higher R² indicates a better fit of the model to the data, demonstrating accurate predictions of insurance premiums based on the input factors.

---

**Solution Workflow**
The solution involves several stages, from understanding the dataset to model deployment:

Exploratory Data Analysis (EDA):

Analyzed the dataset's variables, identifying relationships between features and the target variable, Premium Price.
Key findings included strong correlations between premium prices and factors like age, history of transplants, BMI (calculated from height and weight), and chronic health conditions.

Hypothesis Testing:

Assessed hypotheses on significant predictors:
Age: Older individuals generally have higher premiums due to increased health risks.
AnyTransplants: Transplant history significantly impacts premium costs due to ongoing care needs.
Chronic Diseases: Presence of chronic conditions leads to higher premiums.
Results confirmed these hypotheses, supporting their inclusion in the final model.

Feature Engineering:
Created a BMI feature based on height and weight, enhancing the predictive power for health-related costs.
Categorical variables such as Number of Major Surgeries were converted to numerical representations.
Machine Learning Modeling:

Model Selection: We tried multiple regression models, including Linear Regression, Decision Trees, XGBoost Regressor, Random Forest Regressor and Neural Network.
Random Forest was selected as the final model due to its superior performance and ability to handle complex feature interactions.

Hyperparameter Tuning: Optimized the Random Forest model using Grid Search to achieve the best predictive accuracy.

Insights and Recommendations:
Key Factors: Age, AnyTransplants, Weight, Chronic Diseases, and Family History of Cancer were identified as major drivers of premium costs.

Business Recommendations:
Suggestions for targeted wellness programs, personalized pricing based on high-risk factors, and data-driven strategies to enhance pricing accuracy.

---
**Final Model Performance**

The final Random Forest model achieved the following scores:

Training R² Score: 93%
Testing R² Score: 89%

These scores indicate that the model generalizes well to new data, accurately predicting premium costs across diverse input values.

---
**Deployment Process**
The model was deployed using Streamlit Application:

Built an interactive web interface with Streamlit to capture user inputs and display predicted premium costs.
The app integrates the trained Random Forest model and a pre-trained scaler for feature transformation.

Here's the link: https://insurancepredictorapppy-bhvshrikant.streamlit.app/

---
**Insights and Future Enhancements**

Dynamic Premium Adjustments: Using the model's predictions, insurers can adjust premiums dynamically for different risk profiles.
Wellness Program Integration: Target high-risk individuals with custom wellness programs to potentially reduce claim costs.
Expanded Dataset: Future improvements can include more health-related features to refine model accuracy.
