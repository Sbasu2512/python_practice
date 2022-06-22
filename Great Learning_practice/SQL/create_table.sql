-- DDL statements -> Data Definition Language

create database hr;
use hr;

create table jobs(
job_id int auto_increment primary key,
job_title varchar(256) not null,
min_salary decimal(10,2) default null,
max_salary decimal(10,2) default null
);

create table regions(
region_id int auto_increment primary key ,
region_name varchar(256) not null
);

create table countries(
country_id int primary key,
country_name varchar(20) default null,
region_id int not null,
foreign key (region_id) references regions (region_id)
);

create table locations(
location_id int primary key,
street_address varchar(256),
postal_code varchar(20),
city varchar(200),
state_province varchar(200),
country_id int,
foreign key (country_id) references countries(country_id)
);

drop table regions;