from imageai.Detection import VideoObjectDetection
import time

start = time.time()

model_path = "models/yolo-tiny.h5"
input_path = "input/video_street.mp4"
output_path = "output/detected_video"

detector = VideoObjectDetection()
detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath(model_path)
detector.loadModel()

video_path = detector.detectObjectsFromVideo(input_file_path=input_path,
                                             output_file_path=output_path,
                                             frames_per_second=20,
                                             log_progress=True,
                                             minimum_percentage_probability=45)
print(video_path)

end = time.time()
print(f'detection took {end - start} seconds')
