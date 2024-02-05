from scraping import dataframes

hitter_1_pitch_count_0_0 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("R_batter_1") and key.endswith("0_0")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("0_0")
        ),
    ]
    if any(key.startswith("R_batter_1") and key.endswith("0_0") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("0_0")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("0_0")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("0_0") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_1_pitch_count_0_0 = [
    item for item in hitter_1_pitch_count_0_0 if item is not None
]

# Assuming hitter_1_pitch_count contains a valid entry
if hitter_1_pitch_count_0_0:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_1_pitch_count_0_0[0][0]
    pitcher_df = hitter_1_pitch_count_0_0[0][1]

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

    # Perform element-wise multiplication
    result_df = batter_df[columns_to_multiply].multiply(pitcher_df[columns_to_multiply])

    # Add a new row that contains the sum of each column
    result_df.loc["Sum"] = result_df.sum(axis=0)

    # Remove rows with all NaN values
    result_df = result_df.dropna(how="all")

    # Replace hitter_1_pitch_count with the multiplied dataframe
    hitter_1_pitch_count_0_0 = result_df

    print(hitter_1_pitch_count_0_0)

