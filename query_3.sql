SELECT
    groups.group_name,
    subjects.subject_name,
    round(AVG(grades.grade), 2) AS average_grade
FROM
    groups
    JOIN students ON groups.group_id = students.group_id
    JOIN grades ON students.student_id = grades.student_id
    JOIN subjects ON grades.subject_id = subjects.subject_id
GROUP BY
    groups.group_id, subjects.subject_id;