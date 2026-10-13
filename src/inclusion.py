def inclusion_by_group(df, group_col, score_col="inclusion_score"):
    return df.groupby(group_col)[score_col].mean().round(2).to_dict()

def inclusion_index(df, score_col="inclusion_score"):
    return round(df[score_col].mean(), 2)

def flag_low_inclusion(df, group_col, threshold=3.5, score_col="inclusion_score"):
    by_group = df.groupby(group_col)[score_col].mean()
    return by_group[by_group < threshold].round(2).to_dict()
