from baseball_id import Lookup

batter_1 = "Corbin Carroll"
batter_2 = "Ketel Marte"
batter_3 = "Gabriel Moreno"
batter_4 = "Christian Walker"
batter_5 = "Tommy Pham"
batter_6 = "Lourdes Gurriel Jr."
batter_7 = "Alek Thomas"
batter_8 = "Evan Longoria"
batter_9 = "Pavin Smith"
pitcher = "Nathan Eovaldi"


batter_1_id = (
    Lookup.from_names([batter_1])["mlb_id"].astype(str).values[0].split(".")[0]
)
batter_1_bats = Lookup.from_names([batter_1])["bats"]
batter_2_id = (
    Lookup.from_names([batter_2])["mlb_id"].astype(str).values[0].split(".")[0]
)
batter_2_bats = Lookup.from_names([batter_2])["bats"]
batter_3_id = (
    Lookup.from_names([batter_3])["mlb_id"].astype(str).values[0].split(".")[0]
)
batter_3_bats = Lookup.from_names([batter_3])["bats"]
batter_4_id = (
    Lookup.from_names([batter_4])["mlb_id"].astype(str).values[0].split(".")[0]
)
batter_4_bats = Lookup.from_names([batter_4])["bats"]
batter_5_id = (
    Lookup.from_names([batter_5])["mlb_id"].astype(str).values[0].split(".")[0]
)
batter_5_bats = Lookup.from_names([batter_5])["bats"]
batter_6_id = (
    Lookup.from_names([batter_6])["mlb_id"].astype(str).values[0].split(".")[0]
)
batter_6_bats = Lookup.from_names([batter_6])["bats"]
batter_7_id = (
    Lookup.from_names([batter_7])["mlb_id"].astype(str).values[0].split(".")[0]
)
batter_7_bats = Lookup.from_names([batter_7])["bats"]
batter_8_id = (
    Lookup.from_names([batter_8])["mlb_id"].astype(str).values[0].split(".")[0]
)
batter_8_bats = Lookup.from_names([batter_8])["bats"]
batter_9_id = (
    Lookup.from_names([batter_9])["mlb_id"].astype(str).values[0].split(".")[0]
)
batter_9_bats = Lookup.from_names([batter_9])["bats"]
pitcher_id = Lookup.from_names([pitcher])["mlb_id"].astype(str).values[0].split(".")[0]
