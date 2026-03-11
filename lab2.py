def radix_sort(arr):
    if not arr:
        return arr
    
    max_val = max(arr)
    exp = 1
    
    while max_val // exp > 0:
        buckets = [[] for _ in range(10)]
        
        for num in arr:
            digit = (num // exp) % 10
            buckets[digit].append(num)
        
        arr = []
        for bucket in buckets:
            arr.extend(bucket)
            
        exp *= 10
        
    return arr

def max_hamsters(max_budget, total_available_hamsters, hamsters_data):
    low = 0
    high = total_available_hamsters
    best_result = 0

    while low <= high:
        current_guess = (low + high) // 2
        
        if current_guess == 0:
            low = 1
            continue

        costs = []
        for hamster in hamsters_data:
            individual_cost = hamster[0] + hamster[1] * (current_guess - 1)
            costs.append(individual_cost)
        
        sorted_costs = radix_sort(costs)
        
        total_cost_for_guess = 0
        chosen_ones = sorted_costs[0:current_guess]
        for price in chosen_ones:
            total_cost_for_guess = total_cost_for_guess + price 
        
        if total_cost_for_guess <= max_budget:
            best_result = current_guess
            low = current_guess + 1
        else:
            high = current_guess - 1
            
    return best_result
