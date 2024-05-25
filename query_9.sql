-- Знайти список курсів, які відвідує студент.
SELECT students.student_name, GROUP_CONCAT(DISTINCT subjects.subject_name) AS courses
FROM students
JOIN grades ON grades.student_id = students.student_id
JOIN subjects ON subjects.subject_id = grades.subject_id
GROUP BY students.student_name
ORDER BY students.student_name