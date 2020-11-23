CREATE TABLE IF NOT EXISTS job (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    salary NUMERIC(7,2) NOT NULL,
    vacation_days INT NOT NULL
);

CREATE TABLE IF NOT EXISTS department (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    title_abbreviation VARCHAR(50) NOT NULL
);


CREATE TABLE IF NOT EXISTS employee (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    patronumic VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    place_of_birth VARCHAR(50) NOT NULL,
    current_address VARCHAR(50) NOT NULL,
    department_id BIGINT REFERENCES department(id),
    job_id BIGINT REFERENCES job(id),
    start_at_the_job_possition DATE NOT NULL
);

ALTER TABLE department
ADD head_of_department_id BIGINT REFERENCES employee(id);

ALTER TABLE department
ADD CONSTRAINT head_of_department_unique UNIQUE (head_of_department_id);

CREATE TABLE IF NOT EXISTS employees_jobs (
    employee_id BIGINT REFERENCES employee(id),
    job_id BIGINT REFERENCES job(id)
);

CREATE TABLE IF NOT EXISTS employees_on_vacation(   
    employee_id BIGINT REFERENCES employee(id),
    starting_date DATE NOT NULL,
    ending_date DATE NOT NULL
);

CREATE OR REPLACE FUNCTION before_insert()
    RETURNS trigger AS
$$
DECLARE 
    departmentCount integer;
BEGIN
    SELECT INTO departmentCount COUNT(*) FROM employee WHERE department_id = NEW.department_id;
    IF departmentCount >= 20 THEN
        RETURN NULL;
    ELSE
        RETURN NEW;
    END IF;
END;
$$
LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION check_amount_of_emoloyees()
    RETURNS trigger AS 
$$
DECLARE
    employeeDepartment integer;
    employesCurrentlyInVacation integer;
BEGIN
    SELECT INTO employeeDepartment department_id FROM employee WHERE id = NEW.employee_id;
    SELECT INTO employesCurrentlyInVacation COUNT(*) FROM employee INNER JOIN employees_on_vacation ON employee.id = employees_on_vacation.employee_id WHERE employee.department_id = employeeDepartment AND starting_date BETWEEN starting_date AND ending_date;
    IF  employesCurrentlyInVacation >= 5 THEN
        RETURN NULL;
    ELSE
        RETURN NEW;
    END IF;
END;
$$  
LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION check_employee_department()
    RETURNS trigger AS
$$
DECLARE
    employeeDepartment integer;
    departmentID integer;
BEGIN
    SELECT INTO employeeDepartment department_id FROM employee WHERE id = NEW.head_of_department_id;
    SELECT INTO departmentID id FROM department WHERE id = OLD.id;
    RAISE NOTICE 'dep_id: %', departmentID;
    IF employeeDepartment = departmentID THEN
        RETURN NEW;
    ELSE
        RETURN NULL;
    END IF;
END;
$$
LANGUAGE 'plpgsql';

CREATE TRIGGER insert_into_employee BEFORE INSERT ON employee FOR EACH ROW EXECUTE PROCEDURE before_insert();
CREATE TRIGGER insert_into_vacation_table BEFORE INSERT ON employees_on_vacation FOR EACH ROW EXECUTE PROCEDURE check_amount_of_emoloyees();
CREATE TRIGGER update_head_of_department BEFORE UPDATE ON department FOR EACH ROW EXECUTE PROCEDURE check_employee_department();

-- SYSTEM REPORTS -- 

SELECT * FROM employee WHERE department_id = 1;

SELECT employee.first_name, employee.last_name, job.title, 1.2 * DATE_PART('years', AGE(NOW(),  employee.start_at_the_job_possition)) / 100 * job.salary + job.salary AS salary FROM employee INNER JOIN job ON employee.job_id = job.id;

SELECT employee.first_name, SUM(DATE_PART('day', employees_on_vacation.ending_date::timestamp - employees_on_vacation.starting_date::timestamp)) AS used_days FROM employee INNER JOIN employees_on_vacation ON employee.id = employees_on_vacation.employee_id GROUP BY first_name;

SELECT department.title, department.title_abbreviation, COUNT(employee.id) AS amount_of_employees 
FROM department 
RIGHT JOIN employee ON department.id = employee.department_id 
GROUP BY department.id;

SELECT  dep.title, dep.title_abbreviation, head_of_deparment.first_name || ' ' || head_of_deparment.last_name head_of_deparment, amount_of_employees
FROM (SELECT department.id, department.title, department.title_abbreviation, COUNT(employee.id) AS amount_of_employees FROM department RIGHT JOIN employee ON department.id = employee.department_id GROUP BY department.id) as dep
INNER JOIN (SELECT department.id, employee.first_name, employee.last_name FROM department INNER JOIN employee ON department.head_of_department_id = employee.id) as head_of_deparment
ON dep.id = head_of_deparment.id;
