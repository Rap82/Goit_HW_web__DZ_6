SELECT students.student_id, students.student_name, round(avg(grades.grade), 2) AS average_grade
FROM students
JOIN grades ON students.student_id = grades.student_id
GROUP BY students.student_id
ORDER BY average_grade DESC
LIMIT 5;