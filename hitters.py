import pandas as pd
from scraping import dataframes

# Get all keys that end with "0_0"
keys_0_0 = [key for key in dataframes if key.endswith("0_0")]

# Pair up batter and pitcher dataframes
pairs_0_0 = [
    (dataframes[batter_key], dataframes[pitcher_key])
    for batter_key in keys_0_0 if batter_key.startswith("batter")
    for pitcher_key in keys_0_0 if pitcher_key.startswith("pitcher")
]

columns_to_convert = [
        "Ball",
        "Strike",
        "Swing",
        "Foul",
        "Whiffs",
        "BIP",
        "GB",
        "LD",
        "FB",
        "PU",
        "HR",
    ]

# Perform the conversion on each pair
for batter_df, pitcher_df in pairs_0_0:
    for df in [batter_df, pitcher_df]:
        for column in columns_to_convert:
            df[column] = pd.to_numeric(df[column].str.strip("%"), errors="coerce") / 100.0

# Columns to multiply
columns_to_multiply = [
    "Ball",
    "Strike",
    "Swing",
    "Foul",
    "Whiffs",
    "BIP",
    "GB",
    "LD",
    "FB",
    "PU",
    "HR",
]

# Perform element-wise multiplication on each pair and store the results
results = []
for batter_df, pitcher_df in pairs_0_0:
    result_df = batter_df[columns_to_multiply].multiply(pitcher_df[columns_to_multiply])
    result_df.loc["Sum"] = result_df.sum(axis=0)
    result_df = result_df.dropna(how="all")
    results.append(result_df)
print(results)