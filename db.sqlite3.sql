CREATE TABLE `university_university` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `name` varchar(255) NOT NULL, `name_abbr` varchar(255) NOT NULL, `address_1` varchar(100) NOT NULL, `address_2` varchar(100) NOT NULL, `address_3` varchar(100) NOT NULL, `city` smallint NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `founding` date NOT NULL, `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `description` varchar(255) NOT NULL);
INSERT INTO `university_university` VALUES (1,NULL,'Đại học Luật Hà Nội','','','','',23,'2016-08-20 05:31:03.374316','2016-08-20 05:31:03.374358','1975-08-20',1,'');
CREATE TABLE `university_uclass` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `name` varchar(255) NOT NULL, `name_abbr` varchar(255) NOT NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `course_id` integer NOT NULL REFERENCES `university_course` (`id`), `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `description` varchar(255) NOT NULL);
CREATE TABLE `university_subject` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `name` varchar(255) NOT NULL, `name_abbr` varchar(255) NOT NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `credit` smallint NOT NULL, `description` varchar(255) NOT NULL, `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `specialized_study_id` integer NOT NULL REFERENCES `university_specializedstudy` (`id`));
INSERT INTO `university_subject` VALUES (3,NULL,'Công pháp quốc tế','CPQT','2016-10-20 00:32:03.599000','2016-10-20 00:32:03.599000',3,'',1,1);
CREATE TABLE `university_studysession` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `order` smallint NOT NULL, `start_date` date NOT NULL, `end_date` date NOT NULL, `description` varchar(255) NOT NULL, `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `semester_id` integer NOT NULL REFERENCES `university_semester` (`id`));
INSERT INTO `university_studysession` VALUES (2,'2016-10-20 00:30:53.113000','2016-10-17 15:40:53.595000','2016-10-17 15:40:53.595000',0,'2016-09-17','2016-12-17','',1,2),
 (3,NULL,'2016-10-17 15:40:53.600000','2016-10-17 15:40:53.600000',1,'2016-09-17','2016-10-17','',1,2),
 (4,NULL,'2016-10-17 15:40:53.605000','2016-10-17 15:40:53.605000',2,'2016-10-17','2016-11-17','',1,2),
 (5,NULL,'2016-10-17 15:40:53.610000','2016-10-17 15:40:53.610000',3,'2016-11-17','2016-11-30','',1,2),
 (6,NULL,'2016-10-17 15:41:07.137000','2016-10-17 15:41:07.137000',0,'2016-09-17','2016-12-17','',1,2);
CREATE TABLE `university_student` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `nick_name` varchar(255) NOT NULL, `account_id` integer NOT NULL REFERENCES `account_account` (`id`), `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `description` varchar(255) NOT NULL, `u_class_id` integer NOT NULL REFERENCES `university_uclass` (`id`));
CREATE TABLE `university_specializedstudy` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `name` varchar(255) NOT NULL, `name_abbr` varchar(255) NOT NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `address` varchar(100) NOT NULL, `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `university_id` integer NOT NULL REFERENCES `university_university` (`id`), `description` varchar(255) NOT NULL, `faculty_id` integer NOT NULL REFERENCES `university_faculty` (`id`));
INSERT INTO `university_specializedstudy` VALUES (1,NULL,'Công pháp quốc tế','CPQT','2016-10-20 00:31:46.558000','2016-10-20 00:31:46.558000','',1,1,'',1);
CREATE TABLE `university_semester` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `order` smallint NULL, `start_date` date NOT NULL, `end_date` date NOT NULL, `description` varchar(255) NOT NULL, `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `scholastic_id` integer NOT NULL REFERENCES `university_scholastic` (`id`), `university_id` integer NOT NULL REFERENCES `university_university` (`id`));
INSERT INTO `university_semester` VALUES (2,NULL,'2016-10-17 15:40:53.588000','2016-10-17 15:40:53.588000',1,'2016-09-17','2016-12-17','',1,2,1);
CREATE TABLE `university_scholastic` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `name` varchar(255) NOT NULL, `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `description` varchar(255) NOT NULL, `end_date` date NOT NULL, `start_date` date NOT NULL);
INSERT INTO `university_scholastic` VALUES (2,NULL,'2016-10-17 15:40:06.998000','2016-10-17 15:40:06.998000','2016-2016',1,'','2016-12-17','2016-09-17');
CREATE TABLE `university_lecturer` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `nick_name` varchar(255) NOT NULL, `account_id` integer NOT NULL REFERENCES `account_account` (`id`), `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `description` varchar(255) NOT NULL);
CREATE TABLE `university_faculty` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `name` varchar(255) NOT NULL, `name_abbr` varchar(255) NOT NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `address` varchar(100) NOT NULL, `description` varchar(255) NOT NULL, `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `university_id` integer NOT NULL REFERENCES `university_university` (`id`));
INSERT INTO `university_faculty` VALUES (1,NULL,'Pháp luật quốc tế','PLQT','2016-10-20 00:31:33.073000','2016-10-20 00:31:33.073000','','',1,1);
CREATE TABLE `university_course` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `name` varchar(255) NOT NULL, `name_abbr` varchar(255) NOT NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `description` varchar(255) NOT NULL, `university_id` integer NOT NULL REFERENCES `university_university` (`id`));
CREATE TABLE `softdelete_softdeleterecord` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `created_date` datetime NOT NULL, `object_id` varchar(100) NOT NULL, `changeset_id` integer NOT NULL REFERENCES `softdelete_changeset` (`id`), `content_type_id` integer NOT NULL REFERENCES `django_content_type` (`id`), UNIQUE (`changeset_id`, `content_type_id`, `object_id`));
INSERT INTO `softdelete_softdeleterecord` VALUES (10,'2016-10-20 00:30:53.073000','2',7,42);
CREATE TABLE `softdelete_changeset` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `created_date` datetime NOT NULL, `object_id` varchar(100) NOT NULL, `content_type_id` integer NOT NULL REFERENCES `django_content_type` (`id`));
INSERT INTO `softdelete_changeset` VALUES (7,'2016-10-20 00:30:53.044000','2',42);
CREATE TABLE `schedule_week` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `order` smallint NOT NULL, `description` varchar(255) NOT NULL, `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `outline_id` integer NOT NULL REFERENCES `outline_outline` (`id`));
CREATE TABLE `schedule_subjectschedule` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `description` varchar(255) NOT NULL, `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `week_id` integer NOT NULL REFERENCES `schedule_week` (`id`));
CREATE TABLE `schedule_studysession` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `order` smallint NOT NULL, `end_date` date NOT NULL, `description` varchar(255) NOT NULL, `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `semester_id` integer NOT NULL REFERENCES `schedule_semester` (`id`), `start_date` date NOT NULL);
CREATE TABLE `schedule_semester` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `order` smallint NULL, `end_date` date NOT NULL, `description` varchar(255) NOT NULL, `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `scholastic_id` integer NOT NULL REFERENCES `university_scholastic` (`id`), `university_id` integer NOT NULL REFERENCES `university_university` (`id`), `start_date` date NOT NULL);
CREATE TABLE `schedule_learningdayrequirement` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `content` varchar(255) NOT NULL, `description` varchar(255) NOT NULL, `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `day_id` integer NOT NULL REFERENCES `schedule_learningday` (`id`));
CREATE TABLE `schedule_learningdaycontent` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `content` varchar(255) NOT NULL, `description` varchar(255) NOT NULL, `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `day_id` integer NOT NULL REFERENCES `schedule_learningday` (`id`));
CREATE TABLE `schedule_learningday` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `description` varchar(255) NOT NULL, `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `week_id` integer NOT NULL REFERENCES `schedule_week` (`id`), `order` smallint NULL, `day_type` smallint NOT NULL);
CREATE TABLE `schedule_homeworkaction` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `description` varchar(255) NOT NULL, `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `homework_id` integer NOT NULL REFERENCES `homework_homework` (`id`), `week_id` integer NULL REFERENCES `schedule_week` (`id`), `hwa_type` smallint NOT NULL);
CREATE TABLE `schedule_currentweek` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `start_date` date NOT NULL, `end_date` date NOT NULL, `current_week_15` smallint NOT NULL, `current_week_5` smallint NOT NULL, `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `description` varchar(255) NOT NULL, `semester_id` integer NOT NULL REFERENCES `schedule_semester` (`id`), `off_next_week` bool NOT NULL);
CREATE TABLE `outline_targetawarenessdetail` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `order` smallint NOT NULL, `content` text NOT NULL, `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `target_awareness_id` integer NOT NULL REFERENCES `outline_targetawareness` (`id`), `description` varchar(255) NOT NULL);
CREATE TABLE `outline_targetawareness` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `level` smallint NOT NULL, `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `problem_id` integer NULL REFERENCES `outline_problem` (`id`), `problem_detail_id` integer NULL REFERENCES `outline_problemdetail` (`id`), `description` varchar(255) NOT NULL);
CREATE TABLE `outline_problemdetail` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `content` varchar(255) NOT NULL, `description` varchar(255) NOT NULL, `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `problem_id` integer NOT NULL REFERENCES `outline_problem` (`id`), `order` smallint NOT NULL);
CREATE TABLE `outline_problem` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `name` varchar(255) NOT NULL, `order` smallint NOT NULL, `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `outline_id` integer NOT NULL REFERENCES `outline_outline` (`id`), `description` varchar(255) NOT NULL);
CREATE TABLE `outline_outlinelearningresource` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `description` varchar(255) NOT NULL, `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `learning_resource_id` integer NOT NULL REFERENCES `library_learningresource` (`id`), `outline_id` integer NOT NULL REFERENCES `outline_outline` (`id`), `resource_type` smallint NOT NULL);
CREATE TABLE `outline_outline` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `description` varchar(255) NOT NULL, `course_id` integer NULL REFERENCES `university_course` (`id`), `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `subject_id` integer NOT NULL REFERENCES `university_subject` (`id`), `study_time_type` smallint NOT NULL, `study_session_id` integer NOT NULL REFERENCES `university_studysession` (`id`));
INSERT INTO `outline_outline` VALUES (3,NULL,'2016-10-20 00:35:52.161000','2016-10-20 00:35:52.161000','',NULL,1,3,0,6);
CREATE TABLE `outline_advisorytime` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `day_of_week` smallint NOT NULL, `start_time` time NOT NULL, `end_time` time NOT NULL, `place` varchar(255) NOT NULL, `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `outline_id` integer NOT NULL REFERENCES `outline_outline` (`id`), `description` varchar(255) NOT NULL);
CREATE TABLE `library_publishing` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `name` varchar(255) NOT NULL, `name_abbr` varchar(255) NOT NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `description` varchar(255) NOT NULL);
INSERT INTO `library_publishing` VALUES (1,NULL,'Công an nhân dân','CAND','2016-09-01 15:39:36.193333','2016-09-01 15:39:36.193390',1,''),
 (2,NULL,'Chính trị quốc gia','CTQG','2016-09-01 15:41:23.464973','2016-09-01 15:41:23.465034',1,''),
 (3,NULL,'Giáo dục','GD','2016-09-01 15:42:57.854901','2016-09-01 15:42:57.854962',1,''),
 (4,NULL,'Lao động','LĐ','2016-09-01 15:43:39.584635','2016-09-01 15:43:39.584693',1,'');
