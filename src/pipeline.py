def hiring_funnel_by_group(df_hires, group_col):
    """df_hires: applied, screened, interviewed, hired по группам"""
    return df_hires.groupby(group_col).agg(
        applied=("applied", "sum"),
        screened=("screened", "sum"),
        interviewed=("interviewed", "sum"),
        hired=("hired", "sum"),
    ).assign(
        screen_rate=lambda d: d["screened"] / d["applied"],
        interview_rate=lambda d: d["interviewed"] / d["screened"],
        hire_rate=lambda d: d["hired"] / d["interviewed"],
    ).round(3)
