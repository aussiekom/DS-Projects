### Anomaly Detection in Time Series Data 

It is useful to detect anomalies in time series data before modelling for forecasting. Many forecasting models are autoregressive, meaning that they take into account past values to make predictions. A past outlier will definitely affect the model, and it can be a good idea to remove that outlier to get more reasonable predictions.

**Types of anomaly detection tasks in time series**
There are two main types of anomaly detection tasks with time series data:

* Point-wise anomaly detection
* Pattern-wise anomaly detection

In the first type, we wish to find single points in time that are considered abnormal. *For example, a fraudulent transaction is a point-wise anomaly.*

The second type is interested in finding subsequences that are outliers. *An example of that could be a stock that is trading at an abnormal level for many hours or days.*
