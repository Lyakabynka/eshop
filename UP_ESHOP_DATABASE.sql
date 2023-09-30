--DROP DATABASE IF EXISTS ESHOP;

--CREATE DATABASE ESHOP;

-- Switch to the newly created database
USE ESHOP;

CREATE TABLE Roles(
	Id BIGINT PRIMARY KEY, --AUTO_INCREMENT,

	[Name] NVARCHAR(50),
);

CREATE TABLE Users (
    Id BIGINT PRIMARY KEY, --AUTO_INCREMENT,

    Username NVARCHAR(50) UNIQUE,
    PasswordHash NVARCHAR(MAX),

    RoleId BIGINT,

    FirstName NVARCHAR(50),
    LastName NVARCHAR(50),

    [Address] NVARCHAR(50),

    PhoneNumber NVARCHAR(50),
    Email NVARCHAR(50),

	FOREIGN KEY (RoleId) REFERENCES Roles(Id),
);

CREATE TABLE Categories (
    Id BIGINT PRIMARY KEY, --AUTO_INCREMENT,

    [Name] NVARCHAR(50)
);

CREATE TABLE Items (
    Id BIGINT PRIMARY KEY, --AUTO_INCREMENT,

	[Status] NVARCHAR(20),

    CategoryId BIGINT,
    DiscountId BIGINT NULL,

    [Type] NVARCHAR(50),
    Title NVARCHAR(50),
    [Description] NVARCHAR(1023),
	Quantity INT, --CHECK (Quantity > 0),

    Price FLOAT, --CHECK (Price > 0),

	--Every item has a Category
    FOREIGN KEY (CategoryId) REFERENCES Categories(Id) ON DELETE SET NULL,
);

CREATE TABLE Owns (
	UserId BIGINT,
	ItemId BIGINT UNIQUE,

	FOREIGN KEY (UserId) REFERENCES Users(Id) ON DELETE CASCADE,
	FOREIGN KEY (ItemId) REFERENCES Items(Id) ON DELETE CASCADE,
);

CREATE TABLE Discounts (
    Id BIGINT PRIMARY KEY, --AUTO_INCREMENT,

    ItemId BIGINT,
    [Percentage] INT, --CHECK ([Percentage] >= 0 AND [Percentage] <= 0),

    UserId BIGINT,

	--Discount has specific User (seller, whose item the discount is placed on)
    FOREIGN KEY (UserId) REFERENCES Users(Id),
	--Discount has specific Item
	FOREIGN KEY (ItemId) REFERENCES Items(Id)
);

CREATE TABLE UserItems (
    Id BIGINT PRIMARY KEY, --AUTO_INCREMENT,

    UserId BIGINT,
    ItemId BIGINT,

	--ItemInBucket has specific User (who put it into a bucket i.e. buyer)
    FOREIGN KEY (UserId) REFERENCES Users(Id) ON DELETE CASCADE,
	--ItemInBucket has specific Item (item that is put into a bucket)
    FOREIGN KEY (ItemId) REFERENCES Items(Id) ON DELETE CASCADE,
);

CREATE TABLE WishedUserItems (
	Id BIGINT PRIMARY KEY, --AUTO_INCREMENT,

	UserId BIGINT,
	ItemId BIGINT,

	FOREIGN KEY (UserId) REFERENCES Users(Id) ON DELETE CASCADE,
	FOREIGN KEY (ItemId) REFERENCES Items(Id) ON DELETE CASCADE
)

CREATE TABLE Orders (
    Id BIGINT PRIMARY KEY, --AUTO_INCREMENT,

    Price FLOAT, --CHECK ([Price]>0]
    OrderedAt TIMESTAMP,
    [Type] NVARCHAR(50),

	--One-to-one with DeliveryData
    DeliveryDataId BIGINT,
);

CREATE TABLE Ordered(
	UserId BIGINT,
	OrderId BIGINT UNIQUE,

	FOREIGN KEY (UserId) REFERENCES Users(Id) ON DELETE CASCADE,
	FOREIGN KEY (OrderId) REFERENCES Orders(Id) ON DELETE CASCADE,
)

CREATE TABLE DeliveryDatas (
    Id BIGINT PRIMARY KEY, --AUTO_INCREMENT,

    [Address] NVARCHAR(50),
    [Type] NVARCHAR(50),

    OrderId BIGINT,
    UserId BIGINT,

	--DeliveryData has specific Order
    FOREIGN KEY (OrderId) REFERENCES Orders(Id) ON DELETE CASCADE,
	--DeliveryData has specific User
    FOREIGN KEY (UserId) REFERENCES Users(Id) ON DELETE CASCADE,
);

CREATE TABLE OrderItems (
    Id BIGINT PRIMARY KEY, --AUTO_INCREMENT,

    OrderId BIGINT,
    ItemId BIGINT,

    -- Many-to-many with Items and Orders
    FOREIGN KEY (OrderId) REFERENCES Orders(Id) ON DELETE CASCADE,
    FOREIGN KEY (ItemId) REFERENCES Items(Id), -- If item is deleted, it should not be deleted from OrderItems ( for user to look at his previous orders )
);