CREATE TABLE `library_library` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `name` varchar(255) NOT NULL, `name_abbr` varchar(255) NOT NULL, `address_1` varchar(100) NOT NULL, `address_2` varchar(100) NOT NULL, `address_3` varchar(100) NOT NULL, `city` smallint NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `university_id` integer NOT NULL REFERENCES `university_university` (`id`), `description` varchar(255) NOT NULL);
INSERT INTO `library_library` VALUES (2,NULL,'Đại học Luật Hà Nội','','','','',23,'2016-10-20 00:40:17.831000','2016-10-20 00:40:17.831000',1,1,'');
CREATE TABLE `library_learningresourcetype` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `name` varchar(100) NOT NULL, `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `description` varchar(255) NOT NULL);
INSERT INTO `library_learningresourcetype` VALUES (1,NULL,'2016-08-29 11:09:24.645982','2016-08-29 11:09:24.646019','Sách',1,''),
 (2,NULL,'2016-09-01 15:39:12.584898','2016-09-01 15:39:12.584957','Giáo trình',1,'');
CREATE TABLE `library_learningresource` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `name` varchar(255) NOT NULL, `author` varchar(255) NOT NULL, `is_avaiable` bool NOT NULL, `is_sale` bool NOT NULL, `sale_place` varchar(255) NOT NULL, `is_borrow` bool NOT NULL, `borrow_place` varchar(255) NOT NULL, `description` varchar(255) NOT NULL, `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `library_id` integer NULL REFERENCES `library_library` (`id`), `publishing_id` integer NULL REFERENCES `library_publishing` (`id`), `resource_type_id` integer NULL REFERENCES `library_learningresourcetype` (`id`), `pub_year` smallint NULL);
CREATE TABLE `homework_homeworkformat` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `name` varchar(100) NOT NULL, `page_size` smallint NOT NULL, `font` smallint NOT NULL, `size_unit` smallint NOT NULL, `top_margin` real NOT NULL, `bottom_margin` real NOT NULL, `left_margin` real NOT NULL, `right_margin` real NOT NULL, `break_lines` real NOT NULL, `other` varchar(255) NOT NULL, `description` varchar(255) NOT NULL, `creator_id` integer NOT NULL REFERENCES `account_account` (`id`));
CREATE TABLE `homework_homework` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `deleted_at` datetime NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `hw_type` smallint NOT NULL, `order` smallint NOT NULL, `page_limit_start` smallint NULL, `page_limit_end` smallint NULL, `handwritten` bool NOT NULL, `is_not_presenstation_required` bool NOT NULL, `presentation` varchar(255) NOT NULL, `other_requirement` varchar(255) NOT NULL, `description` varchar(255) NOT NULL, `creator_id` integer NOT NULL REFERENCES `account_account` (`id`), `hw_format_id` integer NOT NULL REFERENCES `homework_homeworkformat` (`id`), `outline_id` integer NOT NULL REFERENCES `outline_outline` (`id`));
CREATE TABLE `django_session` (`session_key` varchar(40) NOT NULL PRIMARY KEY, `session_data` text NOT NULL, `expire_date` datetime NOT NULL);
INSERT INTO `django_session` VALUES ('69kx1hz4r71635ynqwc54pi63hrb2svq','ZTkyOTA0NzgzNjQ4MDIxMzM5MmFhZjJhZDIzMTQ4ZTQzMDZiMzVhMzp7Il9hdXRoX3VzZXJfaGFzaCI6IjhlM2ZiOTdjYjAwZWMxMTE4NWM2NGFhZWRjMDBmZTlhYzNiMzlkY2QiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-09-15 15:35:31.266562'),
 ('g65085qbdsn4b72wd6xtuxtb0ckvhnhf','ODQwOGY0NmE3Njg5OGMwNjFiMTBjMDJlN2EyY2FlNzIwNzIzYTE2Zjp7Il9hdXRoX3VzZXJfaGFzaCI6IjYxNDUxNTljNTQzZjI3ZDlmYWIxZDRhMWU5ZTM3YWE4Yjg5ZWZlZDgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-09-16 01:56:54.293948'),
 ('m66ns2b73iuwuxuet5mnh0qht84n3b9c','OWQwNWJmZjcyODRkNWU0YTZlNGM4MjcyOWM5ODg2NGRkYTE0YTMxNjp7Il9hdXRoX3VzZXJfaGFzaCI6IjQ3OGY4NjNmYmRhZWZkNzcyZWJkNGI0NTM5MDk5NzFmMmNmNzZmMDMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-10-08 05:16:49.463000'),
 ('gfu09bytysc8009b6s4esgy4giul74a3','OWQwNWJmZjcyODRkNWU0YTZlNGM4MjcyOWM5ODg2NGRkYTE0YTMxNjp7Il9hdXRoX3VzZXJfaGFzaCI6IjQ3OGY4NjNmYmRhZWZkNzcyZWJkNGI0NTM5MDk5NzFmMmNmNzZmMDMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-11-12 14:16:47.031000');
