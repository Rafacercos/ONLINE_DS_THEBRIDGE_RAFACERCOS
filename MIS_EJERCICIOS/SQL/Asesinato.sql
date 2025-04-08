select description
from crime_scene_report
where city = 'SQL City' and date = 20180115 and type = 'murder';
--Sospechosa 1
select id
from person 
where name like '%Annabel%' and address_street_name= 'Franklin Ave';
--sospechosa 2
select max(address_number),name,license_id,ssn
from person
where address_street_name like '%NorthWestern%';
--declaraciones de las sospechosas
select transcript 
from interview t1
inner join person t2 on t1.person_id= t2.id
where t2.name = 'Annabel Miller' or t2.name = 'Morty Schapiro';
--posibles avistados 
select t2.name
from drivers_license t1 
inner join person t2 on t1.id=t2.license_id
where plate_number like '%H42W%';
--Tercer sospechoso
select *
from get_fit_now_member
where name in ('Tushar Chandra','Jeremy Bowers','Maxine Whitely');
--Técnicamente este es el asesino
select transcript 
from interview t1
inner join person t2 on t1.person_id= t2.id
where t2.name = 'Jeremy Bowers';
--Buscando a la contratadora 
select height,gender,id,car_make
from drivers_license
where height BETWEEN 55 and 57 and hair_color='red' and gender='female';
--Posibles contratadoras 
select height,gender,t2.id,t2.name,car_make,car_model,t2.ssn
from drivers_license t1 
inner join person t2 on t1.id=t2.license_id
where car_make = 'Tesla' and gender ='female' and hair_color = 'red' and height BETWEEN 65 and 67 and car_model like '%model S%';
--descarto un ssn
select *
from income
where ssn in (961388910,337169072,987756388);
--contratadora
select name, ssn,id
from person t1
inner join facebook_event_checkin t2 on t1.id=t2.person_id
where ssn in (961388910,987756388) and event_name like '%SQL Symphony%';
select transcript 
from interview t1
inner join person t2 on t1.person_id= t2.id
where t2.name = 'Miranda Priestly';
--Asesina
insert into solution(user,value)
values (1,'Miranda Priestly');