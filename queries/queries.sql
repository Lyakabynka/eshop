INSERT INTO Roles(Name)
VALUES
    ('Buyer'),
    ('Seller'),
    ('Admin');

INSERT INTO Users(Username, PasswordHash, RoleId, FirstName, LastName, Address, PhoneNumber,Email)
VALUES
    ('Dima', 'AID*!#IORNF!EUPRHJ#!U$PXYU!#OJ$X!#*(X$!#)', 3, 'Dmytro', 'Murza', 'College Ring 3', '+38011111111', 'dima17741@gmail.com'),
    ('Dima1', 'AID*!#IORNF!EUPRHJ#!U$PXYU!#OJ$X!#*(X$!#)1', 1, 'Dmytro1', 'Murza1', 'College Ring 31', '+380111111111', 'dima17741@gmail.com1'),
    ('Dima2', 'AID*!#IORNF!EUPRHJ#!U$PXYU!#OJ$X!#*(X$!#)2', 3, 'Dmytro2', 'Murza2', 'College Ring 32', '+380111111112', 'dima17741@gmail.com2'),
    ('Dima3', 'AID*!#IORNF!EUPRHJ#!U$PXYU!#OJ$X!#*(X$!#)3', 1, 'Dmytro3', 'Murza3', 'College Ring 33', '+380111111113', 'dima17741@gmail.com3'),
    ('Dima4', 'AID*!#IORNF!EUPRHJ#!U$PXYU!#OJ$X!#*(X$!#)4', 1, 'Dmytro4', 'Murza4', 'College Ring 34', '+380111111114', 'dima17741@gmail.com4'),
    ('Dima5', 'AID*!#IORNF!EUPRHJ#!U$PXYU!#OJ$X!#*(X$!#)5', 1, 'Dmytro5', 'Murza5', 'College Ring 35', '+380111111115', 'dima17741@gmail.com5');

INSERT INTO Orders(Price, OrderedAt, Type, DeliveryDataId)
VALUES(1050, CURRENT_TIMESTAMP, 'Completed', 1),
    (10000, CURRENT_TIMESTAMP, 'Active', 2),
    (1070, CURRENT_TIMESTAMP, 'Physical', 3),
    (1500, CURRENT_TIMESTAMP, 'Active', 4),
    (1090, CURRENT_TIMESTAMP, 'Active', 5),
    (15000, CURRENT_TIMESTAMP, 'Physical', 6);

INSERT INTO Ordered(UserId, OrderId)
VALUES
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6);

INSERT INTO DeliveryDatas(Address, Type, OrderId, UserId)
VALUES('College Ring 3', 'Standart', 1, 1),
    ('College Ring 31', 'Standart', 2, 2),
    ('College Ring 32', 'Express', 3, 3),
    ('College Ring 33', 'Express', 4, 4),
    ('College Ring 34', 'Express', 5, 5),
    ('College Ring 35', 'Standart', 6, 6);



-- Select people with top 3 highest price orders
SELECT Users.Id,
    Users.Username,
    Users.FirstName,
    Users.LastName, 
    Users.Address, 
    Users.PhoneNumber,
    Users. Email, 
    Orders.Id, 
    Orders.Price
FROM Users
JOIN Ordered ON Ordered.UserId = Users.Id
JOIN Orders ON Orders.Id = Ordered.OrderId
ORDER BY Orders.Price DESC
LIMIT 3;

INSERT INTO WishedUserItems(UserId, ItemId)
VALUES(1,5),
    (1,5),
    (2,7),
    (2,6),
    (4,8),
    (4,5);

INSERT INTO Categories(Name)
VALUES('Clothes'),
    ('Devices'),
    ('Furniture');

INSERT INTO Items(Status, CategoryId, DiscountId, Type, Title, Description, Quantity, Price)
VALUES ('Available', 1, 2, 'Physical', 'Jacket', '123123', 12, 100),
    ('Available', 2, 1, 'Physical', 'Headphones', '123123', 3, 85),
    ('Available', 3, 3, 'Physical', 'Office table', '123123', 2, 50),
    ('Available', 3, 4, 'Physical', 'Office chair', '123123', 2, 20);

--input values into the table 
INSERT INTO Discounts(ItemId, Percentage, UserId)
VALUES
    (5,25,1),
    (6,27,2),
    (7,25,3),
    (8,10,4);


--Select the cheapest item and the user himself from the wishlist of each user.
SELECT I.Id as ItemId, U.Id as UserId, I.Price AS MinPrice
FROM Items I
JOIN WishedUserItems WUI ON I.Id = WUI.ItemId
JOIN Users U ON U.Id = WUI.UserId
WHERE I.Price = (
    SELECT MIN(Imin.Price)
    FROM Items Imin
    WHERE Imin.Id = WUI.ItemId AND U.Id = WUI.UserId
)
ORDER BY U.Id

--Select categories which have more than one item in them.
SELECT C.Id, C.Name
FROM Categories C, Items I
WHERE I.CategoryId = C.Id
GROUP BY C.Id
HAVING COUNT(*) > 1

--Select an average price of items in the cart of each user that has more than one item there
SELECT U.Id, I.Id, AVG(I.Price) AS avgprice
FROM Items I, UserItems UI, Users U
WHERE U.Id = UI.UserId AND I.Id = UI.ItemId
GROUP BY U.Id
HAVING COUNT(*) > 1

--Select all administrators
SELECT Users.Id, Users.Username, Users.FirstName, Users.LastName
FROM Users
JOIN Roles ON Roles.Id = Users.RoleId
WHERE Roles.Name = 'Admin';

--Select all current undelivered orders of specific user
SELECT Orders.Id, Orders.OrderedAt, Orders.Type
FROM Orders
JOIN Ordered ON Ordered.OrderId = Orders.Id
JOIN Users ON Users.Id = Ordered.UserId
WHERE Orders.Type = 'Active' AND Users.Id = 2;

--Select all users, who at least once
-- bought something with Express delivery
SELECT DISTINCT Users.Id, Users.Username
FROM Users
JOIN DeliveryDatas ON DeliveryDatas.UserId = Users.Id
WHERE DeliveryDatas.Type = 'Express';

--Select all users from Ukraine,
SELECT Users.Username, Users.FirstName, Users.LastName
FROM Users
WHERE PhoneNumber LIKE '+380%';

--Select all sellers who bought something
SELECT Users.Username
FROM Users
JOIN Roles ON Roles.Id = Users.RoleId
WHERE Roles.Name = 'Seller' AND 
    EXISTS (
        SELECT 1
        FROM Orders
        JOIN Ordered ON Ordered.OrderId = Orders.Id
        WHERE Ordered.UserId == Users.Id
    );

--Get the first 10 most expensive items with discounts
SELECT D.Id, ItemId, Percentage, UserId
FROM Discounts D
LEFT JOIN Items I ON D.Id = I.DiscountId
ORDER BY I.Price
LIMIT 10

--number of items with discounts
SELECT COUNT(I.Id)
FROM Disounts D
JOIN Items I ON I.DiscountId = D.Id

--List 10 items with discount more than 70%
SELECT I.Id, I.Status, I.Title, I.Description
FROM Items I
JOIN Discounts D ON I.DiscountId = Discounts.Id
WHERE D.Percentage > 70
ORDER BY I.Price
LIMIT 10
