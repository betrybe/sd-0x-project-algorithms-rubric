def study_schedule(start_time, end_time, target_time):
    count = 0

    for start_index, start_time in enumerate(start_time):
        if start_time <= target_time and end_time[start_index] >= target_time:
            count += 1

    return count