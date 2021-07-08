use master
--drop database GameSales
go
--create database GameSales
go
use GameSales
go


--create Rank dim
create table RankDim(
	RankID int not null primary key identity,
	Value int not null,
)
go
create table DateDim(
	DateID int not null primary key identity,
	Year int not null,
	Month int not null check ( Month between 1 and 12 )
)
go

create table GenreDim(
	GenreID int not null primary key identity,
	UniqueID int,
	NameGenre nvarchar(255) not null,
	Description nvarchar(255) not null,
	valid_from datetime,
	valid_to datetime
)
go

create table PresidentDim(
	PresidentID int not null primary key identity,
	UniqueID int,
	Name nvarchar(255) not null,
	SecondName nvarchar(255) not null,
	Birthday date,
	Sex varchar(1) check (Sex in ('f','m')),
	valid_from datetime,
	valid_to datetime
)
go

create table PublisherDim(
	PublisherID int not null primary key identity,
	UniqueID int,
	PublisherName nvarchar(255) not null,
	FoundationDate date,
	OfficeCountry nvarchar(255) not null,
	PresidentID int foreign key references PresidentDim(PresidentID),
	valid_from datetime,
	valid_to datetime
)

create table PlatformDim(
	PlatformID int not null primary key identity,
	UniqueID int,
	NamePlatform nvarchar(255) not null,
	Model nvarchar(255),
	valid_from datetime,
	valid_to datetime
)
create table FactTable(
	ID int not null primary key identity,
	RankID int foreign key references RankDim(RankID),
	GameName nvarchar(255) not null,
	PlatformID int foreign key references PlatformDim(PlatformID),
	DateID int foreign key references DateDim(DateID),
	GenreID int foreign key references GenreDim(GenreID),
	PublisherID int foreign key references PublisherDim(PublisherID),
	NA_Sales int,
	EU_Sales int,
	JP_Sales int,
	Other_Sales int,
	Global_Sales int,
)


--drop database GameSales
select * from PresidentDim
select * from PublisherDim
--insert into PresidentDim ( Birthday, Name, SecondName) values ('1978/02/04','q','w')

select PublisherName,Name,SecondName from PublisherDim pu join PresidentDim pr on pu.PresidentID=pr.PresidentID

select * from PlatformDim
select * from RankDim
select * from GenreDim
select * from DateDim
select * from FactTable

--					UPDATE GenreDim 
--					set valid_to = NULL
--					WHERE NameGenre = 'Action' and valid_to is not NULL;

--delete from GenreDim where valid_from is not null 