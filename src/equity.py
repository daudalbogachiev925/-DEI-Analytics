def median_by_group(df, group_col, salary_col="salary"):
    return df.groupby(group_col)[salary_col].median().round(0).to_dict()

def pay_gap(df, group_col, group_a, group_b, salary_col="salary"):
    med_a = df[df[group_col] == group_a][salary_col].median()
    med_b = df[df[group_col] == group_b][salary_col].median()
    if med_a == 0:
        return 0
    return round((med_a - med_b) / med_a * 100, 2)
