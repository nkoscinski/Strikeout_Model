import pandas as pd
from scraping import dataframes

# List of all possible pitch counts
pitch_counts = [
    "0_0",
    "0_1",
    "0_2",
    "1_0",
    "2_0",
    "3_0",
    "1_1",
    "1_2",
    "2_1",
    "2_2",
    "3_1",
    "3_2",
]

# Columns to convert
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

# Initialize an empty list to store the results
all_results = []

# Iterate over all pitch counts
for pitch_count in pitch_counts:
    # Get all keys that end with the current pitch count
    keys = [key for key in dataframes if key.endswith(pitch_count)]

    # Pair up batter and pitcher dataframes
    pairs = [
        (dataframes[batter_key], dataframes[pitcher_key])
        for batter_key in keys
        if batter_key.startswith("batter")
        for pitcher_key in keys
        if pitcher_key.startswith("pitcher")
    ]

    # Perform the conversion on each pair
    for batter_df, pitcher_df in pairs:
        for df in [batter_df, pitcher_df]:
            for column in columns_to_convert:
                df[column] = (
                    pd.to_numeric(df[column].str.strip("%"), errors="coerce") / 100.0
                )

        # Perform element-wise multiplication on each pair and store the results
        result_df = batter_df[columns_to_convert].multiply(
            pitcher_df[columns_to_convert]
        )
        result_df.loc["Sum"] = result_df.sum(axis=0)
        result_df = result_df.dropna(how="all")

        # Append the result to the all_results list
        all_results.append(result_df)

if "__main__" == __name__:
    for pitch_count, result_df in zip(pitch_counts, all_results):
        print(f"Result DataFrame {pitch_count}:\n{result_df}\n")
