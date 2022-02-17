
select distinct employee.eid, employee.ename, employee.esal, address_details.address from employee join address_details where employee.eid = address_details.eid;


use bank;

create table employee(eid int,
 ename varchar(255),
 esal float,
 primary key(eid));
 
 create table address_details(address varchar(255),
 eid int,
 foreign key(eid) references employee(eid));