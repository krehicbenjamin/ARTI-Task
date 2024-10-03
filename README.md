1. How would you scale this (or similar) solution to support large datasets (range of tens of GBs) for training?

From what I could gather strategies like Parallelization, Batch processing and data chuncking will help us scale the this to support latger data sets. Aditionally using distributed computing and their supported frameworks that allow data processin and training across multiple machiines and nodes which enables us to work with larger datasets in a scalable way.

2. How would you scale this (or similar) solution to support large datasets (range of tens of GBs) through APIs?

Strategies that help us with this issue are batch processing, optimizing payload size, load balancing, chunking data and implementing data proprocessing pipelines.
   
3. How would you scale this (or similar) solution to support large number of API calls?
   
To make the system handle more api calls we can implement the following rate limiting, caching, api gateways and load balancers, and async proocessing.
   
4. Both models are having same label variable. Why is one of them better than another one?

(Time Series Model) LSTM -  This model may perform better on sequential or time-dependent data because it captures temporal dependencies between data points.

(Regression Model) XGBoost - XGBoost is better suited for tabular data that lacks a clear temporal component. It can capture complex non-linear relationships and interactions between features.


How to start the app: 
Have the path ready for your python.dll (this has do be done locally in the Program.cs file to have .Net native python compiling.

When you open the app (preferably in Visual Studio) update the fields 
Runtime.PythonDLL 
PythonEngine.PythonHome

When startitring the application you can press the green play button with https next to it. Both models have separate controllers and services for easier checking.
