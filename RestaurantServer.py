from http.server import HTTPServer, BaseHTTPRequestHandler
from restaurantDatabase import RestaurantDatabase
import cgi

class RestaurantPortalHandler(BaseHTTPRequestHandler):
    
    def __init__(self, *args):
        self.database = RestaurantDatabase()
        BaseHTTPRequestHandler.__init__(self, *args)
    
    def do_POST(self):
        try:
            if self.path == '/addReservation':
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                customer_id = int(form.getvalue("customer_id"))
                reservation_time = form.getvalue("reservation_time")
                number_of_guests = int(form.getvalue("number_of_guests"))
                special_requests = form.getvalue("special_requests")
                
                # Call the Database Method to add a new reservation
                self.database.addReservation(customer_id, reservation_time, number_of_guests, special_requests)
                print("Reservation added for customer ID:")
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title>Restaurant Portal</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Restaurant Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'> Home </a>| \
                                 <a href='/addReservation'> Add Reservation </a>|\
                                  <a href='/viewReservations'> View Reservations </a>|\
                                  <a href='/findReservations'> Find Reservations </a>|\
                                  <a href='/deleteReservation'> Delete Reservation </a>|\
                                  <a href='/updateSpecialRequest'> Update Special Request </a>|\
                                  <a href='/searchPreferences'> Search Preferences </a>|\
                                  <a href='/addCustomer'> Add Customer </a></div>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<h3>Reservation has been added</h3>")
                self.wfile.write(b"<div><a href='/addReservation'>Add Another Reservation</a></div>")
                self.wfile.write(b"</center></body></html>")


            if self.path == '/addCustomer':
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                customer_name = form.getvalue("customer_name")
                contact_info = form.getvalue("contact_info")
                
                # Call the Database Method to add a new reservation
                self.database.addCustomer(customer_name, contact_info)
                print("Customer Added Successfully")
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title>Restaurant Portal</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Restaurant Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'> Home </a>| \
                                 <a href='/addReservation'> Add Reservation </a>|\
                                  <a href='/viewReservations'> View Reservations </a>|\
                                  <a href='/findReservations'> Find Reservations </a>|\
                                  <a href='/deleteReservation'> Delete Reservation </a>|\
                                  <a href='/updateSpecialRequest'> Update Special Request </a>|\
                                  <a href='/searchPreferences'> Search Preferences </a>|\
                                  <a href='/addCustomer'> Add Customer </a></div>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<h3>Customer has been added</h3>")
                self.wfile.write(b"<div><a href='/addCustomer'>Add Another Customer</a></div>")
                self.wfile.write(b"</center></body></html>")

            if self.path == '/searchPreferences':
                form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST'}
                )

                customer_id = form.getvalue("customer_id")
                print("Searching preferences for customer ID:", customer_id)
            
                # Call the Database Method to search the customer preferences
                preferences = self.database.getCustomerPreferences(customer_id)
                print("Preferences retrieved:", preferences)

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                # HTML response for displaying preferences
                self.wfile.write(b"<html><head><title>Restaurant Portal</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Restaurant Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'> Home </a>| \
                              <a href='/addReservation'> Add Reservation </a>|\
                                  <a href='/viewReservations'> View Reservations </a>|\
                                  <a href='/findReservations'> Find Reservations </a>|\
                                  <a href='/deleteReservation'> Delete Reservation </a>|\
                                  <a href='/updateSpecialRequest'> Update Special Request </a>|\
                                  <a href='/searchPreferences'> Search Preferences </a>|\
                                  <a href='/addCustomer'> Add Customer </a></div>")
                self.wfile.write(b"<hr><h2>Customer Preferences</h2>")
                self.wfile.write(b"<table border=2> \
                                <tr><th> Customer ID </th>\
                                    <th> Favourite Table </th>\
                                    <th> Dietary Restrictions </th></tr>")

                for row in preferences:
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td></tr>')
            
                self.wfile.write(b"</table></center>")
                self.wfile.write(b"</body></html>")

            if self.path == '/findReservations':
                form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST'}
                )

                customer_id = form.getvalue("customer_id")
                print("Searching preferences for customer ID:", customer_id)
            
                # Call the Database Method to search the customer preferences
                reservations = self.database.getCustomerReservations(customer_id)
                print("Reservations retrieved:", reservations)

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                # HTML response for displaying preferences
                self.wfile.write(b"<html><head><title>Restaurant Portal</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Restaurant Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'> Home </a>| \
                                 <a href='/addReservation'> Add Reservation </a>|\
                                  <a href='/viewReservations'> View Reservations </a>|\
                                  <a href='/findReservations'> Find Reservations </a>|\
                                  <a href='/deleteReservation'> Delete Reservation </a>|\
                                  <a href='/updateSpecialRequest'> Update Special Request </a>|\
                                  <a href='/searchPreferences'> Search Preferences </a>|\
                                  <a href='/addCustomer'> Add Customer </a></div>")
                self.wfile.write(b"<hr><h2>Reservations</h2>")
                self.wfile.write(b"<table border=2> \
                                    <tr><th> Reservation ID </th>\
                                        <th> Customer ID </th>\
                                        <th> Reservation Time </th>\
                                        <th> Number of Guests </th>\
                                        <th> Special Requests </th></tr>")
                for row in reservations:
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[4]).encode())
                    self.wfile.write(b'</td></tr>')
                
                self.wfile.write(b"</table></center>")
                self.wfile.write(b"</body></html>")
            
            if self.path == '/deleteReservation':
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                reservation_id = form.getvalue("reservation_id")
                
                # Call the Database Method to delete reservation
                self.database.deleteReservation(reservation_id)
                print("Reservations removed Successfully")
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title>Restaurant Portal</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Restaurant Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'> Home </a>| \
                                 <a href='/addReservation'> Add Reservation </a>|\
                                  <a href='/viewReservations'> View Reservations </a>|\
                                  <a href='/findReservations'> Find Reservations </a>|\
                                  <a href='/deleteReservation'> Delete Reservation </a>|\
                                  <a href='/updateSpecialRequest'> Update Special Request </a>|\
                                  <a href='/searchPreferences'> Search Preferences </a>|\
                                  <a href='/addCustomer'> Add Customer </a></div>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<h3>Reservations removed Successfully</h3>")
                self.wfile.write(b"<div><a href='/deleteReservation'>Delete Another Reservation</a></div>")
                self.wfile.write(b"</center></body></html>")

            if self.path == '/updateSpecialRequest':
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                special_request = form.getvalue("special_request")
                reservation_id = form.getvalue("reservation_id")
                
                # Call the Database Method to add a new reservation
                self.database.updateSpecialRequest(special_request, reservation_id)
                print("Special Request Updated Successfully")
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title>Restaurant Portal</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Restaurant Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'> Home </a>| \
                                 <a href='/addReservation'> Add Reservation </a>|\
                                  <a href='/viewReservations'> View Reservations </a>|\
                                  <a href='/findReservations'> Find Reservations </a>|\
                                  <a href='/deleteReservation'> Delete Reservation </a>|\
                                  <a href='/updateSpecialRequest'> Update Special Request </a>|\
                                  <a href='/searchPreferences'> Search Preferences </a>|\
                                  <a href='/addCustomer'> Add Customer </a></div>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<h3>Special Request Updated Successfully</h3>")
                self.wfile.write(b"<div><a href='/updateSpecialRequest'>Update Another Request</a></div>")
                self.wfile.write(b"</center></body></html>")
                
        except Exception as e:
            self.send_error(500, f'Internal Server Error: {e}')

        return
    
    def do_GET(self):
        
        try:
            if self.path == '/':
                data = []
                records = self.database.getAllReservations()
                print(records)
                data = records
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title>Restaurant Portal</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Restaurant Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'> Home </a>| \
                                 <a href='/addReservation'> Add Reservation </a>|\
                                  <a href='/viewReservations'> View Reservations </a>|\
                                  <a href='/findReservations'> Find Reservations </a>|\
                                  <a href='/deleteReservation'> Delete Reservation </a>|\
                                  <a href='/updateSpecialRequest'> Update Special Request </a>|\
                                  <a href='/searchPreferences'> Search Preferences </a>|\
                                  <a href='/addCustomer'> Add Customer </a></div>")
                self.wfile.write(b"<hr><h2>All Reservations</h2>")
                self.wfile.write(b"<table border=2> \
                                    <tr><th> Reservation ID </th>\
                                        <th> Customer ID </th>\
                                        <th> Reservation Time </th>\
                                        <th> Number of Guests </th>\
                                        <th> Special Requests </th></tr>")
                for row in data:
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[4]).encode())
                    self.wfile.write(b'</td></tr>')
                
                self.wfile.write(b"</table></center>")
                self.wfile.write(b"</body></html>")
                return
            
            if self.path == '/addReservation':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title>Restaurant Portal</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Restaurant Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'> Home </a>| \
                                 <a href='/addReservation'> Add Reservation </a>|\
                                  <a href='/viewReservations'> View Reservations </a>|\
                                  <a href='/findReservations'> Find Reservations </a>|\
                                  <a href='/deleteReservation'> Delete Reservation </a>|\
                                  <a href='/updateSpecialRequest'> Update Special Request </a>|\
                                  <a href='/searchPreferences'> Search Preferences </a>|\
                                  <a href='/addCustomer'> Add Customer </a></div>")
                self.wfile.write(b"<html><head><title>Add Reservation</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Add Reservation</h1>")
                self.wfile.write(b"<form action='/addReservation' method='POST'>")
                self.wfile.write(b"<table>")
                self.wfile.write(b"<tr><td>Customer ID:</td><td><input type='text' name='customer_id'></td></tr>")
                self.wfile.write(b"<tr><td>Reservation Time:</td><td><input type='datetime-local' name='reservation_time'></td></tr>")
                self.wfile.write(b"<tr><td>Number of Guests:</td><td><input type='text' name='number_of_guests'></td></tr>")
                self.wfile.write(b"<tr><td>Special Requests:</td><td><input type='text' name='special_requests'></td></tr>")
                self.wfile.write(b"<tr><td colspan='2' style='text-align:center;'><input type='submit' value='Add Reservation'></td></tr>")
                self.wfile.write(b"</table>")
                self.wfile.write(b"</form>")
                self.wfile.write(b"</center></body></html>")

                return

            if self.path == '/viewReservations':
                data = []
                records = self.database.getAllReservations()
                print(records)
                data = records
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title>Restaurant Portal</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Restaurant Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'> Home </a>| \
                                 <a href='/addReservation'> Add Reservation </a>|\
                                  <a href='/viewReservations'> View Reservations </a>|\
                                  <a href='/findReservations'> Find Reservations </a>|\
                                  <a href='/deleteReservation'> Delete Reservation </a>|\
                                  <a href='/updateSpecialRequest'> Update Special Request </a>|\
                                  <a href='/searchPreferences'> Search Preferences </a>|\
                                  <a href='/addCustomer'> Add Customer </a></div>")
                self.wfile.write(b"<hr><h2>All Reservations</h2>")
                self.wfile.write(b"<table border=2> \
                                    <tr><th> Reservation ID </th>\
                                        <th> Customer ID </th>\
                                        <th> Reservation Time </th>\
                                        <th> Number of Guests </th>\
                                        <th> Special Requests </th></tr>")
                for row in data:
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[4]).encode())
                    self.wfile.write(b'</td></tr>')
                
                self.wfile.write(b"</table></center>")
                self.wfile.write(b"</body></html>")
                return

            if self.path == '/addCustomer':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title>Restaurant Portal</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Restaurant Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'> Home </a>| \
                                 <a href='/addReservation'> Add Reservation </a>|\
                                  <a href='/viewReservations'> View Reservations </a>|\
                                  <a href='/findReservations'> Find Reservations </a>|\
                                  <a href='/deleteReservation'> Delete Reservation </a>|\
                                  <a href='/updateSpecialRequest'> Update Special Request </a>|\
                                  <a href='/searchPreferences'> Search Preferences </a>|\
                                  <a href='/addCustomer'> Add Customer </a></div>")
                self.wfile.write(b"<html><head><title>Add Reservation</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Add Reservation</h1>")
                self.wfile.write(b"<form action='/addCustomer' method='POST'>")
                self.wfile.write(b"Customer Name: <input type='text' name='customer_name'><br>")
                self.wfile.write(b"Contact Info: <input type='text' name='contact_info'><br>")
                self.wfile.write(b"<input type='submit' value='Add Customer'>")
                self.wfile.write(b"</form>")
                self.wfile.write(b"</center></body></html>")
                return

            if self.path == '/searchPreferences':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title>Restaurant Portal</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Restaurant Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'> Home </a>| \
                                 <a href='/addReservation'> Add Reservation </a>|\
                                  <a href='/viewReservations'> View Reservations </a>|\
                                  <a href='/findReservations'> Find Reservations </a>|\
                                  <a href='/deleteReservation'> Delete Reservation </a>|\
                                  <a href='/updateSpecialRequest'> Update Special Request </a>|\
                                  <a href='/searchPreferences'> Search Preferences </a>|\
                                  <a href='/addCustomer'> Add Customer </a></div>")
                self.wfile.write(b"<html><head><title>Search Preferences</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Search Preferences</h1>")
                self.wfile.write(b"<form action='/searchPreferences' method='POST'>")
                self.wfile.write(b"<table>")
                self.wfile.write(b"<tr><td>Customer ID:</td><td><input type='text' name='customer_id'></td></tr>")
                self.wfile.write(b"<tr><td colspan='2' style='text-align:center;'><input type='submit' value='Search Preferences'></td></tr>")
                self.wfile.write(b"</table>")
                self.wfile.write(b"</form>")
                self.wfile.write(b"</center></body></html>")

                return

            if self.path == '/findReservations':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title>Restaurant Portal</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Restaurant Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'> Home </a>| \
                                 <a href='/addReservation'> Add Reservation </a>|\
                                  <a href='/viewReservations'> View Reservations </a>|\
                                  <a href='/findReservations'> Find Reservations </a>|\
                                  <a href='/deleteReservation'> Delete Reservation </a>|\
                                  <a href='/updateSpecialRequest'> Update Special Request </a>|\
                                  <a href='/searchPreferences'> Search Preferences </a>|\
                                  <a href='/addCustomer'> Add Customer </a></div>")
                self.wfile.write(b"<html><head><title>Search Preferences</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Find Reservations</h1>")
                self.wfile.write(b"<form action='/findReservations' method='POST'>")
                self.wfile.write(b"Customer ID: <input type='text' name='customer_id'><br>")
                self.wfile.write(b"<input type='submit' value='Find Reservations'>")
                self.wfile.write(b"</form>")
                self.wfile.write(b"</center></body></html>")
                return

            if self.path == '/deleteReservation':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title>Restaurant Portal</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Restaurant Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'> Home </a>| \
                                 <a href='/addReservation'> Add Reservation </a>|\
                                  <a href='/viewReservations'> View Reservations </a>|\
                                  <a href='/findReservations'> Find Reservations </a>|\
                                  <a href='/deleteReservation'> Delete Reservation </a>|\
                                  <a href='/updateSpecialRequest'> Update Special Request </a>|\
                                  <a href='/searchPreferences'> Search Preferences </a>|\
                                  <a href='/addCustomer'> Add Customer </a></div>")
                self.wfile.write(b"<html><head><title>Delete Reservation</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Delete Reservation</h1>")
                self.wfile.write(b"<form action='/deleteReservation' method='POST'>")
                self.wfile.write(b"<table>")
                self.wfile.write(b"<tr><td>Reservation ID:</td><td><input type='text' name='reservation_id'></td></tr>")
                self.wfile.write(b"<tr><td colspan='2' style='text-align:center;'><input type='submit' value='Delete Reservation'></td></tr>")
                self.wfile.write(b"</table>")
                self.wfile.write(b"</form>")
                self.wfile.write(b"</center></body></html>")

                return

            if self.path == '/updateSpecialRequest':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title>Restaurant Portal</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Restaurant Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'> Home </a>| \
                                 <a href='/addReservation'> Add Reservation </a>|\
                                  <a href='/viewReservations'> View Reservations </a>|\
                                  <a href='/findReservations'> Find Reservations </a>|\
                                  <a href='/deleteReservation'> Delete Reservation </a>|\
                                  <a href='/updateSpecialRequest'> Update Special Request </a>|\
                                  <a href='/searchPreferences'> Search Preferences </a>|\
                                  <a href='/addCustomer'> Add Customer </a></div>")
                self.wfile.write(b"<html><head><title>Update Special Request</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Update Special Request</h1>")
                self.wfile.write(b"<form action='/updateSpecialRequest' method='POST'>")
                self.wfile.write(b"<table>")
                self.wfile.write(b"<tr><td>Special Request:</td><td><input type='text' name='special_request'></td></tr>")
                self.wfile.write(b"<tr><td>Reservation ID:</td><td><input type='text' name='reservation_id'></td></tr>")
                self.wfile.write(b"<tr><td colspan='2' style='text-align:center;'><input type='submit' value='Update'></td></tr>")
                self.wfile.write(b"</table>")
                self.wfile.write(b"</form>")
                self.wfile.write(b"</center></body></html>")

                return
            
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

def run(server_class=HTTPServer, handler_class=RestaurantPortalHandler, port=8000):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port {}'.format(port))
    httpd.serve_forever()

run()

