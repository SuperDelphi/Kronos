from time import time


def kalk(callback, display=False, iteration_count=1, complete_data=False, input_data_callback=None, **kwargs):
	"""
	:param callback: The function to be called
	:param display: Whether the results of the time calculations should be displayed in the console or not
	:param iteration_count: The amount of iterations of the function call
	:param complete_data: Whether a detailed set of results should be output or not (average duration of each iterations
	and the list of all durations)
	:param input_data_callback: The optional callback function that returns input data to the main callback function.
	A parameter will be added to the callback at each iterations:
		- nth_iteration: The n-th iteration that will be executed
	The return data of this function must be a dict (whose the keys are the name of the parameters) and
	will be input as parameter(s) for the main callback function.
	:param kwargs: The optional parameters of the callback
	:return: A set of data about the time calculations (the callback return data, the total duration - and, if complete_data
	is True, the average duration of each iterations and the list of all durations)
	"""

	data = {}
	total_duration = 0
	average_duration = None
	durations = []
	return_data = None
	
	if display:
		print("[KRS] Starting...")

	for it in range(iteration_count):
		# Duplicating the code below instead of directly putting the if condition allows the duration calculation
		# to be more accurate.
		if input_data_callback:
			it_start_time = time() * 1000
			return_data = callback(**input_data_callback(nth_iteration=it), **kwargs)
			it_duration = time() * 1000 - it_start_time
		else:
			it_start_time = time() * 1000
			return_data = callback(**kwargs)
			it_duration = time() * 1000 - it_start_time
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
