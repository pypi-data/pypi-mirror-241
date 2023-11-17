import os
import sys
from glob import glob
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

import cv2
import numpy as np
from natsort import natsorted

from olympict.files.o_batch import OlympBatch
from olympict.files.o_image import OlympImage
from olympict.files.o_video import OlympVid
from olympict.image_tools import ImTools
from olympict.pipeline import OPipeline
from olympict.types import (
    BBoxAbsolute,
    BBoxHF,
    Color,
    Img,
    ImgFormat,
    LineAbsolute,
    LineRelative,
    PolygonAbsolute,
    PolygonRelative,
    Size,
)
from olympict.utils.bbox_abs_painter import BBoxAbsolutePainter
from olympict.utils.bbox_hf_painter import BBoxHFPainter
from olympict.utils.crop_op import CropOperation
from olympict.utils.debug_window import DebugWindow
from olympict.utils.discarder_op import DiscarderOperation
from olympict.utils.extension_op import ExtensionOperation
from olympict.utils.folder_op import FolderOperation
from olympict.utils.heatmap_op import HeatmapOperation
from olympict.utils.image_op import ImageOperation
from olympict.utils.line_abs_op import LineAbsoluteOperation
from olympict.utils.line_rel_op import LineRelativeOperation
from olympict.utils.path_op import PathOperation, filter_none_packets
from olympict.utils.polygon_abs_op import PolygonAbsoluteOperation
from olympict.utils.polygon_rel_op import PolygonRelativeOperation
from olympict.utils.random_crop_op import RandomCropOperation
from olympict.utils.saver import FolderSaver
from olympict.utils.segmentation_op import SegmentationOperation
from olympict.utils.video_sequencer_op import VideoSequencer
from olympict.video_saver import PipelineVideoSaver


