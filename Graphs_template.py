#-----------------------------------------------------#
#                GRAPH PLOTS TEMPLATE                 #
#                © Jona Cappelle                      #
#           (based on michiel's latex params)         #
#-----------------------------------------------------#

# pip install pandas matplotlib
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
from matplotlib.ticker import ScalarFormatter

#-----------------------------------------------------#
#                   SETTINGS                          #
#-----------------------------------------------------#

# Esthetical ratio
golden_mean = (math.sqrt(5)-1.0)/2.0 

# Adjust to your liking
width = 5                       #inches
height = width * golden_mean    #inches
fontsize = 11                   #pt
axis_linewidth = 0.4            #pt

# Params LaTeX
mpl.use("pgf")
mpl.rcParams.update({
        'backend': 'ps',
        'axes.labelsize': fontsize,
        'axes.titlesize': fontsize,
        'legend.fontsize': fontsize,
        'xtick.labelsize': fontsize,
        'ytick.labelsize': fontsize,
        'axes.linewidth' : axis_linewidth,
        'text.usetex': True,
        "pgf.rcfonts": False,
        "pgf.texsystem": "lualatex",
        'font.family': 'serif',
        "pgf.preamble": [
            r"\usepackage[utf8x]{inputenc}",    # use utf8 fonts
            r"\usepackage[T1]{fontenc}",        # plots will be generated
            r"\usepackage[detect-all]{siunitx}" # to use si units
        ]
    })

#-----------------------------------------------------#
#                   READ DATA                         #
#-----------------------------------------------------#

data = pd.read_csv('path_to_file.csv')
data.head()

# Give name to data columns, will be used below
data.columns = ['x', 'y']

#-----------------------------------------------------#
#                   PLOTTING                          #
#-----------------------------------------------------#

# Figure size
# plt.figure(1,figsize=(width,height))

fig, ax = plt.subplots(figsize=(width,height))

# Black & white option
# plt.style.use('grayscale')

# Plot grid onder data + lichter grid
plt.rc('axes', axisbelow=True)
ax.grid(color='silver', linestyle='-', linewidth=0.25, alpha=0.5)

# Hide the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Point plot
# plt.scatter(data['x'], data['y'], s=5, color='grey') # s=5 --> size of points

# Line plot
ax.plot(data['x'], data['y'], c='0.4') # c=0.4 --> nice grey!

# Select range
# plt.xlim(lower,upper)
# plt.ylim(lower,upper)

# Log scale
# plt.yscale('log')
# plt.xscale('log')

# No legend
# ax.legend().remove()

# Set labels
plt.ylabel("ylabel")
plt.xlabel("xlabel")

#-----------------------------------------------------#
#                   SAVE FILE                         #
#-----------------------------------------------------#

plt.savefig('filename.pgf', bbox_inches='tight')

# OPTIONS
# tweede plot met plt.figure(2, figsize=(width, height))

# Plot done!
print("Done!")