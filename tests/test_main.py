import sys; sys.path.insert(0,'..')
from solutions.main import *

def test_circular_queue():
    cq = CircularQueue(3)
    assert cq.enqueue(1) == True
    assert cq.enqueue(2) == True
    assert cq.enqueue(3) == True
    assert cq.enqueue(4) == False  # Full
    assert cq.front() == 1
    assert cq.dequeue() == True
    assert cq.front() == 2

def test_sliding_window():
    assert sliding_window_max([1,3,-1,-3,5,3,6,7],3) == [3,3,5,5,6,7]
    assert sliding_window_max([1],1) == [1]

def test_top_k():
    result = top_k_frequent([1,1,1,2,2,3], 2)
    assert 1 in result and 2 in result

def test_merge_k():
    assert merge_k_sorted([[1,4,7],[2,5,8],[3,6,9]]) == [1,2,3,4,5,6,7,8,9]

def test_task_scheduler():
    assert task_scheduler(["A","A","A","B","B","B"],2) == 8

def test_generate_binary():
    assert generate_binary_nums(3) == ["1","10","11"]
