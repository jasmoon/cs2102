-- User account (all account password is 1234)
INSERT INTO user_account (email, password, last_login, date_created)
VALUES ('dillon_dudley@test.com', 'pbkdf2:sha256:50000$GsvMXVYh$98eb332735af00dc5fb6246303d3562c0cd714c3085fb9b603b0b9e766e9b5b4', now(), now());
VALUES ('lydia_jimenez@test.com', 'pbkdf2:sha256:50000$GsvMXVYh$98eb332735af00dc5fb6246303d3562c0cd714c3085fb9b603b0b9e766e9b5b4', now(), now());
VALUES ('colt_anderson@test.com', 'pbkdf2:sha256:50000$GsvMXVYh$98eb332735af00dc5fb6246303d3562c0cd714c3085fb9b603b0b9e766e9b5b4', now(), now());
VALUES ('dawn_everett@test.com', 'pbkdf2:sha256:50000$GsvMXVYh$98eb332735af00dc5fb6246303d3562c0cd714c3085fb9b603b0b9e766e9b5b4', now(), now());
VALUES ('ryder_mendez@test.com', 'pbkdf2:sha256:50000$GsvMXVYh$98eb332735af00dc5fb6246303d3562c0cd714c3085fb9b603b0b9e766e9b5b4', now(), now());
VALUES ('tatiana_moses@test.com', 'pbkdf2:sha256:50000$GsvMXVYh$98eb332735af00dc5fb6246303d3562c0cd714c3085fb9b603b0b9e766e9b5b4', now(), now());
VALUES ('joel_combs@test.com', 'pbkdf2:sha256:50000$GsvMXVYh$98eb332735af00dc5fb6246303d3562c0cd714c3085fb9b603b0b9e766e9b5b4', now(), now());
VALUES ('freya_marks@test.com', 'pbkdf2:sha256:50000$GsvMXVYh$98eb332735af00dc5fb6246303d3562c0cd714c3085fb9b603b0b9e766e9b5b4', now(), now());
VALUES ('buckminster_fitzgerald@test.com', 'pbkdf2:sha256:50000$GsvMXVYh$98eb332735af00dc5fb6246303d3562c0cd714c3085fb9b603b0b9e766e9b5b4', now(), now());
VALUES ('fletcher_myers@test.com', 'pbkdf2:sha256:50000$GsvMXVYh$98eb332735af00dc5fb6246303d3562c0cd714c3085fb9b603b0b9e766e9b5b4', now(), now());
VALUES ('ima_cherry@test.com', 'pbkdf2:sha256:50000$GsvMXVYh$98eb332735af00dc5fb6246303d3562c0cd714c3085fb9b603b0b9e766e9b5b4', now(), now());
VALUES ('buckminster_whitfield@test.com', 'pbkdf2:sha256:50000$GsvMXVYh$98eb332735af00dc5fb6246303d3562c0cd714c3085fb9b603b0b9e766e9b5b4', now(), now());
VALUES ('jordan_short@test.com', 'pbkdf2:sha256:50000$GsvMXVYh$98eb332735af00dc5fb6246303d3562c0cd714c3085fb9b603b0b9e766e9b5b4', now(), now());
VALUES ('kadeem_shanton@test.com', 'pbkdf2:sha256:50000$GsvMXVYh$98eb332735af00dc5fb6246303d3562c0cd714c3085fb9b603b0b9e766e9b5b4', now(), now());
VALUES ('mark_nixon@test.com', 'pbkdf2:sha256:50000$GsvMXVYh$98eb332735af00dc5fb6246303d3562c0cd714c3085fb9b603b0b9e766e9b5b4', now(), now());
VALUES ('jolie_sheppard@test.com', 'pbkdf2:sha256:50000$GsvMXVYh$98eb332735af00dc5fb6246303d3562c0cd714c3085fb9b603b0b9e766e9b5b4', now(), now());
VALUES ('shelly_hopkins@test.com', 'pbkdf2:sha256:50000$GsvMXVYh$98eb332735af00dc5fb6246303d3562c0cd714c3085fb9b603b0b9e766e9b5b4', now(), now());
VALUES ('channing_grimes@test.com', 'pbkdf2:sha256:50000$GsvMXVYh$98eb332735af00dc5fb6246303d3562c0cd714c3085fb9b603b0b9e766e9b5b4', now(), now());
VALUES ('rina_mckenzie@test.com', 'pbkdf2:sha256:50000$GsvMXVYh$98eb332735af00dc5fb6246303d3562c0cd714c3085fb9b603b0b9e766e9b5b4', now(), now());
VALUES ('september_cohen@test.com', 'pbkdf2:sha256:50000$GsvMXVYh$98eb332735af00dc5fb6246303d3562c0cd714c3085fb9b603b0b9e766e9b5b4', now(), now());

