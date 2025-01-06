#!/bin/bash
# Create a Conda environment for YOLO
echo "Creating a Conda environment for YOLO..."
conda create -n yolovenv python=3.8 -y

# Activate the environment
echo "Activating the Conda environment..."
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate yolovenv

# Install necessary Python packages
echo "Installing YOLO dependencies..."
pip install ultralytics

# Install LabelImg
echo "Installing LabelImg"
pip install labelimg

# Confirm setup
echo "YOLO environment setup is complete. You can now use the 'yolovenv' environment."
echo "To activate it manually, use: conda activate yolovenv"
