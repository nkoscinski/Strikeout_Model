import time
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from io import StringIO


def scrape_data(
    batter_url: str, pitcher_url: str, batter_handedness: str
) -> dict[str, pd.DataFrame]:
    # Use Safari driver
    driver = webdriver.Safari()

    # List of batter URLs and handedness
    batter_info = [
        {
            "name": "batter",
            "url": batter_url,
        },
        # Jose Abreu
    ]

    # List of pitcher URL
    pitcher_info = [
        {
            "name": "pitcher",
            "url": pitcher_url,
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
                    dataframes[f"{batter['name']}_{balls}_{strikes}"] = df

                # Close current window
                driver.close()

                # Switch back to the main window
                driver.switch_to.window(driver.window_handles[0])

    # Iterate over pitchers
    for pitcher in pitcher_info:
        # Create a subdirectory for each batter hand
        for batter_hand in batter_handedness:
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
                        dataframes[f"{pitcher['name']}_{balls}_{strikes}"] = df

                    # Close the current window
                    driver.close()

                    # Switch back to the main window
                    driver.switch_to.window(driver.window_handles[0])

    return dataframes


if "__main__" == __name__:
    dataframes = scrape_data()
    for key, df in dataframes.items():
        print(f"{key}:\n{df}\n")
