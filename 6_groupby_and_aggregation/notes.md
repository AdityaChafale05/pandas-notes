# GroupBy & Aggregation in Pandas

GroupBy is used to split data, apply a function, and combine results.

---

## Basic GroupBy
```python
df.groupby("Department")["Salary"].mean()
