import os
import pandas as pd
import numpy as np
import scraping

# Get the dataframes from scraping.py
dataframes = scraping.get_data()

# Assuming dataframes is your dictionary
for df_name, df in dataframes.items():
    [...]

# Assuming your dictionary is named 'dataframes'
for key, df in dataframes.items():
    [...]

print(list(dataframes))


# Assuming dataframes is your dictionary
for df_name, df in dataframes.items():
    # List of columns to convert
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

    # Iterate over each column and perform the conversion
    for column in columns_to_convert:
        df[column] = pd.to_numeric(df[column].str.strip("%"), errors="coerce") / 100.0

# Assuming your dictionary is named 'dataframes'
for key, df in dataframes.items():
    if "batter" in key:
        if "_R_" in key:
            df["Handedness"] = "Right"
        else:
            df["Handedness"] = "Left"

# print(list(dataframes))

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

hitter_1_pitch_count_0_1 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("R_batter_1") and key.endswith("0_1")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("0_1")
        ),
    ]
    if any(key.startswith("R_batter_1") and key.endswith("0_1") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("0_1")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("0_1")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("0_1") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_1_pitch_count_0_1 = [
    item for item in hitter_1_pitch_count_0_1 if item is not None
]

# Assuming hitter_1_pitch_count contains a valid entry
if hitter_1_pitch_count_0_1:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_1_pitch_count_0_1[0][0]
    pitcher_df = hitter_1_pitch_count_0_1[0][1]

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
    hitter_1_pitch_count_0_1 = result_df

hitter_1_pitch_count_0_2 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("R_batter_1") and key.endswith("0_2")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("0_2")
        ),
    ]
    if any(key.startswith("R_batter_1") and key.endswith("0_2") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("0_2")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("0_2")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("0_2") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_1_pitch_count_0_2 = [
    item for item in hitter_1_pitch_count_0_2 if item is not None
]

# Assuming hitter_1_pitch_count contains a valid entry
if hitter_1_pitch_count_0_2:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_1_pitch_count_0_2[0][0]
    pitcher_df = hitter_1_pitch_count_0_2[0][1]

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
    hitter_1_pitch_count_0_2 = result_df

hitter_1_pitch_count_1_0 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("R_batter_1") and key.endswith("1_0")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("1_0")
        ),
    ]
    if any(key.startswith("R_batter_1") and key.endswith("1_0") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("1_0")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("1_0")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("1_0") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_1_pitch_count_1_0 = [
    item for item in hitter_1_pitch_count_1_0 if item is not None
]

# Assuming hitter_1_pitch_count contains a valid entry
if hitter_1_pitch_count_1_0:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_1_pitch_count_1_0[0][0]
    pitcher_df = hitter_1_pitch_count_1_0[0][1]

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
    hitter_1_pitch_count_1_0 = result_df

hitter_1_pitch_count_1_1 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("R_batter_1") and key.endswith("1_1")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("1_1")
        ),
    ]
    if any(key.startswith("R_batter_1") and key.endswith("1_1") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("1_1")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("1_1")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("1_1") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_1_pitch_count_1_1 = [
    item for item in hitter_1_pitch_count_1_1 if item is not None
]

# Assuming hitter_1_pitch_count contains a valid entry
if hitter_1_pitch_count_1_1:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_1_pitch_count_1_1[0][0]
    pitcher_df = hitter_1_pitch_count_1_1[0][1]

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
    hitter_1_pitch_count_1_1 = result_df

hitter_1_pitch_count_1_2 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("R_batter_1") and key.endswith("1_2")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("1_2")
        ),
    ]
    if any(key.startswith("R_batter_1") and key.endswith("1_2") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("1_2")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("1_2")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("1_2") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_1_pitch_count_1_2 = [
    item for item in hitter_1_pitch_count_1_2 if item is not None
]

# Assuming hitter_1_pitch_count contains a valid entry
if hitter_1_pitch_count_1_2:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_1_pitch_count_1_2[0][0]
    pitcher_df = hitter_1_pitch_count_1_2[0][1]

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
    hitter_1_pitch_count_1_2 = result_df

hitter_1_pitch_count_2_0 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("R_batter_1") and key.endswith("2_0")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("2_0")
        ),
    ]
    if any(key.startswith("R_batter_1") and key.endswith("2_0") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("2_0")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("2_0")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("2_0") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_1_pitch_count_2_0 = [
    item for item in hitter_1_pitch_count_2_0 if item is not None
]

# Assuming hitter_1_pitch_count contains a valid entry
if hitter_1_pitch_count_2_0:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_1_pitch_count_2_0[0][0]
    pitcher_df = hitter_1_pitch_count_2_0[0][1]

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
    hitter_1_pitch_count_2_0 = result_df

hitter_1_pitch_count_2_1 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("R_batter_1") and key.endswith("2_1")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("2_1")
        ),
    ]
    if any(key.startswith("R_batter_1") and key.endswith("2_1") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("2_1")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("2_1")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("2_1") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_1_pitch_count_2_1 = [
    item for item in hitter_1_pitch_count_2_1 if item is not None
]

# Assuming hitter_1_pitch_count contains a valid entry
if hitter_1_pitch_count_2_1:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_1_pitch_count_2_1[0][0]
    pitcher_df = hitter_1_pitch_count_2_1[0][1]

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
    hitter_1_pitch_count_2_1 = result_df

hitter_1_pitch_count_2_2 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("R_batter_1") and key.endswith("2_2")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("2_2")
        ),
    ]
    if any(key.startswith("R_batter_1") and key.endswith("2_2") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("2_2")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("2_2")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("2_2") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_1_pitch_count_2_2 = [
    item for item in hitter_1_pitch_count_2_2 if item is not None
]

# Assuming hitter_1_pitch_count contains a valid entry
if hitter_1_pitch_count_2_2:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_1_pitch_count_2_2[0][0]
    pitcher_df = hitter_1_pitch_count_2_2[0][1]

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
    hitter_1_pitch_count_2_2 = result_df

hitter_1_pitch_count_3_0 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("R_batter_1") and key.endswith("3_0")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("3_0")
        ),
    ]
    if any(key.startswith("R_batter_1") and key.endswith("3_0") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("3_0")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("3_0")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("3_0") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_1_pitch_count_3_0 = [
    item for item in hitter_1_pitch_count_3_0 if item is not None
]

# Assuming hitter_1_pitch_count contains a valid entry
if hitter_1_pitch_count_3_0:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_1_pitch_count_3_0[0][0]
    pitcher_df = hitter_1_pitch_count_3_0[0][1]

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
    hitter_1_pitch_count_3_0 = result_df

hitter_1_pitch_count_3_1 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("R_batter_1") and key.endswith("3_1")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("3_1")
        ),
    ]
    if any(key.startswith("R_batter_1") and key.endswith("3_1") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("3_1")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("3_1")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("3_1") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_1_pitch_count_3_1 = [
    item for item in hitter_1_pitch_count_3_1 if item is not None
]

# Assuming hitter_1_pitch_count contains a valid entry
if hitter_1_pitch_count_3_1:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_1_pitch_count_3_1[0][0]
    pitcher_df = hitter_1_pitch_count_3_1[0][1]

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
    hitter_1_pitch_count_3_1 = result_df

hitter_1_pitch_count_3_2 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("R_batter_1") and key.endswith("3_2")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("3_2")
        ),
    ]
    if any(key.startswith("R_batter_1") and key.endswith("3_2") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("3_2")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("3_2")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("3_2") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_1_pitch_count_3_2 = [
    item for item in hitter_1_pitch_count_3_2 if item is not None
]

# Assuming hitter_1_pitch_count contains a valid entry
if hitter_1_pitch_count_3_2:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_1_pitch_count_3_2[0][0]
    pitcher_df = hitter_1_pitch_count_3_2[0][1]

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
    hitter_1_pitch_count_3_2 = result_df


# Extracting 'Sum' row from each df
hitter_1_pitch_count_0_0 = hitter_1_pitch_count_0_0[
    hitter_1_pitch_count_0_0.index == "Sum"
]
hitter_1_pitch_count_0_1 = hitter_1_pitch_count_0_1[
    hitter_1_pitch_count_0_1.index == "Sum"
]
hitter_1_pitch_count_0_2 = hitter_1_pitch_count_0_2[
    hitter_1_pitch_count_0_2.index == "Sum"
]
hitter_1_pitch_count_1_0 = hitter_1_pitch_count_1_0[
    hitter_1_pitch_count_1_0.index == "Sum"
]
hitter_1_pitch_count_1_1 = hitter_1_pitch_count_1_1[
    hitter_1_pitch_count_1_1.index == "Sum"
]
hitter_1_pitch_count_1_2 = hitter_1_pitch_count_1_2[
    hitter_1_pitch_count_1_2.index == "Sum"
]
hitter_1_pitch_count_2_0 = hitter_1_pitch_count_2_0[
    hitter_1_pitch_count_2_0.index == "Sum"
]
hitter_1_pitch_count_2_1 = hitter_1_pitch_count_2_1[
    hitter_1_pitch_count_2_1.index == "Sum"
]
hitter_1_pitch_count_2_2 = hitter_1_pitch_count_2_2[
    hitter_1_pitch_count_2_2.index == "Sum"
]
hitter_1_pitch_count_3_0 = hitter_1_pitch_count_3_0[
    hitter_1_pitch_count_3_0.index == "Sum"
]
hitter_1_pitch_count_3_1 = hitter_1_pitch_count_3_1[
    hitter_1_pitch_count_3_1.index == "Sum"
]
hitter_1_pitch_count_3_2 = hitter_1_pitch_count_3_2[
    hitter_1_pitch_count_3_2.index == "Sum"
]

# Combining all 'Sum' rows into 1 df for transition matrix
dfs = [
    hitter_1_pitch_count_0_0,
    hitter_1_pitch_count_0_1,
    hitter_1_pitch_count_0_2,
    hitter_1_pitch_count_1_0,
    hitter_1_pitch_count_1_1,
    hitter_1_pitch_count_1_2,
    hitter_1_pitch_count_2_0,
    hitter_1_pitch_count_2_1,
    hitter_1_pitch_count_2_2,
    hitter_1_pitch_count_3_0,
    hitter_1_pitch_count_3_1,
    hitter_1_pitch_count_3_2,
]

pitch_counts_hitter_1 = pd.concat(dfs, axis=0, ignore_index=True)
pitch_counts_hitter_1.insert(
    0,
    "Pitch Count",
    [
        "0-0",
        "0-1",
        "0-2",
        "1-0",
        "1-1",
        "1-2",
        "2-0",
        "2-1",
        "2-2",
        "3-0",
        "3-1",
        "3-2",
    ],
)
pitch_counts_hitter_1 = pitch_counts_hitter_1[["Pitch Count", "Ball", "Strike", "BIP"]]

# List of all pitch counts
pitch_counts = pitch_counts_hitter_1["Pitch Count"].tolist()

# Initialize an empty transition matrix with float values
transition_matrix = pd.DataFrame(0.0, columns=pitch_counts, index=pitch_counts)

# Populate the transition matrix with probabilities
for i in range(len(pitch_counts)):
    for j in range(len(pitch_counts)):
        # Weighted sum of 'Strike', 'Ball', and 'BIP' columns for transition probabilities
        transition_matrix.iloc[i, j] = (
            pitch_counts_hitter_1.loc[j, "Strike"]
            + pitch_counts_hitter_1.loc[j, "Ball"]
            + pitch_counts_hitter_1.loc[j, "BIP"]
        )

# Normalize the rows to ensure that each row sums to 1
transition_matrix = transition_matrix.div(transition_matrix.sum(axis=1), axis=0)

# print("Transition Matrix:")
# print(transition_matrix)

# Number of steps to simulate the Markov chain
num_steps = 10

# Initialize a probability vector for each pitch count
initial_probabilities = pd.Series(0.0, index=transition_matrix.index)
initial_probabilities.loc["0-0"] = 1.0

# Simulate the Markov chain
current_probabilities = initial_probabilities.copy()
for _ in range(num_steps):
    current_probabilities = np.dot(current_probabilities, transition_matrix)

# Convert the current_probabilities array to a Pandas Series
current_probabilities_series = pd.Series(
    current_probabilities, index=transition_matrix.index
)

# Calculate the probability of reaching a 2-strike count from any initial pitch count
prob_2_strike = current_probabilities_series.loc[
    ["0-0", "0-1", "0-2", "1-0", "1-1", "1-2", "2-0", "2-1", "2-2", "3-0", "3-1", "3-2"]
].sum()

# Calculate the probability of a strike being called after reaching a 2-strike count
prob_strike_after_2_strike = (
    transition_matrix.loc["2-2", "3-0"]
    + transition_matrix.loc["2-2", "3-1"]
    + transition_matrix.loc["2-2", "3-2"]
)

# Calculate the overall probability of a strikeout in the at-bat
prob_strikeout = prob_2_strike * prob_strike_after_2_strike

# print(f"Probability of reaching a 2-strike count: {prob_2_strike}")
print(
    f"Probability of a strike being called after 2 strikes for hitter 1: {prob_strike_after_2_strike}"
)
# print(f"Probability of a strikeout in the at-bat: {prob_strikeout}")


hitter_2_pitch_count_0_0 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_2") and key.endswith("0_0")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("0_0")
        ),
    ]
    if any(key.startswith("L_batter_2") and key.endswith("0_0") for key in dataframes)
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
hitter_2_pitch_count_0_0 = [
    item for item in hitter_2_pitch_count_0_0 if item is not None
]

