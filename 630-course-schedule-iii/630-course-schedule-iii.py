class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        if courses == None or len(courses) == 0:
            return 0
        
        courses.sort(key = lambda x: x[1])
        curr_time = count = 0
        max_heap = []
        heapify(max_heap)
		
        for i in range(len(courses)):
            heappush(max_heap, -1 * courses[i][0])
            curr_time += courses[i][0]
            count += 1
			
            if  curr_time > courses[i][1] :
                curr_time += heappop(max_heap)
                count -= 1

        return count