class ImagePipeline(OPipeline[OlympImage]):
    @staticmethod
    def load_paths(
        paths: List[str],
        metadata_function: Optional[Callable[[str], Any]] = None,
    ) -> "ImagePipeline":
        data = [OlympImage(p) for p in paths]

        if metadata_function is not None:
            for d in data:
                d.metadata = metadata_function(d.path)

        return ImagePipeline(data)

    @staticmethod
    def load_folder(
        path: str,
        extensions: Sequence[str] = ["png", "jpg", "jpeg", "bmp"],
        recursive: bool = False,
        order_func: Optional[Union[bool, Callable[[str], int]]] = True,
        reverse: bool = False,
        metadata_function: Optional[Callable[[str], Any]] = None,
    ) -> "ImagePipeline":
        paths: List[str] = glob(os.path.join(path, "**"), recursive=recursive)

        paths = [p for p in paths if os.path.splitext(p)[1].strip(".") in extensions]

        if order_func is False:
            pass
        elif order_func is True:
            paths = natsorted(paths, reverse=reverse)
        elif order_func is not None:
            paths.sort(key=order_func, reverse=reverse)

        data = [OlympImage(p) for p in paths]

        if metadata_function is not None:
            for d in data:
                d.metadata = metadata_function(d.path)

        return ImagePipeline(data)

    @staticmethod
    def load_folders(
        paths: List[str],
        extensions: Sequence[str] = ["png", "jpg", "jpeg", "bmp"],
        recursive: bool = False,
        order_func: Optional[Union[bool, Callable[[str], int]]] = True,
        reverse: bool = False,
        metadata_function: Optional[Callable[[str], Any]] = None,
    ) -> "ImagePipeline":
        all_data: List[OlympImage] = []
        for path in paths:
            sub_paths: List[str] = glob(os.path.join(path, "**"), recursive=recursive)

            sub_paths = [
                p for p in sub_paths if os.path.splitext(p)[1].strip(".") in extensions
            ]

            if order_func is False:
                pass
            elif order_func is True:
                sub_paths = natsorted(sub_paths, reverse=reverse)
            elif order_func is not None:
                sub_paths.sort(key=order_func, reverse=reverse)

            data = [OlympImage(p) for p in sub_paths]

            if metadata_function is not None:
                for d in data:
                    d.metadata = metadata_function(d.path)

            all_data.extend(data)

        return ImagePipeline(all_data)

    def task(
        self, func: Callable[[OlympImage], OlympImage], count: int = 1
    ) -> "ImagePipeline":
        return ImagePipeline(extending=self.pipeline.task(func, count))

    def task_img(self, func: Callable[[Img], Img], count: int = 1) -> "ImagePipeline":
        return self.class_task(
            ImageOperation, ImageOperation.task, class_args=[func], count=count
        )

    def task_path(self, func: Callable[[str], str], count: int = 1) -> "ImagePipeline":
        return self.class_task(
            PathOperation, PathOperation.task, class_args=[func], count=count
        )

    def explode(self, explode_function: Callable[[OlympImage], List[OlympImage]]):
        return ImagePipeline(extending=self.pipeline.explode(explode_function))

    def rescale(
        self,
        size: Tuple[float, float],
        pad_color: Optional[Tuple[int, int, int]] = None,
        count: int = 1,
    ) -> "ImagePipeline":
        return self.task(OlympImage.rescale(size, pad_color), count)

    def resize(
        self,
        size: Tuple[int, int],
        pad_color: Optional[Tuple[int, int, int]] = None,
        interpolation: int = cv2.INTER_LINEAR,
        count: int = 1,
    ) -> "ImagePipeline":
        return self.task(OlympImage.resize(size, pad_color, interpolation), count)

    def crop(
        self,
        left: int = 0,
        top: int = 0,
        right: int = 0,
        bottom: int = 0,
        pad_color: Color = (0, 0, 0),
        count: int = 1,
    ) -> "ImagePipeline":
        return self.class_task(
            CropOperation,
            CropOperation.task,
            class_kwargs={
                "left": left,
                "top": top,
                "right": right,
                "bottom": bottom,
                "pad_color": pad_color,
            },
            count=count,
        )

    def random_crop(self, output_size: Size, count: int = 1) -> "ImagePipeline":
        return self.class_task(
            RandomCropOperation,
            RandomCropOperation.task,
            class_args=[output_size],
            count=count,
        )

    def filter(
        self, keep_if_true: Optional[Callable[[OlympImage], bool]] = None
    ) -> "ImagePipeline":
        return ImagePipeline(extending=self.pipeline.filter(keep_if_true))

    def keep_each_frame_in(
        self, keep_n: int = 1, discard_n: int = 0
    ) -> "ImagePipeline":
        d = DiscarderOperation(keep_n, discard_n)
        return ImagePipeline(extending=self.pipeline.filter(d.get_next))

    def debug_window(self, name: str) -> "ImagePipeline":
        return self.class_task(DebugWindow, DebugWindow.show, None, class_args=[name])

    def to_video(
        self, img_to_video_path: Callable[[OlympImage], str], fps: int = 25
    ) -> "VideoPipeline":
        p = self.pipeline.class_task(
            PipelineVideoSaver,
            PipelineVideoSaver.process_file,
            [img_to_video_path, fps],
            PipelineVideoSaver.finish,
        ).filter(filter_none_packets)
        return VideoPipeline(extending=p)

    def to_format(self, format: ImgFormat) -> "ImagePipeline":
        return self.class_task(
            ExtensionOperation, ExtensionOperation.change_format, class_args=[format]
        )

    def save_to_folder(self, folder_path: str) -> "ImagePipeline":
        return self.class_task(
            FolderSaver, FolderSaver.save_to_folder, class_args=[folder_path]
        )

    def save(self) -> "ImagePipeline":
        return self.class_task(FolderSaver, FolderSaver.save)

    def draw_relative_polygons(
        self,
        polygon_function: Callable[[OlympImage], List[Tuple[PolygonRelative, Color]]],
    ) -> "ImagePipeline":
        return self.class_task(
            PolygonRelativeOperation,
            PolygonRelativeOperation.draw_relative_polygons,
            class_args=[polygon_function],
        )

    def draw_polygons(
        self,
        polygon_function: Callable[[OlympImage], List[Tuple[PolygonAbsolute, Color]]],
    ) -> "ImagePipeline":
        return self.class_task(
            PolygonAbsoluteOperation,
            PolygonAbsoluteOperation.draw_absolute_polygons,
            class_args=[polygon_function],
        )

    def draw_relative_bboxes(
        self,
        bbox_function: Optional[Callable[[OlympImage], Sequence[BBoxHF]]] = None,
        font_scale: float = ImTools.font_scale,
    ) -> "ImagePipeline":
        return self.task(BBoxHFPainter.bbox_pipe_drawer(bbox_function, font_scale))

    def draw_bboxes(
        self,
        bbox_function: Callable[[OlympImage], List[BBoxAbsolute]],
        font_scale: float = ImTools.font_scale,
    ) -> "ImagePipeline":
        return self.class_task(
            BBoxAbsolutePainter,
            BBoxAbsolutePainter.draw_absolute,
            class_args=[bbox_function, font_scale],
        )

    def draw_relative_lines(
        self,
        polyline_function: Callable[[OlympImage], List[Tuple[LineRelative, Color]]],
    ) -> "ImagePipeline":
        return self.class_task(
            LineRelativeOperation,
            LineRelativeOperation.draw_relative_lines,
            class_args=[polyline_function],
        )

    def draw_lines(
        self,
        polyline_function: Callable[[OlympImage], List[Tuple[LineAbsolute, Color]]],
    ) -> "ImagePipeline":
        return self.class_task(
            LineAbsoluteOperation,
            LineAbsoluteOperation.draw_absolute_lines,
            class_args=[polyline_function],
        )

    def draw_heatmap(
        self, heatmap_function: Callable[[OlympImage], Img]
    ) -> "ImagePipeline":
        return self.class_task(
            HeatmapOperation,
            HeatmapOperation.draw_heatmap,
            class_args=[heatmap_function],
        )

    def draw_segmentation_maps(
        self, segmentation_map: Callable[[OlympImage], Img], color: Color
    ) -> "ImagePipeline":
        return self.class_task(
            SegmentationOperation,
            SegmentationOperation.draw_segmentation,
            class_args=[segmentation_map, color],
        )

    def class_task_img(
        self,
        class_constructor: Any,
        store_results_in_metadata_key: str,
        class_method: Callable[[Any, Img], Any],
        close_method: Optional[Callable[[Any], Any]] = None,
        class_args: List[Any] = [],
        class_kwargs: Dict[str, Any] = {},
    ):
        """_summary_

        Args:
            class_constructor (Any): _description_
            class_method (Callable[[Img], Any]): _description_
            store_results_in_metadata_key (str): _description_
            class_args (List[Any], optional): _description_. Defaults to [].
            close_method (Optional[Callable[[OlympImage], Any]], optional): _description_. Defaults to None.
            class_kwargs (Dict[str, Any], optional): _description_. Defaults to {}.

        Returns:
            _type_: _description_
        """

        class HigherOrderClass(class_constructor):  # type: ignore
            def process_override_function(self, o: OlympImage):
                method = self.__getattribute__(class_method.__name__)
                o.metadata[store_results_in_metadata_key] = method(np.copy(o.img))
                return o

        return self.class_task(
            HigherOrderClass,
            HigherOrderClass.process_override_function,
            close_method,
            class_args,
            class_kwargs,
        )

    def class_task(
        self,
        class_constructor: Any,
        class_method: Callable[[Any, OlympImage], OlympImage],
        close_method: Optional[Callable[[Any], Any]] = None,
        class_args: List[Any] = [],
        class_kwargs: Dict[str, Any] = {},
        count: int = 1,
    ) -> "ImagePipeline":
        """This operation enables the use of a stateful processing using a class

        Args:
            class_constructor (Any): the class constructor, ex: MyClass
            class_method (Callable[[Any, OlympImage], OlympImage]): The processing method applied to each packet, ex: MyClass.process_img
            close_method (Optional[Callable[[Any], Any]], optional): If provided, the method used when the pipeline has processed all packets . Defaults to None.
            class_args (List[Any], optional): The constructor args. Defaults to [].
            class_kwargs (Dict[str, Any], optional): The constructor Kwargs. Defaults to {}.

        Raises:
            Exception: Error if the pipeline is not well defined

        Returns:
            ImagePipeline: the output ImagePipeline
        """

        return ImagePipeline(
            extending=self.pipeline.class_task(
                class_constructor,
                class_method,
                class_args,
                close_method,
                class_kwargs,
                count=count,
            )
        )

    def limit(self, count: int):
        return ImagePipeline(extending=self.pipeline.limit(count))

    def batch(self, batch_size: int) -> "BatchPipeline":
        return BatchPipeline(
            extending=self.pipeline.batch(batch_size).task(OlympBatch.from_images)
        )

    def classify(
        self,
        huggingface_id: str,
        revision: Optional[str] = None,
        huggingface_token: Optional[str] = None,
    ) -> "ImagePipeline":
        from olympict.utils.huggingface_op import HuggingFaceModel

        try:
            return self.class_task(
                HuggingFaceModel,
                HuggingFaceModel.infer,
                class_args=[huggingface_id, revision, huggingface_token],
            )
        except Exception as e:
            print("Could not initialize model", huggingface_id, "\n", e)
            sys.exit(1)

    def detect(
        self,
        huggingface_id: str,
        revision: Optional[str] = None,
        huggingface_token: Optional[str] = None,
    ) -> "ImagePipeline":
        from olympict.utils.huggingface_op import HuggingFaceModel

        try:
            return self.class_task(
                HuggingFaceModel,
                HuggingFaceModel.detect,
                class_args=[huggingface_id, revision, huggingface_token],
            )
        except Exception as e:
            print("Could not initialize model", huggingface_id, "\n", e)
            sys.exit(1)