CREATE TABLE `django_migrations` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `app` varchar(255) NOT NULL, `name` varchar(255) NOT NULL, `applied` datetime NOT NULL);
INSERT INTO `django_migrations` VALUES (1,'account','0001_initial','2016-08-20 05:29:06.494389'),
 (2,'contenttypes','0001_initial','2016-08-20 05:29:06.628493'),
 (3,'admin','0001_initial','2016-08-20 05:29:06.787713'),
 (4,'contenttypes','0002_remove_content_type_name','2016-08-20 05:29:06.956671'),
 (5,'auth','0001_initial','2016-08-20 05:29:07.140681'),
 (6,'auth','0002_alter_permission_name_max_length','2016-08-20 05:29:07.316717'),
 (7,'auth','0003_alter_user_email_max_length','2016-08-20 05:29:07.404670'),
 (8,'auth','0004_alter_user_username_opts','2016-08-20 05:29:07.489508'),
 (9,'auth','0005_alter_user_last_login_null','2016-08-20 05:29:07.569318'),
 (10,'auth','0006_require_contenttypes_0002','2016-08-20 05:29:07.625797'),
 (11,'university','0001_initial','2016-08-20 05:29:08.068688'),
 (12,'library','0001_initial','2016-08-20 05:29:08.586463'),
 (13,'outline','0001_initial','2016-08-20 05:29:09.129216'),
 (14,'homework','0001_initial','2016-08-20 05:29:09.538381'),
 (15,'schedule','0001_initial','2016-08-20 05:29:10.456222'),
 (16,'sessions','0001_initial','2016-08-20 05:29:10.608040'),
 (17,'softdelete','0001_initial','2016-08-20 05:29:11.048973'),
 (18,'account','0002_auto_20160829_0851','2016-08-29 01:52:09.149315'),
 (19,'library','0002_auto_20160829_0851','2016-08-29 01:52:09.586770'),
 (20,'outline','0002_auto_20160829_0851','2016-08-29 01:52:09.810924'),
 (21,'university','0002_auto_20160829_0851','2016-08-29 01:52:11.518230'),
 (22,'account','0002_auto_20160723_0916','2016-09-01 15:35:12.001237'),
 (23,'admin','0002_logentry_remove_auto_add','2016-09-01 15:35:12.048708'),
 (24,'auth','0007_alter_validators_add_error_messages','2016-09-01 15:35:12.236398'),
 (25,'outline','0002_auto_20160723_0916','2016-09-01 15:35:14.029850'),
 (26,'library','0002_auto_20160723_0916','2016-09-01 15:35:14.793184'),
 (27,'university','0002_auto_20160723_0916','2016-09-01 15:35:15.825108'),
 (28,'university','0003_auto_20160723_1951','2016-09-01 15:35:16.711017'),
 (29,'library','0003_auto_20160901_2246','2016-09-01 15:47:00.188048'),
 (30,'outline','0003_auto_20160901_2246','2016-09-01 15:47:00.582820'),
 (31,'library','0003_auto_20160830_1145','2016-09-02 01:51:31.823213'),
 (32,'outline','0003_auto_20160830_1145','2016-09-02 01:51:32.082505'),
 (33,'outline','0004_auto_20160902_1104','2016-09-02 04:04:53.218108'),
 (34,'schedule','0002_learningday_order','2016-09-02 04:04:53.439963'),
 (35,'schedule','0003_auto_20160902_1153','2016-09-02 04:53:54.411814'),
 (36,'schedule','0004_auto_20160902_1155','2016-09-02 04:55:46.025003'),
 (37,'schedule','0005_auto_20160902_1157','2016-09-02 04:57:30.205802'),
 (38,'schedule','0006_auto_20160903_1127','2016-09-03 04:27:39.249435'),
 (39,'schedule','0007_auto_20160903_1150','2016-09-03 04:50:23.130850'),
 (40,'university','0003_scholastic_start_date','2016-09-03 07:37:59.081845'),
 (41,'university','0004_auto_20160903_1439','2016-09-03 07:39:06.899175'),
 (42,'university','0005_scholastic_end_date','2016-09-03 07:47:07.451437'),
 (43,'university','0006_studysession','2016-09-03 08:38:41.563639'),
 (44,'university','0007_auto_20160905_0927','2016-09-05 02:27:13.211541'),
 (45,'schedule','0008_currentweek','2016-09-05 03:22:08.885823'),
 (46,'university','0008_auto_20160905_1021','2016-09-05 03:22:09.586892'),
 (47,'schedule','0009_auto_20160905_1025','2016-09-05 03:25:15.710799'),
 (48,'university','0009_auto_20160905_1517','2016-09-05 08:17:29.171778'),
 (49,'schedule','0010_auto_20160905_1517','2016-09-05 08:17:29.731739'),
 (50,'schedule','0011_semester_university','2016-09-05 08:20:54.335712'),
 (51,'schedule','0012_auto_20160906_1350','2016-09-06 06:51:17.875622'),
 (52,'schedule','0013_currentweek_off_next_week','2016-09-07 08:21:49.653010'),
 (53,'account','0002_auto_20160924_1525','2016-09-24 08:25:18.915000'),
 (54,'library','0002_auto_20160924_1525','2016-09-24 08:25:19.494000'),
 (55,'university','0002_auto_20160924_1525','2016-09-24 08:25:21.001000'),
 (56,'outline','0002_outline_study_time_type','2016-09-26 15:12:34.396000'),
 (57,'outline','0003_auto_20160926_2216','2016-09-26 15:16:08.246000'),
 (58,'university','0003_semester_studysession','2016-09-27 12:59:02.524000'),
 (59,'outline','0004_auto_20160927_1958','2016-09-27 12:59:02.945000'),
 (60,'university','0004_auto_20161017_2251','2016-10-17 15:51:42.151000');
CREATE TABLE `django_content_type` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `app_label` varchar(100) NOT NULL, `model` varchar(100) NOT NULL, UNIQUE (`app_label`, `model`));
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),
 (2,'auth','permission'),
 (3,'auth','group'),
 (4,'contenttypes','contenttype'),
 (5,'sessions','session'),
 (6,'softdelete','changeset'),
 (7,'softdelete','softdeleterecord'),
 (8,'account','account'),
 (9,'schedule','week'),
 (10,'schedule','subjectschedule'),
 (11,'schedule','learningday'),
 (12,'schedule','learningdaycontent'),
 (13,'schedule','learningdayrequirement'),
 (14,'schedule','homeworkaction'),
 (15,'university','university'),
 (16,'university','specializedstudy'),
 (17,'university','course'),
 (18,'university','uclass'),
 (19,'university','subject'),
 (20,'university','scholastic'),
 (21,'university','student'),
 (22,'university','lecturer'),
 (23,'library','library'),
 (24,'library','learningresourcetype'),
 (25,'library','publishing'),
 (26,'library','learningresource'),
 (27,'outline','outline'),
 (28,'outline','outlinelearningresource'),
 (29,'outline','problem'),
 (30,'outline','problemdetail'),
 (31,'outline','targetawareness'),
 (32,'outline','targetawarenessdetail'),
 (33,'outline','advisorytime'),
 (34,'homework','homeworkformat'),
 (35,'homework','homework'),
 (38,'schedule','currentweek'),
 (41,'university','semester'),
 (42,'university','studysession'),
 (43,'university','faculty');
