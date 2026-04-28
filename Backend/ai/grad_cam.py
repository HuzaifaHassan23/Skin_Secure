import numpy as np
import tensorflow as tf
import cv2

def generate_gradcam_heatmap(img_array, model, last_conv_layer_name="resnet50"):
    """
    Robust Grad-CAM for nested Sequential models in modern TensorFlow.
    """
    # 1. Manually trace the layers to bypass the Sequential .output bug
    inputs = tf.keras.Input(shape=(224, 224, 3))
    x = inputs
    conv_output = None
    
    # Loop through the colleague's model and connect the layers
    for layer in model.layers:
        x = layer(x)
        if layer.name == last_conv_layer_name:
            conv_output = x
            
    # Check if we successfully grabbed the ResNet50 output
    if conv_output is None:
        raise ValueError(f"Layer {last_conv_layer_name} not found in model.")
        
    # Create a new, bug-free graph
    grad_model = tf.keras.Model(inputs, [conv_output, x])

    # 2. GradientTape records the math
    with tf.GradientTape() as tape:
        last_conv_layer_output, preds = grad_model(img_array)
        pred_index = tf.argmax(preds[0]) 
        class_channel = preds[:, pred_index]

    # 3. Calculate gradients
    grads = tape.gradient(class_channel, last_conv_layer_output)
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))

    # 4. Multiply feature map by importance weights
    last_conv_layer_output = last_conv_layer_output[0]
    heatmap = last_conv_layer_output @ pooled_grads[..., tf.newaxis] # type: ignore
    heatmap = tf.squeeze(heatmap)

    # 5. Normalize (ReLU)
    heatmap = tf.maximum(heatmap, 0)
    max_val = tf.math.reduce_max(heatmap)
    
    # Prevent division by zero
    if max_val > 0:
        heatmap = heatmap / max_val
        
    return heatmap.numpy()