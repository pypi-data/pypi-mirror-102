# -*- coding: utf-8 -*-

""" Module summary description.

More detailed description.
"""
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates as mdates

from _scripts.plot_pandas_series import pandas_plot

__author__ = 'Benjamin Pillot'
__copyright__ = 'Copyright 2019, Benjamin Pillot'
__email__ = 'benjaminpillot@riseup.net'

ratio = 1/(1000 * 6.00372)
fontsize = 24
df = pd.read_csv("/home/benjamin/Documents/PRO/PROJET_GREECE_OPSPV/001_DONNEES"
                 "/output_ac_power_permissive_NOV2019.csv", index_col=0, sep=',')
df = df.apply(pd.to_numeric)
# df = pd.read_csv("/home/benjamin/ownCloud/Post-doc Guyane/GREECE model/Results/Solar PV/"
#                  "output_ac_power_permissive_contour.csv", index_col=0, sep=",")

new_df = pd.DataFrame(index=df.index)
new_df["Park 1"] = df["polygon 37"] * 6.87 * ratio
new_df["Park 2"] = df["polygon 5"] * 18.52 * ratio
new_df["Park 3"] = df["polygon 6"] * 20 * ratio


# new_df["Ring 3"] = (df["polygon 27"] * 5 + df["polygon 28"] * 5 + df["polygon 70"] * 2.8
#                     + df["polygon 71"] * 5 + df["polygon 72"] * 2.19) * ratio
# new_df["Ring 2"] = (df["polygon 4"] * 5 + df["polygon 5"] * 5 +
#                     df["polygon 2"] * 4.56 + df["polygon 51"] * 4.74) * ratio
# new_df["Ring 1"] = df["polygon 36"] * 0.84 * ratio + df["polygon 37"] * 4.72 * ratio
# new_df["Park 11"] = df["polygon 36"] * 0.84 * ratio
# new_df["Park 12"] = df["polygon 37"] * 4.72 * ratio
#
# new_df["Park 21"] = df["polygon 2"] * 4.56 * ratio
# new_df["Park 22"] = df["polygon 51"] * 4.74 * ratio
# new_df["Park 23"] = df["polygon 5"] * 5 * ratio
# new_df["Park 24"] = df["polygon 4"] * 5 * ratio
#
# new_df["Park 31"] = df["polygon 72"] * 2.19 * ratio
# new_df["Park 32"] = df["polygon 70"] * 2.8 * ratio
# new_df["Park 33"] = df["polygon 27"] * 5 * ratio
# new_df["Park 34"] = df["polygon 28"] * 5 * ratio
# new_df["Park 35"] = df["polygon 71"] * 5 * ratio

# new_df["P4, C65"] = df["polygon 6"] * 29.34 * ratio
# new_df["P4, C65"] = df["polygon 6"] * ratio * 100
# new_df["P4, C45"] = df["polygon 6"] * 28.04 * ratio
# new_df["P3, C40"] = df["polygon 2"] * 24.78 * ratio
# new_df["P3, C40"] = df["polygon 2"] * ratio * 100
# new_df["P2, C30"] = df["polygon 5"] * 17.29 * ratio
# new_df["P2, C30"] = df["polygon 5"] * ratio * 100
# new_df["P1, C10"] = df["polygon 71"] * 4.66 * ratio
# new_df["P1, C10"] = df["polygon 71"] * ratio * 100
# new_df["C20"] = df["polygon 5"] * 9.76 * ratio
# new_df["C30"] = df["polygon 5"] * 17.29 * ratio
# new_df["C35"] = df["polygon 2"] * 20.96 * ratio
# new_df["C40"] = df["polygon 2"] * 24.78 * ratio
# new_df["C45"] = df["polygon 6"] * 28.04 * ratio
# new_df["C50"] = df["polygon 6"] * 29.34 * ratio + df["polygon 71"] * 1.16 * ratio
# new_df["C55"] = df["polygon 6"] * 29.34 * ratio + df["polygon 71"] * 3.77 * ratio
# new_df["C60"] = df["polygon 5"] * 6.26 * ratio + df["polygon 6"] * 29.34 * ratio
# new_df["C65"] = df["polygon 5"] * 8.87 * ratio + df["polygon 6"] * 29.34 * ratio

new_df.index = pd.DatetimeIndex(new_df.index)
new_df.index += pd.DateOffset(months=12 * 12)
new_df = new_df.resample('D').max()

# color_dict = {'Park 12': '#1f77b4ff', 'Park 11': '#1f77b4a0',
#               'Park 24': '#ff5a00ff', 'Park 23': '#ff7b00e6', 'Park 22': '#ff7b00a0',
#               'Park 21': '#ff7b005a',
#               'Park 35': '#008300ff', 'Park 34': '#00a81aff', 'Park 33': '#00a81ab9',
#               'Park 32': '#00a81a73', 'Park 31': '#00a81a2d'}

fig, ax = plt.subplots()


# ax = new_df.plot.bar(ax=ax, stacked=True, fontsize=fontsize, width=1,
#                      color=[color_dict[x] for x in new_df.columns])
ax = new_df.plot.bar(ax=ax, stacked=True, fontsize=fontsize, width=1)
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))

ax.set_ylabel("Power (MW)", fontsize=fontsize)
ax.legend(new_df.columns, fontsize=fontsize)


plt.minorticks_off()
plt.xticks(rotation=0)
plt.show()
