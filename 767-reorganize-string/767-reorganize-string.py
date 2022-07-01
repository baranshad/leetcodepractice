class Solution:
    def reorganizeString(self, s: str) -> str:
        counter_str = Counter(s)
        heap = []
        for k, v in counter_str.items():
            heap.append([-v, k])
        heapq.heapify(heap)
        ans = heap[0][1]
        heap[0][0] += 1   
        for i in range(len(s)-1):
            if heap:
                #1st max num char
                t1 = heapq.heappop(heap) 
                if t1[0] < 0 and t1[1] != ans[-1]: 
                    ans += t1[1]
                    t1[0] += 1 
                    heapq.heappush(heap, t1)
                elif heap:
					#2nd max num char that does not equal to prev char
                    t2 = heapq.heappop(heap) 
                    #print(t2)
                    if t2[0] < 0 and t2[1] != ans[-1]:
                        ans += t2[1]
                        t2[0] += 1
                        heapq.heappush(heap, t2)
                    heapq.heappush(heap, t1)
                        
        return "" if len(ans) != len(s) else ans
                    