class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = collections.deque(students)
        sandwiches.reverse()
        while True:
            changed = False
            for i in range(len(students)):
                if students[0] == sandwiches[-1]:
                    students.popleft()
                    sandwiches.pop()
                    changed = True
                else:
                    s = students[0]
                    students.popleft()
                    students.append(s)
            if not changed:
                return len(students)
            if len(students) == 0:
                return 0
            

        
