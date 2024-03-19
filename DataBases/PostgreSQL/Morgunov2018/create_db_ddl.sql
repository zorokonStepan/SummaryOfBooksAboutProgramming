CREATE TABLE aircrafts
( aircraft_code char( 3 ) NOT NULL,
model text NOT NULL,
range integer NOT NULL,
CHECK ( range > 0 ),
PRIMARY KEY ( aircraft_code )
);

CREATE TABLE seats
(
aircraft_code char( 3 ) NOT NULL,
seat_no varchar( 4 ) NOT NULL,
fare_conditions varchar( 10 ) NOT NULL,
CHECK
( fare_conditions IN ( 'Economy', 'Comfort', 'Business' )
),
PRIMARY KEY ( aircraft_code, seat_no ),
FOREIGN KEY ( aircraft_code )
REFERENCES aircrafts (aircraft_code )
ON DELETE CASCADE
);

CREATE TABLE airports
( airport_code char( 3 ) NOT NULL, -- Код аэропорта
airport_name text NOT NULL, -- Название аэропорта
city text NOT NULL, -- Город
longitude float NOT NULL, -- Координаты аэропорта: долгота
latitude float NOT NULL, -- Координаты аэропорта: широта
timezone text NOT NULL, -- Часовой пояс аэропорта
PRIMARY KEY ( airport_code )
);

CREATE TABLE flights
( flight_id serial NOT NULL, -- Идентификатор рейса
flight_no char( 6 ) NOT NULL, -- Номер рейса
scheduled_departure timestamptz NOT NULL, -- Время вылета по расписанию
scheduled_arrival timestamptz NOT NULL, -- Время прилета по расписанию
departure_airport char( 3 ) NOT NULL, -- Аэропорт отправления
arrival_airport char( 3 ) NOT NULL, -- Аэропорт прибытия
status varchar( 20 ) NOT NULL, -- Статус рейса
aircraft_code char( 3 ) NOT NULL, -- Код самолета, IATA
actual_departure timestamptz, -- Фактическое время вылета
actual_arrival timestamptz, -- Фактическое время прилета
CHECK ( scheduled_arrival > scheduled_departure ),
CHECK ( status IN ( 'On Time', 'Delayed', 'Departed',
'Arrived', 'Scheduled', 'Cancelled' )
),
CHECK ( actual_arrival IS NULL OR
( actual_departure IS NOT NULL AND
actual_arrival IS NOT NULL AND
actual_arrival > actual_departure
)
),
PRIMARY KEY ( flight_id ),
UNIQUE ( flight_no, scheduled_departure ),
FOREIGN KEY ( aircraft_code )
REFERENCES aircrafts ( aircraft_code ),
FOREIGN KEY ( arrival_airport )
REFERENCES airports ( airport_code ),
FOREIGN KEY ( departure_airport )
REFERENCES airports ( airport_code )
);

CREATE TABLE bookings
( book_ref char( 6 ) NOT NULL, -- Номер бронирования
book_date timestamptz NOT NULL, -- Дата бронирования
total_amount numeric( 10, 2 ) NOT NULL, -- Полная стоимость бронирования
PRIMARY KEY ( book_ref )
);

CREATE TABLE tickets
( ticket_no char( 13 ) NOT NULL, -- Номер билета
book_ref char( 6 ) NOT NULL, -- Номер бронирования
passenger_id varchar( 20 ) NOT NULL, -- Идентификатор пассажира
passenger_name text NOT NULL, -- Имя пассажира
contact_data jsonb, -- Контактные данные пассажира
PRIMARY KEY ( ticket_no ),
FOREIGN KEY ( book_ref )
REFERENCES bookings ( book_ref )
);

CREATE TABLE ticket_flights
( ticket_no char( 13 ) NOT NULL, -- Номер билета
flight_id integer NOT NULL, -- Идентификатор рейса
fare_conditions varchar( 10 ) NOT NULL, -- Класс обслуживания
amount numeric( 10, 2 ) NOT NULL, -- Стоимость перелета
CHECK ( amount >= 0 ),
CHECK ( fare_conditions IN ( 'Economy', 'Comfort', 'Business' ) ),
PRIMARY KEY ( ticket_no, flight_id ),
FOREIGN KEY ( flight_id )
REFERENCES flights ( flight_id ),
FOREIGN KEY ( ticket_no )
REFERENCES tickets ( ticket_no )
);

CREATE TABLE boarding_passes
( ticket_no char( 13 ) NOT NULL, -- Номер билета
flight_id integer NOT NULL, -- Идентификатор рейса
boarding_no integer NOT NULL, -- Номер посадочного талона
seat_no varchar( 4 ) NOT NULL, -- Номер места
PRIMARY KEY ( ticket_no, flight_id ),
UNIQUE ( flight_id, boarding_no ),
UNIQUE ( flight_id, seat_no ),
FOREIGN KEY ( ticket_no, flight_id )
REFERENCES ticket_flights ( ticket_no, flight_id )
);