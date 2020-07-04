create database flask_college_proj;

use flask_college_proj;

create table students(
uname varchar(10) ,
pswd varchar(10) ,
sname varchar(20) ,
score integer ,
contact varchar(10) ,
primary key (uname) );

insert into students(uname ,pswd ,sname ,score ,contact) values ('1000000001','kt','krishna',65,'7981286619');

create table colleges(
cid varchar(5) ,
cname varchar(100) ,
location varchar(200) ,
website varchar(1000) ,
primary key (cid) );

insert into colleges(cid ,cname ,location ,website ) values ('20001','Amrita Vishwa Vidyapeetham','Coimbatore','https://www.amrita.edu/campus/coimbatore');

create table colleges(
cid varchar(5) ,
cname varchar(100) ,
location varchar(200) ,
website varchar(1000) ,
primary key (cid) );

insert into colleges(cid ,cname ,location ,website ) values ('20001','Amrita Vishwa Vidyapeetham','Coimbatore','https://www.amrita.edu/campus/coimbatore');


create table cutoff(
cid varchar(5) ,
bname varchar(100) ,
cyear integer ,
cutoff integer ,
num integer,
primary key (cid,bname,cyear,num) );

insert into cutoff(cid ,bname ,cyear ,cutoff,num ) values ('20001','CSE', 2019,70,1);
insert into cutoff(cid ,bname ,cyear ,cutoff,num ) values ('20001','CSE', 2020,75,1);

create table application(
cid varchar(5) ,
bname varchar(100) ,
uname varchar(10) ,
astatus varchar(10) ,
primary key (cid,bname,uname) );

insert into application(cid ,bname ,uname ,astatus ) values ('20001','CSE', '1000000001','pending');