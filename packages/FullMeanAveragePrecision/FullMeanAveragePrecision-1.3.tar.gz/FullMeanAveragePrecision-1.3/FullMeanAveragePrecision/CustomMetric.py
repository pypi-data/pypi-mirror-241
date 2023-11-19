from torchmetrics.detection.mean_ap import MeanAveragePrecision
import torch
import contextlib
import numpy as np
import io
from typing import Dict, List, Tuple, Literal
from torch import Tensor
from pycocotools.cocoeval import COCOeval
from types import ModuleType


class COCOevalCustom(COCOeval):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def summarize(self):
        '''
        Compute and display summary metrics for evaluation results.
        Note this functin can *only* be applied on the default parameter setting
        '''

        def _summarize(ap=1, iouThr=None, areaRng='all', maxDets=100):
            p = self.params
            iStr = ' {:<18} {} @[ IoU={:<9} | area={:>6s} | maxDets={:>3d} ] = {:0.3f}'
            titleStr = 'Average Precision' if ap == 1 else 'Average Recall'
            typeStr = '(AP)' if ap == 1 else '(AR)'
            iouStr = '{:0.2f}:{:0.2f}'.format(p.iouThrs[0], p.iouThrs[-1]) \
                if iouThr is None else '{:0.2f}'.format(iouThr)

            aind = [i for i, aRng in enumerate(p.areaRngLbl) if aRng == areaRng]
            mind = [i for i, mDet in enumerate(p.maxDets) if mDet == maxDets]
            if ap == 1:
                # dimension of precision: [TxRxKxAxM]
                s = self.eval['precision']
                # IoU
                if iouThr is not None:
                    t = np.where(iouThr == p.iouThrs)[0]
                    s = s[t]
                s = s[:, :, :, aind, mind]
            else:
                # dimension of recall: [TxKxAxM]
                s = self.eval['recall']
                if iouThr is not None:
                    t = np.where(iouThr == p.iouThrs)[0]
                    s = s[t]
                s = s[:, :, aind, mind]
            if len(s[s > -1]) == 0:
                mean_s = -1
            else:
                mean_s = np.mean(s[s > -1])
            print(iStr.format(titleStr, typeStr, iouStr, areaRng, maxDets, mean_s))
            return mean_s

        def _summarizeDets():
            # stats = np.zeros((12,))
            stats = np.zeros((21,))
            stats[0] = _summarize(1)
            stats[1] = _summarize(1, iouThr=.5, maxDets=self.params.maxDets[2])
            stats[2] = _summarize(1, iouThr=.75, maxDets=self.params.maxDets[2])
            stats[3] = _summarize(1, areaRng='small', maxDets=self.params.maxDets[2])
            stats[4] = _summarize(1, areaRng='medium', maxDets=self.params.maxDets[2])
            stats[5] = _summarize(1, areaRng='large', maxDets=self.params.maxDets[2])
            stats[6] = _summarize(0, maxDets=self.params.maxDets[0])
            stats[7] = _summarize(0, maxDets=self.params.maxDets[1])
            stats[8] = _summarize(0, maxDets=self.params.maxDets[2])
            stats[9] = _summarize(0, areaRng='small', maxDets=self.params.maxDets[2])
            stats[10] = _summarize(0, areaRng='medium', maxDets=self.params.maxDets[2])
            stats[11] = _summarize(0, areaRng='large', maxDets=self.params.maxDets[2])

            stats[12] = _summarize(1, iouThr=.55, maxDets=self.params.maxDets[2])
            stats[13] = _summarize(1, iouThr=.6, maxDets=self.params.maxDets[2])
            stats[14] = _summarize(1, iouThr=.65, maxDets=self.params.maxDets[2])
            stats[15] = _summarize(1, iouThr=.7, maxDets=self.params.maxDets[2])
            stats[16] = _summarize(1, iouThr=.8, maxDets=self.params.maxDets[2])
            stats[17] = _summarize(1, iouThr=.85, maxDets=self.params.maxDets[2])
            stats[18] = _summarize(1, iouThr=.9, maxDets=self.params.maxDets[2])
            stats[19] = _summarize(1, iouThr=.95, maxDets=self.params.maxDets[2])
            stats[20] = (stats[1] + stats[2] + stats[12] + stats[13] + stats[14] + stats[15] + stats[16] +
                         stats[17] + stats[18] + stats[19]) / 10
            return stats

        def _summarizeKps():
            stats = np.zeros((10,))
            stats[0] = _summarize(1, maxDets=20)
            stats[1] = _summarize(1, maxDets=20, iouThr=.5)
            stats[2] = _summarize(1, maxDets=20, iouThr=.75)
            stats[3] = _summarize(1, maxDets=20, areaRng='medium')
            stats[4] = _summarize(1, maxDets=20, areaRng='large')
            stats[5] = _summarize(0, maxDets=20)
            stats[6] = _summarize(0, maxDets=20, iouThr=.5)
            stats[7] = _summarize(0, maxDets=20, iouThr=.75)
            stats[8] = _summarize(0, maxDets=20, areaRng='medium')
            stats[9] = _summarize(0, maxDets=20, areaRng='large')
            return stats

        if not self.eval:
            raise Exception('Please run accumulate() first')
        iouType = self.params.iouType
        if iouType == 'segm' or iouType == 'bbox':
            summarize = _summarizeDets
        elif iouType == 'keypoints':
            summarize = _summarizeKps
        self.stats = summarize()

    def __str__(self):
        self.summarize()


