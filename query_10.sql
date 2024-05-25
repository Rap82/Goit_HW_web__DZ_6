-- Список курсів, які певному студенту читає певний викладач.
-- SELECT teachers.teacher_name, students.student_name
-- FROM grades
-- LEFT JOIN grades ON grades.subject_id = subjects.subject_id
-- LEFT JOIN students ON students.student_id = grades.student_id
-- LEFT JOIN teachers ON teachers.teacher_id = subjects.teacher_id
-- WHERE students.student_name = 3 AND teachers.teacher_name = 1
-- GROUP BY grades.subject_name
-- ORDER BY grades.subject_name

SELECT students.student_name, GROUP_CONCAT(DISTINCT subjects.subject_name) AS courses , teachers.teacher_name
FROM students
JOIN grades ON grades.student_id = students.student_id
JOIN subjects ON subjects.subject_id = grades.subject_id
JOIN teachers ON teachers.teacher_id = subjects.teacher_id

GROUP BY subjects.subject_name
ORDER BY subjects.subject_name

