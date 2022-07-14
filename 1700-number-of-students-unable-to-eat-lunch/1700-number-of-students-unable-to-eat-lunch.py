class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i = 0 
        while i < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                i = 0
            else:
                students.append(students.pop(0))
                i+= 1 
            if i == len(students):
                return len(students)
        
        
        
        
        