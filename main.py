import pandas as pd
import matplotlib.pyplot as plt

#xGF Chart#
df = pd.read_csv("xG data.csv")
fig, ax = plt.subplots()
my_scatter_plot = ax.scatter(
df["Team"], #x values
df["xGF"], #y values
df["GF"] #scale
)
ax.set_xlabel("Team")
ax.set_ylabel("xGF")
ax.set_title("xGF Comparison - Premier League 19/20")
plt.xticks(rotation=90)
plt.show()

#xGA Chart#
fig, ax = plt.subplots()
my_scatter_plot = ax.scatter(
df["Team"], #x values
df["xGA"], #y values
df["GA"] #scale
)
ax.set_xlabel("Team")
ax.set_ylabel("xGA")
ax.set_title("xGA Comparison - Premier League 19/20")
plt.xticks(rotation=90)
plt.show()

#xP Chart#
fig, ax = plt.subplots()
my_scatter_plot = ax.scatter(
df["Team"], #x values
df["xP"], #y values
df["P"]
)
ax.set_xlabel("Team")
ax.set_ylabel("xP")
ax.set_title("xP Comparison - Premier League 19/20")
plt.xticks(rotation=90)
plt.show()

#Analysis Function#
def xAnalysis():
    print(Team)
    if GF < xGF - 0.5:
        print("This team needs to sign a forward")
    if GA > xGA + 0.5:
        print("This team needs to sign a defender")
    if P < xP - 0.5:
        print("This team underperformed last season")
    if GF > xGF - 0.5 and GA < xGA + 0.5 and P > xP - 0.5:
        print("This team has no immediate concerns")

#Start  Analysis of Individual Teams#
#Liverpool#
Team = "1. Liverpool"
xGF = 75.19
GF = 85
xGA = 39.67
GA = 33
xP = 74.28
P = 99

xAnalysis()

#Manchester City#
Team = "2. Manchester City"
xGF = 102.21
GF = 102
xGA = 37
GA = 35
xP = 86.76
P = 81

xAnalysis()
#Manchester United#
Team = "3. Manchester United"
xGF = 66.19
GF = 66
xGA = 38.06
GA = 36
xP = 70.99
P = 66

xAnalysis()
#Chelsea#
Team = "4. Chelsea"
xGF = 76.23
GF = 69
xGA = 41.09
GA = 54
xP = 73.49
P = 66

xAnalysis()
#Leicester#
Team = "5. Leicester"
xGF = 61.02
GF = 67
xGA = 47.89
GA = 41
xP = 61.16
P = 62

xAnalysis()
#Tottenham#
Team = "6. Tottenham"
xGF = 49.02
GF = 61
xGA = 54.13
GA = 47
xP = 49.26
P = 59

xAnalysis()
#Wolverhampton#
Team = "7. Wolverhampton"
xGF = 54.22
GF = 51
xGA = 37.39
GA = 40
xP = 63.82
P = 59

xAnalysis()
#Arsenal#
Team = "8. Arsenal"
xGF = 50.82
GF = 56
xGA = 57.25
GA = 48
xP = 50.15
P = 56

xAnalysis()
#Sheffield United#
Team = "9. Sheffield United"
xGF = 45.81
GF = 39
xGA = 52.04
GA = 39
xP = 49.34
P = 54

xAnalysis()
#Burnley#
Team = "10. Burnley"
xGF = 49.35
GF = 43
xGA = 53.84
GA = 50
xP = 49.54
P = 54

xAnalysis()
#Southampton#
Team = "11. Southampton"
xGF = 56.5
GF = 51
xGA = 56.59
GA = 60
xP = 56.87
P = 52

xAnalysis()
#Everton#
Team = "12. Everton"
xGF = 53.71
GF = 44
xGA = 49.21
GA = 56
xP = 55.78
P = 49

xAnalysis()
#Newcastle#
Team = "13. Newcastle"
xGF = 36.49
GF = 38
xGA = 67.03
GA = 58
xP = 31.92
P = 44

xAnalysis()
#Crystal Palace#
Team = "14. Crystal Palace"
xGF = 34.45
GF = 31
xGA = 57.39
GA = 50
xP = 38.26
P = 43

xAnalysis()
#Brighton#
Team = "15. Brighton"
xGF = 47.42
GF = 39
xGA = 60.42
GA = 54
xP = 48.02
P = 41

xAnalysis()
#West Ham#
Team = "16. West Ham"
xGF = 49.07
GF = 49
xGA = 68.42
GA = 62
xP = 38.75
P = 39

xAnalysis()
#Aston Villa#
Team = "17. Aston Villa"
xGF = 45.09
GF = 41
xGA = 71.6
GA = 67
xP = 37.23
P = 35

xAnalysis()
#Bournemouth#
Team = "18. Bournemouth"
xGF = 44.67
GF = 40
xGA = 63.29
GA = 65
xP = 47.87
P = 34

xAnalysis()
#Watford#
Team = "19. Watford"
xGF = 48.56
GF = 36
xGA = 59.53
GA = 64
xP = 47.87
P = 34

xAnalysis()
#Norwich#
Team = "20. Norwich"
xGF = 37.23
GF = 26
xGA = 71.61
GA = 75
xP = 33.12
P = 21

xAnalysis()
