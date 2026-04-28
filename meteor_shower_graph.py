import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ── Data ──────────────────────────────────────────────────────────
data = {
    'Shower': ['Perseids', 'Geminids', 'Quadrantids', 'Leonids', 'Orionids'],
    'Peak ZHR': [100, 120, 80, 15, 25],
    'Entry Speed (km/s)': [59, 35, 41, 71, 66],
    'Parent Body Type': ['Comet', 'Asteroid', 'Asteroid', 'Comet', 'Comet']
}

df = pd.DataFrame(data)
print(df)

# ── Colors ────────────────────────────────────────────────────────
colors = {'Comet': '#E8A838', 'Asteroid': '#5B8FE8'}
bar_colors = [colors[t] for t in df['Parent Body Type']]

# ── Figure setup ─────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.patch.set_facecolor('#0A0E2A')

# ── Left: Bar chart (Peak ZHR) ────────────────────────────────────
ax1 = axes[0]
ax1.set_facecolor('#111840')
bars = ax1.barh(df['Shower'], df['Peak ZHR'], color=bar_colors, edgecolor='none', height=0.55)

ax1.set_xlabel('Meteors per Hour (ZHR)', color='#C8D6F0', fontsize=11)
ax1.set_title('Peak Activity Rate', color='white', fontsize=14, fontweight='bold', pad=12)
ax1.tick_params(colors='#C8D6F0', labelsize=11)
ax1.spines['bottom'].set_color('#2E4A8A')
ax1.spines['left'].set_color('#2E4A8A')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.xaxis.label.set_color('#C8D6F0')
ax1.set_xlim(0, 140)

# Add value labels on each bar
for bar, val in zip(bars, df['Peak ZHR']):
    ax1.text(val + 2, bar.get_y() + bar.get_height() / 2,
             f'~{val}', va='center', color='white', fontsize=10, fontweight='bold')

# ── Right: Scatter (Speed vs. Activity) ───────────────────────────
ax2 = axes[1]
ax2.set_facecolor('#111840')

for _, row in df.iterrows():
    ax2.scatter(row['Entry Speed (km/s)'], row['Peak ZHR'],
                color=colors[row['Parent Body Type']],
                s=160, zorder=3, edgecolors='white', linewidths=0.6)
    ax2.annotate(row['Shower'],
                 (row['Entry Speed (km/s)'], row['Peak ZHR']),
                 textcoords='offset points', xytext=(7, 4),
                 color='#C8D6F0', fontsize=10)

ax2.set_xlabel('Entry Speed (km/s)', color='#C8D6F0', fontsize=11)
ax2.set_ylabel('Peak ZHR', color='#C8D6F0', fontsize=11)
ax2.set_title('Speed vs. Activity', color='white', fontsize=14, fontweight='bold', pad=12)
ax2.tick_params(colors='#C8D6F0', labelsize=10)
for spine in ax2.spines.values():
    spine.set_color('#2E4A8A')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.grid(color='#2E4A8A', linestyle='--', linewidth=0.5, alpha=0.5)

# ── Shared legend ─────────────────────────────────────────────────
legend_patches = [
    mpatches.Patch(color='#E8A838', label='Comet origin'),
    mpatches.Patch(color='#5B8FE8', label='Asteroid origin')
]
fig.legend(handles=legend_patches, loc='lower center', ncol=2,
           frameon=False, fontsize=11,
           labelcolor='#C8D6F0', bbox_to_anchor=(0.5, -0.02))

fig.suptitle('Meteor Shower Comparison', color='white', fontsize=16, fontweight='bold', y=1.01)
plt.tight_layout(rect=[0, 0.06, 1, 1])

plt.savefig('meteor_chart.png', dpi=150, bbox_inches='tight',
            facecolor='#0A0E2A', edgecolor='none')
plt.show()
print("Chart saved!")