# Assuming hitter_2_pitch_count contains a valid entry
if hitter_2_pitch_count_0_0:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_2_pitch_count_0_0[0][0]
    pitcher_df = hitter_2_pitch_count_0_0[0][1]

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

    # Replace hitter_2_pitch_count with the multiplied dataframe
    hitter_2_pitch_count_0_0 = result_df

hitter_2_pitch_count_0_1 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_2") and key.endswith("0_1")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("0_1")
        ),
    ]
    if any(key.startswith("L_batter_2") and key.endswith("0_1") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("0_1")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("0_1")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("0_1") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_2_pitch_count_0_1 = [
    item for item in hitter_2_pitch_count_0_1 if item is not None
]

# Assuming hitter_2_pitch_count contains a valid entry
if hitter_2_pitch_count_0_1:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_2_pitch_count_0_1[0][0]
    pitcher_df = hitter_2_pitch_count_0_1[0][1]

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

    # Replace hitter_2_pitch_count with the multiplied dataframe
    hitter_2_pitch_count_0_1 = result_df

hitter_2_pitch_count_0_2 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_2") and key.endswith("0_2")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("0_2")
        ),
    ]
    if any(key.startswith("L_batter_2") and key.endswith("0_2") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("0_2")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("0_2")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("0_2") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_2_pitch_count_0_2 = [
    item for item in hitter_2_pitch_count_0_2 if item is not None
]

# Assuming hitter_2_pitch_count contains a valid entry
if hitter_2_pitch_count_0_2:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_2_pitch_count_0_2[0][0]
    pitcher_df = hitter_2_pitch_count_0_2[0][1]

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

    # Replace hitter_2_pitch_count with the multiplied dataframe
    hitter_2_pitch_count_0_2 = result_df

hitter_2_pitch_count_1_0 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_2") and key.endswith("1_0")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("1_0")
        ),
    ]
    if any(key.startswith("L_batter_2") and key.endswith("1_0") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("1_0")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("1_0")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("1_0") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_2_pitch_count_1_0 = [
    item for item in hitter_2_pitch_count_1_0 if item is not None
]

# Assuming hitter_2_pitch_count contains a valid entry
if hitter_2_pitch_count_1_0:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_2_pitch_count_1_0[0][0]
    pitcher_df = hitter_2_pitch_count_1_0[0][1]

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

    # Replace hitter_2_pitch_count with the multiplied dataframe
    hitter_2_pitch_count_1_0 = result_df

hitter_2_pitch_count_1_1 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_2") and key.endswith("1_1")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("1_1")
        ),
    ]
    if any(key.startswith("L_batter_2") and key.endswith("1_1") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("1_1")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("1_1")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("1_1") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_2_pitch_count_1_1 = [
    item for item in hitter_2_pitch_count_1_1 if item is not None
]

# Assuming hitter_2_pitch_count contains a valid entry
if hitter_2_pitch_count_1_1:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_2_pitch_count_1_1[0][0]
    pitcher_df = hitter_2_pitch_count_1_1[0][1]

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

    # Replace hitter_2_pitch_count with the multiplied dataframe
    hitter_2_pitch_count_1_1 = result_df

hitter_2_pitch_count_1_2 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_2") and key.endswith("1_2")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("1_2")
        ),
    ]
    if any(key.startswith("L_batter_2") and key.endswith("1_2") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("1_2")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("1_2")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("1_2") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_2_pitch_count_1_2 = [
    item for item in hitter_2_pitch_count_1_2 if item is not None
]

# Assuming hitter_2_pitch_count contains a valid entry
if hitter_2_pitch_count_1_2:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_2_pitch_count_1_2[0][0]
    pitcher_df = hitter_2_pitch_count_1_2[0][1]

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

    # Replace hitter_2_pitch_count with the multiplied dataframe
    hitter_2_pitch_count_1_2 = result_df

hitter_2_pitch_count_2_0 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_2") and key.endswith("2_0")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("2_0")
        ),
    ]
    if any(key.startswith("L_batter_2") and key.endswith("2_0") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("2_0")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("2_0")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("2_0") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_2_pitch_count_2_0 = [
    item for item in hitter_2_pitch_count_2_0 if item is not None
]

# Assuming hitter_2_pitch_count contains a valid entry
if hitter_2_pitch_count_2_0:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_2_pitch_count_2_0[0][0]
    pitcher_df = hitter_2_pitch_count_2_0[0][1]

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

    # Replace hitter_2_pitch_count with the multiplied dataframe
    hitter_2_pitch_count_2_0 = result_df

hitter_2_pitch_count_2_1 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_2") and key.endswith("2_1")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("2_1")
        ),
    ]
    if any(key.startswith("L_batter_2") and key.endswith("2_1") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("2_1")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("2_1")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("2_1") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_2_pitch_count_2_1 = [
    item for item in hitter_2_pitch_count_2_1 if item is not None
]

# Assuming hitter_2_pitch_count contains a valid entry
if hitter_2_pitch_count_2_1:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_2_pitch_count_2_1[0][0]
    pitcher_df = hitter_2_pitch_count_2_1[0][1]

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

    # Replace hitter_2_pitch_count with the multiplied dataframe
    hitter_2_pitch_count_2_1 = result_df

hitter_2_pitch_count_2_2 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_2") and key.endswith("2_2")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("2_2")
        ),
    ]
    if any(key.startswith("L_batter_2") and key.endswith("2_2") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("2_2")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("2_2")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("2_2") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_2_pitch_count_2_2 = [
    item for item in hitter_2_pitch_count_2_2 if item is not None
]

# Assuming hitter_2_pitch_count contains a valid entry
if hitter_2_pitch_count_2_2:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_2_pitch_count_2_2[0][0]
    pitcher_df = hitter_2_pitch_count_2_2[0][1]

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

    # Replace hitter_2_pitch_count with the multiplied dataframe
    hitter_2_pitch_count_2_2 = result_df

hitter_2_pitch_count_3_0 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_2") and key.endswith("3_0")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("3_0")
        ),
    ]
    if any(key.startswith("L_batter_2") and key.endswith("3_0") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("3_0")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("3_0")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("3_0") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_2_pitch_count_3_0 = [
    item for item in hitter_2_pitch_count_3_0 if item is not None
]

# Assuming hitter_2_pitch_count contains a valid entry
if hitter_2_pitch_count_3_0:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_2_pitch_count_3_0[0][0]
    pitcher_df = hitter_2_pitch_count_3_0[0][1]

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

    # Replace hitter_2_pitch_count with the multiplied dataframe
    hitter_2_pitch_count_3_0 = result_df

hitter_2_pitch_count_3_1 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_2") and key.endswith("3_1")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("3_1")
        ),
    ]
    if any(key.startswith("L_batter_2") and key.endswith("3_1") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("3_1")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("3_1")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("3_1") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_2_pitch_count_3_1 = [
    item for item in hitter_2_pitch_count_3_1 if item is not None
]

# Assuming hitter_2_pitch_count contains a valid entry
if hitter_2_pitch_count_3_1:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_2_pitch_count_3_1[0][0]
    pitcher_df = hitter_2_pitch_count_3_1[0][1]

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

    # Replace hitter_2_pitch_count with the multiplied dataframe
    hitter_2_pitch_count_3_1 = result_df

hitter_2_pitch_count_3_2 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_2") and key.endswith("3_2")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("3_2")
        ),
    ]
    if any(key.startswith("L_batter_2") and key.endswith("3_2") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("3_2")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("3_2")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("3_2") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_2_pitch_count_3_2 = [
    item for item in hitter_2_pitch_count_3_2 if item is not None
]

# Assuming hitter_2_pitch_count contains a valid entry
if hitter_2_pitch_count_3_2:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_2_pitch_count_3_2[0][0]
    pitcher_df = hitter_2_pitch_count_3_2[0][1]

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

    # Replace hitter_2_pitch_count with the multiplied dataframe
    hitter_2_pitch_count_3_2 = result_df


# Extracting 'Sum' row from each df
hitter_2_pitch_count_0_0 = hitter_2_pitch_count_0_0[
    hitter_2_pitch_count_0_0.index == "Sum"
]
hitter_2_pitch_count_0_1 = hitter_2_pitch_count_0_1[
    hitter_2_pitch_count_0_1.index == "Sum"
]
hitter_2_pitch_count_0_2 = hitter_2_pitch_count_0_2[
    hitter_2_pitch_count_0_2.index == "Sum"
]
hitter_2_pitch_count_1_0 = hitter_2_pitch_count_1_0[
    hitter_2_pitch_count_1_0.index == "Sum"
]
hitter_2_pitch_count_1_1 = hitter_2_pitch_count_1_1[
    hitter_2_pitch_count_1_1.index == "Sum"
]
hitter_2_pitch_count_1_2 = hitter_2_pitch_count_1_2[
    hitter_2_pitch_count_1_2.index == "Sum"
]
hitter_2_pitch_count_2_0 = hitter_2_pitch_count_2_0[
    hitter_2_pitch_count_2_0.index == "Sum"
]
hitter_2_pitch_count_2_1 = hitter_2_pitch_count_2_1[
    hitter_2_pitch_count_2_1.index == "Sum"
]
hitter_2_pitch_count_2_2 = hitter_2_pitch_count_2_2[
    hitter_2_pitch_count_2_2.index == "Sum"
]
hitter_2_pitch_count_3_0 = hitter_2_pitch_count_3_0[
    hitter_2_pitch_count_3_0.index == "Sum"
]
hitter_2_pitch_count_3_1 = hitter_2_pitch_count_3_1[
    hitter_2_pitch_count_3_1.index == "Sum"
]
hitter_2_pitch_count_3_2 = hitter_2_pitch_count_3_2[
    hitter_2_pitch_count_3_2.index == "Sum"
]

# Combining all 'Sum' rows into 1 df for transition matrix
dfs = [
    hitter_2_pitch_count_0_0,
    hitter_2_pitch_count_0_1,
    hitter_2_pitch_count_0_2,
    hitter_2_pitch_count_1_0,
    hitter_2_pitch_count_1_1,
    hitter_2_pitch_count_1_2,
    hitter_2_pitch_count_2_0,
    hitter_2_pitch_count_2_1,
    hitter_2_pitch_count_2_2,
    hitter_2_pitch_count_3_0,
    hitter_2_pitch_count_3_1,
    hitter_2_pitch_count_3_2,
]

pitch_counts_hitter_2 = pd.concat(dfs, axis=0, ignore_index=True)
pitch_counts_hitter_2.insert(
    0,
    "Pitch Count",
    [
        "0-0",
        "0-1",
        "0-2",
        "1-0",
        "1-1",
        "1-2",
        "2-0",
        "2-1",
        "2-2",
        "3-0",
        "3-1",
        "3-2",
    ],
)
pitch_counts_hitter_2 = pitch_counts_hitter_2[["Pitch Count", "Ball", "Strike", "BIP"]]

# List of all pitch counts
pitch_counts = pitch_counts_hitter_2["Pitch Count"].tolist()

# Initialize an empty transition matrix with float values
transition_matrix = pd.DataFrame(0.0, columns=pitch_counts, index=pitch_counts)

# Populate the transition matrix with probabilities
for i in range(len(pitch_counts)):
    for j in range(len(pitch_counts)):
        # Weighted sum of 'Strike', 'Ball', and 'BIP' columns for transition probabilities
        transition_matrix.iloc[i, j] = (
            pitch_counts_hitter_2.loc[j, "Strike"]
            + pitch_counts_hitter_2.loc[j, "Ball"]
            + pitch_counts_hitter_2.loc[j, "BIP"]
        )

# Normalize the rows to ensure that each row sums to 1
transition_matrix = transition_matrix.div(transition_matrix.sum(axis=1), axis=0)

# print("Transition Matrix:")
# print(transition_matrix)

# Number of steps to simulate the Markov chain
num_steps = 10

# Initialize a probability vector for each pitch count
initial_probabilities = pd.Series(0.0, index=transition_matrix.index)
initial_probabilities.loc["0-0"] = 1.0

# Simulate the Markov chain
current_probabilities = initial_probabilities.copy()
for _ in range(num_steps):
    current_probabilities = np.dot(current_probabilities, transition_matrix)

# Convert the current_probabilities array to a Pandas Series
current_probabilities_series = pd.Series(
    current_probabilities, index=transition_matrix.index
)

# Calculate the probability of a strike being called after reaching a 2-strike count
prob_strike_after_2_strike = (
    transition_matrix.loc["2-2", "3-0"]
    + transition_matrix.loc["2-2", "3-1"]
    + transition_matrix.loc["2-2", "3-2"]
)

print(
    f"Probability of a strike being called after 2 strikes for hitter 2: {prob_strike_after_2_strike}"
)

hitter_3_pitch_count_0_0 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("R_batter_3") and key.endswith("0_0")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("0_0")
        ),
    ]
    if any(key.startswith("R_batter_3") and key.endswith("0_0") for key in dataframes)
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
hitter_3_pitch_count_0_0 = [
    item for item in hitter_3_pitch_count_0_0 if item is not None
]

