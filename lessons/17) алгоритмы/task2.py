def merge_intervals(intervals):
    # сортируем по времени начала
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)

    return merged


def update_schedule(schedule, new_interval):
    schedule.append(new_interval)
    return merge_intervals(schedule)


schedule = [(8, 15), (18, 22), (23, 7)]
#
new_interval = (17, 20)
