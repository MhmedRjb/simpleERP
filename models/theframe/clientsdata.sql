-- Insert sample data into the clients table
INSERT INTO clients (name, address, industry, company_size, website, registration_date, notes, payment_terms, billing_address, shipping_address, tax_id, sales_representative)
VALUES
    ('Acme Inc.', '123 Main St, City, Country', 'Technology', 'Medium', 'http://www.acme.com', '2023-10-20', 'This is a new client.', 'Net 30', '456 Billing St, City, Country', '789 Shipping St, City, Country', '12345', 'John Doe'),
    ('Healthcare Pro', '456 Elm St, City, Country', 'Healthcare', 'Large', 'http://www.healthcarepro.com', '2023-10-21', 'A well-established healthcare provider.', 'Net 45', '789 Billing St, City, Country', '101 Shipping St, City, Country', '67890', 'Jane Smith'),
    ('RetailHub', '789 Oak St, City, Country', 'Retail', 'Small', 'http://www.retailhub.com', '2023-10-22', 'New retail startup.', 'Net 60', '147 Billing St, City, Country', '369 Shipping St, City, Country', '54321', 'Bob Johnson'),
    ('Tech Enterprises', '101 Elm St, City, Country', 'Technology', 'Enterprise', 'http://www.techent.com', '2023-10-23', 'Global tech giant.', 'Net 30', '789 Billing St, City, Country', '101 Shipping St, City, Country', '99999', 'Alice Green'),
    ('Sunshine Retail', '456 Maple St, City, Country', 'Retail', 'Medium', 'http://www.sunshineretail.com', '2023-10-24', 'Family-owned retail store.', 'Net 45', '789 Billing St, City, Country', '101 Shipping St, City, Country', '77777', 'David White'),
    ('MediCare', '333 Pine St, City, Country', 'Healthcare', 'Large', 'http://www.medicare.com', '2023-10-25', 'Leading healthcare provider.', 'Net 30', '789 Billing St, City, Country', '101 Shipping St, City, Country', '55555', 'Sarah Brown'),
    ('InnovateTech', '555 Cedar St, City, Country', 'Technology', 'Medium', 'http://www.innovatetech.com', '2023-10-26', 'Tech innovation company.', 'Net 60', '789 Billing St, City, Country', '101 Shipping St, City, Country', '88888', 'Michael Lee'),
    ('Green Retail', '777 Oak St, City, Country', 'Retail', 'Small', 'http://www.greenretail.com', '2023-10-27', 'Eco-friendly retail.', 'Net 45', '789 Billing St, City, Country', '101 Shipping St, City, Country', '66666', 'Karen Wilson'),
    ('Tech Innovators', '999 Redwood St, City, Country', 'Technology', 'Enterprise', 'http://www.techinnovators.com', '2023-10-28', 'Cutting-edge tech firm.', 'Net 30', '789 Billing St, City, Country', '101 Shipping St, City, Country', '11111', 'Daniel Turner'),
    ('HealthCare Solutions', '123 Cedar St, City, Country', 'Healthcare', 'Large', 'http://www.healthcaresolutions.com', '2023-10-29', 'Healthcare solutions provider.', 'Net 60', '789 Billing St, City, Country', '101 Shipping St, City, Country', '22222', 'Emily Adams');

INSERT INTO contacts (client_id, name, email, phone, role)
VALUES
    (1, 'John Smith', 'john.smith@email.com', '123-456-7890', 'CEO'),
    (2, 'Mary Johnson', 'mary.johnson@email.com', '987-654-3210', 'CFO'),
    (3, 'David Williams', 'david.williams@email.com', '555-555-5555', 'Manager'),
    (4, 'Sarah Davis', 'sarah.davis@email.com', '111-222-3333', 'Sales Rep'),
    (1, 'Alice Wilson', 'alice.wilson@email.com', '777-888-9999', 'Marketing'),
    (5, 'Michael Brown', 'michael.brown@email.com', '333-333-3333', 'HR'),
    (2, 'Karen Miller', 'karen.miller@email.com', '444-444-4444', 'IT Specialist'),
    (6, 'Daniel Lee', 'daniel.lee@email.com', '666-666-6666', 'Engineer'),
    (3, 'Emily Turner', 'emily.turner@email.com', '999-999-9999', 'Project Manager'),
    (4, 'Alex Martin', 'alex.martin@email.com', '222-222-2222', 'Consultant');