# Assuming hitter_3_pitch_count contains a valid entry
if hitter_3_pitch_count_0_0:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_3_pitch_count_0_0[0][0]
    pitcher_df = hitter_3_pitch_count_0_0[0][1]

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

    # Replace hitter_3_pitch_count with the multiplied dataframe
    hitter_3_pitch_count_0_0 = result_df

hitter_3_pitch_count_0_1 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("R_batter_3") and key.endswith("0_1")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("0_1")
        ),
    ]
    if any(key.startswith("R_batter_3") and key.endswith("0_1") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("0_1")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("0_1")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("0_1") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_3_pitch_count_0_1 = [
    item for item in hitter_3_pitch_count_0_1 if item is not None
]

# Assuming hitter_3_pitch_count contains a valid entry
if hitter_3_pitch_count_0_1:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_3_pitch_count_0_1[0][0]
    pitcher_df = hitter_3_pitch_count_0_1[0][1]

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

    # Replace hitter_3_pitch_count with the multiplied dataframe
    hitter_3_pitch_count_0_1 = result_df

hitter_3_pitch_count_0_2 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("R_batter_3") and key.endswith("0_2")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("0_2")
        ),
    ]
    if any(key.startswith("R_batter_3") and key.endswith("0_2") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("0_2")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("0_2")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("0_2") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_3_pitch_count_0_2 = [
    item for item in hitter_3_pitch_count_0_2 if item is not None
]

# Assuming hitter_3_pitch_count contains a valid entry
if hitter_3_pitch_count_0_2:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_3_pitch_count_0_2[0][0]
    pitcher_df = hitter_3_pitch_count_0_2[0][1]

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

    # Replace hitter_3_pitch_count with the multiplied dataframe
    hitter_3_pitch_count_0_2 = result_df

hitter_3_pitch_count_1_0 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("R_batter_3") and key.endswith("1_0")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("1_0")
        ),
    ]
    if any(key.startswith("R_batter_3") and key.endswith("1_0") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("1_0")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("1_0")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("1_0") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_3_pitch_count_1_0 = [
    item for item in hitter_3_pitch_count_1_0 if item is not None
]

# Assuming hitter_3_pitch_count contains a valid entry
if hitter_3_pitch_count_1_0:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_3_pitch_count_1_0[0][0]
    pitcher_df = hitter_3_pitch_count_1_0[0][1]

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

    # Replace hitter_3_pitch_count with the multiplied dataframe
    hitter_3_pitch_count_1_0 = result_df

hitter_3_pitch_count_1_1 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("R_batter_3") and key.endswith("1_1")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("1_1")
        ),
    ]
    if any(key.startswith("R_batter_3") and key.endswith("1_1") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("1_1")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("1_1")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("1_1") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_3_pitch_count_1_1 = [
    item for item in hitter_3_pitch_count_1_1 if item is not None
]

# Assuming hitter_3_pitch_count contains a valid entry
if hitter_3_pitch_count_1_1:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_3_pitch_count_1_1[0][0]
    pitcher_df = hitter_3_pitch_count_1_1[0][1]

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

    # Replace hitter_3_pitch_count with the multiplied dataframe
    hitter_3_pitch_count_1_1 = result_df

hitter_3_pitch_count_1_2 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("R_batter_3") and key.endswith("1_2")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("1_2")
        ),
    ]
    if any(key.startswith("R_batter_3") and key.endswith("1_2") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("1_2")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("1_2")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("1_2") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_3_pitch_count_1_2 = [
    item for item in hitter_3_pitch_count_1_2 if item is not None
]

# Assuming hitter_3_pitch_count contains a valid entry
if hitter_3_pitch_count_1_2:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_3_pitch_count_1_2[0][0]
    pitcher_df = hitter_3_pitch_count_1_2[0][1]

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

    # Replace hitter_3_pitch_count with the multiplied dataframe
    hitter_3_pitch_count_1_2 = result_df

hitter_3_pitch_count_2_0 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("R_batter_3") and key.endswith("2_0")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("2_0")
        ),
    ]
    if any(key.startswith("R_batter_3") and key.endswith("2_0") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("2_0")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("2_0")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("2_0") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_3_pitch_count_2_0 = [
    item for item in hitter_3_pitch_count_2_0 if item is not None
]

# Assuming hitter_3_pitch_count contains a valid entry
if hitter_3_pitch_count_2_0:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_3_pitch_count_2_0[0][0]
    pitcher_df = hitter_3_pitch_count_2_0[0][1]

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

    # Replace hitter_3_pitch_count with the multiplied dataframe
    hitter_3_pitch_count_2_0 = result_df

hitter_3_pitch_count_2_1 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("R_batter_3") and key.endswith("2_1")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("2_1")
        ),
    ]
    if any(key.startswith("R_batter_3") and key.endswith("2_1") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("2_1")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("2_1")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("2_1") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_3_pitch_count_2_1 = [
    item for item in hitter_3_pitch_count_2_1 if item is not None
]

# Assuming hitter_3_pitch_count contains a valid entry
if hitter_3_pitch_count_2_1:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_3_pitch_count_2_1[0][0]
    pitcher_df = hitter_3_pitch_count_2_1[0][1]

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

    # Replace hitter_3_pitch_count with the multiplied dataframe
    hitter_3_pitch_count_2_1 = result_df

hitter_3_pitch_count_2_2 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("R_batter_3") and key.endswith("2_2")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("2_2")
        ),
    ]
    if any(key.startswith("R_batter_3") and key.endswith("2_2") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("2_2")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("2_2")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("2_2") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_3_pitch_count_2_2 = [
    item for item in hitter_3_pitch_count_2_2 if item is not None
]

# Assuming hitter_3_pitch_count contains a valid entry
if hitter_3_pitch_count_2_2:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_3_pitch_count_2_2[0][0]
    pitcher_df = hitter_3_pitch_count_2_2[0][1]

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

    # Replace hitter_3_pitch_count with the multiplied dataframe
    hitter_3_pitch_count_2_2 = result_df

hitter_3_pitch_count_3_0 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("R_batter_3") and key.endswith("3_0")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("3_0")
        ),
    ]
    if any(key.startswith("R_batter_3") and key.endswith("3_0") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("3_0")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("3_0")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("3_0") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_3_pitch_count_3_0 = [
    item for item in hitter_3_pitch_count_3_0 if item is not None
]

# Assuming hitter_3_pitch_count contains a valid entry
if hitter_3_pitch_count_3_0:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_3_pitch_count_3_0[0][0]
    pitcher_df = hitter_3_pitch_count_3_0[0][1]

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

    # Replace hitter_3_pitch_count with the multiplied dataframe
    hitter_3_pitch_count_3_0 = result_df

hitter_3_pitch_count_3_1 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("R_batter_3") and key.endswith("3_1")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("3_1")
        ),
    ]
    if any(key.startswith("R_batter_3") and key.endswith("3_1") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("3_1")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("3_1")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("3_1") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_3_pitch_count_3_1 = [
    item for item in hitter_3_pitch_count_3_1 if item is not None
]

# Assuming hitter_3_pitch_count contains a valid entry
if hitter_3_pitch_count_3_1:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_3_pitch_count_3_1[0][0]
    pitcher_df = hitter_3_pitch_count_3_1[0][1]

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

    # Replace hitter_3_pitch_count with the multiplied dataframe
    hitter_3_pitch_count_3_1 = result_df

hitter_3_pitch_count_3_2 = [
    [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("R_batter_3") and key.endswith("3_2")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_R") and key.endswith("3_2")
        ),
    ]
    if any(key.startswith("R_batter_3") and key.endswith("3_2") for key in dataframes)
    else [
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("L_batter_1") and key.endswith("3_2")
        ),
        next(
            df
            for key, df in dataframes.items()
            if key.startswith("pitcher_vs_L") and key.endswith("3_2")
        ),
    ]
    if any(key.startswith("L_batter_1") and key.endswith("3_2") for key in dataframes)
    else None
]
# Filter out None values (in case any condition is not met)
hitter_3_pitch_count_3_2 = [
    item for item in hitter_3_pitch_count_3_2 if item is not None
]