def _load_backend_tools(backend: Literal["pycocotools", "faster_coco_eval"]) -> Tuple[object, object, ModuleType]:
    """Load the backend tools for the given backend."""
    if backend == "pycocotools":
        import pycocotools.mask as mask_utils
        from pycocotools.coco import COCO
        # from pycocotools.cocoeval import COCOeval

        return COCO, COCOevalCustom, mask_utils


class FullMeanAveragePrecision(MeanAveragePrecision):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def compute(self) -> dict:
        """Computes the metric."""
        coco_preds, coco_target = self._get_coco_datasets(average=self.average)

        result_dict = {}
        with contextlib.redirect_stdout(io.StringIO()):
            for i_type in self.iou_type:
                prefix = "" if len(self.iou_type) == 1 else f"{i_type}_"
                if len(self.iou_type) > 1:
                    # the area calculation is different for bbox and segm and therefore to get the small, medium and
                    # large values correct we need to dynamically change the area attribute of the annotations
                    for anno in coco_preds.dataset["annotations"]:
                        anno["area"] = anno[f"area_{i_type}"]

                coco_eval = self.cocoeval(coco_target, coco_preds, iouType=i_type)
                coco_eval.params.iouThrs = np.array(self.iou_thresholds, dtype=np.float64)
                coco_eval.params.recThrs = np.array(self.rec_thresholds, dtype=np.float64)
                coco_eval.params.maxDets = self.max_detection_thresholds

                coco_eval.evaluate()
                coco_eval.accumulate()
                coco_eval.summarize()
                stats = coco_eval.stats
                result_dict.update(self._coco_stats_to_tensor_dict(stats, prefix=prefix))

                summary = {}
                if self.extended_summary:
                    summary = {
                        f"{prefix}ious": self.apply_to_collection(
                            coco_eval.ious, np.ndarray, lambda x: torch.tensor(x, dtype=torch.float32)
                        ),
                        f"{prefix}precision": torch.tensor(coco_eval.eval["precision"]),
                        f"{prefix}recall": torch.tensor(coco_eval.eval["recall"]),
                    }
                result_dict.update(summary)

                # if class mode is enabled, evaluate metrics per class
                if self.class_metrics:
                    if self.average == "micro":
                        # since micro averaging have all the data in one class, we need to reinitialize the coco_eval
                        # object in macro mode to get the per class stats
                        coco_preds, coco_target = self._get_coco_datasets(average="macro")
                        coco_eval = self.cocoeval(coco_target, coco_preds, iouType=i_type)
                        coco_eval.params.iouThrs = np.array(self.iou_thresholds, dtype=np.float64)
                        coco_eval.params.recThrs = np.array(self.rec_thresholds, dtype=np.float64)
                        coco_eval.params.maxDets = self.max_detection_thresholds

                    map_per_class_list = []
                    mar_100_per_class_list = []
                    for class_id in self._get_classes():
                        coco_eval.params.catIds = [class_id]
                        with contextlib.redirect_stdout(io.StringIO()):
                            coco_eval.evaluate()
                            coco_eval.accumulate()
                            coco_eval.summarize()
                            class_stats = coco_eval.stats

                        map_per_class_list.append(torch.tensor([class_stats[0]]))
                        mar_100_per_class_list.append(torch.tensor([class_stats[8]]))

                    map_per_class_values = torch.tensor(map_per_class_list, dtype=torch.float32)
                    mar_100_per_class_values = torch.tensor(mar_100_per_class_list, dtype=torch.float32)
                else:
                    map_per_class_values = torch.tensor([-1], dtype=torch.float32)
                    mar_100_per_class_values = torch.tensor([-1], dtype=torch.float32)
                prefix = "" if len(self.iou_type) == 1 else f"{i_type}_"
                result_dict.update(
                    {
                        f"{prefix}map_per_class": map_per_class_values,
                        f"{prefix}mar_100_per_class": mar_100_per_class_values,
                    },
                )
        result_dict.update({"classes": torch.tensor(self._get_classes(), dtype=torch.int32)})

        return result_dict

    @property
    def coco(self) -> object:
        """Returns the coco module for the given backend, done in this way to make metric picklable."""
        coco, _, _ = _load_backend_tools(self.backend)
        return coco

    @property
    def cocoeval(self) -> object:
        """Returns the coco eval module for the given backend, done in this way to make metric picklable."""
        _, cocoeval, _ = _load_backend_tools(self.backend)
        return cocoeval

    @property
    def mask_utils(self) -> object:
        """Returns the mask utils object for the given backend, done in this way to make metric picklable."""
        _, _, mask_utils = _load_backend_tools(self.backend)
        return mask_utils

    @staticmethod
    def _coco_stats_to_tensor_dict(stats: List[float], prefix: str) -> Dict[str, Tensor]:
        """Converts the output of COCOeval.stats to a dict of tensors."""
        return {
            f"{prefix}map": torch.tensor([stats[0]], dtype=torch.float32),
            f"{prefix}map_50": torch.tensor([stats[1]], dtype=torch.float32),
            f"{prefix}map_75": torch.tensor([stats[2]], dtype=torch.float32),
            f"{prefix}map_small": torch.tensor([stats[3]], dtype=torch.float32),
            f"{prefix}map_medium": torch.tensor([stats[4]], dtype=torch.float32),
            f"{prefix}map_large": torch.tensor([stats[5]], dtype=torch.float32),
            f"{prefix}mar_1": torch.tensor([stats[6]], dtype=torch.float32),
            f"{prefix}mar_10": torch.tensor([stats[7]], dtype=torch.float32),
            f"{prefix}mar_100": torch.tensor([stats[8]], dtype=torch.float32),
            f"{prefix}mar_small": torch.tensor([stats[9]], dtype=torch.float32),
            f"{prefix}mar_medium": torch.tensor([stats[10]], dtype=torch.float32),
            f"{prefix}mar_large": torch.tensor([stats[11]], dtype=torch.float32),

            f"{prefix}map_55": torch.tensor([stats[12]], dtype=torch.float32),
            f"{prefix}map_60": torch.tensor([stats[13]], dtype=torch.float32),
            f"{prefix}map_65": torch.tensor([stats[14]], dtype=torch.float32),
            f"{prefix}map_70": torch.tensor([stats[15]], dtype=torch.float32),
            f"{prefix}map_80": torch.tensor([stats[16]], dtype=torch.float32),
            f"{prefix}map_85": torch.tensor([stats[17]], dtype=torch.float32),
            f"{prefix}map_90": torch.tensor([stats[18]], dtype=torch.float32),
            f"{prefix}map_95": torch.tensor([stats[19]], dtype=torch.float32),
            f"{prefix}map_50:95": torch.tensor([stats[20]], dtype=torch.float32),
        }


