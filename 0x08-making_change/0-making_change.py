from collections import deque

def makeChange(coins, total):
    if total <= 0:
        return 0

    # Sort coins to try larger coins first
    coins.sort(reverse=True)
    
    queue = deque([(0, 0)])  # (current_sum, number_of_coins)
    visited = set()  # To avoid revisiting the same sum

    while queue:
        current_sum, num_coins = queue.popleft()

        for coin in coins:
            next_sum = current_sum + coin

            if next_sum == total:
                return num_coins + 1
            if next_sum > total:
                continue
            if next_sum not in visited:
                visited.add(next_sum)
                queue.append((next_sum, num_coins + 1))

    return -1
