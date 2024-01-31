import time
import io
import os
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

# Use Safari driver
driver = webdriver.Safari()

# List of batter URLs
batter_info = [
    {"name": "batter_1", "url": "https://www.brooksbaseball.net//h_tabs.php?player=547989&gFilt=&time=month&minmax=ci&var=po&s_type=2&startDate=01/01/2023&endDate=01/01/2024&balls={}&strikes={}&b_hand=R"}, # Jose Abreu
    {"name": "batter_2", "url": "https://www.brooksbaseball.net//h_tabs.php?player=457705&gFilt=&time=month&minmax=ci&var=po&s_type=2&startDate=01/01/2023&endDate=01/01/2024&balls={}&strikes={}&b_hand=R"}, # Andrew McCutchen
    {"name": "batter_3", "url": "https://www.brooksbaseball.net//h_tabs.php?player=608369&gFilt=&time=month&minmax=ci&var=po&s_type=2&startDate=01/01/2023&endDate=01/01/2024&balls={}&strikes={}&b_hand=R"} # Corey Seager
]

# List of pitcher URL
pitcher_info = [
    {"name": "pitcher", "url": "https://www.brooksbaseball.net//tabs.php?player=543135&p_hand=-1&ppos=-1&cn=200&compType=none&gFilt=&time=month&minmax=ci&var=po&s_type=2&startDate=03/30/2007&endDate=11/11/2023&balls={}&strikes={}&b_hand={}"}
]

# Create a main directory output
main_output_directory = 'output.csv'
os.makedirs(main_output_directory, exist_ok=True)

# Function to get batter output directory based on batter name and batter hand
def get_batter_output_directory(batter_name, batter_hand):
    return os.path.join(main_output_directory, batter_name, f"vs_{batter_hand}_batter")

# Iterate over batters
for batter in batter_info:
    # Create a subdirectory for each batter
    batter_output_directory = os.path.join(main_output_directory, batter["name"])
    os.makedirs(batter_output_directory, exist_ok=True)

# Iterate over batters
for batter in batter_info:
    # Create a subdirectory for each batter
    batter_output_directory = os.path.join(main_output_directory, batter["name"])
    os.makedirs(batter_output_directory, exist_ok=True)

    # Iterate over pitch counts
    for balls in range (4): # 0 to 3 balls
        for strikes in range (3): # 0 to 2 strikes
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
            soup = BeautifulSoup(html, 'html.parser')

            # Find the <table> element
            table_element = soup.find('table')

            # Convert the table HTML to a Pandas DataFrame
            if table_element:
                table_df = pd.read_html(io.StringIO(str(table_element)))[0]

                # Save the DataFrame to a CSV file
                csv_filename = f"{batter_output_directory}/pitch_count_{balls}_{strikes}.csv"
                table_df.to_csv(csv_filename, index=False)

                # Read the CSV file, drop the lsat row, and save the modified DataFrame back to the CSV file
                df_modified = pd.read_csv(csv_filename)
                df_modified = df_modified.iloc[:-1] # Drop the last row
                df_modified.to_csv(csv_filename, index=False)

            # Close current window
            driver.close()

            # Switch back to the main window
            driver.switch_to.window(driver.window_handles[0])

# Iterate over pitchers
for pitcher in pitcher_info:
    # Create a subdirectory for each batter hand
    for batter_hand in ["L", "R"]:
        pitcher_output_directory = os.path.join(main_output_directory, pitcher["name"], f"vs_{batter_hand}_batter")
        os.makedirs(pitcher_output_directory, exist_ok=True)

        # Iterate over pitch counts
        for balls in range(4):  # 0 to 3 balls
            for strikes in range(3):  # 0 to 2 strikes
                # Create the modified URL using the pitcher_url and f-string
                url = pitcher["url"].format(balls, strikes, batter_hand)

                # Open the URL in a new window
                driver.execute_script("window.open('', '_blank');")
                driver.switch_to.window(driver.window_handles[-1])
                driver.get(url)

                # Wait for the page to load (you might need to adjust the time)
                time.sleep(2)

                # Extract the HTML content
                html = driver.page_source

                # Use BeautifulSoup to parse the HTML
                soup = BeautifulSoup(html, 'html.parser')

                # Find the <table> element
                table_element = soup.find('table')

                # Convert the table HTML to a Pandas DataFrame
                if table_element:
                    table_df = pd.read_html(io.StringIO(str(table_element)))[0]

                    # Save the DataFrame to a CSV file in the subdirectory
                    csv_filename = f"{pitcher_output_directory}/pitch_count_{balls}_{strikes}.csv"
                    table_df.to_csv(csv_filename, index=False)

                    # Read the CSV file, drop the last row, and save the modified DataFrame back to the CSV file
                    df_modified = pd.read_csv(csv_filename)
                    df_modified = df_modified.iloc[:-1]  # Drop the last row
                    df_modified.to_csv(csv_filename, index=False)

                # Close the current window
                driver.close()

                # Switch back to the main window
                driver.switch_to.window(driver.window_handles[0])
