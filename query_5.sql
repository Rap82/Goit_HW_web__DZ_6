SELECT teachers.teacher_name, GROUP_CONCAT(subjects.subject_name) AS course
FROM subjects
JOIN teachers ON teachers.teacher_id = subjects.teacher_id
GROUP BY teachers.teacher_id;