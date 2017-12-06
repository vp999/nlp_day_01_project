# Tokenizer

This assignment comprises of implementation of one of the preprocessing steps namely Tokenization.


## Write a function `q02_tokenize` that 
- Makes use of input data from previous question.
- Converts the training data to pandas series.
- Converts all the alphabets to lower case in each row.
- Uses `TreebankWordTokenizer` function to tokenize the training data in string format.



### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| path | String | compulsory |  | Path of data folder |




### Returns:

| Return | dtype | description |
| --- | --- | --- | 
| variable | pandas.core.series.Series | tokenized text belonging to each category of data |