CREATE TABLE `django_admin_log` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `object_id` text NULL, `object_repr` varchar(200) NOT NULL, `action_flag` smallint unsigned NOT NULL, `change_message` text NOT NULL, `content_type_id` integer NULL REFERENCES `django_content_type` (`id`), `user_id` integer NOT NULL REFERENCES `account_account` (`id`), `action_time` datetime NOT NULL);
INSERT INTO `django_admin_log` VALUES (1,'1','2016-2017',1,'',20,1,'2016-08-20 05:30:36.266872'),
 (2,'1','Đại học Luật Hà Nội',1,'',15,1,'2016-08-20 05:31:03.375594'),
 (3,'1','KHOA LÍ LUẬN CHÍNH TRỊ',1,'',16,1,'2016-08-20 05:31:13.268136'),
 (4,'1','Đường lối cách mạng của Đảng Cộng sản Việt Nam',1,'',19,1,'2016-08-20 05:31:30.913696'),
 (5,'1','40',1,'',17,1,'2016-08-20 05:31:37.912206'),
 (6,'1','Đường lối cách mạng của Đảng Cộng sản Việt Nam K40 Năm học 2016-2017',1,'',27,1,'2016-08-20 05:31:43.191523'),
 (7,'1','03',1,'',18,1,'2016-08-29 10:17:49.285861'),
 (8,'1','luanhlu3503@gmail.com',1,'',22,1,'2016-08-29 10:33:19.800748'),
 (9,'2','luanvuhlu@gmail.com',1,'',8,1,'2016-08-29 10:34:19.399966'),
 (10,'1','luanvuhlu@gmail.com',2,'account đã được thay đổi.',22,1,'2016-08-29 10:34:38.850504'),
 (11,'1','luanvuhlu@gmail.com',1,'',21,1,'2016-08-29 10:34:55.643162'),
 (12,'1','Vấn đề 1',1,'',29,1,'2016-08-29 10:52:41.199811'),
 (13,'1','Sách',1,'',24,1,'2016-08-29 11:09:24.647049'),
 (14,'2','Pháp luật quốc tế',1,'Được thêm.',16,1,'2016-09-01 15:36:36.619017'),
 (15,'2','Công pháp quốc tế',1,'Được thêm.',19,1,'2016-09-01 15:36:45.270646'),
 (16,'2','Giáo trình',1,'Được thêm.',24,1,'2016-09-01 15:39:12.585891'),
 (17,'1','Công an nhân dân',1,'Được thêm.',25,1,'2016-09-01 15:39:36.194325'),
 (18,'1','Đại học Luật Hà Nội',1,'Được thêm.',23,1,'2016-09-01 15:40:17.208639'),
 (19,'1','Giáo trình luật quốc tế',1,'Được thêm.',26,1,'2016-09-01 15:40:28.019211'),
 (20,'2','Chính trị quốc gia',1,'Được thêm.',25,1,'2016-09-01 15:41:23.466017'),
 (21,'2','Các tổ chức quốc tế và Việt Nam',1,'Được thêm.',26,1,'2016-09-01 15:41:35.528607'),
 (22,'3','Các văn bản công pháp quốc tế và văn bản pháp luật Việt Nam có liên quan',1,'Được thêm.',26,1,'2016-09-01 15:42:23.980397'),
 (23,'3','Giáo dục',1,'Được thêm.',25,1,'2016-09-01 15:42:57.855953'),
 (24,'4','Luật quốc tế - Lí luận và thực tiễn',1,'Được thêm.',26,1,'2016-09-01 15:43:07.055537'),
 (25,'4','Lao động',1,'Được thêm.',25,1,'2016-09-01 15:43:39.585628'),
 (26,'5','Luật biển quốc tế hiện đại',1,'Được thêm.',26,1,'2016-09-01 15:43:47.116612'),
 (27,'6','Toà án công lí quốc tế',1,'Được thêm.',26,1,'2016-09-01 15:44:24.576840'),
 (28,'7','Luật hình sự quốc tế',1,'Được thêm.',26,1,'2016-09-01 15:45:02.728934'),
 (29,'2','Công pháp quốc tế K40 Năm học 2016-2017',1,'Được thêm. Vấn đề `Vấn đề 1` đã được thêm vào. Vấn đề `Vấn đề 2` đã được thêm vào. Vấn đề `Vấn đề 3` đã được thêm vào. Vấn đề `Vấn đề 4` đã được thêm vào. Vấn đề `Vấn đề 5` đã được thêm vào. Vấn đề `Vấn đề 6` đã được thêm vào. Vấn đề `Vấn đề 7` đã được thêm vào. Vấn đề `Vấn đề 8` đã được thêm vào. Vấn đề `Vấn đề 9` đã được thêm vào. Vấn đề `Vấn đề 10` đã được thêm vào. Tài liệu cho môn học `Giáo trình luật quốc tế` đã được thêm vào. Tài liệu cho môn học `Các tổ chức quốc tế và Việt Nam` đã được thêm vào. Tài liệu cho môn học `Các văn bản công pháp quốc tế và văn bản pháp luật Việt Nam có liên quan` đã được thêm vào. Tài liệu cho môn học `Luật quốc tế - Lí luận và thực tiễn` đã được thêm vào. Tài liệu cho môn học `Luật biển quốc tế hiện đại` đã được thêm vào. Tài liệu cho môn học `Toà án công lí quốc tế` đã được thêm vào. Tài liệu cho môn học `Luật hình sự quốc tế` đã được thêm vào. Thời gian tư vấn `Công pháp quốc tế K40 Năm học 2016-2017 Thứ 4` đã được thêm vào.',27,1,'2016-09-01 15:46:09.279226'),
 (30,'2','Công pháp quốc tế KNone Năm học 2016-2017',2,'course đã được thay đổi.',27,1,'2016-09-01 15:47:06.238063'),
 (31,'1','Đường lối cách mạng của Đảng Cộng sản Việt Nam K40 Năm học 2016-2017',3,'',27,1,'2016-09-01 15:47:22.460786'),
 (32,'2','Vấn đề 1',2,'Nội dung vấn đề `Vấn đề 1.1` đã được thêm vào. Nội dung vấn đề `Vấn đề 1.2` đã được thêm vào. Nội dung vấn đề `Vấn đề 1.3` đã được thêm vào.',29,1,'2016-09-01 15:51:28.760738'),
 (33,'3','Vấn đề 2',2,'Nội dung vấn đề `Vấn đề 2.1` đã được thêm vào. Nội dung vấn đề `Vấn đề 2.2` đã được thêm vào. Nội dung vấn đề `Vấn đề 2.3` đã được thêm vào. Nội dung vấn đề `Vấn đề 2.4` đã được thêm vào. Nội dung vấn đề `Vấn đề 2.5` đã được thêm vào.',29,1,'2016-09-01 15:52:28.624612'),
 (34,'4','Vấn đề 3',2,'Nội dung vấn đề `Vấn đề 3.1` đã được thêm vào. Nội dung vấn đề `Vấn đề 3.2` đã được thêm vào. Nội dung vấn đề `Vấn đề 3.3` đã được thêm vào.',29,1,'2016-09-01 15:53:42.598374'),
 (35,'5','Vấn đề 4',2,'Nội dung vấn đề `Vấn đề 4.1` đã được thêm vào. Nội dung vấn đề `Vấn đề 4.2` đã được thêm vào. Nội dung vấn đề `Vấn đề 4.3` đã được thêm vào.',29,1,'2016-09-01 15:54:04.405374'),
 (36,'6','Vấn đề 5',2,'Nội dung vấn đề `Vấn đề 5.1` đã được thêm vào. Nội dung vấn đề `Vấn đề 5.2` đã được thêm vào. Nội dung vấn đề `Vấn đề 5.3` đã được thêm vào. Nội dung vấn đề `Vấn đề 5.4` đã được thêm vào.',29,1,'2016-09-01 15:54:49.680173'),
 (37,'7','Vấn đề 6',2,'Nội dung vấn đề `Vấn đề 6.1` đã được thêm vào. Nội dung vấn đề `Vấn đề 6.2` đã được thêm vào. Nội dung vấn đề `Vấn đề 6.3` đã được thêm vào. Nội dung vấn đề `Vấn đề 6.4` đã được thêm vào.',29,1,'2016-09-01 15:55:13.143957'),
 (38,'8','Vấn đề 7',2,'Nội dung vấn đề `Vấn đề 7.1` đã được thêm vào. Nội dung vấn đề `Vấn đề 7.2` đã được thêm vào. Nội dung vấn đề `Vấn đề 7.3` đã được thêm vào.',29,1,'2016-09-01 15:55:40.209580'),
 (39,'9','Vấn đề 8',2,'Nội dung vấn đề `Vấn đề 8.1` đã được thêm vào. Nội dung vấn đề `Vấn đề 8.2` đã được thêm vào. Nội dung vấn đề `Vấn đề 8.3` đã được thêm vào. Nội dung vấn đề `Vấn đề 8.4` đã được thêm vào.',29,1,'2016-09-01 15:56:18.623173'),
 (40,'10','Vấn đề 9',2,'Nội dung vấn đề `Vấn đề 9.1` đã được thêm vào. Nội dung vấn đề `Vấn đề 9.2` đã được thêm vào.',29,1,'2016-09-01 15:56:40.116606'),
 (41,'11','Vấn đề 10',2,'Nội dung vấn đề `Vấn đề 10.1` đã được thêm vào. Nội dung vấn đề `Vấn đề 10.2` đã được thêm vào. Nội dung vấn đề `Vấn đề 10.3` đã được thêm vào.',29,1,'2016-09-01 15:57:02.410960'),
 (42,'1','Mặc định',1,'Được thêm.',34,1,'2016-09-01 16:15:12.473572'),
 (43,'1','Cá nhân 1 Công pháp quốc tế 2016-2017',1,'Được thêm.',35,1,'2016-09-01 16:16:20.607587'),
 (44,'2','Cá nhân 2 Công pháp quốc tế 2016-2017',1,'Được thêm.',35,1,'2016-09-01 16:18:10.400292'),
 (45,'3','Nhóm tháng 1 Công pháp quốc tế 2016-2017',1,'Được thêm.',35,1,'2016-09-01 16:18:31.997739'),
 (46,'4','Học kỳ Công pháp quốc tế 2016-2017',1,'Được thêm.',35,1,'2016-09-01 16:18:55.664600'),
 (47,'3','Nhóm tháng Công pháp quốc tế 2016-2017',2,'order đã được thay đổi.',35,1,'2016-09-01 16:19:00.850060'),
 (48,'2','Công pháp quốc tế 2016-2017',2,'Không có trường nào thay đổi',27,1,'2016-09-01 16:23:53.609363'),
 (49,'1','Tuần 0 - Công pháp quốc tế 2016-2017',1,'',9,1,'2016-09-02 04:21:05.648265'),
 (50,'2','Tuần 1 - Công pháp quốc tế 2016-2017',1,'',9,1,'2016-09-02 04:22:01.743136'),
 (51,'2','Công pháp quốc tế 2016-2017',2,'Tuần học `Tuần 2 - Công pháp quốc tế 2016-2017` đã được thêm vào. Tuần học `Tuần 3 - Công pháp quốc tế 2016-2017` đã được thêm vào. Tuần học `Tuần 4 - Công pháp quốc tế 2016-2017` đã được thêm vào. Tuần học `Tuần 5 - Công pháp quốc tế 2016-2017` đã được thêm vào. Tuần học `Tuần 6 - Công pháp quốc tế 2016-2017` đã được thêm vào. Tuần học `Tuần 7 - Công pháp quốc tế 2016-2017` đã được thêm vào. Tuần học `Tuần 8 - Công pháp quốc tế 2016-2017` đã được thêm vào. Tuần học `Tuần 9 - Công pháp quốc tế 2016-2017` đã được thêm vào. Tuần học `Tuần 10 - Công pháp quốc tế 2016-2017` đã được thêm vào. Tuần học `Tuần 11 - Công pháp quốc tế 2016-2017` đã được thêm vào. Tuần học `Tuần 12 - Công pháp quốc tế 2016-2017` đã được thêm vào. Tuần học `Tuần 13 - Công pháp quốc tế 2016-2017` đã được thêm vào. Tuần học `Tuần 14 - Công pháp quốc tế 2016-2017` đã được thêm vào. Tuần học `Tuần 15 - Công pháp quốc tế 2016-2017` đã được thêm vào.',27,1,'2016-09-02 04:25:20.391366'),
 (52,'3','Tuần 2 - Công pháp quốc tế 2016-2017',2,'Không có trường nào thay đổi',9,1,'2016-09-02 04:57:32.451060'),
 (53,'3','Tuần 2 - Công pháp quốc tế 2016-2017',2,'Hoạt động bài tập `Nhận Học kỳ Công pháp quốc tế 2016-2017` đã được thêm vào.',9,1,'2016-09-02 04:57:42.618853'),
 (54,'6','Tuần 5 - Công pháp quốc tế 2016-2017',2,'Hoạt động bài tập `Làm Cá nhân 1 Công pháp quốc tế 2016-2017` đã được thêm vào.',9,1,'2016-09-02 04:58:29.607112'),
 (55,'9','Tuần 8 - Công pháp quốc tế 2016-2017',2,'Hoạt động bài tập `Nhận Nhóm tháng Công pháp quốc tế 2016-2017` đã được thêm vào.',9,1,'2016-09-02 04:58:43.302850'),
 (56,'12','Tuần 11 - Công pháp quốc tế 2016-2017',2,'Hoạt động bài tập `Làm Cá nhân 2 Công pháp quốc tế 2016-2017` đã được thêm vào.',9,1,'2016-09-02 07:58:49.693847'),
 (57,'14','Tuần 13 - Công pháp quốc tế 2016-2017',2,'Hoạt động bài tập `Nộp Nhóm tháng Công pháp quốc tế 2016-2017` đã được thêm vào.',9,1,'2016-09-02 07:59:02.624775'),
 (58,'15','Tuần 14 - Công pháp quốc tế 2016-2017',2,'Hoạt động bài tập `Thuyết trình Nhóm tháng Công pháp quốc tế 2016-2017` đã được thêm vào. Hoạt động bài tập `Nộp Học kỳ Công pháp quốc tế 2016-2017` đã được thêm vào.',9,1,'2016-09-02 07:59:18.370188'),
 (59,'4','Giờ Lý thuyết Tuần Tuần 1 - Công pháp quốc tế 2016-2017',1,'',11,1,'2016-09-03 04:43:20.051716'),
 (60,'4','Giờ Lý thuyết Tuần Tuần 1 - Công pháp quốc tế 2016-2017',3,'',11,1,'2016-09-03 04:43:41.225519'),
 (61,'1','Giờ Lý thuyết Tuần Tuần 0 - Công pháp quốc tế 2016-2017',2,'Nội dung học `Giờ Lý thuyết Tuần Tuần 0 - Công pháp quốc tế 2016-2017 Nội dung thứ 1` đã được thêm vào. Nội dung học `Giờ Lý thuyết Tuần Tuần 0 - Công pháp quốc tế 2016-2017 Nội dung thứ 2` đã được thêm vào. Nội dung học `Giờ Lý thuyết Tuần Tuần 0 - Công pháp quốc tế 2016-2017 Nội dung thứ 3` đã được thêm vào. Nội dung học `Giờ Lý thuyết Tuần Tuần 0 - Công pháp quốc tế 2016-2017 Nội dung thứ 4` đã được thêm vào. Yêu cầu chuẩn bị cho giờ học `Giờ Lý thuyết Tuần Tuần 0 - Công pháp quốc tế 2016-2017 Yêu cầu thứ 1` đã được thêm vào. Yêu cầu chuẩn bị cho giờ học `Giờ Lý thuyết Tuần Tuần 0 - Công pháp quốc tế 2016-2017 Yêu cầu thứ 2` đã được thêm vào. Yêu cầu chuẩn bị cho giờ học `Giờ Lý thuyết Tuần Tuần 0 - Công pháp quốc tế 2016-2017 Yêu cầu thứ 3` đã được thêm vào.',11,1,'2016-09-03 04:45:48.428627'),
 (62,'5','Giờ Lý thuyết Tuần Tuần 2 - Công pháp quốc tế 2016-2017',1,'',11,1,'2016-09-03 06:38:29.890113'),
 (63,'6','Giờ Thảo luận Tuần Tuần 2 - Công pháp quốc tế 2016-2017',1,'',11,1,'2016-09-03 06:39:00.609441'),
 (64,'7','Giờ Tự học Tuần Tuần 2 - Công pháp quốc tế 2016-2017',1,'',11,1,'2016-09-03 06:39:41.520297'),
 (65,'6','Giờ Thảo luận Tuần Tuần 2 - Công pháp quốc tế 2016-2017',2,'order đã được thay đổi.',11,1,'2016-09-03 06:39:47.014521'),
 (66,'5','Giờ Lý thuyết Tuần Tuần 2 - Công pháp quốc tế 2016-2017',2,'Không có trường nào thay đổi',11,1,'2016-09-03 06:40:01.495406'),
 (67,'6','Giờ Thảo luận Tuần Tuần 2 - Công pháp quốc tế 2016-2017',2,'order đã được thay đổi.',11,1,'2016-09-03 06:40:05.343601'),
 (68,'3','Giờ Thảo luận Tuần Tuần 1 - Công pháp quốc tế 2016-2017',3,'',11,1,'2016-09-03 06:40:39.747499'),
 (69,'2','Giờ Lý thuyết Tuần Tuần 1 - Công pháp quốc tế 2016-2017',3,'',11,1,'2016-09-03 06:40:39.872974'),
 (70,'7','Giờ Tự học Tuần Tuần 1 - Công pháp quốc tế 2016-2017',2,'week đã được thay đổi.',11,1,'2016-09-03 06:40:45.682953'),
 (71,'6','Giờ Thảo luận Tuần Tuần 1 - Công pháp quốc tế 2016-2017',2,'week đã được thay đổi.',11,1,'2016-09-03 06:40:50.674676'),
 (72,'5','Giờ Lý thuyết Tuần Tuần 1 - Công pháp quốc tế 2016-2017',2,'week đã được thay đổi.',11,1,'2016-09-03 06:40:55.067154'),
 (73,'8','Giờ Lý thuyết Tuần Tuần 2 - Công pháp quốc tế 2016-2017',1,'',11,1,'2016-09-03 06:41:25.250836'),
 (74,'9','Giờ Thảo luận Tuần Tuần 2 - Công pháp quốc tế 2016-2017',1,'',11,1,'2016-09-03 06:41:52.431656'),
 (75,'10','Giờ Tự học Tuần Tuần 2 - Công pháp quốc tế 2016-2017',1,'',11,1,'2016-09-03 06:42:11.213465'),
 (76,'1','2016-2017',2,'start_date đã được thay đổi.',20,1,'2016-09-03 07:39:17.093650'),
 (77,'1','2016-2017',2,'end_date đã được thay đổi.',20,1,'2016-09-03 07:55:08.911351'),
 (78,'1','2016-2017',2,'Không có trường nào thay đổi',20,1,'2016-09-03 07:55:32.348900'),
 (79,'1','2016-2018',2,'Không có trường nào thay đổi',20,1,'2016-09-03 07:59:37.166596'),
 (80,'1','2016-2017',2,'end_date đã được thay đổi.',20,1,'2016-09-03 07:59:45.642103'),
 (81,'1','2016-2017',2,'Không có trường nào thay đổi',20,1,'2016-09-03 08:01:32.413783'),
 (84,'1','Năm học 2016-2017 Học kỳ 1',1,'',NULL,1,'2016-09-05 08:41:48.404936'),
 (85,'2','Năm học 2016-2017 Học kỳ 2',1,'',NULL,1,'2016-09-05 08:44:11.470383'),
 (86,'1','CurrentWeek object',1,'',38,1,'2016-09-06 06:47:22.449199'),
 (87,'1','CurrentWeek object',3,'',38,1,'2016-09-06 06:49:07.319795'),
 (88,'2','Tuần hiện tại',1,'',38,1,'2016-09-06 06:51:48.300793'),
 (89,'2','Năm học 2016-2017 Học kỳ 2 Đợt 0',3,'',NULL,1,'2016-09-06 06:55:08.517875'),
 (90,'2','Pháp luật quốc tế',2,'name_abbr và address đã được thay đổi.',16,1,'2016-09-06 07:31:19.530500'),
 (91,'2','Công pháp quốc tế 2016-2017',2,'study_time_type đã được thay đổi.',27,1,'2016-09-26 15:14:55.976000'),
 (92,'2','Công pháp quốc tế 2016-2017',2,'Không có trường nào thay đổi',27,1,'2016-09-26 15:16:23.533000'),
 (93,'2','Tuần hiện tại',2,'current_week_15 và current_week_5 đã được thay đổi.',38,1,'2016-09-26 15:34:44.906000'),
 (94,'1','Năm học 2016-2017 Học kỳ 1',1,'Được thêm. Đợt học `Năm học 2016-2017 Học kỳ 1 Đợt 0` đã được thêm vào.',41,1,'2016-09-27 13:00:16.185000'),
 (95,'2','2016-2016',1,'Được thêm.',20,1,'2016-10-17 15:40:07.011000'),
 (96,'2','Năm học 2016-2016 Học kỳ 1',1,'Được thêm. Đợt học `Năm học 2016-2016 Học kỳ 1 Đợt 0` đã được thêm vào. Đợt học `Năm học 2016-2016 Học kỳ 1 Đợt 1` đã được thêm vào. Đợt học `Năm học 2016-2016 Học kỳ 1 Đợt 2` đã được thêm vào. Đợt học `Năm học 2016-2016 Học kỳ 1 Đợt 3` đã được thêm vào.',41,1,'2016-10-17 15:40:53.615000'),
 (97,'6','Năm học 2016-2016 Học kỳ 1 Đợt 0',1,'Được thêm.',42,1,'2016-10-17 15:41:07.148000'),
 (98,'2','Năm học 2016-2016 Học kỳ 1 Đợt 0',3,'',42,1,'2016-10-20 00:30:52.994000'),
 (99,'1','Pháp luật quốc tế',1,'Được thêm.',43,1,'2016-10-20 00:31:33.080000'),
 (100,'1','Công pháp quốc tế',1,'Được thêm.',16,1,'2016-10-20 00:31:46.563000'),
 (101,'3','Công pháp quốc tế',1,'Được thêm.',19,1,'2016-10-20 00:32:03.605000'),
 (102,'3','Công pháp quốc tế Năm học 2016-2016 Học kỳ 1 Đợt 0',1,'Được thêm.',27,1,'2016-10-20 00:35:52.184000'),
 (103,'2','Đại học Luật Hà Nội',1,'Được thêm.',23,1,'2016-10-20 00:40:17.837000');
