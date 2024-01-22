import cv2

# Input and output file paths
source = "44.png"
destination = "newimage.png"

# Percentage by which the image will be scaled
scale_percent = 50

# Read the source image with unchanged color channels
src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

# src.shape[0]: Height of the image.
# src.shape[1]: Width of the image.
# src.shape[2]: Number of channels in the image (e.g., 3 for RGB or 4 for RGBA).
# Calculate the new dimensions based on the scaling percentage
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

# Resize the image using the calculated dimensions
output = cv2.resize(src, (new_width, new_height))

# Save the resized image to the destination path
cv2.imwrite(destination, output)

# Wait until a key is pressed (you may change this behavior based on your needs)
cv2.waitKey()

