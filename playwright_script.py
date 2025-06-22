from playwright.sync_api import sync_playwright
import csv

filename = "state_cities.csv"

playwright = sync_playwright().start()
# Use playwright.chromium, playwright.firefox or playwright.webkit
# Pass headless=False to launch() to see the browser UI
browser = playwright.chromium.launch(headless=True)
page = browser.new_page()
page.goto("https://www.indiapost.gov.in/vas/pages/LocatePostOffices.aspx")
state_select = page.locator('xpath=//select[contains(@title, "State")]')
city_select = page.locator('xpath=//select[contains(@title, "City")]')
states = state_select.locator("option").all_text_contents()

file = open(filename, mode='w', newline='')
writer = csv.writer(file)
# Write header (optional)
writer.writerow(["State", "City"])

for state in states:
  if 'Select' in state:
    continue
  state_select.select_option(state)
  cities = city_select.locator("option").all_text_contents()
  # Write each state-city pair
  for city in cities:
    if 'Select' in state:
      continue
    writer.writerow([state, city])

browser.close()
playwright.stop()

    
    

