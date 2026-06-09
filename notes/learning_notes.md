# Queue — Learning Notes
# By Kushagra Bansal | Project Lab India

## Queue Types Comparison
| Type | Python | Push | Pop | Access |
|------|--------|------|-----|--------|
| Queue | deque | append | popleft | O(1) |
| Stack | list | append | pop | O(1) |
| Priority Queue | heapq | heappush | heappop | O(log n) |
| Deque | deque | append/appendleft | pop/popleft | O(1) |

## Monotonic Deque (Sliding Window Max)
Keep deque decreasing. Front = current window max.
- Remove from front if out of window (i - dq[0] >= k)
- Remove from back while back < current (maintain decreasing)

## heapq in Python
heapq is MIN heap by default.
For MAX heap: push negative values.
heapq.nlargest(k, arr) → top k largest
heapq.nsmallest(k, arr) → top k smallest

## BFS Template
from collections import deque
q = deque([(start, 0)])  # (node, distance)
visited = {start}
while q:
    node, dist = q.popleft()
    if node == target: return dist
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            q.append((neighbor, dist+1))
