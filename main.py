from scraping import scrape_data
from hitters import calculate_transition_matrix
from markov import calculate_total_probability
from players import (
    batter_1_id,
    batter_1_bats,
    batter_2_id,
    batter_3_id,
    batter_4_id,
    batter_5_id,
    batter_6_id,
    batter_7_id,
    batter_8_id,
    batter_9_id,
    pitcher_id,
)


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
