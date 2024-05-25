SELECT groups.group_name, students.student_id, students.student_name
FROM students
JOIN groups ON students.group_id = groups.group_id
ORDER BY groups.group_name, students.student_name