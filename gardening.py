def task_func(matrix):
    if not matrix or not matrix[0]:
        return [], 0, [], 0

    result_sequence = []
    stops_history = []
    time_count = 0
    total_pumpkins = 0
    
    for i in range(len(matrix)):
        if i > 0:
            time_count += 4
            if time_count > 30:
                stops_history.append(total_pumpkins)
                time_count = 4

        row = matrix[i] if i % 2 == 0 else matrix[i][::-1]

        for j in range(len(row)):
            if j > 0:
                time_count += 1
            
            if time_count > 30:
                stops_history.append(total_pumpkins)
                time_count = 0
            
            total_pumpkins += row[j]
            result_sequence.append(row[j])
            
    return result_sequence, len(stops_history), stops_history, total_pumpkins
