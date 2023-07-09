# Pandas Rechunking

Run `pytest decorators_lru` to run all of the tests
Run `python ./decorators_lru/run.py` to run a test script
Edit the solution.py file and run.py files only 

## Problem

Write a function (skeleton below) that takes a list of pandas dataframes of varying number of rows, but the same columns, and resizes them into fixed size chunks. If there is a remainder at the end then this must be yielded also.

```python
def rechunk_dataframes(dataframes: List[pd.DataFrame], fixed_size: int) -> Iterator[pd.DataFrame]:
    # Your code here
    pass
```

The motivation for this problem comes from the real-world scenario of pulling in a large number of rest requests and needing to write them to a database. Certain database drivers are limited to inserting a maximum number of rows. Use this method to minimise the number of network requests in your code by chunking up the returns from the rest api.

#### Example

**input**
fixed_size = 2

| Name  | Age | City     |
|-------|-----|----------|
| John  | 25  | New York |
| Jane  | 30  | London   |
| Emily | 28  | Sydney   |


| Name | Age |   City   |
|------|-----|----------|
| Bob  | 30  | Madrid   |


|  Name  | Age |     City     |
|--------|-----|--------------|
| Jack   | 25  |   New York   |
| Peter  | 30  |    London    |
| Paul   | 35  |    Paris     |

**output**

| Name  | Age | City     |
|-------|-----|----------|
| John  | 25  | New York |
| Jane  | 30  | London   |


| Name | Age |   City   |
|------|-----|----------|
| Emily| 28  | Sydney   |
| Bob  | 30  | Madrid   |


|  Name  | Age |     City     |
|--------|-----|--------------|
| Jack   | 25  |   New York   |
| Peter  | 30  |    London    |

|  Name  | Age |     City     |
|--------|-----|--------------|
| Paul   | 35  |    Paris     |