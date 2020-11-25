import pandas as pd
import matplotlib.pyplot as plt
import pandas_profiling
import seaborn as sns

plt.style.use('seaborn')

terror_df = pd.read_csv(
                        'globalterrorismdb_0718dist.csv',
                        encoding='ISO-8859-1',
                        low_memory=False
                        )

terror_df_clean = terror_df[[
                            "iyear",
                            "imonth",
                            "iday",
                            "approxdate",
                            "country_txt",
                            "city",
                            "latitude",
                            "longitude",
                            "attacktype1_txt",
                            "gname",
                            "nkill",
                            "property",
                            "region"
                            ]]
terror_df_clean.to_csv("cleaned_df.csv")

west_europe = terror_df_clean.loc[terror_df_clean["region"] == 8]
east_europe = terror_df_clean.loc[terror_df_clean["region"] == 9]

europe = pd.concat([west_europe, east_europe])

sns.countplot(europe["country_txt"])
plt.title("Europe")
plt.xticks(rotation=45)
plt.show()

"""
sns.countplot(east_europe["country_txt"])
plt.title("Eastern Europe")
plt.xticks(rotation=90)
plt.show()
"""
