"""
Dask is a library that's used for distributing computing across multiple
threads, processes, or even computers in order to effectively perform
computation at a huge scale. This can greatly improve performance and
throughput, even if you are working on a single laptop computer. Dask provides
replacements for most of the data structures from the Python scientific stack,
such as NumPy arrays and Pandas DataFrames. These replacements have very similar
interfaces, but under the hood, they are built for distributed computing so that
they can be shared between multiple threads, processes, or computers. In many
cases, switching to Dask is as simple as changing the import statement, and
possibly adding a couple of extra method calls to start concurrent computations.

This module illustrates how to use Dask to do some simple computations on a
DataFrame.
"""
import dask.dataframe as dd

data = dd.read_csv("miscellaneous-topics/sample.csv")
print(data.head())

sum_data = data.lower + data.upper
print(sum_data)

result = sum_data.compute()
print(result.head())

means = data.loc[:, ("lower", "upper")].mean().compute()
print(means)
