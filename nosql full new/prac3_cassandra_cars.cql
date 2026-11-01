-- PRACTICAL 3 - Cassandra car database (run inside cqlsh)
-- Code is unchanged. Lines starting with -- are expected output (safe to paste).

CREATE KEYSPACE car_db
WITH replication = {
  'class': 'SimpleStrategy',
  'replication_factor': 1
};

-- Output: (no output, returns to cqlsh> prompt)

USE car_db;

-- Output: prompt changes to  cqlsh:car_db>

DESCRIBE KEYSPACE car_db;

-- Output:
-- CREATE KEYSPACE car_db WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'} AND durable_writes = true;


CREATE TABLE cars (
  car_id int PRIMARY KEY,
  manufacturer text,
  type text,
  max_performance int,
  max_torque int
);

DESCRIBE TABLE cars;

-- Output:
-- CREATE TABLE car_db.cars (
--     car_id int PRIMARY KEY,
--     manufacturer text,
--     max_performance int,
--     max_torque int,
--     type text
-- ) WITH ... (default table options)


INSERT INTO cars (car_id, manufacturer, type, max_performance, max_torque)
VALUES (101, 'Toyota', 'Sedan', 203, 243);

INSERT INTO cars (car_id, manufacturer, type, max_performance, max_torque)
VALUES (102, 'BMW', 'Sedan', 255, 400);

INSERT INTO cars (car_id, manufacturer, type, max_performance, max_torque)
VALUES (103, 'Audi', 'SUV', 261, 370);

INSERT INTO cars (car_id, manufacturer, type, max_performance, max_torque)
VALUES (104, 'Mercedes', 'Sedan', 255, 400);

INSERT INTO cars (car_id, manufacturer, type, max_performance, max_torque)
VALUES (105, 'Ford', 'SUV', 250, 380);

-- Output: (no output for each INSERT)


SELECT * FROM cars;

-- Output (row order may differ):
--  car_id | manufacturer | max_performance | max_torque | type
-- --------+--------------+-----------------+------------+-------
--     101 |       Toyota |             203 |        243 | Sedan
--     102 |          BMW |             255 |        400 | Sedan
--     103 |         Audi |             261 |        370 |   SUV
--     104 |     Mercedes |             255 |        400 | Sedan
--     105 |         Ford |             250 |        380 |   SUV
--
-- (5 rows)


-- Consistency levels

CONSISTENCY;

-- Output: Current consistency level is ONE.

CONSISTENCY ONE;

-- Output: Consistency level set to ONE.

SELECT * FROM cars;

-- Output: same 5 rows

CONSISTENCY QUORUM;

-- Output: Consistency level set to QUORUM.

SELECT * FROM cars;

-- Output: same 5 rows (on one node QUORUM needs just that node)

CONSISTENCY ALL;

-- Output: Consistency level set to ALL.

SELECT * FROM cars;

-- Output: same 5 rows (on one node ALL needs just that node)

CONSISTENCY ONE;

-- Output: Consistency level set to ONE.


-- Replication: run ONLY on a 3-node cluster (new keyspace, replication factor 3)

-- CREATE KEYSPACE car_db3 WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 3};

-- USE car_db3;

-- CREATE TABLE cars (car_id int PRIMARY KEY, manufacturer text, type text, max_performance int, max_torque int);

-- INSERT INTO cars (car_id, manufacturer, type, max_performance, max_torque) VALUES (101, 'Toyota', 'Sedan', 203, 243);

-- SELECT * FROM cars;
