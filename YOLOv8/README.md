# YOLOv8 Algorithm on MSLS (doesn't work yet)
This includes all of the files from my Saturn Cloud YOLOv8 enviroment. To run, make sure your data is stored in datasets/data in their appropriate folders. YOLO is very particular about their names and where to store the files, so try not to change the configuration if you want to do so.
In order to run these, first put your test and train data in their respective folders. Make sure you images are in the image folder and then your masks are in the labels folder. Then you can run preprocessing.ipynb which will automatically 1) resize your images for the 640x640 pixel requirement in YOLO, 2) generate bounding boxes from the masks and replace the masks .png files with the bounding box .txt files, and 3) move 20% of the images and labels from train into the validation folder.
## data.yaml
This is the configuration in which YOLO reads to understand where the data is and what are the classes that it is segmenting
## preprocessing.ipynb
This is the notebook where if you have your images and masks in the images and labels folder respectivly, it will 1) resize your images for the 640x640 pixel requirement in YOLO, 2) generate bounding boxes from the masks and replace the masks .png files with the bounding box .txt files, and 3) move 20% of the images and labels from train into the 
## YOLO_MSLS.ipynb
The simple notebook that runs the model. Currently experiencing issues relating to the CUDA going outside of the bounds.
## yolov8n-seg.pt
A pretrained model from ultralytics that does segmentation.