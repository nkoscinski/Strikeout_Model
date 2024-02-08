from scraping import scrape_data
from hitters import calculate_transition_matrix
from markov import calculate_total_probability
from baseball_id import Lookup

batter_1_id = Lookup.from_names(["Corbin Carroll"])["mlb_id"].astype(int)
batter_2_id = Lookup.from_names(["Ketel Marte"])["mlb_id"].astype(int)
batter_3_id = Lookup.from_names(["Gabriel Moreno"])["mlb_id"].astype(int)
batter_4_id = Lookup.from_names(["Christian Walker"])["mlb_id"].astype(int)
batter_5_id = Lookup.from_names(["Tommy Pham"])["mlb_id"].astype(int)
batter_6_id = Lookup.from_names(["Lourdes Gurriel Jr."])["mlb_id"].astype(int)
batter_7_id = Lookup.from_names(["Alek Thomas"])["mlb_id"].astype(int)
batter_8_id = Lookup.from_names(["Evan Longoria"])["mlb_id"].astype(int)
batter_9_id = Lookup.from_names(["Emmanual Rivera"])["mlb_id"].astype(int)
pitcher_id = Lookup.from_names(["Geraldo Perdomo"])["mlb_id"].astype(int)

batters = [
    {
        "url": f"https://www.brooksbaseball.net//h_tabs.php?player={batter_1_id}Filt=&time=month&minmax=ci&var=po&s_type=2&startDate=01/01/2023&endDate=01/01/2024&balls={{}}&strikes={{}}&b_hand=R",
        "handedness": "L",
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
