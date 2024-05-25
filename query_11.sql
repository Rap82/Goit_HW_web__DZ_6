SELECT teachers.teacher_name, students.student_name, ROUND(AVG(grades.grade), 2) AS average_grade
FROM grades
JOIN students ON students.student_id = grades.student_id
JOIN subjects ON subjects.subject_id = grades.subject_id
JOIN teachers ON teachers.teacher_id = subjects.teacher_id
WHERE students.student_name = ? AND teachers.teacher_name = ?
GROUP BY students.student_id, teachers.teacher_id