import matplotlib.pyplot as plt

# PIE PLOT

goal_types = 'NATIONAL TEAMS','YOUNG TEAMS','CLUB TEAMS'

goals = [102,18,660]
colors = ['y','r','b']

# Shadow & Explode for Much better visualization. # f%%f shows the ratio.
plt.pie(goals,labels=goal_types,colors=colors, shadow=True, explode=(0.05,0.05,0.05))
plt.show()

# STACK PLOT
years = [1,2,3]
lebron = [20.9, 27.2, 31.4]
kd = [20.3, 25.3, 30.1]
steph = [17.5, 18.6, 14.7]

plt.plot([],[],color="y",label="LeBron James")
plt.plot([],[],color="r",label="Kevin Durant")
plt.plot([],[],color="b",label="Stephen Curry")

plt.stackplot(years,lebron,kd,steph, colors=["y","r","b"])
plt.title("SCORERS")
plt.xlabel("Year")
plt.ylabel("PPG")
plt.legend()
plt.show()

# BAR PLOT ( SÜTUN GRAFİĞİ )

plt.bar(["PPG","RPG","APG","SPG","BPG"],[31.6,10.7,10.4,1.6,0.4],label="MVP Westbrook",width=.5)

plt.legend()
plt.xlabel("STATS")
plt.ylabel("STATS")
plt.title("MVP Westbrook")

plt.show()

# MULTIPLE BAR PLOT ( ÇOKLU KARŞILAŞTIRILMALI SÜTUN GRAFİĞİ )

plt.bar(["PPG","RPG","APG","SPG","BPG"],[31.6,10.7,10.4,1.6,0.4],label="MVP Westbrook",width=.5)
plt.bar(["PPG","RPG","APG","SPG","BPG"],[30.4,5.4,8.8,1.8,0.7],label="MVP Harden",width=.5)

plt.legend()
plt.xlabel("STATS")
plt.ylabel("STATS")
plt.title("MVP Harden vs MVP Westbrook")

plt.show()