class BatchPipeline(OPipeline[OlympBatch]):
    def task(
        self, func: Callable[[OlympBatch], OlympBatch], count: int = 1
    ) -> "BatchPipeline":
        return BatchPipeline(extending=self.pipeline.task(func, count))

    def task_img_batch(
        self, func: Callable[[Img], Img], count: int = 1
    ) -> "BatchPipeline":
        def r(o: OlympBatch) -> OlympBatch:
            o.data = func(o.data)
            return o

        return self.task(r, count)

    def limit(self, count: int):
        return BatchPipeline(extending=self.pipeline.limit(count))

    def to_images(self) -> "ImagePipeline":
        return ImagePipeline(extending=self.pipeline.explode(OlympBatch.to_images))

    def class_task(
        self,
        class_constructor: Any,
        class_method: Callable[[Any, OlympBatch], OlympBatch],
        close_method: Optional[Callable[[Any], Any]] = None,
        class_args: List[Any] = [],
        class_kwargs: Dict[str, Any] = {},
    ) -> "BatchPipeline":
        """This operation enables the use of a stateful processing using a class

        Args:
            class_constructor (Any): the class constructor, ex: MyClass
            class_method (Callable[[Any, OlympBatch], OlympBatch]): The processing method applied to each packet, ex: MyClass.process_img
            close_method (Optional[Callable[[Any], Any]], optional): If provided, the method used when the pipeline has processed all packets . Defaults to None.
            class_args (List[Any], optional): The constructor args. Defaults to [].
            class_kwargs (Dict[str, Any], optional): The constructor Kwargs. Defaults to {}.

        Raises:
            Exception: Error if the pipeline is not well defined

        Returns:
            BatchPipeline: the output BatchPipeline
        """
        return BatchPipeline(
            extending=self.pipeline.class_task(
                class_constructor, class_method, class_args, close_method, class_kwargs
            )
        )

    def class_task_batch(
        self,
        class_constructor: Any,
        store_results_in_metadata_key: str,
        class_method: Callable[[Any, Img], Any],
        close_method: Optional[Callable[[Any], Any]] = None,
        class_args: List[Any] = [],
        class_kwargs: Dict[str, Any] = {},
    ) -> "BatchPipeline":
        """
        Args:
            class_constructor (Any): _description_
            class_method (Callable[[Img], Any]): _description_
            store_results_in_metadata_key (str): _description_
            class_args (List[Any], optional): _description_. Defaults to [].
            close_method (Optional[Callable[[OlympImage], Any]], optional): _description_. Defaults to None.
            class_kwargs (Dict[str, Any], optional): _description_. Defaults to {}.
        """

        class HigherOrderClass(class_constructor):  # type: ignore
            def process_override_function(self, o: OlympBatch):
                method = self.__getattribute__(class_method.__name__)
                res = method(np.copy(o.data))
                for i in range(res.shape[0]):
                    o.metadata[i][store_results_in_metadata_key] = res[i]
                return o

        return self.class_task(
            HigherOrderClass,
            HigherOrderClass.process_override_function,
            close_method,
            class_args,
            class_kwargs,
        )


