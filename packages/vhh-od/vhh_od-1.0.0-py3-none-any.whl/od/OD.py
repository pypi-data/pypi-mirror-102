from od.Configuration import Configuration
from od.Video import Video
from od.Models import *
from od.utils import *
from od.Shot import Shot
from od.CustObject import CustObject
from od.visualize import visualize_video

from deep_sort.deep_sort import DeepSort

import numpy as np
import os
import cv2
from matplotlib import cm
import torch
from torch.autograd import Variable
from torch.utils import data
from torchvision import transforms


class OD(object):
    """
        Main class of shot type classification (stc) package.
    """

    def __init__(self, config_file: str):
        """
        Constructor

        :param config_file: [required] path to configuration file (e.g. PATH_TO/config.yaml)
                                       must be with extension ".yaml"
        """

        if (config_file == ""):
            printCustom("No configuration file specified!", STDOUT_TYPE.ERROR)
            exit()

        self.config_instance = Configuration(config_file)
        self.config_instance.loadConfig()

        if (self.config_instance.debug_flag == True):
            print("DEBUG MODE activated!")
            self.debug_results = "/data/share/maxrecall_vhh_mmsi/develop/videos/results/od/develop/"

        # prepare object detection model
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.use_tracker = self.config_instance.use_deepsort

        if self.use_tracker:
            printCustom(f"Initializing Deep Sort Tracker...", STDOUT_TYPE.INFO)
            ds_model_path = self.config_instance.ds_model_path
            ds_max_dist = self.config_instance.ds_max_dist
            ds_min_conf = self.config_instance.ds_min_conf
            ds_nms_max_overlap = self.config_instance.ds_nms_max_overlap
            ds_max_iou_dist = self.config_instance.ds_max_iou_dist
            ds_max_age = self.config_instance.ds_max_age
            ds_num_init = self.config_instance.ds_num_init
            use_cuda = (self.device == "cuda")

            self.tracker = DeepSort(ds_model_path, ds_max_dist, ds_min_conf, ds_nms_max_overlap, ds_max_iou_dist, ds_max_age,
                               ds_num_init, use_cuda=torch.cuda.is_available())
            printCustom(f"Deep Sort Tracker initialized successfully!", STDOUT_TYPE.INFO)

        self.num_colors = 10
        self.color_map = cm.get_cmap('gist_rainbow', self.num_colors)


    def runOnSingleVideo(self, shots_per_vid_np=None, max_recall_id=-1):
        """
        Method to run stc classification on specified video.

        :param shots_per_vid_np: [required] numpy array representing all detected shots in a video
                                 (e.g. sid | movie_name | start | end )
        :param max_recall_id: [required] integer value holding unique video id from VHH MMSI system
        """

        print("run od detector on single video ... ")

        if (type(shots_per_vid_np) == None):
            print("ERROR: you have to set the parameter shots_per_vid_np!")
            exit()

        if (max_recall_id == -1 or max_recall_id == 0):
            print("ERROR: you have to set a valid max_recall_id [1-n]!")
            exit()

        if(self.config_instance.debug_flag == True):
            # load shot list from result file
            printCustom(f"Loading SBD Results from \"{self.config_instance.sbd_results_path}\"...", STDOUT_TYPE.INFO)
            shots_np = self.loadSbdResults(self.config_instance.sbd_results_path)
        else:
            shots_np = shots_per_vid_np

        if (len(shots_np) == 0):
            print("ERROR: there must be at least one shot in the list!")
            exit()

        if (self.config_instance.debug_flag == True):
            num_shots = 10
            offset = 0
        else:
            num_shots = len(shots_per_vid_np)
            offset = 0

        # load video instance
        vid_name = shots_np[0][0]
        vid_instance = Video()
        vid_instance.load(os.path.join(self.config_instance.path_videos, vid_name))

        # prepare numpy shot list
        shot_instance = None
        for s in range(offset, offset + num_shots):
            # print(shots_per_vid_np[s])
            shot_instance = Shot(sid=int(s + 1),
                                 movie_name=shots_per_vid_np[s][0],
                                 start_pos=int(shots_per_vid_np[s][2]),
                                 end_pos=int(shots_per_vid_np[s][3]) + 1 )

            vid_instance.addShotObject(shot_obj=shot_instance)

        printCustom(f"Initializing Model using \"{self.config_instance.model_config_path}\"...", STDOUT_TYPE.INFO)
        model = Darknet(config_path=self.config_instance.model_config_path,
                        img_size=self.config_instance.resize_dim).to(self.device)

        printCustom(f"Loading Weights from \"{self.config_instance.path_pre_trained_model}\"...", STDOUT_TYPE.INFO)
        if self.config_instance.path_pre_trained_model.endswith(".weights"):
            # Load darknet weights
            model.load_darknet_weights(self.config_instance.path_pre_trained_model)
        else:
            # Load checkpoint weights
            model.load_state_dict(torch.load(self.config_instance.path_pre_trained_model))

        printCustom(f"Loading Class Names from \"{self.config_instance.model_class_names_path}\"... ", STDOUT_TYPE.INFO)
        classes = load_classes(self.config_instance.model_class_names_path)

        printCustom(f"Loading Class Selection from \"{self.config_instance.model_class_selection_path}\"... ", STDOUT_TYPE.INFO)
        class_selection = load_classes(self.config_instance.model_class_selection_path)
        printCustom(f"Classes of interest: {class_selection}", STDOUT_TYPE.INFO)

        # prepare transformation for od model
        preprocess = transforms.Compose([
            transforms.ToPILImage(),
            # transforms.Resize((int(vid_instance.height), vid_instance.width)),
            # transforms.CenterCrop((int(vid_instance.height), int(vid_instance.height))),
            transforms.Resize(self.config_instance.resize_dim),
            # ToGrayScale(),
            transforms.ToTensor(),
            # transforms.Normalize((self.config_instance.mean_values[0] / 255.0,
            #                      self.config_instance.mean_values[1] / 255.0,
            #                      self.config_instance.mean_values[2] / 255.0),
            #                     (self.config_instance.std_dev[0] / 255.0,
            #                      self.config_instance.std_dev[1] / 255.0,
            #                      self.config_instance.std_dev[2] / 255.0))
        ])

        resized_dim_y = self.config_instance.resize_dim[0]
        resized_dim_x = self.config_instance.resize_dim[1]

        # Old solution for retrieving all frames at once
        # frames = vid_instance.getAllFrames(preprocess_pytorch=preprocess)
        # all_tensors_l = frames["Tensors"]
        # images_orig = frames["Images"]

        printCustom(f"Starting Object Detection (Executing on device {self.device})... ", STDOUT_TYPE.INFO)
        results_od_l = []

        for shot_frames in vid_instance.getFramesByShots_NEW(preprocess_pytorch=preprocess):
            shot_tensors = shot_frames["Tensors"]
            images_orig = shot_frames["Images"]
            current_shot = shot_frames["ShotInfo"]

            shot_id = int(current_shot.sid)
            vid_name = str(current_shot.movie_name)
            start = int(current_shot.start_pos)
            stop = int(current_shot.end_pos)

            if(self.config_instance.debug_flag == True):
                print("-----")
                print(f"Video Name: {vid_name}")
                print(f"Shot ID: {shot_id}")
                print(f"Start: {start} / Stop: {stop}")
                print(f"Duration: {stop - start} Frames")

            # run od detector
            predictions_l = self.runModel(model=model, tensor_l=shot_tensors, classes=classes, class_filter=class_selection)

            # reset tracker for every new shot
            if self.use_tracker:
                self.tracker.reset()

            # for each frame, track predictions and store results
            for a in range(0, len(predictions_l)):
                frame_id = start + a
                frame_based_predictions = predictions_l[a]
                obj_id = 0

                if(self.config_instance.debug_flag == True):
                    print("##################################################################################")

                if (frame_based_predictions is None):
                    results_od_l.append(["None", shot_id, vid_name, start, stop, frame_id,
                                         "None", "None", "None", "None", "None", "None", "None"])

                    if (self.config_instance.debug_flag == True):
                        tmp = str(None) + ";" + str(shot_id) + ";" + str(vid_name) + ";" + str(start) + ";" + str(
                            stop) + ";" + str(frame_id) + ";" + str(None) + ";" + str(None) + ";" + str(
                            None) + ";" + str(None) + ";" + str(None) + ";" + str(None) + ";" + str(None)
                        print(tmp)
                else:

                    # rescale bounding boxes to fit original video resolution
                    im = cv2.cvtColor(images_orig[a], cv2.COLOR_BGR2RGB)
                    y_factor = im.shape[0] / resized_dim_y
                    x_factor = im.shape[1] / resized_dim_x
                    x = (frame_based_predictions[:, 0]).cpu().numpy() * x_factor
                    y = (frame_based_predictions[:, 1]).cpu().numpy() * y_factor
                    w = (frame_based_predictions[:, 2]).cpu().numpy() * x_factor - x
                    h = (frame_based_predictions[:, 3]).cpu().numpy() * y_factor - y

                    if self.use_tracker:

                        # Convert BBoxes from XYXY (corner points) to XYWH (center + width/height) representation
                        x = x+w/2
                        y = y+h/2
                        bbox_xywh = np.array([[x[i],y[i],w[i],h[i]] for i in range(len(frame_based_predictions))])

                        # get class confidences
                        cls_conf = frame_based_predictions[:, 5].cpu().numpy()
                        class_predictions = frame_based_predictions[:, 6].cpu().numpy()

                        # Track Objects using Deep Sort tracker
                        # Tracker expects Input as XYWH but returns Boxes as XYXY
                        tracking_results = np.array(self.tracker.update(bbox_xywh, cls_conf, class_predictions, im))
                        num_results = len(tracking_results)
                        #print(f"Outputs:\n{tracking_results}")

                        if num_results > 0:
                            x1_list = tracking_results[:,0]
                            x2_list = tracking_results[:,2]
                            y1_list = tracking_results[:,1]
                            y2_list = tracking_results[:,3]
                            ids = tracking_results[:,4]
                            object_classes = tracking_results[:,5]
                            object_confs = None
                            class_confs = None

                        # visualization
                        '''
                        num_colors = 10
                        color_map = cm.get_cmap('gist_rainbow', num_colors)

                        if len(tracking_results) > 0:
                            for box in tracking_results:
                                x1v = int(box[0])
                                x2v = int(box[2])
                                y1v = int(box[1])
                                y2v = int(box[3])

                                color_idx = box[4] % self.num_colors
                                color = color_map(color_idx)[0:3]
                                color = tuple([int(color[i] * 255) for i in range(len(color))])

                                class_name = classes[int(box[5])]
                                label = f"{class_name} {box[4]}"
                                font_size = 0.5
                                font_thickness = 1
                                text_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, font_size , font_thickness)[0]

                                # draw bounding box
                                im = cv2.rectangle(im, (x1v, y1v), (x2v, y2v), color, 5)

                                # draw text and background
                                cv2.rectangle(im, (x1v, y1v), (x1v + text_size[0] + 3, y1v + text_size[1] + 4), color, -1)
                                cv2.putText(im, label, (x1v, y1v + text_size[1]), cv2.FONT_HERSHEY_SIMPLEX, font_size,
                                            [0, 0, 0], font_thickness)

                            cv2.imshow("im", im)
                            cv2.waitKey()
                        '''


                    else:
                        # if no tracker is used, store the detection results
                        x1_list = x
                        x2_list = x + w
                        y1_list = y
                        y2_list = y + h
                        ids = None
                        object_confs = frame_based_predictions[:,4].cpu().numpy()
                        class_confs = frame_based_predictions[:,5].cpu().numpy()
                        object_classes = frame_based_predictions[:, 6].cpu().numpy()
                        num_results = len(frame_based_predictions)


                    # store predictions for each object in the frame
                    for object_idx in range(0, num_results):

                        x1 = int(x1_list[object_idx])
                        x2 = int(x2_list[object_idx])
                        y1 = int(y1_list[object_idx])
                        y2 = int(y2_list[object_idx])

                        if ids is None:
                            instance_id = obj_id
                            obj_id = obj_id + 1
                        else:
                            instance_id = ids[object_idx]

                        if object_confs is None:
                            obj_conf = "N/A"
                        else:
                            obj_conf = object_confs[object_idx]

                        if class_confs is None:
                            class_conf = "N/A"
                        else:
                            class_conf = class_confs[object_idx]

                        class_idx = int(object_classes[object_idx])
                        class_name = classes[class_idx]

                        results_od_l.append([instance_id, shot_id, vid_name, start, stop, frame_id,
                                             x1, y1, x2, y2, obj_conf, class_conf, class_idx])

                        # (x1, y1, x2, y2, object_conf, class_score, class_pred)
                        obj_instance = CustObject(oid=instance_id,
                                                  fid=frame_id,
                                                  object_class_name=class_name,
                                                  object_conf=obj_conf,
                                                  class_score=class_conf,
                                                  bb_x1=x1,
                                                  bb_y1=y1,
                                                  bb_x2=x2,
                                                  bb_y2=y2
                                                  )
                        current_shot.addCustomObject(obj_instance)

                        if (self.config_instance.debug_flag == True):
                            tmp = str(obj_id) + ";" + str(shot_id) + ";" + str(vid_name) + ";" + str(start) + ";" + \
                                  str(stop) + ";" + str(frame_id) + ";" + str(x1) + ";" + str(y1) + ";" + \
                                  str(x2) + ";" + str(y2) + ";" + str(obj_conf) + ";" + str(class_conf) + ";" + \
                                  str(class_idx)
                            print(tmp)

        if (self.config_instance.debug_flag == True):
            vid_instance.printVIDInfo()

        final_csv_path = None

        if (self.config_instance.save_final_results == True):

            results_path = self.config_instance.path_final_results

            if not os.path.isdir(results_path):
                os.makedirs(results_path)
                printCustom(f"Created results folder \"{results_path}\"", STDOUT_TYPE.INFO)

            filepath = f"{results_path}{vid_name.split('.')[0]}.{self.config_instance.path_postfix_final_results}"
            final_csv_path = filepath
            vid_instance.export2csv(filepath=filepath)

        if (self.config_instance.save_raw_results == True and final_csv_path is not None):

            results_path = self.config_instance.path_raw_results

            if not os.path.isdir(results_path):
                os.makedirs(results_path)
                printCustom(f"Created results folder \"{results_path}\"", STDOUT_TYPE.INFO)

            visualize_video(vid_instance, final_csv_path, results_path)

            '''
            for shot in vid_instance.shot_list:
                vid_instance.visualizeShotsWithBB(path=results_path,
                                                  sid=int(shot.sid),
                                                  all_frames_tensors=all_tensors_l,
                                                  save_single_plots_flag=True,
                                                  plot_flag=False,
                                                  boundingbox_flag=True,
                                                  save_as_video_flag=True
                                                  ) '''

    def runModel(self, model, tensor_l, classes, class_filter):
        """
        Method to calculate stc predictions of specified model and given list of tensor images (pytorch).

        :param model: [required] pytorch model instance
        :param tensor_l: [required] list of tensors representing a list of frames.
        :return: predicted class_name for each tensor frame,
                 the number of hits within a shot,
                 frame-based predictions for a whole shot
        """

        # run od detector

        # prepare pytorch dataloader
        Tensor = torch.cuda.FloatTensor if torch.cuda.is_available() else torch.FloatTensor
        dataset = data.TensorDataset(tensor_l)  # create your datset
        inference_dataloader = data.DataLoader(dataset=dataset,
                                               batch_size=self.config_instance.batch_size)

        predictions_l = []
        for i, inputs in enumerate(inference_dataloader):
            input_batch = inputs[0]
            input_batch = Variable(input_batch.type(Tensor))

            # move the input and model to GPU for speed if available
            if torch.cuda.is_available():
                input_batch = input_batch.to('cuda')
                model.to('cuda')

            model.eval()
            with torch.no_grad():
                nms_thres = 0.4
                output = model(input_batch)
                batch_detections = non_max_suppression(prediction=output,
                                                 conf_thres=self.config_instance.confidence_threshold,
                                                 nms_thres=nms_thres)

                #predictions_l.extend(batch_detections)
                #continue

                for frame_detection in batch_detections:

                    filtered_detection = None

                    if frame_detection is not None:

                        for i in range(len(frame_detection)):

                            detected_object = frame_detection[i]
                            class_idx = detected_object[6].int().item()
                            #print(f"{classes[class_idx]} in {class_filter}?")

                            if classes[class_idx] in class_filter:
                                #print(f"Detected {classes[class_idx]}")

                                if filtered_detection is None:
                                    filtered_detection = detected_object.unsqueeze(dim=0)
                                else:
                                    filtered_detection = torch.cat([filtered_detection, detected_object.unsqueeze(dim=0)], dim=0)

                        #print(frame_detection)
                        #print(filtered_detection)

                    predictions_l.append(filtered_detection)

        return predictions_l

    def loadSbdResults(self, sbd_results_path):
        """
        Method for loading shot boundary detection results as numpy array

        .. note::
            Only used in debug_mode.

        :param sbd_results_path: [required] path to results file of shot boundary detection module (vhh_sbd)
        :return: numpy array holding list of detected shots.
        """

        # open sbd results
        fp = open(sbd_results_path, 'r')
        lines = fp.readlines()
        lines = lines[1:]

        lines_n = []
        for i in range(0, len(lines)):
            line = lines[i].replace('\n', '')
            line_split = line.split(';')
            lines_n.append([line_split[0], os.path.join(line_split[1]), line_split[2], line_split[3]])
        lines_np = np.array(lines_n)
        #print(lines_np.shape)

        return lines_np
