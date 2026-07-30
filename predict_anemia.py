import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import tkinter as tk
from tkinter import filedialog, messagebox

# Hide the main tkinter window
root = tk.Tk()
root.withdraw()

# Load your trained model
model_path = r"C:\Users\anany\OneDrive\Desktop\anemic detection\code\anemia_cnn_model.h5"
model = tf.keras.models.load_model(model_path)

# Open file dialog to select image
messagebox.showinfo("Select Image", "Please select the eye image to predict.")
file_path = filedialog.askopenfilename(
    title="Select Eye Image",
    filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]
)

if not file_path:
    messagebox.showwarning("No File Selected", "No image was selected. Exiting.")
    exit()

# Load and preprocess the image
img = image.load_img(file_path, target_size=(150, 150))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array /= 255.0

# Predict
prediction = model.predict(img_array)
predicted_class = "Anemic" if prediction[0][0] > 0.5 else "Non-Anemic"

# Show result
messagebox.showinfo("Prediction Result", f"The model predicts: {predicted_class}")

print(f"\nPrediction complete! The image is classified as: {predicted_class}")
print(f" Image path: {file_path}")
