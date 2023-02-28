def quicksort(items, index):
    if len(items) <= 1:
        return items
    pivot = items[0]
    smaller = [item for item in items[1:] if item[index] <= pivot[index]]
    larger = [item for item in items[1:] if item[index] > pivot[index]]
    return quicksort(smaller, index) + [pivot] + quicksort(larger, index)