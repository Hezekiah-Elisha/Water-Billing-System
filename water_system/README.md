# Water System

## Description
This is a water billing system for a water company. It is a web application that allows the company to manage its customers and their water bills. The system also allows the customers to view their water bills and pay them online.

## Features
- Admin can create, read, update and delete customers
- Admin can create, read, update and delete water bills
- Customers can view their water bills
- Customers can pay their water bills online

## Technologies
- Python 3.11.5
- Flask 2.0.2
- Flask-sqlalchemy 2.5.2
- Flask-migrate 3.1.0
- flask Marshmallow 0.15.1
- Flask Cors 3.0.10
- Flask JWT Extended 4.3.1

## Setup

export the environment variables
```bash
export FLASK_APP=water_systemy.py
export FLASK_config=development
export FLASK_DEBUG=1
```

initiate the database with flask migrate

```bash
flask db init
flask db migrate
flask db upgrade
```

all these can be found at the file

```bash
./run_app.sh
```

Then each time the database models change repeat the `migrate` and `upgrade` commands.

for help:

```bash
flask db --help
```

## Purpose of this side

This is a backend of the system

## routes

### User Authentication and Authorization:

+ `/api/auth/register` - Register a new user (field worker, supervisor, or customer).
+ `/api/auth/login` - Authenticate and log in a user.
+ `/api/auth/logout` - Log out the authenticated user.
+ `/api/auth/reset` -password - Initiate a password reset process.
+ `/api/auth/verify-email` - Verify a user's email address after registration.
+ `/api/user/profile` - Retrieve and update user profiles.

### Meter Reading:

+ `/api/meter-reading` - Submit a new meter reading for a customer.
+ `/api/meter-reading/{id}` - Retrieve, update, or delete a specific meter reading.
+ `/api/meter-reading/customer/{customer_id}` - Retrieve all meter readings for a specific customer.
+ `/api/meter-reading/worker/{worker_id}` - Retrieve all meter readings assigned to a field worker.
+ `/api/meter-reading/unprocessed` - Retrieve unprocessed meter readings.

### Billing:

+ `/api/billing` - Generate a new bill for a customer.
+ `/api/billing/{id}` - Retrieve, update, or delete a specific bill.
+ `/api/billing/customer/{customer_id}` - Retrieve all bills for a specific customer.
+ `/api/billing/worker/{worker_id}` - Retrieve bills assigned to a field worker.
+ `/api/billing/unpaid` - Retrieve unpaid bills.
+ `/api/billing/pay` - Process a payment for a bill.

### Notifications:

+ `/api/notifications` - Send notifications to users (e.g., payment reminders, system updates).
+ `/api/notifications/{id}` - Retrieve or mark notifications as read.

### Dashboard and Reporting:

+ `/api/dashboard` - Retrieve summary data for supervisors and administrators.
+ `/api/reporting` - Generate reports on meter readings, billing, and water consumption.

### Settings and Configuration:

+ `/api/settings` - Manage system settings and configuration options.

### Security and Compliance:

+ `/api/security/audit-logs` - Retrieve audit logs for security and compliance purposes.

### Miscellaneous:

+ `/api/search` - Implement a search endpoint for various entities (e.g., customers, workers, bills).
+ `/api/version` - Retrieve the API version and status information.