# Assuming hitter_3_pitch_count contains a valid entry
if hitter_3_pitch_count_3_2:
    # Extract batter_df and pitcher_df from the entry
    batter_df = hitter_3_pitch_count_3_2[0][0]
    pitcher_df = hitter_3_pitch_count_3_2[0][1]

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

    # Replace hitter_3_pitch_count with the multiplied dataframe
    hitter_3_pitch_count_3_2 = result_df


# Extracting 'Sum' row from each df
hitter_3_pitch_count_0_0 = hitter_3_pitch_count_0_0[
    hitter_3_pitch_count_0_0.index == "Sum"
]
hitter_3_pitch_count_0_1 = hitter_3_pitch_count_0_1[
    hitter_3_pitch_count_0_1.index == "Sum"
]
hitter_3_pitch_count_0_2 = hitter_3_pitch_count_0_2[
    hitter_3_pitch_count_0_2.index == "Sum"
]
hitter_3_pitch_count_1_0 = hitter_3_pitch_count_1_0[
    hitter_3_pitch_count_1_0.index == "Sum"
]
hitter_3_pitch_count_1_1 = hitter_3_pitch_count_1_1[
    hitter_3_pitch_count_1_1.index == "Sum"
]
hitter_3_pitch_count_1_2 = hitter_3_pitch_count_1_2[
    hitter_3_pitch_count_1_2.index == "Sum"
]
hitter_3_pitch_count_2_0 = hitter_3_pitch_count_2_0[
    hitter_3_pitch_count_2_0.index == "Sum"
]
hitter_3_pitch_count_2_1 = hitter_3_pitch_count_2_1[
    hitter_3_pitch_count_2_1.index == "Sum"
]
hitter_3_pitch_count_2_2 = hitter_3_pitch_count_2_2[
    hitter_3_pitch_count_2_2.index == "Sum"
]
hitter_3_pitch_count_3_0 = hitter_3_pitch_count_3_0[
    hitter_3_pitch_count_3_0.index == "Sum"
]
hitter_3_pitch_count_3_1 = hitter_3_pitch_count_3_1[
    hitter_3_pitch_count_3_1.index == "Sum"
]
hitter_3_pitch_count_3_2 = hitter_3_pitch_count_3_2[
    hitter_3_pitch_count_3_2.index == "Sum"
]

