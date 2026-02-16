# Create a printable 7-branch antibiotic disc layout template (90 mm plate)

import numpy as np
import matplotlib.pyplot as plt

# Physical plate dimensions
plate_diameter_mm = 90  # standard petri dish
plate_radius_mm = plate_diameter_mm / 2

# Recommended center-to-edge buffer for disc centers (~15 mm from rim)
disc_center_radius_mm = 30  # distance of disc centers from plate center

# Angles for 7 evenly spaced branches (in degrees), starting at 90° (top) and going clockwise
n = 7
angles_deg = [90 - i * (360 / n) for i in range(n)]

# Figure size in inches to approximate true-to-scale (90 mm ≈ 3.543 in)
fig_size_in = (90 / 25.4, 90 / 25.4)

def draw_template(save_path_pdf="antibiotic_disc_template_7_branches.pdf",
                  save_path_png="antibiotic_disc_template_7_branches.png"):
    fig = plt.figure(figsize=fig_size_in)
    ax = fig.add_axes([0, 0, 1, 1])  # full-bleed
    ax.set_aspect('equal')
    ax.axis('off')

    # Center dot
    ax.plot(0, 0, marker='o', markersize=60, color='#f9eef9')

    # Place seven markers and labels
    labels = ['CPX', 'FO', 'AM', 'PS', 'EN', 'GN', 'TM']
    for idx, (ang, lab) in enumerate(zip(angles_deg, labels)):
        rad = np.deg2rad(ang)
        x = disc_center_radius_mm * np.cos(rad)
        y = disc_center_radius_mm * np.sin(rad)
        ax.plot(x, y, marker='o', markersize=30, color='blue')
       # Small tick mark towards center to help placement
        tick_inset_mm = 20
        x_in = (disc_center_radius_mm - tick_inset_mm) * np.cos(rad)
        y_in = (disc_center_radius_mm - tick_inset_mm) * np.sin(rad)
        ax.plot([x_in, x], [y_in, y], linewidth=15, color='blue')

        # Label slightly outside the point
        label_offset_mm = 0
        x_lab = (disc_center_radius_mm + label_offset_mm) * np.cos(rad)
        y_lab = (disc_center_radius_mm + label_offset_mm) * np.sin(rad)
        ax.text(x_lab, y_lab, lab, ha='center', va='center', fontsize=9)

    # Limits tightly fit the 90 mm circle
    lim = plate_radius_mm + 2
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)

    fig.savefig(save_path_pdf, bbox_inches='tight', pad_inches=0)
    fig.savefig(save_path_png, dpi=300, bbox_inches='tight', pad_inches=0)
    plt.close(fig)
    return save_path_pdf, save_path_png

pdf_path, png_path = draw_template()
(pdf_path, png_path)