CREATE TABLE `auth_permission` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `content_type_id` integer NOT NULL REFERENCES `django_content_type` (`id`), `codename` varchar(100) NOT NULL, `name` varchar(255) NOT NULL, UNIQUE (`content_type_id`, `codename`));
INSERT INTO `auth_permission` VALUES (1,1,'add_logentry','Can add log entry'),
 (2,1,'change_logentry','Can change log entry'),
 (3,1,'delete_logentry','Can delete log entry'),
 (4,2,'add_permission','Can add permission'),
 (5,2,'change_permission','Can change permission'),
 (6,2,'delete_permission','Can delete permission'),
 (7,3,'add_group','Can add group'),
 (8,3,'change_group','Can change group'),
 (9,3,'delete_group','Can delete group'),
 (10,4,'add_contenttype','Can add content type'),
 (11,4,'change_contenttype','Can change content type'),
 (12,4,'delete_contenttype','Can delete content type'),
 (13,5,'add_session','Can add session'),
 (14,5,'change_session','Can change session'),
 (15,5,'delete_session','Can delete session'),
 (16,6,'add_changeset','Can add change set'),
 (17,6,'change_changeset','Can change change set'),
 (18,6,'delete_changeset','Can delete change set'),
 (19,7,'add_softdeleterecord','Can add soft delete record'),
 (20,7,'change_softdeleterecord','Can change soft delete record'),
 (21,7,'delete_softdeleterecord','Can delete soft delete record'),
 (22,8,'add_account','Can add Tài khoản'),
 (23,8,'change_account','Can change Tài khoản'),
 (24,8,'delete_account','Can delete Tài khoản'),
 (25,9,'add_week','Can add Tuần học'),
 (26,9,'change_week','Can change Tuần học'),
 (27,9,'delete_week','Can delete Tuần học'),
 (28,10,'add_subjectschedule','Can add Lịch trình học hàng tuần'),
 (29,10,'change_subjectschedule','Can change Lịch trình học hàng tuần'),
 (30,10,'delete_subjectschedule','Can delete Lịch trình học hàng tuần'),
 (31,11,'add_learningday','Can add Ngày học'),
 (32,11,'change_learningday','Can change Ngày học'),
 (33,11,'delete_learningday','Can delete Ngày học'),
 (34,12,'add_learningdaycontent','Can add Nội dung học'),
 (35,12,'change_learningdaycontent','Can change Nội dung học'),
 (36,12,'delete_learningdaycontent','Can delete Nội dung học'),
 (37,13,'add_learningdayrequirement','Can add Yêu cầu chuẩn bị cho giờ học'),
 (38,13,'change_learningdayrequirement','Can change Yêu cầu chuẩn bị cho giờ học'),
 (39,13,'delete_learningdayrequirement','Can delete Yêu cầu chuẩn bị cho giờ học'),
 (40,14,'add_homeworkaction','Can add Hoạt động bài tập'),
 (41,14,'change_homeworkaction','Can change Hoạt động bài tập'),
 (42,14,'delete_homeworkaction','Can delete Hoạt động bài tập'),
 (43,15,'add_university','Can add Đại học'),
 (44,15,'change_university','Can change Đại học'),
 (45,15,'delete_university','Can delete Đại học'),
 (46,16,'add_specializedstudy','Can add Khoa'),
 (47,16,'change_specializedstudy','Can change Khoa'),
 (48,16,'delete_specializedstudy','Can delete Khoa'),
 (49,17,'add_course','Can add Khoá'),
 (50,17,'change_course','Can change Khoá'),
 (51,17,'delete_course','Can delete Khoá'),
 (52,18,'add_uclass','Can add Lớp'),
 (53,18,'change_uclass','Can change Lớp'),
 (54,18,'delete_uclass','Can delete Lớp'),
 (55,19,'add_subject','Can add Môn học'),
 (56,19,'change_subject','Can change Môn học'),
 (57,19,'delete_subject','Can delete Môn học'),
 (58,20,'add_scholastic','Can add Năm học'),
 (59,20,'change_scholastic','Can change Năm học'),
 (60,20,'delete_scholastic','Can delete Năm học'),
 (61,21,'add_student','Can add Sinh viên'),
 (62,21,'change_student','Can change Sinh viên'),
 (63,21,'delete_student','Can delete Sinh viên'),
 (64,22,'add_lecturer','Can add Giảng viên'),
 (65,22,'change_lecturer','Can change Giảng viên'),
 (66,22,'delete_lecturer','Can delete Giảng viên'),
 (67,23,'add_library','Can add Thư viện'),
 (68,23,'change_library','Can change Thư viện'),
 (69,23,'delete_library','Can delete Thư viện'),
 (70,24,'add_learningresourcetype','Can add Loại học liệu'),
 (71,24,'change_learningresourcetype','Can change Loại học liệu'),
 (72,24,'delete_learningresourcetype','Can delete Loại học liệu'),
 (73,25,'add_publishing','Can add Nhà xuất bản'),
 (74,25,'change_publishing','Can change Nhà xuất bản'),
 (75,25,'delete_publishing','Can delete Nhà xuất bản'),
 (76,26,'add_learningresource','Can add Học liệu'),
 (77,26,'change_learningresource','Can change Học liệu'),
 (78,26,'delete_learningresource','Can delete Học liệu'),
 (79,27,'add_outline','Can add Đề cương'),
 (80,27,'change_outline','Can change Đề cương'),
 (81,27,'delete_outline','Can delete Đề cương'),
 (82,28,'add_outlinelearningresource','Can add Tài liệu cho môn học'),
 (83,28,'change_outlinelearningresource','Can change Tài liệu cho môn học'),
 (84,28,'delete_outlinelearningresource','Can delete Tài liệu cho môn học'),
 (85,29,'add_problem','Can add Vấn đề'),
 (86,29,'change_problem','Can change Vấn đề'),
 (87,29,'delete_problem','Can delete Vấn đề'),
 (88,30,'add_problemdetail','Can add Nội dung vấn đề'),
 (89,30,'change_problemdetail','Can change Nội dung vấn đề'),
 (90,30,'delete_problemdetail','Can delete Nội dung vấn đề'),
 (91,31,'add_targetawareness','Can add Mục tiêu nhận thức'),
 (92,31,'change_targetawareness','Can change Mục tiêu nhận thức'),
 (93,31,'delete_targetawareness','Can delete Mục tiêu nhận thức'),
 (94,32,'add_targetawarenessdetail','Can add target awareness detail'),
 (95,32,'change_targetawarenessdetail','Can change target awareness detail'),
 (96,32,'delete_targetawarenessdetail','Can delete target awareness detail'),
 (97,33,'add_advisorytime','Can add advisory time'),
 (98,33,'change_advisorytime','Can change advisory time'),
 (99,33,'delete_advisorytime','Can delete advisory time'),
 (100,34,'add_homeworkformat','Can add Định dạng bài tập'),
 (101,34,'change_homeworkformat','Can change Định dạng bài tập'),
 (102,34,'delete_homeworkformat','Can delete Định dạng bài tập'),
 (103,35,'add_homework','Can add Bài tập'),
 (104,35,'change_homework','Can change Bài tập'),
 (105,35,'delete_homework','Can delete Bài tập'),
 (112,38,'add_currentweek','Can add current week'),
 (113,38,'change_currentweek','Can change current week'),
 (114,38,'delete_currentweek','Can delete current week'),
 (121,41,'add_semester','Can add Học kỳ'),
 (122,41,'change_semester','Can change Học kỳ'),
 (123,41,'delete_semester','Can delete Học kỳ'),
 (124,42,'add_studysession','Can add Đợt học'),
 (125,42,'change_studysession','Can change Đợt học'),
 (126,42,'delete_studysession','Can delete Đợt học'),
 (127,43,'add_faculty','Can add Khoa'),
 (128,43,'change_faculty','Can change Khoa'),
 (129,43,'delete_faculty','Can delete Khoa');
