# Count the tokenized words

Your job is to convert a collection of text documents to matrix of token counts.

## Write a function `q04_count_vectors` that 
- Makes use of input data from `q01_load_data` question.
- Convert the training data into pandas series.
- Removes the stop words on the tokenized text using.
- Fits and transforms the tokenized training data using `CountVectorizer`.
- Transforms the test data.

Note : You need to specify the `decode_error as 'ignore'` while using `CountVectorizer`.


### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| path | String | compulsory |  | Path of data folder |
| ranges | tuple | optional | (1,2) | value of n_grams |
| max_df | float | optional | 0.5 | ignore terms freq that are higher than max_freq |
| min_df | float | optional | 2.0 | ignore terms freq that are lower than min_freq |




### Returns:

| Return | dtype | description |
| --- | --- | --- | 
| variable1 | scipy.sparse.csr.csr_matrix | transformed train data |
| variable2 | scipy.sparse.csr.csr_matrix | transformed test data |

