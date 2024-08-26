def partial_sums(*rest):
    result = [0]
    for elem in rest:
        sum_in_list = result[-1]
        result.append(sum_in_list + elem)
    return result
