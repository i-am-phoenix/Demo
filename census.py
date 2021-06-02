import pandas as pd

pd.read_html("https://txcip.org/tac/census/profile.php?FIPS=48201")

df_harris = pd.read_html("https://txcip.org/tac/census/profile.php?FIPS=48201")
df_fortbend = pd.read_html("https://txcip.org/tac/census/profile.php?FIPS=48157")
df_montegomery = pd.read_html("https://txcip.org/tac/census/profile.php?FIPS=48339")
df_trinity = pd.read_html("https://txcip.org/tac/census/profile.php?FIPS=48455")
df_galveston = pd.read_html("https://txcip.org/tac/census/profile.php?FIPS=48167")
