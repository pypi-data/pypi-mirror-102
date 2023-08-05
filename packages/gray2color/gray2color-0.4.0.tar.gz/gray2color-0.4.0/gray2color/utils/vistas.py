import numpy as np

vistas_class_names = ["bird","ground-animal","curb","fence","guard-rail","other-barrier","wall",
                "bike-lane","crosswalk-plain","curb-cut","parking","pedestrian-area","rail-track","road",
                "service-lane","sidewalk","bridge","building","tunnel","person","bicyclist","motorcyclist",
                "other-rider","crosswalk-zebra","general","mountain","sand","sky","snow","terrain","vegetation",
                "water","banner","bench","bike-rack","billboard","catch-basin","cctv-camera","fire-hydrant",
                "junction-box","mailbox","manhole","phone-booth","pothole","street-light","pole","traffic-sign-frame",
                "utility-pole","traffic-light","back","front","trash-can","bicycle","boat","bus","car",
                "caravan","motorcycle","on-rails","other-vehicle","trailer","truck",
                "wheeled-slow","car-mount","ego-vehicle","unlabeled"]

# this will be usefull in case you wanna do Panoptic Segmentation

vistas_THING_LIST = [0,1,8,19,20,21,22,23,32,33,34,35,36,37,38,39,40,41,42,44,
                      45,46,47,48,49,50,51,52,53,54,55,56,57,59,60,61,62]

pallet_vistas = np.array([[[165, 42, 42],
                          [0, 192, 0],
                          [196, 196, 196],
                          [190, 153, 153],
                          [180, 165, 180],
                          [102, 102, 156],
                          [102, 102, 156],
                          [128, 64, 255],
                          [140, 140, 200],
                          [170, 170, 170],
                          [250, 170, 160],
                          [96, 96, 96],
                          [230, 150, 140],
                          [128, 64, 128],
                          [110, 110, 110],
                          [244, 35, 232],
                          [150, 100, 100],
                          [70, 70, 70],
                          [150, 120, 90],
                          [220, 20, 60],
                          [255, 0, 0],
                          [255, 0, 0],
                          [255, 0, 0],
                          [200, 128, 128],
                          [255, 255, 255],
                          [64, 170, 64],
                          [128, 64, 64],
                          [70, 130, 180],
                          [255, 255, 255],
                          [152, 251, 152],
                          [107, 142, 35],
                          [0, 170, 30],
                          [255, 255, 128],
                          [250, 0, 30],
                          [0, 0, 0],
                          [220, 220, 220],
                          [170, 170, 170],
                          [222, 40, 40],
                          [100, 170, 30],
                          [40, 40, 40],
                          [33, 33, 33],
                          [170, 170, 170],
                          [0, 0, 142],
                          [170, 170, 170],
                          [210, 170, 100],
                          [153, 153, 153],
                          [128, 128, 128],
                          [0, 0, 142],
                          [250, 170, 30],
                          [192, 192, 192],
                          [220, 220, 0],
                          [180, 165, 180],
                          [119, 11, 32],
                          [0, 0, 142],
                          [0, 60, 100],
                          [0, 0, 142],
                          [0, 0, 90],
                          [0, 0, 230],
                          [0, 80, 100],
                          [128, 64, 64],
                          [0, 0, 110],
                          [0, 0, 70],
                          [0, 0, 192],
                          [32, 32, 32],
                          [0, 0, 0],
                          [0, 0, 0]]], np.uint8) / 255