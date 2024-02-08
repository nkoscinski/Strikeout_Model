from scraping import scrape_data
from hitters import calculate_transition_matrix
from markov import calculate_total_probability
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


batter_1_id = Lookup.from_names([batter_1])["mlb_id"].astype(str).values[0].split('.')[0]
batter_1_bats = Lookup.from_names([batter_1])["bats"]
batter_2_id = Lookup.from_names([batter_2])["mlb_id"].astype(str).values[0].split('.')[0]
batter_2_bats = Lookup.from_names([batter_2])["bats"]
batter_3_id = Lookup.from_names([batter_3])["mlb_id"].astype(str).values[0].split('.')[0]
batter_3_bats = Lookup.from_names([batter_3])["bats"]
batter_4_id = Lookup.from_names([batter_4])["mlb_id"].astype(str).values[0].split('.')[0]
batter_4_bats = Lookup.from_names([batter_4])["bats"]
batter_5_id = Lookup.from_names([batter_5])["mlb_id"].astype(str).values[0].split('.')[0]
batter_5_bats = Lookup.from_names([batter_5])["bats"]
batter_6_id = Lookup.from_names([batter_6])["mlb_id"].astype(str).values[0].split('.')[0]
batter_6_bats = Lookup.from_names([batter_6])["bats"]
batter_7_id = Lookup.from_names([batter_7])["mlb_id"].astype(str).values[0].split('.')[0]
batter_7_bats = Lookup.from_names([batter_7])["bats"]
batter_8_id = Lookup.from_names([batter_8])["mlb_id"].astype(str).values[0].split('.')[0]
batter_8_bats = Lookup.from_names([batter_8])["bats"]
batter_9_id = Lookup.from_names([batter_9])["mlb_id"].astype(str).values[0].split('.')[0]
batter_9_bats = Lookup.from_names([batter_9])["bats"]
pitcher_id = Lookup.from_names([pitcher])["mlb_id"].astype(str).values[0].split('.')[0]

batters = [
    {
        "url": f"https://www.brooksbaseball.net//h_tabs.php?player={batter_1_id}Filt=&time=month&minmax=ci&var=po&s_type=2&startDate=01/01/2023&endDate=01/01/2024&balls={{}}&strikes={{}}&b_hand=R",
        "handedness": batter_1_bats,
    },
    {
        "url": f"https://www.brooksbaseball.net//h_tabs.php?player={batter_2_id}&gFilt=&time=month&minmax=ci&var=po&s_type=2&startDate=01/01/2023&endDate=01/01/2024&balls={{}}&strikes={{}}&b_hand=R",
        "handedness": "L",
    },
    {
        "url": f"https://www.brooksbaseball.net//h_tabs.php?player={batter_3_id}&gFilt=&time=month&minmax=ci&var=po&s_type=2&startDate=01/01/2023&endDate=01/01/2024&balls={{}}&strikes={{}}&b_hand=R",
        "handedness": "R",
    },
    {
        "url": f"https://www.brooksbaseball.net//h_tabs.php?player={batter_4_id}&gFilt=&time=month&minmax=ci&var=po&s_type=2&startDate=01/01/2023&endDate=01/01/2024&balls={{}}&strikes={{}}&b_hand=R",
        "handedness": "R",
    },
    {
        "url": f"https://www.brooksbaseball.net//h_tabs.php?player={batter_5_id}&gFilt=&time=month&minmax=ci&var=po&s_type=2&startDate=01/01/2023&endDate=01/01/2024&balls={{}}&strikes={{}}&b_hand=R",
        "handedness": "R",
    },
    {
        "url": f"https://www.brooksbaseball.net//h_tabs.php?player={batter_6_id}&gFilt=&time=month&minmax=ci&var=po&s_type=2&startDate=01/01/2023&endDate=01/01/2024&balls={{}}&strikes={{}}&b_hand=R",
        "handedness": "R",
    },
    {
        "url": f"https://www.brooksbaseball.net//h_tabs.php?player={batter_7_id}&gFilt=&time=month&minmax=ci&var=po&s_type=2&startDate=01/01/2023&endDate=01/01/2024&balls={{}}&strikes={{}}&b_hand=R",
        "handedness": "L",
    },
    {
        "url": f"https://www.brooksbaseball.net//h_tabs.php?player={batter_8_id}&gFilt=&time=month&minmax=ci&var=po&s_type=2&startDate=01/01/2023&endDate=01/01/2024&balls={{}}&strikes={{}}&b_hand=R",
        "handedness": "R",
    },
    {
        "url": f"https://www.brooksbaseball.net//h_tabs.php?player={batter_9_id}&gFilt=&time=month&minmax=ci&var=po&s_type=2&startDate=01/01/2023&endDate=01/01/2024&balls={{}}&strikes={{}}&b_hand=R",
        "handedness": "L",
    },
]


pitcher_url = f"https://www.brooksbaseball.net//tabs.php?player={pitcher_id}&p_hand=-1&ppos=-1&cn=200&compType=none&gFilt=&time=month&minmax=ci&var=po&s_type=2&startDate=01/01/2023&endDate=01/01/2024&balls={{}}&strikes={{}}&b_hand={{}}"

times_faced = 2.33  # The number of times the pitcher faces each batter
total_strikeouts = 0  # Initialize the total strikeouts

for i, batter in enumerate(batters, start=1):
    dataframes = scrape_data(batter["url"], pitcher_url, batter["handedness"])
    transition_matrix = calculate_transition_matrix(dataframes)
    total_probability = calculate_total_probability(transition_matrix)
    strikeouts = (
        total_probability * times_faced
    )  # Calculate the forecasted strikeouts for this batter
    total_strikeouts += strikeouts  # Add the forecasted strikeouts to the total
    # print(f"Batter {i} Total probaility: {total_probability}, Forecasted strikeouts: {strikeouts}")

print(f"Total forecasted strikeouts for the pitcher: {total_strikeouts}")
