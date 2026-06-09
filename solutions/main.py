# DSA-Queue-Mastery — Solutions
# Author: Kushagra Bansal — Project Lab India
import heapq
from collections import deque, Counter

class CircularQueue:
    """Array-based circular queue | O(1) enqueue/dequeue"""
    def __init__(self, k):
        self.q = [0]*k; self.head=self.tail=self.size=0; self.cap=k
    def enqueue(self, val):
        if self.size==self.cap: return False
        self.q[self.tail]=val; self.tail=(self.tail+1)%self.cap; self.size+=1; return True
    def dequeue(self):
        if self.size==0: return False
        self.head=(self.head+1)%self.cap; self.size-=1; return True
    def front(self): return -1 if self.size==0 else self.q[self.head]
    def rear(self):  return -1 if self.size==0 else self.q[(self.tail-1)%self.cap]
    def is_empty(self): return self.size==0
    def is_full(self):  return self.size==self.cap

def sliding_window_max(nums, k):
    """Monotonic deque — O(n) T, O(k) S"""
    dq = deque(); result = []
    for i, n in enumerate(nums):
        while dq and nums[dq[-1]] < n: dq.pop()
        dq.append(i)
        if dq[0] <= i-k: dq.popleft()
        if i >= k-1: result.append(nums[dq[0]])
    return result

def top_k_frequent(nums, k):
    """Max heap on frequency | O(n log k) T, O(n) S"""
    count = Counter(nums)
    return [x for x,_ in count.most_common(k)]

def merge_k_sorted(arrays):
    """Min heap k-way merge | O(N log k) T, O(k) S"""
    heap = []; result = []
    for i, arr in enumerate(arrays):
        if arr: heapq.heappush(heap, (arr[0], i, 0))
    while heap:
        val, i, j = heapq.heappop(heap)
        result.append(val)
        if j+1 < len(arrays[i]):
            heapq.heappush(heap, (arrays[i][j+1], i, j+1))
    return result

def task_scheduler(tasks, n):
    """Greedy with max heap | O(n) T, O(1) S"""
    count = Counter(tasks)
    heap = [-c for c in count.values()]
    heapq.heapify(heap)
    time = 0
    while heap:
        temp = []; cycle = n+1
        while cycle and heap:
            temp.append(-heapq.heappop(heap)); cycle -= 1
        for c in temp:
            if c-1 > 0: heapq.heappush(heap, -(c-1))
        time += n+1 if heap else n+1-cycle
    return time

def bfs_shortest_path(grid):
    """BFS level-by-level | O(n*m) T, O(n*m) S"""
    n = len(grid); m = len(grid[0])
    if grid[0][0] or grid[n-1][m-1]: return -1
    q = deque([(0,0,1)]); visited = {(0,0)}
    while q:
        r,c,dist = q.popleft()
        if r==n-1 and c==m-1: return dist
        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]:
            nr,nc = r+dr, c+dc
            if 0<=nr<n and 0<=nc<m and grid[nr][nc]==0 and (nr,nc) not in visited:
                visited.add((nr,nc)); q.append((nr,nc,dist+1))
    return -1

def generate_binary_nums(n):
    """BFS-based binary number generation | O(2^n) T"""
    q = deque(["1"]); result = []
    while len(result) < n:
        front = q.popleft(); result.append(front)
        q.append(front+"0"); q.append(front+"1")
    return result

if __name__ == "__main__":
    print("="*58)
    print("  DSA Queue Mastery — Project Lab India")
    print("="*58)
    cq=CircularQueue(3); cq.enqueue(1); cq.enqueue(2); cq.enqueue(3)
    print(f"  CircularQueue full:          {cq.is_full()}")
    print(f"  SlidingWindowMax k=3:        {sliding_window_max([1,3,-1,-3,5,3,6,7],3)}")
    print(f"  TopKFrequent([1,1,1,2,2,3]): {top_k_frequent([1,1,1,2,2,3],2)}")
    print(f"  MergeKSorted:                {merge_k_sorted([[1,4,7],[2,5,8],[3,6,9]])}")
    print(f"  TaskScheduler n=2:           {task_scheduler(['A','A','A','B','B','B'],2)}")
    print(f"  GenerateBinary(5):           {generate_binary_nums(5)}")
    print("="*58)
