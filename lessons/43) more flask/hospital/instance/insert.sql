
INSERT INTO specialization (name) VALUES 
('Терапевт'),
('Стоматолог'),
('Невролог'),
('Офтальмолог'),
('Кардиолог');


INSERT INTO procedure (name, specialization_id) VALUES 
('Общий осмотр', 1),
('Вакцинация', 1),
('Чистка зубов', 2),
('Пломбирование', 2),
('МРТ диагностика', 3),
('Проверка зрения', 4),
('Подбор очков', 4),
('ЭКГ', 5),
('УЗИ сердца', 5),
('Консультация по анализам', 1);


INSERT INTO user (username, password, email, role) VALUES 
('doctor1', 'password123', 'doctor1@clinic.ru', 'doctor'),
('doctor2', 'password123', 'doctor2@clinic.ru', 'doctor'),
('doctor3', 'password123', 'doctor3@clinic.ru', 'doctor'),
('doctor4', 'password123', 'doctor4@clinic.ru', 'doctor'),
('doctor5', 'password123', 'doctor5@clinic.ru', 'doctor'),
('doctor6', 'password123', 'doctor6@clinic.ru', 'doctor'),
('doctor7', 'password123', 'doctor7@clinic.ru', 'doctor'),
('doctor8', 'password123', 'doctor8@clinic.ru', 'doctor'),
('doctor9', 'password123', 'doctor9@clinic.ru', 'doctor'),
('doctor10', 'password123', 'doctor10@clinic.ru', 'doctor');

INSERT INTO doctor (name, user_id, specialization_id) VALUES 
('Доктор Специалист 1', 1, 1),
('Доктор Специалист 2', 2, 2),
('Доктор Специалист 3', 3, 3),
('Доктор Специалист 4', 4, 4),
('Доктор Специалист 5', 5, 5),
('Доктор Специалист 6', 6, 1),
('Доктор Специалист 7', 7, 2),
('Доктор Специалист 8', 8, 3),
('Доктор Специалист 9', 9, 4),
('Доктор Специалист 10', 10, 5);


INSERT INTO user (username, password, email, role) VALUES 
('patient1', 'password123', 'patient1@mail.ru', 'patient'),
('patient2', 'password123', 'patient2@mail.ru', 'patient'),
('patient3', 'password123', 'patient3@mail.ru', 'patient'),
('patient4', 'password123', 'patient4@mail.ru', 'patient'),
('patient5', 'password123', 'patient5@mail.ru', 'patient'),
('patient6', 'password123', 'patient6@mail.ru', 'patient'),
('patient7', 'password123', 'patient7@mail.ru', 'patient'),
('patient8', 'password123', 'patient8@mail.ru', 'patient'),
('patient9', 'password123', 'patient9@mail.ru', 'patient'),
('patient10', 'password123', 'patient10@mail.ru', 'patient');

INSERT INTO patient (name, user_id) VALUES 
('Иванов Пациент 1', 11),
('Иванов Пациент 2', 12),
('Иванов Пациент 3', 13),
('Иванов Пациент 4', 14),
('Иванов Пациент 5', 15),
('Иванов Пациент 6', 16),
('Иванов Пациент 7', 17),
('Иванов Пациент 8', 18),
('Иванов Пациент 9', 19),
('Иванов Пациент 10', 20);


INSERT INTO appointment (patient_id, doctor_id, procedure_id, appointment_time, status) VALUES 
(1, 1, 1, datetime('now', '+0 days', '+0 hours'), 'scheduled'),
(2, 2, 2, datetime('now', '+1 days', '+1 hours'), 'scheduled'),
(3, 3, 3, datetime('now', '+2 days', '+2 hours'), 'scheduled'),
(4, 4, 4, datetime('now', '+3 days', '+3 hours'), 'scheduled'),
(5, 5, 5, datetime('now', '+4 days', '+4 hours'), 'scheduled'),
(6, 6, 6, datetime('now', '+5 days', '+5 hours'), 'scheduled'),
(7, 7, 7, datetime('now', '+6 days', '+6 hours'), 'scheduled'),
(8, 8, 8, datetime('now', '+7 days', '+7 hours'), 'scheduled'),
(9, 9, 9, datetime('now', '+8 days', '+8 hours'), 'scheduled'),
(10, 10, 10, datetime('now', '+9 days', '+9 hours'), 'scheduled');