# Combining all 'Sum' rows into 1 df for transition matrix
dfs = [
    hitter_3_pitch_count_0_0,
    hitter_3_pitch_count_0_1,
    hitter_3_pitch_count_0_2,
    hitter_3_pitch_count_1_0,
    hitter_3_pitch_count_1_1,
    hitter_3_pitch_count_1_2,
    hitter_3_pitch_count_2_0,
    hitter_3_pitch_count_2_1,
    hitter_3_pitch_count_2_2,
    hitter_3_pitch_count_3_0,
    hitter_3_pitch_count_3_1,
    hitter_3_pitch_count_3_2,
]

pitch_counts_hitter_3 = pd.concat(dfs, axis=0, ignore_index=True)
pitch_counts_hitter_3.insert(
    0,
    "Pitch Count",
    [
        "0-0",
        "0-1",
        "0-2",
        "1-0",
        "1-1",
        "1-2",
        "2-0",
        "2-1",
        "2-2",
        "3-0",
        "3-1",
        "3-2",
    ],
)
pitch_counts_hitter_3 = pitch_counts_hitter_3[["Pitch Count", "Ball", "Strike", "BIP"]]

# List of all pitch counts
pitch_counts = pitch_counts_hitter_3["Pitch Count"].tolist()

# Initialize an empty transition matrix with float values
transition_matrix = pd.DataFrame(0.0, columns=pitch_counts, index=pitch_counts)

