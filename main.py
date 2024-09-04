def find_missing_ids(first_ids, second_ids):
    result = []
    second_id_set = set(second_ids)
    for id in first_ids:
        if id not in second_id_set:
            result.append(id)
    return list(set(result))