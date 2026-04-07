		--TAREA 1
--CREATE TABLE users (
--    id SERIAL PRIMARY KEY,
--    name VARCHAR(255) NOT NULL,
--    email VARCHAR(255) NOT NULL UNIQUE,
--    username VARCHAR(255) NOT NULL UNIQUE,
--    password VARCHAR(255) NOT NULL,
--    birth_date DATE NOT NULL,
--    state_id INT NOT NULL REFERENCES user_states(id)
--);

--CREATE TABLE user_states (
--	id SERIAL PRIMARY KEY,
--	state VARCHAR (15)
--);

--CREATE TABLE model (
--	id SERIAL PRIMARY KEY,
--	model VARCHAR (15) NOT NULL,
--	model_year INT NOT NULL
--);

--CREATE TABLE make (
--	id SERIAL PRIMARY KEY,
--	make VARCHAR (30) NOT NULL
--);

--CREATE TABLE car_state (
--	id SERIAL PRIMARY KEY,
--	state VARCHAR (15) NOT NULL
--);

--CREATE TABLE car (
--	id SERIAL PRIMARY KEY,
--	make_id INT NOT NULL REFERENCES make (id),
--	model_id INT NOT NULL REFERENCES model (id),
--	state_id INT NOT NULL REFERENCES car_state (id)
--);


--CREATE TABLE rent_car (
--	id SERIAL PRIMARY KEY,
--	car_id INT NOT NULL REFERENCES car(id),
--	user_id INT NOT NULL REFERENCES users(id),
--	rent_date DATE,
--	rent_state_id INT REFERENCES rent_state(id)
--);

--CREATE TABLE rent_state (
--	id SERIAL PRIMARY KEY,
--	state VARCHAR (15)
--);


		--TAREA 2

		--2.a.
--INSERT INTO user_states (state)
--	VALUES('Unactive');
	

--INSERT INTO users (name, email, username, password, birth_date, state_id)
--	VALUES('Marvin Villalobos', 'marvinv@gmail.com', 'marvinvi', 'Marvin123', '11/19/1990', 4);

		--2.b
--INSERT INTO make (make)
--	VALUES ('Mitsubishi');

--INSERT INTO model (model, model_year)
--	VALUES ('Hilux', 2025);

--INSERT INTO car_state (state)
--	VALUES ('Unavailable');

--INSERT INTO car (make_id, model_id, state_id)
--	VALUES (2,7,1);

		--2.c
--UPDATE users SET
--state_id = 3
--WHERE name like 'Rufus%';


		--2.d

--UPDATE car SET
--state_id = 1
--FROM model
--WHERE car.model_id = model.id AND model.model_year >= 2020;

	

--SELECT car.id, make.make, model.model, model.model_year, car_state.state, car_state.id
--FROM car
--JOIN model ON car.model_id = model.id
--JOIN make ON car.make_id = make.id
--JOIN car_state ON car.state_id = car_state.id

		--2.e

--INSERT INTO rent_car (car_id, user_id, rent_date, rent_state_id)
--	VALUES (3,18,'18/11/2025',2);


		--2.f


		--2.g
--UPDATE car SET
--state_id = 2
--WHERE id = 10


		--2.h
	--Rented
--SELECT rent_car.id, users.name, make.make, model.model, rent_state.state
--FROM rent_car
--JOIN users ON rent_car.user_id = users.id
--JOIN car ON rent_car.car_id = car.id
--JOIN model ON car.model_id = model.id
--JOIN make ON car.make_id = make.id
--JOIN rent_state ON rent_car.rent_state_id = rent_state.id
--WHERE rent_car.rent_state_id = 2

	--Available
--SELECT rent_car.id, users.name, make.make, model.model, rent_state.state
--FROM rent_car
--JOIN users ON rent_car.user_id = users.id
--JOIN car ON rent_car.car_id = car.id
--JOIN model ON car.model_id = model.id
--JOIN make ON car.make_id = make.id
--JOIN rent_state ON rent_car.rent_state_id = rent_state.id
--WHERE rent_car.rent_state_id = 1




SELECT rent_car.id, users.name, make.make, model.model, rent_car.rent_date, rent_state.state
FROM rent_car
JOIN users ON rent_car.user_id = users.id
JOIN car ON rent_car.car_id = car.id
JOIN model ON car.model_id = model.id
JOIN make ON car.make_id = make.id
JOIN rent_state ON rent_car.rent_state_id = rent_state.id



SELECT *
FROM car


SELECT * 
FROM model

SELECT *
FROM make


SELECT *
FROM rent_state





