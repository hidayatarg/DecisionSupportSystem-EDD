inp = u"""a0:86:c6:52:4e:e8,0.006568,0.006620,Out
a0:86:c6:52:4e:e8,0.006663,0.006695,In
a0:86:c6:52:4e:e8,0.008089,0.008141,Out
a0:86:c6:52:4e:e8,0.008185,0.008217,In
01:00:5e:00:00:fb,0.033096,0.035016,Out
33:33:00:00:00:fb,0.034997,0.037077,Out
01:00:5e:7f:ff:fa,0.039969,0.042057,Out
ff:ff:ff:ff:ff:ff,0.059823,0.061639,Out
a0:86:c6:52:4e:e8,0.068865,0.068917,Out
a0:86:c6:52:4e:e8,0.068962,0.068994,In
a0:86:c6:52:4e:e8,0.083492,0.083544,Out
a0:86:c6:52:4e:e8,0.083588,0.083620,In"""

import pandas as pd
import io
import matplotlib.pyplot as plt

df = pd.read_csv(io.StringIO(inp), header=None, names=["Task", "Start", "Finish", "Resource"])
print(pd)
df["Diff"] = df.Finish - df.Start

color = {"In": "blue", "Out": "crimson"}
fig, ax = plt.subplots(figsize=(6, 3))

labels = []
for i, task in enumerate(df.groupby("Task")):
    labels.append(task[0])
    for r in task[1].groupby("Resource"):
        data = r[1][["Start", "Diff"]]
        ax.broken_barh(data.values, (i-0.4, 0.8), color=color[r[0]] )

ax.set_yticks(range(len(labels)))
ax.set_yticklabels(labels)
ax.set_xlabel("Time")
plt.tight_layout()
plt.show()