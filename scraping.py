import time
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from io import StringIO

# Use Safari driver
driver = webdriver.Safari()

# List of batter URLs
batter_info = [
    {
        "name": "batter_1",
        "url": "https://www.brooksbaseball.net//h_tabs.php?player=547989&gFilt=&time=month&minmax=ci&var=po&s_type=2&startDate=01/01/2023&endDate=01/01/2024&balls={}&strikes={}&b_hand=R",
    },
    # Jose Abreu
    {
        "name": "batter_2",
        "url": "https://www.brooksbaseball.net//h_tabs.php?player=457705&gFilt=&time=month&minmax=ci&var=po&s_type=2&startDate=01/01/2023&endDate=01/01/2024&balls={}&strikes={}&b_hand=R",
    },
    # Andrew McCutchen
    {
        "name": "batter_3",
        "url": "https://www.brooksbaseball.net//h_tabs.php?player=608369&gFilt=&time=month&minmax=ci&var=po&s_type=2&startDate=01/01/2023&endDate=01/01/2024&balls={}&strikes={}&b_hand=R",
    },
    # Corey Seager
]

# List of pitcher URL
pitcher_info = [
    {
        "name": "pitcher",
        "url": "https://www.brooksbaseball.net//tabs.php?player=543135&p_hand=-1&ppos=-1&cn=200&compType=none&gFilt=&time=month&minmax=ci&var=po&s_type=2&startDate=03/30/2007&endDate=11/11/2023&balls={}&strikes={}&b_hand={}",
    }
]

# Create a dictionary to store the dataframes
dataframes = {}

# Iterate over batters
for batter in batter_info:
    # Iterate over pitch counts
    for balls in range(4):  # 0 to 3 balls
        for strikes in range(3):  # 0 to 2 strikes
            # Create the modified URL using f-string
            url = batter["url"].format(balls, strikes)

            # Open the URL in a new window
            driver.execute_script("window.open('', '_blank');")
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(url)

            # Wait for 2 seconds
            time.sleep(2)

            # Extract the HTML content
            html = driver.page_source

            # Use BeautifulSoup to parse the HTML
            soup = BeautifulSoup(html, "html.parser")

            # Find the <table> element
            table_element = soup.find("table")

            # Convert the table HTML to a Pandas DataFrame
            if table_element:
                # Create a StringIO object from the HTML string
                html_io = StringIO(str(table_element))

                # Pass the StringIO object to pd.read_html
                df = pd.read_html(html_io, header=0)[0]

                # Instead of saving the DataFrame as a CSV file, store it in the dictionary
                dataframes[f"{batter['name']}_B{balls}_S{strikes}"] = df

            # Close current window
            driver.close()

            # Switch back to the main window
            driver.switch_to.window(driver.window_handles[0])

# Iterate over pitchers
for pitcher in pitcher_info:
    # Create a subdirectory for each batter hand
    for batter_hand in ["L", "R"]:
        # Iterate over pitch counts
        for balls in range(4):  # 0 to 3 balls
            for strikes in range(3):  # 0 to 2 strikes
                # Create the modified URL using f-string
                url = pitcher["url"].format(balls, strikes, batter_hand)

                # Open the URL in a new window
                driver.execute_script("window.open('', '_blank');")
                driver.switch_to.window(driver.window_handles[-1])
                driver.get(url)

                # Wait for 2 seconds
                time.sleep(2)

                # Extract the HTML content
                html = driver.page_source

                # Use BeautifulSoup to parse the HTML
                soup = BeautifulSoup(html, "html.parser")

                # Find the <table> element
                table_element = soup.find("table")

                # Convert the table HTML to a Pandas DataFrame
                if table_element:
                    # Create a StringIO object from the HTML string
                    html_io = StringIO(str(table_element))

                    # Pass the StringIO object to pd.read_html
                    df = pd.read_html(html_io, header=0)[0]

                    # Instead of saving the DataFrame as a CSV file, store it in the dictionary
                    dataframes[f"{batter['name']}_B{balls}_S{strikes}"] = df

                # Close the current window
                driver.close()

                # Switch back to the main window
                driver.switch_to.window(driver.window_handles[0])


# Return the dictionary of dataframes
def get_data():
    return dataframes
