## file name: restaurantDatabase.py
from sqlite3 import connect
import mysql.connector
from mysql.connector import Error

class RestaurantDatabase():
    def __init__(self,
                 host="localhost",
                 port="3306",
                 database="restaurant_reservations",
                 user='root',
                 password='admin'):

        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password)
            
            if self.connection.is_connected():
                print("Successfully connected to the database")
                return
        except Error as e:
            print("Error while connecting to MySQL", e)
        

    def addReservation(self, customer_id, reservation_time, number_of_guests, special_requests):
        ''' Method to insert a new reservation into the reservations table '''
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "INSERT INTO reservations (customerId, reservationTime, numberOfGuests, specialRequests) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (customer_id, reservation_time, number_of_guests, special_requests))
            self.connection.commit()
            print("Reservation added successfully")
            return

    def getAllReservations(self):
        ''' Method to get all reservations from the reservations table '''
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "SELECT * FROM reservations"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records

    def addCustomer(self, customer_name, contact_info):
        ''' Method to add a new customer to the customers table '''
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "INSERT INTO customers (customerName, contactInfo) VALUES (%s, %s)"
            self.cursor.execute(query, (customer_name, contact_info))
            self.connection.commit()
            print("Customer added successfully")
            return

    def getCustomerPreferences(self, customer_id):
        ''' Method to retrieve dining preferences for a specific customer '''
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "SELECT * FROM diningPreferences WHERE customerId = %s"
            self.cursor.execute(query, (customer_id,))
            preferences = self.cursor.fetchall()
            return preferences

    def getCustomerReservations(self, customer_id):
        ''' Method to retrieve reservations from the reservations table for specific customer '''
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "SELECT * FROM reservations WHERE customerId = %s"
            self.cursor.execute(query, (customer_id,))
            preferences = self.cursor.fetchall()
            return preferences
    
    def deleteReservation(self, reservation_id):
        ''' Method to Delete reservations from the reservations table for specific customer '''
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "DELETE FROM reservations WHERE reservationId = %s"
            self.cursor.execute(query, (reservation_id,))
            self.connection.commit()
            print("Reservation removed successfully")
            return

    def updateSpecialRequest(self, special_request, reservation_id):
        ''' Method to Update special request from the reservations table using reservation id '''
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "UPDATE reservations SET specialRequests = %s WHERE reservationId = %s"
            self.cursor.execute(query, (special_request, reservation_id,))
            self.connection.commit()
            print("Special request updated successfully")
            return



    # Add more methods as needed for restaurant operations

