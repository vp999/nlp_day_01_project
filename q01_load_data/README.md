# Load data 

Your job is to read the files present in data given.

## Write a function `q01_load_data` that 
- Specifically loads the data from four categories mentioned below
    - `alt.atheism`
    - `soc.religion.christian`
    - `comp.graphics` 
    - `sci.med`
-  Makes use of function `load_files`.  

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| path | String | compulsory |  | Path of data folder |
| seed | int | optional | 9 | Seed value |



### Returns:

| Return | dtype | description |
| --- | --- | --- | 
| data | sklearn.utils.bunch | text belonging to each category of data |
| X_train | list | training data set |
| X_test | list | testing data set |
| y_train | numpy.ndarray |training target variable|
| y_test | numpy.ndarray  |testing target variable |