class VideoPipeline(OPipeline[OlympVid]):
    @staticmethod
    def load_folder(
        path: str,
        extensions: Sequence[str] = ["mkv", "mp4"],
        recursive: bool = False,
        order_func: Optional[Union[bool, Callable[[str], int]]] = True,
        reverse: bool = False,
    ) -> "VideoPipeline":
        paths: List[str] = glob(os.path.join(path, "**"), recursive=recursive)
        paths = [p for p in paths if os.path.splitext(p)[1].strip(".") in extensions]

        if order_func is False:
            pass
        elif order_func is True:
            paths = natsorted(paths, reverse=reverse)
        elif order_func is not None:
            paths.sort(key=order_func, reverse=reverse)

        data = [OlympVid(p) for p in paths]

        return VideoPipeline(data)

    def task(
        self, func: Callable[[OlympVid], OlympVid], count: int = 1
    ) -> "VideoPipeline":
        return VideoPipeline(extending=self.pipeline.task(func, count))

    def class_task(
        self,
        class_constructor: Any,
        class_method: Callable[[Any, OlympVid], OlympVid],
        close_method: Optional[Callable[[Any], Any]] = None,
        class_args: List[Any] = [],
        class_kwargs: Dict[str, Any] = {},
    ) -> "VideoPipeline":
        """This operation enables the use of a stateful processing using a class

        Args:
            class_constructor (Any): the class constructor, ex: MyClass
            class_method (Callable[[Any, OlympVid], OlympVid]): The processing method applied to each packet, ex: MyClass.process_img
            close_method (Optional[Callable[[Any], Any]], optional): If provided, the method used when the pipeline has processed all packets . Defaults to None.
            class_args (List[Any], optional): The constructor args. Defaults to [].
            class_kwargs (Dict[str, Any], optional): The constructor Kwargs. Defaults to {}.

        Raises:
            Exception: Error if the pipeline is not well defined

        Returns:
            BatchPipeline: the output BatchPipeline
        """
        return VideoPipeline(
            extending=self.pipeline.class_task(
                class_constructor, class_method, class_args, close_method, class_kwargs
            )
        )

    def limit(self, count: int):
        return VideoPipeline(extending=self.pipeline.limit(count))

    def move_to_folder(self, folder_path: str) -> "VideoPipeline":
        return self.class_task(
            FolderOperation,
            FolderOperation.change_folder_path,
            class_args=[folder_path],
        )

    def to_sequence(self) -> "ImagePipeline":
        seq = VideoSequencer()
        return ImagePipeline(extending=self.pipeline.explode(seq.generator))
