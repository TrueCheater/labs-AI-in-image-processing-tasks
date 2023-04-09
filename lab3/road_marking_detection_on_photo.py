import cv2
import numpy as np

img = cv2.imread('media/road.jpg')

grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel_size = 5
blur = cv2.GaussianBlur(grayscale, (kernel_size, kernel_size), 0)

low_t = 50
high_t = 150
edges = cv2.Canny(blur, low_t, high_t)

vertices = np.array([[
    (70, img.shape[0]), (200, 110), (360, 110), (img.shape[1], img.shape[0])
]], dtype=np.int32)
mask = np.zeros_like(edges)
ignore_mask_color = 255
cv2.fillPoly(mask, vertices, ignore_mask_color)
masked_edges = cv2.bitwise_and(edges, mask)


def draw_lines(image, lines, color=[255, 0, 0], thickness=7):
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(image, (x1, y1), (x2, y2), color, thickness)


rho = 1
theta = np.pi / 180
threshold = 15
min_line_len = 150
max_line_gap = 60
lines = cv2.HoughLinesP(masked_edges, rho, theta, threshold, np.array([]), minLineLength=min_line_len,
                        maxLineGap=max_line_gap)

try:
    draw_lines(img, lines)
except:
    pass

cv2.imshow('road', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
