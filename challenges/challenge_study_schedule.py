def study_schedule(permanence_period, target_time):
    if not target_time or not permanence_period:
        return None

    count = 0

    for period in permanence_period:
        if (
            None in period
            or isinstance(period[0], str)
            or isinstance(period[1], str)
        ):
            count = None
            break

        if period[0] <= target_time <= period[1]:
            count += 1

    return count
