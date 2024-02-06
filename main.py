from scraping import scrape_data
from hitters import calculate_transition_matrix
from markov import calculate_total_probability

batter_url = "https://www.brooksbaseball.net//h_tabs.php?player=547989&gFilt=&time=month&minmax=ci&var=po&s_type=2&startDate=01/01/2023&endDate=01/01/2024&balls={}&strikes={}&b_hand=R"

pitcher_url = "https://www.brooksbaseball.net//tabs.php?player=543135&p_hand=-1&ppos=-1&cn=200&compType=none&gFilt=&time=month&minmax=ci&var=po&s_type=2&startDate=03/30/2007&endDate=11/11/2023&balls={}&strikes={}&b_hand={}"

batter_handedness = "R"

dataframes = scrape_data(batter_url, pitcher_url, batter_handedness)

transition_matrix = calculate_transition_matrix(dataframes)

total_probability = calculate_total_probability(transition_matrix)
