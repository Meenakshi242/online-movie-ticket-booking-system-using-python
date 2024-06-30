import mysql.connector
import random
import datetime
import smtplib

gst_rate=5

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="project_2"
)
mycursor = mydb.cursor()

def email_sending(receiver_email, charges_with_gst, movies, hall,time, date, name, seat_num):
    try:  
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("meena2003dummy@gmail.com", "ozpv uoyu ltco sjjd")
        message = (f"Subject: Booking Confirmation\n\n")
        message +=(f"Thank you for booking with 5-STAR TICKET BOOKING SYSTEM.\n\n")
        message += (f"Movie Name: {movies}\n")
        message += (f"Name: {', '.join(name)}\n")
        message += (f"Hall: {hall}\n")
        message += (f"Time: {time}\n")
        message += (f"Date: {date}\n")
        message += (f"Charges (including GST): Rs {charges_with_gst}\n")
        message += (f"Seat Numbers: {seat_num}\n")
        s.sendmail("meena2003dummy@gmail.com", receiver_email, message)
        s.quit()
        print(f"Email sent successfully to {receiver_email}\n")
    except: 
        print("mail not send\n")

def main():
    print("\n**********WELCOME TO 5-STAR TICKET BOOKING SYSTEM**********\n")

    user = input("Do you have an account? (yes/no): ").lower()
    email = ""

    try:
        if user == "yes" or user=="y":
            email = input("Enter your email id: ")
            password = input("Enter your password: ")
            print(".....login successfully.....\n")
        else:
            name = input("Enter your full name: ")
            phone = int(input("Enter your phone number: "))
            city = input("Enter your city name: ")
            state = input("Enter your state: ")
            email = input("Enter your email id: ")
            password = input("Enter your password: ")
            print(".....Your account is created successfully.....\n")
    except ValueError:
        print("Invalid input")

    print("\n*****THESE ARE THE LATEST MOVIES*****\n")
    query1 = "select movies from movies"
    mycursor.execute(query1)
    for movie in mycursor.fetchall():
        print(movie)

    name = []
    movies = input("Which movie do you want to watch: ")
    ticket = int(input("Enter the number of tickets you want: "))
    print(f"{ticket} tickets booked for {movies}.\n")
    for i in range(ticket):
        name.append(input("Enter name: "))

    try:
        query_details = "select hall, date, time, charges from movies where movies = %s"
        mycursor.execute(query_details, (movies,))
        result = mycursor.fetchone()

        hall = result[0]
        date = result[1]
        time = result[2]
        charge_per_ticket = result[3]

        charges_before_gst = charge_per_ticket * ticket
        gst_amount = charges_before_gst * (gst_rate/100)
        charges_with_gst = charges_before_gst + gst_amount

        seatnum = random.randint(1, 100)

        print(f"You have to pay {charges_with_gst} Rs.\n")
        pay = input("To confirm payment, enter 'pay': ")
        if pay.lower()=="pay":
            print("payment confirmed\n")

        print("\n***Your ticket generated in bill.txt***\n")
            
        sql="insert into Booking_Details(name,movies,hall,time,date,charges_with_gst,seat_num) values (%s,%s,%s,%s,%s,%s,%s)"
        if ticket==1:
            values=(','.join(name),movies,hall,time,date,charges_with_gst,f"Seat number: {seatnum}")
        else:
            values=(','.join(name),movies,hall,time,date,charges_with_gst,f"Seat number: {seatnum} to {seatnum + (ticket - 1)}")
        mycursor.execute(sql,values)
        mydb.commit()
        print("data saved successfully\n")

        f=open("bill.txt", "a") 
        x = datetime.datetime.now()
        present_day = x.strftime("%A")
        current_month = x.strftime("%B")
        
        f.write("  \n")
        f.write("\nBILL DETAILS:\n")
        f.write(f"Date: {x}\n")
        f.write(f"Day: {present_day}\n")
        f.write(f"Month: {current_month}\n")
        f.write("  \n")
        f.write(f"Names: {', '.join(name)}\n")
        f.write(f"Movie name: {movies}\n")
        f.write(f"Hall: {hall}\n")
        f.write(f"Time: {time}\n")
        f.write(f"Date: {date}\n")
        f.write(f"Charges: {charges_with_gst}\n")
        if ticket==1:
            f.write(f"Seat number: {seatnum}\n")
        else:
            f.write(f"Seat number: {seatnum} to {seatnum + (ticket - 1)}\n\n")
        f.write("****************************")
        
        if ticket==1:
            email_sending(email, charges_with_gst, movies, hall, time, date, name,f"Seat number: {seatnum}")
        else:
            email_sending(email, charges_with_gst, movies, hall, time, date, name,f"Seat number: {seatnum} to {seatnum + (ticket - 1)}")

    except mysql.connector.errors:
        print("error occured or error performing database")
    except ValueError:
        print("value error..Type numbers only")  

    print("Bill print successfully via email\n")  
main()