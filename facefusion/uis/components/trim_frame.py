from typing import Optional, Tuple, Any

import gradio
from gradio_rangeslider import RangeSlider

from facefusion import state_manager, wording
from facefusion.face_store import clear_static_faces
from facefusion.filesystem import is_video
from facefusion.uis.core import get_ui_components
from facefusion.uis.typing import ComponentOptions
from facefusion.vision import count_video_frame_total

TRIM_FRAME_RANGE_SLIDER: Optional[RangeSlider] = None
TRIM_START_BUTTON: Optional[gradio.Button] = None
TRIM_END_BUTTON: Optional[gradio.Button] = None


def render() -> None:
	global TRIM_FRAME_RANGE_SLIDER
	global TRIM_START_BUTTON
	global TRIM_END_BUTTON

	trim_frame_range_slider_options: ComponentOptions = \
		{
			'label': wording.get('uis.trim_frame_slider'),
			'minimum': 0,
			'step': 1,
			'visible': False
		}
	if is_video(state_manager.get_item('target_path')):
		video_frame_total = count_video_frame_total(state_manager.get_item('target_path'))
		trim_frame_start = state_manager.get_item('trim_frame_start') or 0
		trim_frame_end = state_manager.get_item('trim_frame_end') or video_frame_total
		trim_frame_range_slider_options['maximum'] = video_frame_total
		trim_frame_range_slider_options['value'] = (trim_frame_start, trim_frame_end)
		trim_frame_range_slider_options['visible'] = True
		with gradio.Row():
			TRIM_START_BUTTON = gradio.Button(
				value="set to Trim-Start",
				variant='primary',
				size='sm'
			)
			TRIM_END_BUTTON = gradio.Button(
				value="set to Trim-End",
				variant='primary',
				size='sm'
			)
	TRIM_FRAME_RANGE_SLIDER = RangeSlider(**trim_frame_range_slider_options)


def set_start(trim_frame: Tuple[float, float]) -> tuple[Any, float]:
	trim_frame_start, trim_frame_end = trim_frame
	return state_manager.get_item('reference_frame_number'), trim_frame_end


def set_end(trim_frame: Tuple[float, float]) -> tuple[float, Any]:
	trim_frame_start, trim_frame_end = trim_frame
	return trim_frame_start, state_manager.get_item('reference_frame_number')


def listen() -> None:
	TRIM_FRAME_RANGE_SLIDER.release(update_trim_frame, inputs=TRIM_FRAME_RANGE_SLIDER)
	for ui_component in get_ui_components(
		[
			'target_image',
			'target_video'
		]):
		for method in ['upload', 'change', 'clear']:
			getattr(ui_component, method)(remote_update, outputs=[TRIM_FRAME_RANGE_SLIDER])
	TRIM_START_BUTTON.click(set_start, inputs=TRIM_FRAME_RANGE_SLIDER, outputs=TRIM_FRAME_RANGE_SLIDER)
	TRIM_END_BUTTON.click(set_end, inputs=TRIM_FRAME_RANGE_SLIDER, outputs=TRIM_FRAME_RANGE_SLIDER)


def remote_update() -> RangeSlider:
	if is_video(state_manager.get_item('target_path')):
		video_frame_total = count_video_frame_total(state_manager.get_item('target_path'))
		state_manager.clear_item('trim_frame_start')
		state_manager.clear_item('trim_frame_end')
		return RangeSlider(value=(0, video_frame_total), maximum=video_frame_total, visible=True)
	return RangeSlider(visible=False)


def update_trim_frame(trim_frame: Tuple[float, float]) -> None:
	clear_static_faces()
	trim_frame_start, trim_frame_end = trim_frame
	video_frame_total = count_video_frame_total(state_manager.get_item('target_path'))
	trim_frame_start = int(trim_frame_start) if trim_frame_start > 0 else None
	trim_frame_end = int(trim_frame_end) if trim_frame_end < video_frame_total else None
	state_manager.set_item('trim_frame_start', trim_frame_start)
	state_manager.set_item('trim_frame_end', trim_frame_end)
