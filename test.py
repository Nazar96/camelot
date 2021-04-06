import numpy as np
import cv2
from matplotlib import pyplot as plt

from table_parser.parsers.lattice import Lattice
from table_parser import plot
from table_parser.utils import derotate_angle, rotate_custom, draw_lines, draw_cells
from table_parser.utils import get_cells_bbox

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

# Extract tabels
tables = parser.extract_tables(img, layout_kwargs={'run_ocr': False})
print(len(tables))

try:
    fig = plot(tables[0], kind='joint')
    fig.set_size_inches(15, 15)
    fig.show()
except:
    pass
for t in tables:
    print(t.parsing_report)
    fig = draw_lines(img, t)
    fig.set_size_inches(15, 15)
    fig.show()

# Draw the first one  and the last one cells
cell_bbox = get_cells_bbox(tables[0])
fig = draw_cells(img, [cell_bbox[0], cell_bbox[-1]])
fig.set_size_inches(15, 15)
fig.show()
