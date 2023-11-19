### Description

**FullMeanAveragePrecision is an extended count of metric MeanAveragePrecision from torchmetrics library (https://pypi.org/project/torchmetrics/)**

This library allows you to count not only mAP@50, mAP@95, but also mAP@55, 
mAP@60, mAP@65, mAP@70, mAP@75, mAP@80, mAP@85, mAP@90, mAP@95 and mAP@50:95.

All **MeanAveragePrecision** arguments from the torchmetrics library correspond 
to **FullMeanAveragePrecision** arguments

### Installation
```bash
pip install FullMeanAveragePrecision
```

Example code:

```python
from torch import tensor
from pprint import pprint
from FullMeanAveragePrecision import FullMeanAveragePrecision
from torchmetrics.detection.mean_ap import MeanAveragePrecision

preds = [
    dict(
        boxes=tensor([[258.0, 41.0, 606.0, 285.0]]),
        scores=tensor([0.536]),
        labels=tensor([0]),
    )
]
target = [
    dict(
        boxes=tensor([[214.0, 41.0, 562.0, 285.0]]),
        labels=tensor([0]),
    )
]

torchmetric_mAP = MeanAveragePrecision(iou_type="bbox", box_format="xyxy",
                                       max_detection_thresholds=[1, 10, 100],
                                       iou_thresholds=[0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95],
                                       extended_summary=False,
                                       class_metrics=False)

custom_mAP = FullMeanAveragePrecision(iou_type="bbox", box_format="xyxy",
                                      max_detection_thresholds=[1, 10, 100],
                                      iou_thresholds=[0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95],
                                      extended_summary=False,
                                      class_metrics=False)

torchmetric_mAP.update(preds, target)
custom_mAP.update(preds, target)

res_1 = torchmetric_mAP.compute()
res_2 = custom_mAP.compute()

pprint(res_1)
pprint(res_2)

```

Result code
```
Torchmetric mAP
{'classes': tensor(0, dtype=torch.int32),
 'map': tensor(0.6000),
 'map_50': tensor(1.),
 'map_75': tensor(1.),
 'map_large': tensor(0.6000),
 'map_medium': tensor(-1.),
 'map_per_class': tensor(-1.),
 'map_small': tensor(-1.),
 'mar_1': tensor(0.6000),
 'mar_10': tensor(0.6000),
 'mar_100': tensor(0.6000),
 'mar_100_per_class': tensor(-1.),
 'mar_large': tensor(0.6000),
 'mar_medium': tensor(-1.),
 'mar_small': tensor(-1.)}

Custom mAP
{'classes': tensor(0, dtype=torch.int32),
 'map': tensor(0.6000),
 'map_50': tensor(1.),
 'map_50:95': tensor(0.6000),
 'map_55': tensor(1.),
 'map_60': tensor(1.),
 'map_65': tensor(1.),
 'map_70': tensor(1.),
 'map_75': tensor(1.),
 'map_80': tensor(0.),
 'map_85': tensor(0.),
 'map_90': tensor(0.),
 'map_95': tensor(0.),
 'map_large': tensor(0.6000),
 'map_medium': tensor(-1.),
 'map_per_class': tensor(-1.),
 'map_small': tensor(-1.),
 'mar_1': tensor(0.6000),
 'mar_10': tensor(0.6000),
 'mar_100': tensor(0.6000),
 'mar_100_per_class': tensor(-1.),
 'mar_large': tensor(0.6000),
 'mar_medium': tensor(-1.),
 'mar_small': tensor(-1.)}
```

Real world example

```python
import torch
import cv2
import pandas as pd
from pprint import pprint
from FullMeanAveragePrecision import FullMeanAveragePrecision


def custom_example(path_to_image: str,
                   path_to_predicted: str,
                   path_to_ground_truth: str,
                   device: str):
    image = cv2.imread(path_to_image)
    image_h, image_w = image.shape[:2]
    df_pred = pd.read_csv(path_to_predicted)

    metric = FullMeanAveragePrecision(iou_type="bbox", box_format="cxcywh",
                                      max_detection_thresholds=[1, 10, 1000],
                                      iou_thresholds=[0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95],
                                      extended_summary=False,
                                      class_metrics=False
                                      )
    metric.to(device)

    bboxes = df_pred[["xc", "yc", "width", "height"]].values
    scores = df_pred["probs"].values
    pred_dict = {"boxes": torch.Tensor(bboxes).to(device),
                 "scores": torch.Tensor(scores).to(device),
                 "labels": torch.Tensor([0] * len(df_pred)).to(int).to(device)}

    gt_boxes = []
    gt_labels = []
    with open(path_to_ground_truth, "r") as txt_file:
        lines = txt_file.readlines()
        for line in lines:
            cl, x_center, y_center, b_width, b_height = line.strip().split(" ")
            x_center = eval(x_center) * image_w
            y_center = eval(y_center) * image_h
            b_width = eval(b_width) * image_w
            b_height = eval(b_height) * image_h
            gt_boxes.append([x_center, y_center, b_width, b_height])
            gt_labels.append(eval(cl))

    gt_dict = {"boxes": torch.Tensor(gt_boxes).to(device),
               "labels": torch.Tensor(gt_labels).to(int).to(device)}

    metric.update([pred_dict], [gt_dict])
    mAP = metric.compute()

    return mAP


metric = custom_example(path_to_image="./168_img.jpg",
                        path_to_predicted="./168_img.csv",
                        path_to_ground_truth="./168_img.txt",
                        device="cpu")

pprint(metric)

```

```
{'classes': tensor(0, dtype=torch.int32),
 'map': tensor(-1.),
 'map_50': tensor(0.9732),
 'map_50:95': tensor(0.8469),
 'map_55': tensor(0.9596),
 'map_60': tensor(0.9596),
 'map_65': tensor(0.9448),
 'map_70': tensor(0.9287),
 'map_75': tensor(0.9151),
 'map_80': tensor(0.8801),
 'map_85': tensor(0.8093),
 'map_90': tensor(0.6699),
 'map_95': tensor(0.4285),
 'map_large': tensor(0.8640),
 'map_medium': tensor(0.4641),
 'map_per_class': tensor(-1.),
 'map_small': tensor(-1.),
 'mar_1': tensor(0.0028),
 'mar_10': tensor(0.0280),
 'mar_100': tensor(0.8838),
 'mar_100_per_class': tensor(-1.),
 'mar_large': tensor(0.9006),
 'mar_medium': tensor(0.4714),
 'mar_small': tensor(-1.)}

```



