CREATE TABLE `warehouse`(
    `warehouse_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT INDEX,
    `location` CHAR(255) NOT NULL,
    `name` CHAR(255) NOT NULL
);
-- This table stores information about items in the ERP system.

CREATE TABLE item (
    item_id INT PRIMARY KEY,        -- Unique identifier for each item.
    name VARCHAR(255),             -- Name or title of the item.
    type VARCHAR(255),             -- Type or category of the item.
    dimension VARCHAR(255),        -- Dimensions or size of the item.
    date_created DATE,             -- Date when the item was originally created.
    date_added DATE,               -- Date when the item was added to the ERP system.
    identifier VARCHAR(255)        -- Text-based unique identifier for the item.
);

CREATE TABLE `transactions`(
    `transactions_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `transactions_id_row` BIGINT NOT NULL COMMENT 'like in transactions_id 1 there is 1,2,3,4',
    `item_id` BIGINT NOT NULL,
    `source_warehouse_id` BIGINT NOT NULL,
    `destination_warehouse_id` BIGINT NOT NULL,
    `quantity_numeric` BIGINT NOT NULL,
    `quantity_weight` BIGINT NOT NULL,
    `person_id` BIGINT NOT NULL COMMENT 'in inv system all we care only about warehouses in/out this col just for scalability',
    `date` DATE NOT NULL
);
ALTER TABLE
    `transactions` ADD INDEX `transactions_item_id_index`(`item_id`);
CREATE TABLE `manufacturing`(
    `manufacturing_id` BIGINT NOT NULL,
    `process_id` BIGINT UNSIGNED NULL AUTO_INCREMENT,
    `warehouse_id` BIGINT NOT NULL,
    `item_id` BIGINT NOT NULL,
    `quantity_numeric` BIGINT NOT NULL,
    `quantity_weight` BIGINT NOT NULL,
    `type` ENUM('') NOT NULL,
    `date` DATE NOT NULL
);
ALTER TABLE
    `manufacturing` ADD INDEX `manufacturing_manufacturing_id_index`(`manufacturing_id`);
ALTER TABLE
    `manufacturing` ADD INDEX `manufacturing_item_id_index`(`item_id`);
ALTER TABLE
    `item` ADD CONSTRAINT `item_item_id_foreign` FOREIGN KEY(`item_id`) REFERENCES `manufacturing`(`item_id`);
ALTER TABLE
    `transactions` ADD CONSTRAINT `transactions_item_id_foreign` FOREIGN KEY(`item_id`) REFERENCES `item`(`item_id`);
ALTER TABLE
    `transactions` ADD CONSTRAINT `transactions_source_warehouse_id_foreign` FOREIGN KEY(`source_warehouse_id`) REFERENCES `warehouse`(`warehouse_id`);
ALTER TABLE
    `manufacturing` ADD CONSTRAINT `manufacturing_warehouse_id_foreign` FOREIGN KEY(`warehouse_id`) REFERENCES `warehouse`(`warehouse_id`);