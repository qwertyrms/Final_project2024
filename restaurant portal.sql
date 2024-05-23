Create database restaurant_reservations;
USE restaurant_reservations;

CREATE TABLE Customers (
    customerId INT NOT NULL AUTO_INCREMENT,
    customerName VARCHAR(45) NOT NULL,
    contactInfo VARCHAR(200),
    PRIMARY KEY (customerId)
);

INSERT INTO Customers (customerId, customerName) VALUES
(1, 'Remon'),
(2, 'Yanilda'),
(3, 'Lehman');

-- Create Reservations table
CREATE TABLE Reservations (
    reservationId INT NOT NULL AUTO_INCREMENT,
    customerId INT NOT NULL,
    reservationTime DATETIME NOT NULL,
    numberOfGuests INT NOT NULL,
    specialRequests VARCHAR(200),
    PRIMARY KEY (reservationId),
    FOREIGN KEY (customerId) REFERENCES Customers(customerId)
);

-- Insert data into Reservations table
INSERT INTO Reservations (reservationId, customerId, reservationTime, numberOfGuests, specialRequests) VALUES
(1, 1, '2024-05-20 18:30:00', 2, 'Peanut allergy'),
(2, 2, '2024-05-21 19:00:00', 4, 'Window seat'),
(3, 3, '2024-05-22 20:00:00', 3, 'Birthday/Anniversary');

-- Create DiningPreferences table
CREATE TABLE DiningPreferences (
    preferenceId INT NOT NULL AUTO_INCREMENT,
    customerId INT NOT NULL,
    favoriteTable VARCHAR(45),
    dietaryRestrictions VARCHAR(200),
    PRIMARY KEY (preferenceId),
    FOREIGN KEY (customerId) REFERENCES Customers(customerId)
);

-- Select statement to get reservations for a specific customer
SELECT *
FROM Reservations
WHERE customerId = 1;  -- Example customerId

-- Create procedure to find reservations
DELIMITER //
CREATE PROCEDURE findReservations(IN customerId INT)
BEGIN
    SELECT *
    FROM Reservations
    WHERE customerId = customerId;
END //
DELIMITER ;

-- Call the findReservations procedure
CALL findReservations(1);

-- Update statement to modify a reservation
UPDATE Reservations
SET specialRequests = 'Increase spice level'
WHERE reservationId = 1;

-- Create procedure to add a reservation
DELIMITER $$

CREATE PROCEDURE addReservation(
    IN p_customerId INT,
    IN p_name VARCHAR(255),
    IN p_contact_info VARCHAR(200),
    IN p_reservation_time DATETIME,
    IN p_number_of_guests INT,
    IN p_special_requests VARCHAR(200)
)
BEGIN
    -- Check if the customer exists
    DECLARE customer_exists INT;
    SET customer_exists = (SELECT COUNT(*) FROM Customers WHERE customerId = p_customerId);

    -- If the customer does not exist, insert the customer
    IF customer_exists = 0 THEN
        INSERT INTO Customers (customerName, contactInfo)
        VALUES (p_name, p_contact_info);
        -- Set the new customerId to the last inserted id
        SET p_customerId = LAST_INSERT_ID();
    END IF;

    -- Add the reservation
    INSERT INTO Reservations (customerId, reservationTime, numberOfGuests, specialRequests)
    VALUES (p_customerId, p_reservation_time, p_number_of_guests, p_special_requests);
END$$

DELIMITER ;

-- Call the addReservation procedure
CALL addReservation(1, 'Remon', 'remon.sabuz@lc.cuny.edu', '2024-05-23 18:00:00', 2, 'Vegetarian meal');