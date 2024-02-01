# UNet Algorithm on MSLS
This includes all of the files from my Saturn Cloud UNET enviroment. To run, make sure your data is stored in data in the appropriate folders. There is already data there.
## extract_slices.ipynb
I have already extracted the slices from the raw flairs from the MICCAI Challenge 2016. This is the code that I used for that
## UNET_MSLS_test.ipynb
This code was created by Thomas Grenier from Creatis Lab. This is used to test a pre-trained model located in the pretrained_model folder on the test data. Run all cells to do so.
## UNET_MSLS_train.ipynb
This code was created by Thomas Grenier from Creatis Lab. This is used to train a new model that will be stored in the trained_model folder. Run all cells to do so.
## trained_model folder
This folder includes the trained model that I have during my own testing.