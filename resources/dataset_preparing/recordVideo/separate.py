import cv2
vidcap = cv2.VideoCapture('WIN_20180903_14_23_55_Pro.mp4')
success,image = vidcap.read()
count = 0
start=1
success = True
while success:
	success,image = vidcap.read()
	if count%20==0:
		print('Read a new frame: ', success)
		img = cv2.resize(image, (480, 360))
		cv2.imwrite("Images/%d.jpg" % start, img)     # save frame as JPEG file
		start+=1
	count += 1
