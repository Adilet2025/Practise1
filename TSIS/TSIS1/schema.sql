create table if not exists contacts(
    contact_id serial PRIMARY key,
    contact_first_name varchar(255) not null,
    contact_last_name varchar(255),
    contact_number varchar(15) not null,
    contact_email varchar(511),
    contact_extra_info varchar(255)
);

CREATE TABLE if not exists groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

ALTER TABLE contacts
    ADD COLUMN birthday DATE,
    ADD COLUMN group_id INTEGER REFERENCES groups(id);

CREATE TABLE if not exists phones (
    id SERIAL PRIMARY KEY,
    contact_id INTEGER REFERENCES contacts(contact_id) ON DELETE CASCADE,
    phone_number VARCHAR(20) NOT NULL,
    phone_type VARCHAR(10) CHECK (phone_type IN ('home', 'work', 'mobile'))
);

-- to update phone_number if there is another number in the same phone_type
ALTER TABLE phones
ADD CONSTRAINT unique_contact_phone_type
UNIQUE (contact_id, phone_type);


INSERT INTO groups(name) VALUES
('work'),
('family'),
('friend'),
('other');