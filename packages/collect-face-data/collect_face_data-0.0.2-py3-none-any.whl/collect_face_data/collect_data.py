import cv2
import time
from mtcnn_cv2 import MTCNN
import os
import random
from scipy import ndimage
from glob import glob
import math
from math import sqrt
import copy 
import shutil

class InputData():

    def __init__(self, source=0, output_path="", label="user_id" , num_of_img=30, percent_test=20, augment=False) -> None:
        self.source = source
        self.user_id = label.upper()
        self.num_of_img = num_of_img
        self.augment = augment
        self.percent_test = percent_test
        self.train_path = output_path + r"/train"
        self.test_path = output_path + r"/test"
        try:
            os.mkdir(output_path + r"/train")
        except FileExistsError:
            pass
        try:
            os.mkdir(output_path + r"/test")
        except FileExistsError:
            pass

        self.temp_dir = output_path + f"/temp"

    def run(self):
        if self.num_of_img < 1:
            return print("Please input number of image!")
        start = time.time()
        try:
            shutil.rmtree(self.temp_dir, ignore_errors=True)
            os.mkdir(self.temp_dir)
        except FileExistsError:
            pass
        status = self.get_image()
        if not status: 
            shutil.rmtree(self.temp_dir, ignore_errors=True)
            return print("Data not enough. Please try again!")
        if self.augment:
            self.augment_data(self.temp_dir)
        end = time.time()
        total = end - start
        # write data to test folder
        self.split_data(self.temp_dir, self.test_path, self.percent_test)
        # write data to train folder
        self.split_data(self.temp_dir, self.train_path)
        try:
            shutil.rmtree(self.temp_dir, ignore_errors=True)
        except:
            print("Please try again")
        print("Done!", f"{total}s")

    def split_data(self, src_path, des_path, percent_test=100): 
        des_path = des_path + f"/{self.user_id}"
        try:
            os.mkdir(des_path)
        except FileExistsError:
            pass
        list_img = []
        for ext in ["png", "jpg", "jpeg"]:
            list_img += glob(src_path + "/*." + f"{ext}")
        num_of_test_img = math.floor(len(list_img)*percent_test/100)
        list_test_img = random.sample(list_img, num_of_test_img)
        for test_img in list_test_img:
            current = test_img.replace("\\", "/")
            img_name = current.split("/")[-1]
            destination = des_path + "/" + f"{img_name}"
            shutil.move(current, destination)

    def check_face_fully_visible(self, image, keypoints):
        h, w, c = image.shape
        for key in keypoints:
            key_w, key_h = keypoints[key]
            if (key_w*key_h == 0) or key_w > w or key_h > h:
                return False
        return True
    
    def check_face_exist(self, image):
        detector = MTCNN()
        result = detector.detect_faces(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        if len(result) > 0 and self.check_face_fully_visible(image, result[0]["keypoints"]):
            return True
        else:
            return False

    def get_image(self):
        print("Loading...")
        cam = cv2.VideoCapture(self.source)
        img_counter = 0
        frame_num = 0
        detector = MTCNN()
        start = time.time()
        red_flag = 10
        img_size = 180
        scale_w = 30
        scale_h = 0
        percent_progress = 0
        try:
            os.mkdir(self.temp_dir)
        except FileExistsError:
            pass
        print("Start")
        while True:
            ret, frame = cam.read()
            h, w, c = frame.shape
            frame = frame[round(h/2)-img_size:round(h/2)+img_size, round(w/2)-img_size:round(w/2)+img_size]
            h, w, c = frame.shape
            if not ret:
                print("failed to grab frame")
                break
            visible_frame = copy.deepcopy(frame)
            result = detector.detect_faces(cv2.cvtColor(visible_frame[scale_h:h-scale_h, scale_w:w-scale_w], cv2.COLOR_BGR2RGB))
            keypoints = {}
            check_face = False
            nose = ()

            if len(result) == 1:
                bounding_box = result[0]['box']
                # check if the face is small (less 20% than frame ==> ignore)
                if sqrt(bounding_box[2]**2+bounding_box[3]**2) > sqrt(h**2+w**2)*0.4:
                    keypoints = result[0]["keypoints"]
                    nose = list(keypoints['nose'])
                    nose[0] = nose[0] + scale_w
                    nose[1] = nose[1] + scale_h
                    nose = tuple(nose)
                    if self.check_face_fully_visible(visible_frame[scale_h+10:h-(scale_h+10), scale_w+10:w-(scale_w+10)], keypoints):
                        check_face = True
            # tracking face
            img_track = copy.deepcopy(frame)
            h, w, _ = frame.shape
            try:
                if check_face and abs(nose[0]-round(w/2)) < sqrt((img_size-50)**2-(nose[1]-round(h/2))**2) \
                and abs(nose[1]-round(h/2)) < sqrt((img_size-50)**2-(nose[0]-round(w/2))**2):
                    try:
                        x,y,r = self.findCircle(nose, (round(w/2)-img_size, round(h/2)), (round(w/2)+img_size, round(h/2)))
                        cv2.circle(img_track, (round(x), round(y)), round(r), (255,255,255), thickness=2)
                    except ZeroDivisionError:
                        cv2.line(img_track, (round(w/2)-img_size, round(h/2)), (round(w/2)+img_size, round(h/2)), (255,255,255), thickness=2)
                    try:
                        x,y,r = self.findCircle(nose, (round(w/2), round(h/2)-img_size), (round(w/2), round(h/2)+img_size))
                        cv2.circle(img_track, (round(x), round(y)), round(r), (255,255,255), thickness=2)
                    except ZeroDivisionError:
                        cv2.line(img_track, (round(w/2), round(h/2)-img_size), (round(w/2), round(h/2)+img_size), (255,255,255), thickness=2)
                else:
                    check_face = False
            except:
                img_track = copy.deepcopy(frame)
            

            # write image
            if check_face and red_flag > 10 and (frame_num == 0  or frame_num > 5):
                if img_counter==0:
                        old_keypoints = keypoints

                if img_counter==0 or self.check_different(old_keypoints, keypoints):
                    old_keypoints = keypoints
                    img_name = f"{self.temp_dir}/{self.user_id}_{round(time.time())}{img_counter}.png"
                    cv2.imwrite(img_name, frame[scale_h:h-scale_h, scale_w:w-scale_w])
                    print(f"{img_name} has been written! {img_counter+1}")
                    img_counter += 1
                    frame_num = 0
                    percent_progress = round((img_counter/self.num_of_img)*100)
            
            # draw info
            img_track = cv2.flip(img_track, 1)
            img = copy.deepcopy(img_track)
            img_temp = copy.deepcopy(img_track)
            cv2.circle(img, (round(w/2), round(h/2)), img_size, (0,0,0), thickness=-1)
            visible_frame = cv2.subtract(img_temp, img)
            if check_face:
                cv2.circle(visible_frame, (round(w/2), round(h/2)), img_size, (0,255,0), thickness=2)
                cv2.circle(visible_frame, (round(w/2), round(h/2)), img_size-50, (0,255,0), thickness=2)
            # cv2.rectangle(visible_frame, (scale_w, scale_h), (round(w)-scale_w, round(h)-scale_h), (0,0,255), thickness=2)
            visible_frame = cv2.copyMakeBorder(visible_frame,50,150,150,150,cv2.BORDER_CONSTANT,value=[0, 0, 0])
            # check if more than 1 people, red_flag is delay frame after more than 1 people appear
            if len(result) > 1 or red_flag < 10:
                cv2.putText(visible_frame, "Confirm only one face and nothing like a face.", (25, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                        1, (50, 50, 255), thickness=1)
                if len(result) > 1: 
                    red_flag = 0
            red_flag += 1
            cv2.putText(visible_frame, str(percent_progress) + "%", (300, 450), cv2.FONT_HERSHEY_DUPLEX,
                                            1, (0, 255, 0), thickness=1)
            cv2.putText(visible_frame, "Approach the camera until 2 green circles appear.", (10, 480), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                            1, (255, 255, 255), thickness=1)
            cv2.putText(visible_frame, "Move your head slowly to complete.", (10, 510), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                            1, (255, 255, 255), thickness=1)
            cv2.putText(visible_frame, "Make sure your nose is inside the small circle.", (10, 540), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                            1, (255, 255, 255), thickness=1)
            cv2.imshow("visible_frame", visible_frame)
            cv2.waitKey(1)
             
            frame_num += 1
            end = time.time()
            total = end - start
            if img_counter==self.num_of_img or total>120: 
                cam.release()
                cv2.destroyAllWindows()
                if img_counter<self.num_of_img:
                    return False
                else:
                    return True

    def check_different(self, keypoints_1, keypoints_2):
        threshold = 30
        for key in keypoints_1:
            if self.cal_vector(keypoints_1[key], keypoints_2[key]) < threshold:
                return False
        return True
    
    def cal_vector(slef, point_A, point_B):
        return sqrt((point_A[0]-point_B[0])**2 + (point_A[1]-point_B[1])**2)    

    def augment_data(self, source_path):
        i = 0
        print("Augment image")
        for img_name in glob(f"{source_path}/*.png"): 
            if img_name.split("_")[-1].split(".")[0].isnumeric():
                i += 1
                img = cv2.imread(img_name)

                # Increase brightness (alpha: constract, beta: brightness )
                if "_ib.png" not in img_name:
                    new_image = cv2.convertScaleAbs(img, alpha=1.5, beta=40)
                    new_img_name = img_name.replace(".png", "_ib.png")
                    cv2.imwrite(new_img_name, new_image)
                # Decrease brightness(alpha: constract, beta: brightness )
                if "_ib.png" not in img_name:
                    new_image = cv2.convertScaleAbs(img, alpha=1.5, beta=-40)
                    new_img_name = img_name.replace(".png", "_db.png")
                    cv2.imwrite(new_img_name, new_image)
                #Rotate POSITIVE degree
                if "_ib.png" not in img_name:
                    new_image = ndimage.rotate(img, 10)
                    new_img_name = img_name.replace(".png", "_pr.png")
                    cv2.imwrite(new_img_name, new_image)
                # Rotate NEGATIVE degree
                if "_ib.png" not in img_name:
                    new_image = ndimage.rotate(img, -10)
                    new_img_name = img_name.replace(".png", "_nr.png")
                    cv2.imwrite(new_img_name, new_image)
                # Mirror
                if "_ib.png" not in img_name:
                    new_image = cv2.flip(img, 1)
                    new_img_name = img_name.replace(".png", "_m.png")
                    cv2.imwrite(new_img_name, new_image)
    def findCircle(self, p1, p2, p3) :
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3

        x12 = x1 - x2
        x13 = x1 - x3
    
        y12 = y1 - y2
        y13 = y1 - y3
    
        y31 = y3 - y1
        y21 = y2 - y1
    
        x31 = x3 - x1
        x21 = x2 - x1
    
        # x1^2 - x3^2
        sx13 = pow(x1, 2) - pow(x3, 2)
    
        # y1^2 - y3^2
        sy13 = pow(y1, 2) - pow(y3, 2)
    
        sx21 = pow(x2, 2) - pow(x1, 2)
        sy21 = pow(y2, 2) - pow(y1, 2)
    
        f = (((sx13) * (x12) + (sy13) *
            (x12) + (sx21) * (x13) +
            (sy21) * (x13)) // (2 *
            ((y31) * (x12) - (y21) * (x13))))
                
        g = (((sx13) * (y12) + (sy13) * (y12) +
            (sx21) * (y13) + (sy21) * (y13)) //
            (2 * ((x31) * (y12) - (x21) * (y13))))
    
        c = (-pow(x1, 2) - pow(y1, 2) -
            2 * g * x1 - 2 * f * y1)
    
        # eqn of circle be x^2 + y^2 + 2*g*x + 2*f*y + c = 0
        # where centre is (h = -g, k = -f) and
        # radius r as r^2 = h^2 + k^2 - c
        h = -g
        k = -f
        sqr_of_r = h * h + k * k - c
    
        # r is the radius
        r = round(sqrt(sqr_of_r), 5)
        return h, k, r
    

