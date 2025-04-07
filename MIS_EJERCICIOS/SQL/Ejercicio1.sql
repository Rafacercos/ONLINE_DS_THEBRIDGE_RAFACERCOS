--Ejercicio 11
select billingcountry,COUNT(invoiceid) as Nfacturas
from invoices
group by billingcountry
order by 2 desc;
--Ejercicio 12 
select count(invoiceDate)
from invoices 
where invoiceDate like ('%2009%') or invoiceDate like ('%2011%');
--Ejercicio 13
select count(invoicedate)
from invoices
where invoicedate BETWEEN '2008-12-31' and '2011-12-31';
--Ejercicio 14
select count(country)
from customers
where country in ('Brazil','Spain');
-- Ejercicio 15
select Name 
from tracks
where name like 'You%';
--Ejercicio 1 Parte 2 
select billingcountry,invoiceid,Invoicedate,customers.FirstName|| ' '||lastname as Fullname
from invoices 
inner join customers on customers.CustomerId = invoices.CustomerId
where billingcountry = 'Brazil';
--Ejercicio 2 parte 2
select employees.firstname||'  '||employees.lastname as fullname,employees.title,invoices.invoiceid
from employees
inner join customers on customers.SupportRepId = employees.EmployeeId
inner join invoices on invoices.CustomerId =  customers.CustomerId 
where title = 'Sales Support Agent';
--Ejercicio 3 Parte 2
select 
customers.firstname||' '||customers.lastname as fullname,
customers.country,
invoices.total,
employees.FirstName|| ' '||employees.LastName as employeename
from customers
inner join invoices on invoices.CustomerId = customers.CustomerId
inner join employees on employees.EmployeeId= customers.SupportRepId;
--Ejercicio 4 parte 2
select 
invoices.invoiceid,
tracks.Name,
invoice_items.InvoiceLineId
from invoices
inner join invoice_items on invoices.InvoiceId= invoice_items.InvoiceId
inner join tracks on invoice_items.TrackId = tracks.TrackId
order by 1 asc;
-- Ejer 5 parte 2
select 
tracks.Name As cancion,
albums.Title as album,
genres.Name as genero,
media_types.Name as formato
from tracks
inner join albums on albums.AlbumId = tracks.AlbumId
inner join genres on genres.GenreId = tracks.GenreId
inner join media_types on media_types.MediaTypeId = tracks.MediaTypeId;
--Ejercicio 6 Parte 2 
SELECT 
playlists.Name,
count(playlist_track.TrackId) as Ncanciones
from playlists
inner join playlist_track on playlist_track.PlaylistId = playlists.PlaylistId
group by 1;
--Ejercicio 7 Parte 2 
select employees.FirstName|| ' ' ||employees.Lastname as fullname,
count(invoice_items.TrackId)
from employees
inner join customers on employees.EmployeeId = customers.SupportRepId
inner join invoices on customers.CustomerId = invoices.CustomerId
inner join invoice_items on invoices.InvoiceId = invoice_items.InvoiceId
group by 1;
--Ejercicio 8 Parte 2 
select employees.FirstName|| ' '|| employees.Lastname as fullname,
count(invoices.Total)
from employees
inner join customers on customers.SupportRepId = employees.EmployeeId
inner join invoices on customers.CustomerId = invoices.CustomerId
inner join invoice_items on invoice_items.InvoiceId=invoices.InvoiceId
where invoices.InvoiceDate like '2009%'
group by 1
order by 2 desc;
