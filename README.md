# YOLO-Vegetables

This is a small personal project where I trained a YOLO model on a custom dataset consisting of vegetables. The goal was to explore object detection using custom-labeled data.

Overview

	•	Dataset: The dataset consists of various vegetable images, annotated using Roboflow.
	•	Model: YOLO (You Only Look Once) was selected as the object detection model for its speed and performance.
	•	Training: The model was trained using Google Colab to leverage free GPU resources.

Files in this Repository

	•	best_yolov11s_100epochs.pt: The trained YOLOv11 model, saved after 100 epochs.
	•	YOLO_vegetables.ipynb: The Jupyter Notebook used for training the model in Google Colab, including data preparation, training routines, and evaluation.
	•	main.py: A script to open the webcam and run real-time object detection using the trained YOLO model.

Steps

	1.	Data Collection: Images of vegetables were gathered and organized into a dataset.
	2.	Annotation: Used Roboflow to annotate and prepare the data for YOLO training.
	3.	Model Training: Trained the YOLO model in Google Colab, utilizing GPU acceleration for faster training.
