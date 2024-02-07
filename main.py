from scraping import scrape_data
from hitters import calculate_transition_matrix
from markov import calculate_total_probability

batters = [
    {
        "url": "https://www.brooksbaseball.net//h_tabs.php?player=682998&gFilt=&time=month&minmax=ci&var=po&s_type=2&startDate=01/01/2023&endDate=01/01/2024&balls={}&strikes={}&b_hand=R",
        "handedness": "L",
    },
    {
        "url": "https://www.brooksbaseball.net//h_tabs.php?player=606466&gFilt=&time=month&minmax=ci&var=po&s_type=2&startDate=01/01/2023&endDate=01/01/2024&balls={}&strikes={}&b_hand=R",
        "handedness": "L",
    },
    {
        "url": "https://www.brooksbaseball.net//h_tabs.php?player=672515&gFilt=&time=month&minmax=ci&var=po&s_type=2&startDate=01/01/2023&endDate=01/01/2024&balls={}&strikes={}&b_hand=R",
        "handedness": "R",
    },
    {
        "url": "https://www.brooksbaseball.net//h_tabs.php?player=572233&gFilt=&time=month&minmax=ci&var=po&s_type=2&startDate=01/01/2023&endDate=01/01/2024&balls={}&strikes={}&b_hand=R",
        "handedness": "R",
    },
    {
        "url": "https://www.brooksbaseball.net//h_tabs.php?player=502054&gFilt=&time=month&minmax=ci&var=po&s_type=2&startDate=01/01/2023&endDate=01/01/2024&balls={}&strikes={}&b_hand=R",
        "handedness": "R",
    },
    {
        "url": "https://www.brooksbaseball.net//h_tabs.php?player=666971&gFilt=&time=month&minmax=ci&var=po&s_type=2&startDate=01/01/2023&endDate=01/01/2024&balls={}&strikes={}&b_hand=R",
        "handedness": "R",
    },
    {
        "url": "https://www.brooksbaseball.net//h_tabs.php?player=677950&gFilt=&time=month&minmax=ci&var=po&s_type=2&startDate=01/01/2023&endDate=01/01/2024&balls={}&strikes={}&b_hand=R",
        "handedness": "L",
    },
    {
        "url": "https://www.brooksbaseball.net//h_tabs.php?player=446334&gFilt=&time=month&minmax=ci&var=po&s_type=2&startDate=01/01/2023&endDate=01/01/2024&balls={}&strikes={}&b_hand=R",
        "handedness": "R",
    },
    {
        "url": "https://www.brooksbaseball.net//h_tabs.php?player=672695&gFilt=&time=month&minmax=ci&var=po&s_type=2&startDate=01/01/2023&endDate=01/01/2024&balls={}&strikes={}&b_hand=R",
        "handedness": "L",
    },
]

pitcher_url = "https://www.brooksbaseball.net//tabs.php?player=543135&p_hand=-1&ppos=-1&cn=200&compType=none&gFilt=&time=month&minmax=ci&var=po&s_type=2&startDate=01/01/2023&endDate=01/01/2024&balls={}&strikes={}&b_hand={}"

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
