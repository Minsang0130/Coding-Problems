class MaxHeap:
    def __init__(self):
        self.heap = []

    def heappush(self, item):
        self.heap.append(item)
        self._siftup(len(self.heap) -1 )

    def heappop(self):
        if len(self.heap) == 0:
            raise IndexError("힙이 비었습니다.")
        if len(self.heap) == 1:
            return self.haep[0]
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sitdown(0)
        return root

    def heapify(self, array):
        self.heap = array[:]
        n = len(array)
        for i in range(n // 2 -1, -1, -1):
            self._sitdown(i)

    def _siftup(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self.heap[idx] > self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent
            parent = (idx - 1) // 2

    def _siftdown(self, idx):
        n = len(self.heap)
        largest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < n and self.heap[left] > self.heap[largest]:
            largest = left
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != idx:
            self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
            self._siftup(largest)

    def __str__(self):
        return str(self.heap)


my_heap = MaxHeap()
my_heap.heappush(1)
my_heap.heappush(3)
my_heap.heappush(2)
my_heap.heappush(-2)

print(my_heap)