CREATE TABLE `auth_group_permissions` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `group_id` integer NOT NULL REFERENCES `auth_group` (`id`), `permission_id` integer NOT NULL REFERENCES `auth_permission` (`id`), UNIQUE (`group_id`, `permission_id`));
CREATE TABLE `auth_group` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `name` varchar(80) NOT NULL UNIQUE);
CREATE TABLE `account_account` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `password` varchar(128) NOT NULL, `last_login` datetime NULL, `deleted_at` datetime NULL, `address_1` varchar(100) NOT NULL, `address_2` varchar(100) NOT NULL, `address_3` varchar(100) NOT NULL, `city` smallint NULL, `create_time` datetime NOT NULL, `update_time` datetime NULL, `email` varchar(255) NOT NULL UNIQUE, `login_type` smallint NOT NULL, `reset_pass_key` varchar(255) NULL, `reset_pass_expire` datetime NULL, `is_admin` bool NOT NULL, `is_active` bool NOT NULL, `is_block` bool NOT NULL, `block_expire` datetime NULL, `avarta_url_full` varchar(255) NOT NULL, `avarta_url` varchar(200) NOT NULL, `failure_count` smallint NOT NULL, `is_login_again_required` bool NOT NULL, `date_of_birth` date NULL, `family_name` varchar(255) NOT NULL, `name` varchar(255) NOT NULL, `description` varchar(255) NOT NULL, `creator_id` integer NULL REFERENCES `account_account` (`id`));
INSERT INTO `account_account` VALUES (1,'pbkdf2_sha256$24000$q67qYgArFdlT$KUVwJiLKtKa0tGpvoas7+aFovbpLBbHuyxMTM7j/ObA=','2016-10-29 14:16:47.013000',NULL,'','','',NULL,'2016-08-20 05:29:25.085721','2016-08-20 05:29:25.085760','luanhlu3503@gmail.com',0,NULL,NULL,1,1,0,NULL,'','',0,0,NULL,'','','',NULL),
 (2,'pbkdf2_sha256$20000$76fzs3cAKtBc$CBUsjYJl1wneDx4M/qoM3qWdhE3js3TGXPXhvAU5XJE=',NULL,NULL,'','','',23,'2016-08-29 10:34:19.399079','2016-08-29 10:34:19.399117','luanvuhlu@gmail.com',0,NULL,NULL,0,1,0,NULL,'','',0,0,'1992-12-30','Luân','Vũ','',1);
