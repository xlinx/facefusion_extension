from typing import Optional, Tuple, Any
import gradio

from facefusion.uis.components import about, age_modifier_options, common_options, execution, execution_queue_count, \
	execution_thread_count, expression_restorer_options, face_debugger_options, face_detector, face_editor_options, \
	face_enhancer_options, face_landmarker, face_masker, face_selector, face_swapper_options, frame_colorizer_options, \
	frame_enhancer_options, instant_runner, job_manager, job_runner, lip_syncer_options, memory, output, output_options, \
	preview, processors, source, target, temp_frame, trim_frame, ui_workflow, terminal

from gradio_rangeslider import RangeSlider
from facefusion import state_manager, wording
from facefusion.filesystem import is_video
from facefusion.uis.components.trim_frame import TRIM_FRAME_RANGE_SLIDER
from facefusion.uis.typing import ComponentOptions
from facefusion.vision import count_video_frame_total

# from facefusion.uis.typing import Update

EXT_TRIM_START_BUTTON: Optional[gradio.Button] = None
EXT_TRIM_END_BUTTON: Optional[gradio.Button] = None
EXT_TRIM_TIME_LENGTH_SLIDER: Optional[RangeSlider] = None


def pre_check() -> bool:
	return True


def pre_render() -> bool:
	return True


def runX(ui: gradio.Blocks) -> None:
	ui.launch()


def run(ui: gradio.Blocks) -> None:
	ui.launch(server_name="0.0.0.0", favicon_path='facefusion.ico', inbrowser=state_manager.get_item('open_browser'))


# def update() -> Update:
# 	return gradio.update()
def render() -> gradio.Blocks:
	with gradio.Blocks() as layout:
		with gradio.Row():
			with gradio.Column(scale=4):
				with gradio.Blocks():
					about.render()
				with gradio.Blocks():
					processors.render()
				with gradio.Blocks():
					age_modifier_options.render()
				with gradio.Blocks():
					expression_restorer_options.render()
				with gradio.Blocks():
					face_debugger_options.render()
				with gradio.Blocks():
					face_editor_options.render()
				with gradio.Blocks():
					face_enhancer_options.render()
				with gradio.Blocks():
					face_swapper_options.render()
				with gradio.Blocks():
					frame_colorizer_options.render()
				with gradio.Blocks():
					frame_enhancer_options.render()
				with gradio.Blocks():
					lip_syncer_options.render()
				with gradio.Blocks():
					execution.render()
					execution_thread_count.render()
					execution_queue_count.render()
				with gradio.Blocks():
					memory.render()
				with gradio.Blocks():
					temp_frame.render()
				with gradio.Blocks():
					output_options.render()

			with gradio.Column(scale=4):
				with gradio.Blocks():
					source.render()
				with gradio.Blocks():
					target.render()
				with gradio.Blocks():
					output.render()
				with gradio.Blocks():
					terminal.render()
				with gradio.Blocks():
					ui_workflow.render()
					instant_runner.render()
					job_runner.render()
					job_manager.render()
			with gradio.Column(scale=7):
				with gradio.Blocks():
					preview.render()
					renderX()
				with gradio.Blocks():
					trim_frame.render()
				with gradio.Blocks():
					face_selector.render()
				with gradio.Blocks():
					face_masker.render()
				with gradio.Blocks():
					face_detector.render()
				with gradio.Blocks():
					face_landmarker.render()
				with gradio.Blocks():
					common_options.render()

	return layout


def renderX() -> gradio.Blocks:
	global EXT_TRIM_START_BUTTON
	global EXT_TRIM_END_BUTTON
	# global EXT_TRIM_TIME_LENGTH_SLIDER
	with gradio.Blocks() as layout:
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
			# EXT_TRIM_TIME_LENGTH_SLIDER = gradio.Slider(-600, 600, value=0, label="Quick Trim-Time(sec)"),
			with gradio.Row():
				EXT_TRIM_START_BUTTON = gradio.Button(
					value="set to Trim-Start",
					variant='primary',
					size='sm'
				)
				EXT_TRIM_END_BUTTON = gradio.Button(
					value="set to Trim-End",
					variant='primary',
					size='sm'
				)
	return layout


def set_start(trim_frame: Tuple[float, float]) -> tuple[float, float]:
	trim_frame_start, trim_frame_end = trim_frame
	if state_manager.get_item('reference_frame_number') <= trim_frame_end:
		trim_frame_start = float(state_manager.get_item('reference_frame_number'))
	update_trim_frame((trim_frame_start, trim_frame_end))
	return trim_frame_start, trim_frame_end


def set_end(trim_frame: Tuple[float, float]) -> tuple[float, float]:
	trim_frame_start, trim_frame_end = trim_frame
	if state_manager.get_item('reference_frame_number') >= trim_frame_start:
		trim_frame_end = float(state_manager.get_item('reference_frame_number'))
	update_trim_frame((trim_frame_start, trim_frame_end))
	return trim_frame_start, trim_frame_end


def update_trim_frame(trim_frame: Tuple[float, float]) -> None:
	trim_frame_start, trim_frame_end = trim_frame
	video_frame_total = count_video_frame_total(state_manager.get_item('target_path'))
	trim_frame_start = int(trim_frame_start) if trim_frame_start > 0 else None
	trim_frame_end = int(trim_frame_end) if trim_frame_end < video_frame_total else None
	state_manager.set_item('trim_frame_start', trim_frame_start)
	state_manager.set_item('trim_frame_end', trim_frame_end)


def listen() -> None:
	processors.listen()
	age_modifier_options.listen()
	expression_restorer_options.listen()
	face_debugger_options.listen()
	face_editor_options.listen()
	face_enhancer_options.listen()
	face_swapper_options.listen()
	frame_colorizer_options.listen()
	frame_enhancer_options.listen()
	lip_syncer_options.listen()
	execution.listen()
	execution_thread_count.listen()
	execution_queue_count.listen()
	memory.listen()
	temp_frame.listen()
	output_options.listen()
	source.listen()
	target.listen()
	output.listen()
	instant_runner.listen()
	job_runner.listen()
	job_manager.listen()
	terminal.listen()
	preview.listen()
	trim_frame.listen()
	face_selector.listen()
	face_masker.listen()
	face_detector.listen()
	face_landmarker.listen()
	common_options.listen()
	listenX()


def listenX() -> None:
	if is_video(state_manager.get_item('target_path')):
		EXT_TRIM_START_BUTTON.click(set_start, inputs=trim_frame.TRIM_FRAME_RANGE_SLIDER, outputs=trim_frame.TRIM_FRAME_RANGE_SLIDER)
		EXT_TRIM_END_BUTTON.click(set_end, inputs=trim_frame.TRIM_FRAME_RANGE_SLIDER, outputs=trim_frame.TRIM_FRAME_RANGE_SLIDER)


RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
ENDC = '\033[0m'
print(f"{BLUE}[20241101][Extension][decadetw.QuickTrim]{ENDC}\n\n")
