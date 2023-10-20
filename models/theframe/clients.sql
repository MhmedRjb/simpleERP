CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    name VARCHAR(255) NOT NULL, -- Name of the client or business
    address TEXT, -- Physical address of the client
    industry VARCHAR(100), -- Industry in which the client operates
    company_size ENUM('Small', 'Medium', 'Large', 'Enterprise', 'Other') NOT NULL, -- Company size level
    website VARCHAR(255), -- Client's website URL
    registration_date DATE, -- Date of client registration
    notes TEXT, -- General notes or comments about the client
    payment_terms VARCHAR(50), -- Payment terms for the client
    billing_address TEXT, -- Billing address for the client
    shipping_address TEXT, -- Shipping address for the client
    tax_id VARCHAR(20), -- Tax ID or identification number
    sales_representative VARCHAR(255), -- Name of the sales representative
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the client record was created
    modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Date and time when the client record was last modified
    location VARCHAR(255) -- Location of the client
    
);

CREATE TABLE contacts (
    contact_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each contact
    client_id INT, -- Foreign key linking the contact to a specific client
    name VARCHAR(255), -- Name of the contact person
    email VARCHAR(255), -- Email address of the contact person
    phone VARCHAR(20), -- Contact person's phone number
    role VARCHAR(100), -- Role or position of the contact person
    FOREIGN KEY (client_id) REFERENCES clients (client_id) -- Relationship to the "clients" table
);