CREATE INDEX `university_university_3700153c` ON `university_university` (`creator_id`);
CREATE INDEX `university_uclass_ea134da7` ON `university_uclass` (`course_id`);
CREATE INDEX `university_uclass_3700153c` ON `university_uclass` (`creator_id`);
CREATE INDEX `university_subject_a9a5974d` ON `university_subject` (`specialized_study_id`);
CREATE INDEX `university_subject_3700153c` ON `university_subject` (`creator_id`);
CREATE INDEX `university_studysession_5d4db337` ON `university_studysession` (`semester_id`);
CREATE INDEX `university_studysession_3700153c` ON `university_studysession` (`creator_id`);
CREATE INDEX `university_student_d6eb0b12` ON `university_student` (`u_class_id`);
CREATE INDEX `university_student_8a089c2a` ON `university_student` (`account_id`);
CREATE INDEX `university_student_3700153c` ON `university_student` (`creator_id`);
CREATE INDEX `university_specializedstudy_890553cf` ON `university_specializedstudy` (`university_id`);
CREATE INDEX `university_specializedstudy_5bb92a88` ON `university_specializedstudy` (`faculty_id`);
CREATE INDEX `university_specializedstudy_3700153c` ON `university_specializedstudy` (`creator_id`);
CREATE INDEX `university_semester_f244b28d` ON `university_semester` (`scholastic_id`);
CREATE INDEX `university_semester_890553cf` ON `university_semester` (`university_id`);
CREATE INDEX `university_semester_3700153c` ON `university_semester` (`creator_id`);
CREATE INDEX `university_scholastic_3700153c` ON `university_scholastic` (`creator_id`);
CREATE INDEX `university_lecturer_8a089c2a` ON `university_lecturer` (`account_id`);
CREATE INDEX `university_lecturer_3700153c` ON `university_lecturer` (`creator_id`);
CREATE INDEX `university_faculty_890553cf` ON `university_faculty` (`university_id`);
CREATE INDEX `university_faculty_3700153c` ON `university_faculty` (`creator_id`);
CREATE INDEX `university_course_890553cf` ON `university_course` (`university_id`);
CREATE INDEX `university_course_3700153c` ON `university_course` (`creator_id`);
CREATE INDEX `softdelete_softdeleterecord_ea970247` ON `softdelete_softdeleterecord` (`changeset_id`);
CREATE INDEX `softdelete_softdeleterecord_417f1b1c` ON `softdelete_softdeleterecord` (`content_type_id`);
CREATE INDEX `softdelete_changeset_417f1b1c` ON `softdelete_changeset` (`content_type_id`);
CREATE INDEX `schedule_week_c9c749d1` ON `schedule_week` (`outline_id`);
CREATE INDEX `schedule_week_3700153c` ON `schedule_week` (`creator_id`);
CREATE INDEX `schedule_subjectschedule_c01e06f5` ON `schedule_subjectschedule` (`week_id`);
CREATE INDEX `schedule_subjectschedule_3700153c` ON `schedule_subjectschedule` (`creator_id`);
CREATE INDEX `schedule_studysession_5d4db337` ON `schedule_studysession` (`semester_id`);
CREATE INDEX `schedule_studysession_3700153c` ON `schedule_studysession` (`creator_id`);
CREATE INDEX `schedule_semester_f244b28d` ON `schedule_semester` (`scholastic_id`);
CREATE INDEX `schedule_semester_890553cf` ON `schedule_semester` (`university_id`);
CREATE INDEX `schedule_semester_3700153c` ON `schedule_semester` (`creator_id`);
CREATE INDEX `schedule_learningdayrequirement_95a5af44` ON `schedule_learningdayrequirement` (`day_id`);
CREATE INDEX `schedule_learningdayrequirement_3700153c` ON `schedule_learningdayrequirement` (`creator_id`);
CREATE INDEX `schedule_learningdaycontent_95a5af44` ON `schedule_learningdaycontent` (`day_id`);
CREATE INDEX `schedule_learningdaycontent_3700153c` ON `schedule_learningdaycontent` (`creator_id`);
CREATE INDEX `schedule_learningday_c01e06f5` ON `schedule_learningday` (`week_id`);
CREATE INDEX `schedule_learningday_3700153c` ON `schedule_learningday` (`creator_id`);
CREATE INDEX `schedule_homeworkaction_c01e06f5` ON `schedule_homeworkaction` (`week_id`);
CREATE INDEX `schedule_homeworkaction_495b1752` ON `schedule_homeworkaction` (`homework_id`);
CREATE INDEX `schedule_homeworkaction_3700153c` ON `schedule_homeworkaction` (`creator_id`);
CREATE INDEX `schedule_currentweek_5d4db337` ON `schedule_currentweek` (`semester_id`);
CREATE INDEX `schedule_currentweek_3700153c` ON `schedule_currentweek` (`creator_id`);
CREATE INDEX `outline_targetawarenessdetail_8a96b1e1` ON `outline_targetawarenessdetail` (`target_awareness_id`);
CREATE INDEX `outline_targetawarenessdetail_3700153c` ON `outline_targetawarenessdetail` (`creator_id`);
CREATE INDEX `outline_targetawareness_919b1d80` ON `outline_targetawareness` (`problem_id`);
CREATE INDEX `outline_targetawareness_5c046e10` ON `outline_targetawareness` (`problem_detail_id`);
CREATE INDEX `outline_targetawareness_3700153c` ON `outline_targetawareness` (`creator_id`);
CREATE INDEX `outline_problemdetail_919b1d80` ON `outline_problemdetail` (`problem_id`);
CREATE INDEX `outline_problemdetail_3700153c` ON `outline_problemdetail` (`creator_id`);
CREATE INDEX `outline_problem_c9c749d1` ON `outline_problem` (`outline_id`);
CREATE INDEX `outline_problem_3700153c` ON `outline_problem` (`creator_id`);
CREATE INDEX `outline_outlinelearningresource_c9c749d1` ON `outline_outlinelearningresource` (`outline_id`);
CREATE INDEX `outline_outlinelearningresource_3700153c` ON `outline_outlinelearningresource` (`creator_id`);
CREATE INDEX `outline_outlinelearningresource_1c117410` ON `outline_outlinelearningresource` (`learning_resource_id`);
CREATE INDEX `outline_outline_ffaba1d1` ON `outline_outline` (`subject_id`);
CREATE INDEX `outline_outline_ea134da7` ON `outline_outline` (`course_id`);
CREATE INDEX `outline_outline_9e860f67` ON `outline_outline` (`study_session_id`);
CREATE INDEX `outline_outline_3700153c` ON `outline_outline` (`creator_id`);
CREATE INDEX `outline_advisorytime_c9c749d1` ON `outline_advisorytime` (`outline_id`);
CREATE INDEX `outline_advisorytime_3700153c` ON `outline_advisorytime` (`creator_id`);
CREATE INDEX `library_publishing_3700153c` ON `library_publishing` (`creator_id`);
CREATE INDEX `library_library_890553cf` ON `library_library` (`university_id`);
CREATE INDEX `library_library_3700153c` ON `library_library` (`creator_id`);
CREATE INDEX `library_learningresourcetype_3700153c` ON `library_learningresourcetype` (`creator_id`);
CREATE INDEX `library_learningresource_cde18a14` ON `library_learningresource` (`resource_type_id`);
CREATE INDEX `library_learningresource_9cde0d35` ON `library_learningresource` (`library_id`);
CREATE INDEX `library_learningresource_3700153c` ON `library_learningresource` (`creator_id`);
CREATE INDEX `library_learningresource_0ac49fc5` ON `library_learningresource` (`publishing_id`);
CREATE INDEX `homework_homework_c9c749d1` ON `homework_homework` (`outline_id`);
CREATE INDEX `homework_homework_62921edb` ON `homework_homework` (`hw_format_id`);
CREATE INDEX `homework_homework_3700153c` ON `homework_homework` (`creator_id`);
CREATE INDEX `django_session_de54fa62` ON `django_session` (`expire_date`);
CREATE INDEX `django_admin_log_e8701ad4` ON `django_admin_log` (`user_id`);
CREATE INDEX `django_admin_log_417f1b1c` ON `django_admin_log` (`content_type_id`);
CREATE INDEX `auth_permission_417f1b1c` ON `auth_permission` (`content_type_id`);
CREATE INDEX `auth_group_permissions_8373b171` ON `auth_group_permissions` (`permission_id`);
CREATE INDEX `auth_group_permissions_0e939a4f` ON `auth_group_permissions` (`group_id`);
CREATE INDEX `account_account_3700153c` ON `account_account` (`creator_id`);
