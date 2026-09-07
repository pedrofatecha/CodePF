# Data

The data we will be working with in this repo is [this dataset of 7+ million companies](https://www.kaggle.com/datasets/peopledatalabssf/free-7-million-company-dataset) from Kaggle.

To demonstrate the power of embedded databases, the data is converted to parquet format via `polars` as shown below.

1. Unzip the CSV file `companies_sorted.zip`
2. Make sure to run `pip3 install polars` prior to running the Python code snippet below.

```py
import polars as pl

df = pl.read_csv("companies_sorted.csv")
df.write_parquet("companies_sorted.parquet")
```

This saves the data to a parquet file. We'll use it in our speed test.