import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv("adult.data", header=None, names=[
        "age", "workclass", "fnlwgt", "education", "education-num", "marital-status",
        "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss",
        "hours-per-week", "native-country", "salary"
    ])

    df["salary"] = df["salary"].str.strip()

    race_count = df["race"].value_counts()
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)
    percent_bachelors = round((df["education"] == "Bachelors").mean() * 100, 1)

    advanced_edu = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    higher_ed_rich = round((df[advanced_edu]["salary"] == ">50K").mean() * 100, 1)
    lower_ed_rich = round((df[~advanced_edu]["salary"] == ">50K").mean() * 100, 1)

    min_work_hours = df["hours-per-week"].min()
    min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_percentage_min_workers = round((min_workers["salary"] == ">50K").mean() * 100, 1)

    country_earnings = df.groupby("native-country")["salary"].value_counts(normalize=True).unstack().fillna(0)
    highest_earning_country = country_earnings[">50K"].idxmax()
    highest_earning_country_perc = round(country_earnings[">50K"].max() * 100, 1)

    india_rich = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]
    top_IN_occupation = india_rich["occupation"].value_counts().idxmax()

    result = {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percent_bachelors": percent_bachelors,
        "higher_ed_rich": higher_ed_rich,
        "lower_ed_rich": lower_ed_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage_min_workers": rich_percentage_min_workers,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_perc": highest_earning_country_perc,
        "top_IN_occupation": top_IN_occupation
    }

    if print_data:
        for key, value in result.items():
            print(f"{key}:\n{value}\n")

    return result
