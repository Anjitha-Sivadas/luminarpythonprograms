#store data in the form of tables
# show databases;--querry for database list
# create database python feb;
# use pythonfeb;

# employees--table name
# eid, ename salary desig
# create table employee(eid int,ename varchar(50),desig varchar(50),salary int);
# show tables;
# desc employee;--to show field
# insert into employee(eid.ename desig, salary) values(100,'varun','developer',25000);
# insert into employee(eid.ename desig, salary) values(100,'anju','ssytem engineer',28000);
# insert into employee(eid.ename desig, salary) values(100,'vinod','analyst',30000);
# select * from employee;
#primary key--key used to identify uniquely (unique identify field)
#foreign key--refrential purpose
# alter table employee add coloumn location varchar(25);
# desc employee;

# create table location(id int, loca_name varchar(50));
# insert into location(id,loca_name) values(1,'ekm');
# select * from location;
# select * from emloyee;
# update employee set location='1' where eid=100;
# update employee set location='2' where eid=101;
# select * from employee;
