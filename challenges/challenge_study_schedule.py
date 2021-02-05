def study_schedule(start_time, end_time, target_time):

    if not end_time or not start_time:
        return 0
    elif target_time > max(end_time) or target_time < min(start_time):
        return 0

    counter = 0
    for index in range(len(start_time)):
        if start_time[index] <= target_time <= end_time[index]:
            counter += 1

    return counter
