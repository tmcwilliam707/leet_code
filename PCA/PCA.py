import numpy as np
from PIL import Image
import requests
from io import BytesIO
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

url = "PCA/Image.jpg"
response = requests.get(url)
img = Image.open(BytesIO(response.content))

# Convert the image to grayscale
img_gray = img.convert('L')

# Convert the image to a numpy array
img_array = np.array(img_gray)

# Flatten the image array and perform PCA
img_flattened = img_array.flatten().reshape(1, -1)
pca = PCA(n_components=200)
pca.fit(img_flattened)

# Use the principal components to reconstruct the image
components = pca.transform(img_flattened)
projected = pca.inverse_transform(components)

# Reshape the reconstructed image to its original dimensions
reconstructed_img = projected.reshape(img_array.shape)

# Display the original and reconstructed images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img_array, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(reconstructed_img, cmap='gray')
plt.title('Reconstructed Image')

plt.show()

reconstructed_img_pil = Image.fromarray(reconstructed_img.astype('uint8'))
reconstructed_img_pil.save('reconstructed_image.jpg')