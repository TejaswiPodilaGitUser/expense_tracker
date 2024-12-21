from faker import Faker
import random

fake = Faker()

# Expense Categories and Payment Modes
CATEGORIES = ['Food', 'Transportation', 'Bills', 'Groceries', 'Subscriptions', 
              'Personal Spending', 'Investments', 'Stationary', 'Fruits & Vegetables', 
              'Home Essentials', 'Sports & Fitness', 'School Fees']

PAYMENT_MODES = ['UPI', 'Netbanking', 'Credit Card', 'Debit Card', 'Online', 'Wallet', 'Cash']

# Descriptions based on categories
CATEGORY_DESCRIPTIONS = {
    'Food': ['Lunch Bills', 'Dinner', 'Takeaway', 'Snacks', 'Cafe'],
    'Transportation': ['Taxi Fare', 'Bus Ticket', 'Train Ticket', 'Fuel','Tours'],
    'Bills': ['Electricity Bills', 'Water Bills', 'Internet Bills'],
    'Groceries': ['Grocery Shopping', 'Pulses & Grains', 'Milk & Eggs','Dry Fruits','Chocolates & Biscuits'],
    'Subscriptions': ['Amazon Subscription', 'Netflix Subscription', 'Spotify Subscription', 'Magazine Subscription'],
    'Personal Spending': ['Clothing', 'Cosmetics', 'Haircut'],
    'Investments': ['Investment Bonds', 'Fixed Deposits', 'Stocks Purchase'],
    'Stationary': ['Pens & Pencils', 'Notebooks', 'Paper'],
    'Fruits & Vegetables': ['Fruits', 'Vegetables'],
    'Home Essentials': ['Cookware', 'Cleaning Supplies', 'Furniture'],
    'Sports & Fitness': ['Gym Membership', 'Yoga Class', 'Cricket Kit'],
    'School Fees': ['Tuition Fees', 'Books & Stationary','School Fees','Trips']
}

# Generate Random Expense Data
def generate_expense_report(num_entries):
    report = []
    for _ in range(num_entries):
        category = random.choice(CATEGORIES)
        expense = {
            'date': fake.date_this_year(),
            'category': category,
            'payment_mode': random.choice(PAYMENT_MODES),
            'description': random.choice(CATEGORY_DESCRIPTIONS[category]),
            'amount_paid': round(random.uniform(10.0, 500.0), 2),
            'cashback': round(random.uniform(0.0, 10.0), 2)
        }
        report.append(expense)
    return report


