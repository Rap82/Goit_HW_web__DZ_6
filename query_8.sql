-- Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT teachers.teacher_name, subjects.subject_name, ROUND(AVG(grades.grade), 2) AS average_grade
FROM grades
JOIN subjects ON grades.subject_id == subjects.subject_id
JOIN teachers ON subjects.teacher_id == teachers.teacher_id
GROUP BY subjects.subject_id;