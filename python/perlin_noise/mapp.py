def v_map(start_val1, end_val1, start_val2, end_val2, samp):
    # Figure out how 'wide' each range is
    leftSpan = end_val1 - start_val1
    rightSpan = end_val2 - start_val2

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(samp - start_val1) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return start_val2 + (valueScaled * rightSpan)