-- User Profile
INSERT INTO "user_profile" (id, first_name, last_name, address1, address2, postal_code, phone_number, profile_image, description,credit_card)
VALUES (1,'Dillon','Dudley','Ap #630-1388 In Street','Bafra','26189','(829) 298-0021', 'https://randomuser.me/api/portraits/women/7.jpg', 'risus. Donec egestas. Duis ac arcu. Nunc mauris. Morbi non sapien molestie orci tincidunt','525385 9724873767')
,(2,'Lydia','Jimenez','2617 Vitae Av.','Sorbo Serpico','8318 PK','(114) 389-1040', 'https://randomuser.me/api/portraits/men/43.jpg', 'nonummy ipsum non arcu. Vivamus sit amet risus. Donec egestas. Aliquam nec enim. Nunc ut','5297 3808 9761 4472')
,(3,'Colt','Anderson','276-5818 Turpis Street','Tintange','53984','(161) 138-5905', 'https://randomuser.me/api/portraits/men/28.jpg', 'lectus quis massa. Mauris vestibulum, neque sed dictum eleifend, nunc risus varius orci, in','5133451220635308')
,(4,'Dawn','Everett','6571 Mauris. St.','Cheyenne','05603','(651) 862-2459', 'https://randomuser.me/api/portraits/women/84.jpg', 'elit pede, malesuada vel, venenatis vel, faucibus id, libero. Donec consectetuer mauris','512937 691898 5358')
,(5,'Ryder','Mendez','731-7648 Nec, Avenue','Gubbio','793085','(993) 887-3113', 'https://randomuser.me/api/portraits/men/48.jpg', 'lorem ut aliquam iaculis, lacus pede sagittis augue, eu tempor erat neque non quam. Pellentesque','5247596307403468')
,(6,'Tatiana','Moses','P.O. Box 587, 6826 Nibh. Av.','Bearberry','1726','(611) 670-4920', 'https://randomuser.me/api/portraits/men/24.jpg', 'ultrices posuere cubilia Curae; Phasellus ornare. Fusce mollis. Duis sit amet diam eu dolor egestas','526608 208002 4637')
,(7,'Joel','Combs','176-4951 Magnis Rd.','Saint-Martin','R57 6AX','(952) 235-8947', 'https://randomuser.me/api/portraits/men/47.jpg', 'Fusce aliquam, enim nec tempus scelerisque, lorem ipsum sodales purus, in molestie tortor nibh sit amet orci. Ut sagittis','5104621899610122')
,(8,'Freya','Marks','8422 Eu St.','Frutillar','40914','(433) 445-2959', 'https://randomuser.me/api/portraits/men/50.jpg','ipsum. Curabitur consequat, lectus sit amet luctus vulputate, nisi sem semper erat, in consectetuer ipsum nunc id enim.','5333386898100847')
,(9,'Buckminster','Fitzgerald','2657 Elementum St.','Introd','525814','(791) 903-9868', 'https://randomuser.me/api/portraits/women/2.jpg','ut, molestie in, tempus eu, ligula. Aenean euismod mauris eu elit. Nulla facilisi. Sed','5569292442374323')

,(10,'Fletcher','Myers','P.O. Box 173, 3519 Eros. Street','Carbonear','XG7 7FI','(958) 843-6998', 'https://randomuser.me/api/portraits/women/9.jpg','luctus. Curabitur egestas nunc sed libero. Proin sed turpis nec mauris blandit mattis. Cras eget nisi dictum','536245 313390 5978')
,(11,'Ima','Cherry','500-882 Nascetur Rd.','Winnipeg','21503','(452) 441-5164', 'https://randomuser.me/api/portraits/men/5.jpg', 'mi lorem, vehicula et, rutrum eu, ultrices sit amet, risus. Donec','5136477096049073')
,(12,'Buckminster','Whitfield','621-9427 Vitae Road','Tay','34-301','(251) 745-4480', 'https://randomuser.me/api/portraits/men/42.jpg', 'scelerisque, lorem ipsum sodales purus, in molestie tortor nibh sit amet orci.','530984 592912 4621')
,(13,'Jordan','Short','Ap #455-1274 Est, Rd.','Oelegem','49408','(107) 174-6947', 'https://randomuser.me/api/portraits/men/89.jpg','metus vitae velit egestas lacinia. Sed congue, elit sed consequat','523180 2951209211')
,(14,'Kadeem','Stanton','3177 Dignissim Ave','Contulmo','1094 OB','(374) 746-8373', 'https://randomuser.me/api/portraits/men/97.jpg', 'eget metus. In nec orci. Donec nibh. Quisque nonummy ipsum non','5325 4040 5997 8602')
,(15,'Mark','Nixon','5633 Commodo Street','Ravels','49156','(519) 687-8278', 'https://randomuser.me/api/portraits/women/30.jpg', 'gravida non, sollicitudin a, malesuada id, erat. Etiam vestibulum massa rutrum magna. Cras convallis convallis dolor. Quisque tincidunt','512 70097 18918 137')
,(16,'Jolie','Sheppard','Ap #256-9164 Augue St.','Coleville Lake','289127','(323) 867-4383', 'https://randomuser.me/api/portraits/women/1.jpg', 'vulputate velit eu sem. Pellentesque ut ipsum ac mi eleifend egestas. Sed pharetra, felis eget varius ultrices, mauris','5129318554918277')
,(17,'Shelly','Hopkins','Ap #837-3393 Orci Rd.','Bridge of Allan','C3T 5L4','(536) 169-8747', 'https://randomuser.me/api/portraits/men/99.jpg', 'varius. Nam porttitor scelerisque neque. Nullam nisl. Maecenas malesuada fringilla est. Mauris eu turpis. Nulla aliquet.','512382 168044 3785')
,(18,'Channing','Grimes','960-7027 Et St.','Langen','54703','(613) 748-5131', 'https://randomuser.me/api/portraits/women/18.jpg', 'massa. Quisque porttitor eros nec tellus. Nunc lectus pede, ultrices a, auctor non, feugiat nec,','5452 0703 2938 0146')
,(19,'Rina','Mckenzie','P.O. Box 736, 6481 Mollis. Street','Toernich','4088','(726) 685-7944', 'https://randomuser.me/api/portraits/women/31.jpg', 'vel, mauris. Integer sem elit, pharetra ut, pharetra sed, hendrerit a, arcu. Sed et libero. Proin mi. Aliquam','519130 6988744479')
,(20,'September','Cohen','P.O. Box 507, 2335 Adipiscing Street','Bavikhove','39616','(153) 718-4987', 'https://randomuser.me/api/portraits/men/2.jpg', 'sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Proin vel nisl. Quisque fringilla','558125 313839 3286');

-- Campaigns