# Populate the transition matrix with probabilities
for i in range(len(pitch_counts)):
    for j in range(len(pitch_counts)):
        # Weighted sum of 'Strike', 'Ball', and 'BIP' columns for transition probabilities
        transition_matrix.iloc[i, j] = (
            pitch_counts_hitter_3.loc[j, "Strike"]
            + pitch_counts_hitter_3.loc[j, "Ball"]
            + pitch_counts_hitter_3.loc[j, "BIP"]
        )

# Normalize the rows to ensure that each row sums to 1
transition_matrix = transition_matrix.div(transition_matrix.sum(axis=1), axis=0)
# pd.set_option('display.max_columns', None)
# print("Transition Matrix:")
# print(transition_matrix)

# Number of steps to simulate the Markov chain
num_steps = 10

# Initialize a probability vector for each pitch count
initial_probabilities = pd.Series(0.0, index=transition_matrix.index)
initial_probabilities.loc["0-0"] = 1.0

# Simulate the Markov chain
current_probabilities = initial_probabilities.copy()
for _ in range(num_steps):
    current_probabilities = np.dot(current_probabilities, transition_matrix)

# Convert the current_probabilities array to a Pandas Series
current_probabilities_series = pd.Series(
    current_probabilities, index=transition_matrix.index
)

# Calculate the probability of a strike being called after reaching a 2-strike count
prob_strike_after_2_strike = (
    transition_matrix.loc["2-2", "3-0"]
    + transition_matrix.loc["2-2", "3-1"]
    + transition_matrix.loc["2-2", "3-2"]
)

print(
    f"Probability of a strike being called after 2 strikes for hitter 3: {prob_strike_after_2_strike}"
)
