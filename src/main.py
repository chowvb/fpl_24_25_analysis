import requests,json
import pandas as pd
pd.set_option("display.max_columns", None)

base_url = "https://fantasy.premierleague.com/api/bootstrap-static/"
response = requests.get(base_url).json()

teams_df = pd.json_normalize(response["teams"])

positions_df = pd.json_normalize(response["element_types"])

players_df = pd.json_normalize(response["elements"])


main_df = pd.merge(
    left = players_df,
    right = teams_df,
    left_on = "team",
    right_on = "id"
)

main_df = main_df.merge(
    positions_df,
    left_on = "element_type",
    right_on = "id"
)

main_df = main_df.rename(
    columns= {"name" : "team_name", "singular_name" : "position"}
)

main_df[["first_name", "second_name", "team_name", "position"]].head()