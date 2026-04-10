"""
VLA-0 Quantization Paper — Figure Generator
Run this in your local environment or a Kaggle/Colab notebook.
Outputs: vla0_pertask_results.pdf  (vector, print-quality)
         vla0_pertask_results.png  (300 dpi, fallback)

Requirements: pip install matplotlib numpy
"""

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── publication style ────────────────────────────────────────────────────────
matplotlib.rcParams.update({
    'font.family':      'serif',
    'font.size':        8,
    'axes.titlesize':   8,
    'axes.labelsize':   8,
    'xtick.labelsize':  7,
    'ytick.labelsize':  7,
    'legend.fontsize':  7,
    'figure.dpi':       300,
    'pdf.fonttype':     42,    # embed fonts — required by IEEE
    'ps.fonttype':      42,
})

# ── data ─────────────────────────────────────────────────────────────────────
tasks = [
    'Open\ndrawer',
    'Put bowl\non stove',
    'Alphabet\nsoup',
    'Cream\ncheese*',
    'Bowl\n(plate)',
    'Bowl\n(ramekin)',
]

bf16 = np.array([10, 10,  9, 10,  9, 10]) / 10 * 100
int8 = np.array([10, 10, 10,  9,  9, 10]) / 10 * 100
nf4  = np.array([ 9, 10,  8,  3,  9, 10]) / 10 * 100

x     = np.arange(len(tasks))
width = 0.26

# ── colors (IEEE-safe, print-distinguishable) ─────────────────────────────
C_BF16     = '#2166ac'   # blue
C_INT8     = '#4dac26'   # green
C_NF4      = '#d6604d'   # orange-red for normal NF4 bars
C_NF4_FAIL = '#b2182b'   # deep red for the collapse bar (cream cheese)

nf4_colors = [C_NF4_FAIL if tasks[i] == 'Cream\ncheese*' else C_NF4
              for i in range(len(tasks))]

# ── figure: single column width for IEEE two-column (3.5 inches) ──────────
fig, ax = plt.subplots(figsize=(3.5, 2.5))

bars_bf16 = ax.bar(x - width, bf16, width, color=C_BF16,  label='BF16',
                   edgecolor='white', linewidth=0.3)
bars_int8 = ax.bar(x,          int8, width, color=C_INT8,  label='INT8',
                   edgecolor='white', linewidth=0.3)
bars_nf4  = ax.bar(x + width,  nf4,  width, color=nf4_colors,
                   edgecolor='white', linewidth=0.3)

# ── annotate the collapse bar ─────────────────────────────────────────────
collapse_idx = tasks.index('Cream\ncheese*')
collapse_x   = collapse_idx + width
ax.annotate('30%',
            xy=(collapse_x, 30),
            xytext=(collapse_x + 0.45, 48),
            fontsize=6.5, color=C_NF4_FAIL, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=C_NF4_FAIL,
                            lw=0.8, connectionstyle='arc3,rad=-0.2'))

# ── axes ──────────────────────────────────────────────────────────────────
ax.set_ylabel('Task success rate (%)')
ax.set_ylim(0, 115)
ax.set_yticks([0, 25, 50, 75, 100])
ax.set_xticks(x)
ax.set_xticklabels(tasks, linespacing=1.2)
ax.yaxis.grid(True, linewidth=0.4, color='#cccccc', zorder=0)
ax.set_axisbelow(True)
ax.spines[['top', 'right']].set_visible(False)
ax.spines[['left', 'bottom']].set_linewidth(0.5)
ax.tick_params(length=2)

# ── suite dividers ────────────────────────────────────────────────────────
for xpos, label in [(0.99, 'Goal'), (2.99, 'Object'), (4.99, 'Spatial')]:
    if xpos > 0:
        ax.axvline(xpos, color='#aaaaaa', linewidth=0.5, linestyle='--', zorder=1)

# ── suite labels (above chart) ────────────────────────────────────────────
suite_centers = [0.5, 2.5, 4.5]
suite_labels  = ['Goal', 'Object', 'Spatial']
for cx, sl in zip(suite_centers, suite_labels):
    ax.text(cx, 108, sl, ha='center', va='center',
            fontsize=6.5, color='#555555',
            bbox=dict(boxstyle='round,pad=0.15', facecolor='#f5f5f5',
                      edgecolor='#cccccc', linewidth=0.4))

# ── legend ────────────────────────────────────────────────────────────────
legend_handles = [
    mpatches.Patch(color=C_BF16, label='BF16 (baseline)'),
    mpatches.Patch(color=C_INT8, label='INT8'),
    mpatches.Patch(color=C_NF4,  label='NF4'),
]
ax.legend(handles=legend_handles, loc='lower left',
          frameon=True, framealpha=0.9, edgecolor='#cccccc',
          borderpad=0.4, labelspacing=0.2, handlelength=1.2,
          handletextpad=0.4)

# ── caption note (below x-axis) ──────────────────────────────────────────
fig.text(0.5, -0.04,
         '* Cream cheese NF4 vs. BF16: $p = 0.003$ (Fisher\'s exact)',
         ha='center', fontsize=6, color='#555555', style='italic')

plt.tight_layout(pad=0.4)

# ── save ──────────────────────────────────────────────────────────────────
plt.savefig('vla0_pertask_results.pdf', bbox_inches='tight',
            pad_inches=0.02, format='pdf')
plt.savefig('vla0_pertask_results.png', bbox_inches='tight',
            pad_inches=0.02, dpi=300)

print("Saved: vla0_pertask_results.pdf")
print("Saved: vla0_pertask_results.png")
plt.show()
