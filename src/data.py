import pandas as pd
import numpy as np

def generate_dei_data(n=1500, seed=42):
    np.random.seed(seed)
    return pd.DataFrame({
        "employee_id": [f"E{i:04d}" for i in range(n)],
        "gender": np.random.choice(["M", "F", "Other"], n, p=[0.52, 0.45, 0.03]),
        "age_group": np.random.choice(["<25", "25-34", "35-44", "45-54", "55+"],
                                        n, p=[0.1, 0.35, 0.3, 0.18, 0.07]),
        "ethnicity": np.random.choice(["A", "B", "C", "D"], n, p=[0.5, 0.25, 0.15, 0.1]),
        "level": np.random.choice(["Junior","Middle","Senior","Lead","Director"],
                                    n, p=[0.3, 0.35, 0.2, 0.1, 0.05]),
        "department": np.random.choice(["Engineering","Sales","HR","Marketing"], n),
        "salary": np.random.normal(150000, 50000, n).round(0),
        "inclusion_score": np.random.uniform(1, 5, n).round(1),
    })
