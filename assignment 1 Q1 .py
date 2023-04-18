def find_pairs(arr, target):
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    return pairs

arr = [2, 4, 5, 3, 6, 7, 8, 9]
target = 10
pairs = find_pairs(arr, target)
print(pairs)
