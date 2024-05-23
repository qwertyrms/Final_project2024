
Project Description:
Finalize the web platform for Restaurant Managers to manage reservation schedules and dining experiences. 
•	You are given a started code in Python with a platform that runs on a Python HTTP Server. Your task will be to connect to the MySQL server and complete the Database class so that the platform functions smoothly.
•	Once complete, the Restaurant Managers will be able to access the platform to add, modify, or cancel reservations, as well as update dining preferences for regular customers. 
•	Create a Report explaining the code. 
•	Upload your source code (public), with the report in PDF to GitHub, and submit the link to Blackboard.
•	Make a presentation in person. 
Guidelines: 
Link to starter code: [https://github.com/synac1/CIS344/tree/main/Spring-2024
](https://github.com/synac1/CIS344/tree/main/spring2024) You can download the files. 
•	The platform must handle checking whether a customer already exists in the Customers table before making a reservation. If not, the customer should be added.
•	A new customer can be added either through a direct addition to the Customers table or during the reservation process if they do not already exist.
•	Integration of customer data across the platform enhances the ability to track and manage customer interactions comprehensively, from reservations to dining preferences.

MySQL to-do list (40 points):
1.	(5 points) Create a database named restaurant_reservations.
2.	Use the previously created database.
MySQL Tables and Relationships
1.	Customers Table(5 points):
o	customerId INT NOT NULL UNIQUE AUTO_INCREMENT
o	customerName VARCHAR(45) NOT NULL
o	contactInfo VARCHAR(200) // Stores email or phone number
Primary Key: customerId
2.	Reservations Table(5 points):
o	reservationId INT NOT NULL UNIQUE AUTO_INCREMENT
o	customerId INT NOT NULL
o	reservationTime DATETIME NOT NULL
o	numberOfGuests INT NOT NULL
o	specialRequests VARCHAR(200)
Primary Key: reservationId
Foreign Key: customerId references Customers(customerId)
3.	DiningPreferences Table(5 points):
o	preferenceId INT NOT NULL UNIQUE AUTO_INCREMENT
o	customerId INT NOT NULL
o	favoriteTable VARCHAR(45)
o	dietaryRestrictions VARCHAR(200)
Primary Key: preferenceId
Foreign Key: customerId references Customers(customerId)
MySQL Procedures and Modifications
1.	Stored Procedures and Relationships:
o	findReservations(customerId) (5 points): Retrieves all reservations for a specific customer using the customerId.
o	addSpecialRequest(reservationId, requests) (5 points): Updates the specialRequests field in the reservations table.
o	addReservation(5 points): Now includes a check or creation of a customer in the Customers table before adding a reservation.
Populate the tables with at least three tuples per table. (5 points).
Python MySQL (30 Points) + Extra (20 points):
1.	Open the restaurantDatabase.py file in your editor and change the default parameter values to match your MySQL server information in the constructor.
2.	Run restaurantServer.py on your machine. if you completed all the MySQL instructions from part 1. When you go to the browser and type: localhost:8000/ you will be able to see this: If you accomplish running and getting results, that’s 10 points.
3.	Go back to your source code file restaurantDatabase.py and go to method addReservation(self, customerName, reservationTime, numberOfGuests, specialRequests), complete the method so it successfully insert a new Reservation to the database table. 
a.	Please follow the documentation on the official mysql website: https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html
b.	Using Connector/Python Verify that it worked by checking the web platform table home link: localhost:8000/ in your browser. Make sure to re-run after every modification to the files. If it worked correctly that is (20 points)
4.	bonus: if you complete the addSpecialRequest(), findReservations(), deleteReservation(), searchPreferences() methods in restaurantDatabase.py (8 points)
5.	bonus: if you implement the bonus methods with restaurantServer.py (8 points each).
6.	bonus: if you complete and implement the viewAllReservations() method (4 points). 
Publishing (15 points)
3.	Write a report explaining the code and showing how it works.
4.	Upload your source code and SQL script file with MySQL queries to GitHub in a public repository. (5 points)
5.	Provide the links to your repository in the report. Put the extra screenshots in the appendix.
6.	The report is worth (10 points) Submit the report in PDF to the blackboard. 
7.	Presentation In Person (15 points). Present your work on the date of the presentation in person.

