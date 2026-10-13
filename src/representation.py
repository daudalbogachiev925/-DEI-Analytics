def representation(df, group_col):
    return df[group_col].value_counts(normalize=True).round(3).to_dict()

def by_level(df, group_col):
    return df.groupby(["level", group_col]).size().unstack(fill_value=0)

def leadership_representation(df, group_col, leader_levels=("Lead", "Director")):
    leaders = df[df["level"].isin(leader_levels)]
    return leaders[group_col].value_counts(normalize=True).round(3).to_dict()
