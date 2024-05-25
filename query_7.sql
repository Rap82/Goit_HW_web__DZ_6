
SELECT groups.group_name, subjects.subject_name, students.student_name, grades.grade

FROM students
JOIN grades ON grades.student_id == students.student_id
JOIN subjects ON grades.subject_id == subjects.subject_id
JOIN groups ON groups.group_id == students.group_id
ORDER BY group_name, subject_name, student_name, grade

