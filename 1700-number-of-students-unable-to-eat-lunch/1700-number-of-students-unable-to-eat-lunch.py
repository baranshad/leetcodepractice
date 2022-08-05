class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i = 0
        while i < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                i= 0
            else:
                students.append(students.pop(0))
                i+=1 
            if i == len(students):
                return i 

            # This block of code handles both scenarios at the end of each iteration:
            #           1) All students currently in the queue are unable to eat.
            #           2) Every student has taken a sandwich.


        
        