from table_parser.parsers.lattice import Lattice
from table_parser import plot
from table_parser.utils import derotate_angle, rotate_custom, draw_lines, draw_cells

import numpy as np
import cv2
import matplotlib.pyplot as plt

img_path = './path_to_image.png'

# Rotate image
angle = np.random.uniform(-3, 3)
img = cv2.imread(img_path)
img = rotate_custom(img, angle)

plt.figure(figsize=(15, 15))
plt.imshow(img)
plt.show()

# Derotate image
derot_angle = derotate_angle(img)
img = rotate_custom(img, derot_angle)
parser = Lattice()

# Extract tables
tables = parser.extract_tables(img)
print(len(tables))

fig = plot(tables[0], kind='joint')
fig.set_size_inches(15, 15)
fig.show()

for t in tables:
    print(t.parsing_report)
    fig = draw_lines(img, t)
    fig.set_size_inches(15, 15)
    fig.show()

# Draw certain cells
spans = tables[-1].spans[:10:2]
fig = draw_cells(img, spans, alpha=0.9)
fig.set_size_inches(15, 15)
fig.show()
