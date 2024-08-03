# 🌾 Crop Recommendation and Yield Prediction

Welcome to the Crop Recommendation and Yield Prediction project! This project aims to provide valuable insights to farmers by recommending the best crops to cultivate based on soil and weather conditions and predicting crop yields to optimize agricultural practices.

## 🌟 Project Overview
Agriculture plays a vital role in the economy, and optimizing crop selection and yield prediction can significantly enhance productivity and sustainability. This project leverages machine learning techniques to recommend suitable crops and predict their yields based on weather patterns and soil conditions.

# Data Preparation

## 🌟 Challenges
Data preparation is the most challenging task for building this application. Our aim is to generate crop recommendations and yield predictions for farmers based on parameters like temperature, humidity, rainfall, and soil conditions such as N, P, K, and pH using Machine Learning.

The most challenging part is finding data to train ML algorithms. Although there is vast data available on the internet, it is often random, unorganized, and isolated to each attribute. We need to use the available data from various sources and organize it in the right format to train an ML algorithm that is diverse enough to recommend crops or predict yield in various weather and soil conditions, instead of confining it to a particular region limited by data availability.

## 📋 Procedure
The objective is to prepare data to train machine learning models for recommending crops to farmers and predicting crop yields based on weather and soil parameters.

### 📚 Data Sources
The data is sourced from various datasets available on Kaggle:

- **Crop Recommendation Dataset**: Contains soil parameters and recommended crops.
- **Indian Agriculture Crop Production Dataset**: Contains crop production data.
- **District Coordinates Dataset**: Contains geographic coordinates of districts.
- **Soil Data**: Contains soil information.

### 📊 Process Flow Diagram

```text
+-----------------------------------------------------------+
|                       🚀 Start                             |
+-----------------------------------------------------------+
                |
                v
+-----------------------------------------------------------+
|                   📥 Load Datasets                        |
|-----------------------------------------------------------|
| - Load crop recommendation data                           |
| - Load crop production data                               |
| - Load district coordinates                               |
| - Load soil data                                          |
+-----------------------------------------------------------+
                |
                v
+-----------------------------------------------------------+
|                   🔄 Merge Datasets                       |
|-----------------------------------------------------------|
| - Merge crop and production data on 'District'            |
| - Merge with district coordinates on 'District'           |
| - Merge with soil data on 'District'                      |
+-----------------------------------------------------------+
                |
                v
+-----------------------------------------------------------+
|                   ☁️ Fetch Weather Data                   |
|-----------------------------------------------------------|
| - Define API function to fetch weather data               |
| - Iterate through merged data and fetch weather data      |
| - Process and merge weather data                          |
+-----------------------------------------------------------+
                |
                v
+-----------------------------------------------------------+
|                   🛠️ Final Data Preparation               |
|-----------------------------------------------------------|
| - Process combined data                                   |
| - Handle missing values, normalize features               |
| - Save final combined data to CSV                         |
+-----------------------------------------------------------+
                |
                v
+-----------------------------------------------------------+
|                       🏁 End                              |
+-----------------------------------------------------------+
```

# 🌾 Crop Recommendation Model

The crop recommendation model is designed to suggest the most suitable crops for cultivation based on various soil parameters and weather conditions. By leveraging machine learning techniques, the model analyzes the relationship between input features and the recommended crops to provide accurate and data-driven recommendations to farmers.

## 🧠 Model Used: Random Forest Classifier

### 🔧 Parameters
- **n_estimators**: 100
- **max_depth**: 10
- **min_samples_split**: 2
- **min_samples_leaf**: 1

### 📊 Classification Report
```text
              precision    recall  f1-score   support

           0       1.00      1.00      1.00         3
           1       1.00      1.00      1.00        12
           2       1.00      1.00      1.00        13
           3       1.00      1.00      1.00         7
           4       1.00      1.00      1.00        15

    accuracy                           1.00        50
   macro avg       1.00      1.00      1.00        50
weighted avg       1.00      1.00      1.00        50
.:. Random Forest: 100.000% .:.

Note : Here the model had great score with test data also but the 100% accuracy is due to less data availability.
       The model will perform better when retrained wwith large amount of data. But limited availability of data might compromise it           capability
```

# 🌾 Yield Prediction Model

The yield prediction model is designed to estimate the agricultural yield of crops based on various input features such as soil properties, weather conditions, and historical production data. This model uses the Random Forest Classifier to analyze complex relationships between the input parameters and yield outcomes, providing accurate yield predictions to help farmers and agricultural planners make informed decisions.

## 🧠 Model Used: Random Forest Classifier

### 🔧 Parameters
- **n_estimators**: 568
- **min_samples_split**: 16
- **min_samples_leaf**: 7
- **max_depth**: 3

### 📊 Performance Metric
- **RMSE for Random Forest**: 0.5483




