# 916 CAR CLINIC Service Management System

A comprehensive service management system for automotive workshops, built with Django and modern web technologies. This system helps manage customer service records, parts inventory, and billing.

## Features

- 📱 Mobile-responsive design for on-the-go access
- 👥 Customer management with vehicle details
- 🔧 Service and parts tracking
- 💰 Automatic bill calculation
- 🖨️ Bill generation and printing
- 📊 Service history tracking
- 🔍 Search and filter capabilities

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd service-management-system
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
```bash
python manage.py migrate
```

5. Create a superuser (admin account):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

## Project Structure

```
service-management-system/
├── manage.py
├── requirements.txt
├── service_app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── service_app/
│   │       ├── service_list.html
│   │       ├── edit_bill.html
│   │       └── ...
│   └── static/
│       └── service_app/
│           └── ...
└── README.md
```

## Usage

### Customer Management

1. Add new customers with their vehicle details
2. Track customer service history
3. Manage customer contact information

### Service Records

1. Create new service records
2. Add parts and services
3. Calculate total bill automatically
4. Generate and print bills
5. Edit existing service records

### Mobile Access

The system is fully responsive and can be accessed from:
- Smartphones
- Tablets
- Desktop computers

## API Endpoints

- `GET /service/list/` - List all service records
- `POST /service/create/` - Create new service record
- `GET /service/bill/<id>/` - View service bill
- `POST /service/bill/<id>/edit/` - Edit service bill
- `GET /service/bill/<id>/print/` - Print service bill

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please contact:
- Email: support@916carclinic.com
- Phone: [Your Support Phone Number]

## Acknowledgments

- Django Framework
- Tailwind CSS
- Font Awesome Icons
- All contributors and users of the system 