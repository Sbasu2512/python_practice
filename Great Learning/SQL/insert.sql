create table regions(
region_id int auto_increment primary key ,
region_name varchar(256) not null
);

insert into regions(region_name) values('south');
insert into regions(region_name) values ('north');
insert into regions(region_name) values('east');
insert into regions(region_name) values('west');

select * from regions;

-- delete a specific value
delete from regions where region_id=5;

-- see what is inside a table
desc regions