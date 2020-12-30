from time import time
from decimal import Decimal


def kalk(callback, display=False, iteration_count=1, complete_data=False, **kwargs):
	"""
	:param callback: The function to be called
	:param display: Whether the results of the time calculations should be displayed in the console or not
	:param iteration_count: The amount of iterations of the function call
	:param complete_data: Whether a detailed set of results should be output or not (average duration of each iterations
	and the list of all durations)
	:param kwargs: The optional parameters of the callback
	:return: A set of data about the time calculations (the callback return data, the total duration - and, if complete_data
	is True, the average duration of each iterations and the list of all durations)
	"""

	data = {}
	total_duration = 0
	average_duration = None
	durations = []
	
	if display:
		print("[KRS] Starting...")

	for it in range(iteration_count):
		it_start_time = Decimal(time())
		# Invoking callback
		return_data = callback(**kwargs)
		# Invoking callback
		it_duration = Decimal((Decimal(time()) - it_start_time) * 1000)
		total_duration += it_duration
		if complete_data:
			durations.append(it_duration)

	if display:
		print("[KRS] Done!")
	
	data.update({
		"return_data": return_data,
		"total_duration": total_duration
	})
	
	if complete_data:
		average_duration = total_duration / iteration_count
		data.update({
			"average_duration": average_duration,
			"durations": durations
		})
	
	if display:
		print("[KRS] Time elapsed:", total_duration, "ms")
		if complete_data:
			print("      Average time:", average_duration, "ms")
	
	return data
