from typing import Any, List, Optional, Sequence, Tuple

import huggingface_hub
import transformers

from olympict.files.o_batch import OlympBatch
from olympict.files.o_image import OlympImage
from olympict.types import BBoxHF


class HuggingFaceModel:
    def __init__(
        self,
        hf_id: str,
        revision: Optional[str] = None,
        huggingface_token: Optional[str] = None,
    ) -> None:
        self._hf_id = hf_id
        infos = huggingface_hub.model_info(
            self._hf_id, revision=revision, token=huggingface_token
        )

        self.model_constructor = getattr(
            transformers, infos.transformersInfo["auto_model"]
        )
        self.processor_constructor = getattr(
            transformers, infos.transformersInfo["processor"]
        )

        self.model = self.model_constructor.from_pretrained(self._hf_id)
        self.processor = self.processor_constructor.from_pretrained(self._hf_id)

    def infer(self, o: OlympImage) -> OlympImage:
        # Pillow format
        inputs = self.processor(images=[o.img[:, :, ::-1]], return_tensors="pt")

        outputs = self.model(**inputs)
        logits = outputs.logits

        # model predicts one of the 1000 ImageNet classes
        label_id = logits.argmax(-1).item()

        o.metadata["label"] = self.model.config.id2label[label_id]
        o.metadata["label_id"] = label_id

        return o

    def _convert_result_to_bbox(self, results: Any) -> Sequence[BBoxHF]:
        bboxes: List[BBoxHF] = []
        for score, label, box in zip(
            results["scores"], results["labels"], results["boxes"]
        ):
            box: Tuple[
                float,
                float,
                float,
                float,
            ] = (round(i, 3) for i in box.tolist())
            i_label: int = label.item()
            t_label: str = self.model.config.id2label[i_label]
            f_score: float = round(score.item(), 3)

            bbox: BBoxHF = (*box, t_label, i_label, f_score, self._hf_id)

            bboxes.append(bbox)
        return bboxes

    def detect(self, o: OlympImage) -> OlympImage:
        # Pillow format
        inputs = self.processor(images=[o.img[:, :, ::-1]], return_tensors="pt")

        outputs = self.model(**inputs)
        results = self.processor.post_process_object_detection(outputs, threshold=0.5)[
            0
        ]

        if "pred_bboxes" not in o.metadata:
            o.metadata["pred_bboxes"] = []

        bboxes = self._convert_result_to_bbox(results)

        _ = o.metadata["pred_bboxes"].extend(bboxes)

        return o

    def detect_batch(self, o: OlympBatch) -> OlympBatch:
        # Pillow format
        inputs = self.processor(images=[o.data[:, :, :, ::-1]], return_tensors="pt")

        outputs = self.model(**inputs)
        results = self.processor.post_process_object_detection(outputs, threshold=0.5)

        bbox_batch = [self._convert_result_to_bbox(r) for r in results]

        for i, batch in enumerate(bbox_batch):
            if "pred_bboxes" not in o.metadata[i]:
                o.metadata[i]["pred_bboxes"] = []
            o.metadata[i]["pred_bboxes"].extend(batch)

        return o
