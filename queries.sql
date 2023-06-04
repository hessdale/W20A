INSERT INTO client(username, password, joined_on) values
('dale1', 'password', '2021-01-01'),('dale2', 'password', '2022-02-02'),('dale3', 'password', '2022-03-02'),
('dale4', 'password', '2022-04-02'),('dale5', 'password', '2022-05-02'),('dale6', 'password', '2022-06-02');

INSERT INTO W20A.post (client_id, title, content) values
(1, 'title1', 'blah blah blah1'),(2, 'title2', 'blah blah blah2'),(3, 'title3', 'blah blah blah3'),
(4, 'title4', 'blah blah blah4'),(5, 'title5', 'blah blah blah5'),(6, 'title6', 'blah blah blah6'),
(1, 'title1', 'blah blah blah1'),(1, 'title', 'blah blah blah1'),(2, 'title2', 'blah blah blah2'),
(2, 'title2', 'blah blah blah2'),(3, 'title3', 'blah blah blah3'),(3, 'title3', 'blah blah blah3');

call get_user_id ('dale1','password');

select id from client where username='dale1' and password='password';

select p.title,p.content,c.username from post p inner join client c where p.client_id = c.id;
