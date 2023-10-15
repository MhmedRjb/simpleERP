CREATE TABLE `warehouse`(
    `warehouse_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `location` CHAR(255) NOT NULL,
    `name` CHAR(255) NOT NULL,
    PRIMARY KEY (`warehouse_id`)
);

CREATE TABLE item (
    item_id BIGINT NOT NULL PRIMARY KEY,        
    item_name VARCHAR(255),             
    type VARCHAR(255),             
    dimension VARCHAR(255),        
    date_created DATE,             
    date_added DATE,               
    identifier VARCHAR(255)        
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

CREATE TABLE `manufacturing`(
    `manufacturing_id` BIGINT NOT NULL,
    `process_id` BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    `warehouse_id` BIGINT NOT NULL,
    `item_id` BIGINT NOT NULL,
    `quantity_numeric` BIGINT NOT NULL,
    `quantity_weight` BIGINT NOT NULL,
    `type` ENUM('Type1', 'Type2') NOT NULL, -- replace 'Type1', 'Type2' with your actual types
    `date` DATE NOT NULL
);

ALTER TABLE
    `transactions` ADD INDEX `transactions_item_id_index`(`item_id`);
ALTER TABLE
    `manufacturing` ADD INDEX `manufacturing_manufacturing_id_index`(`manufacturing_id`);
ALTER TABLE
    `manufacturing` ADD INDEX `manufacturing_item_id_index`(`item_id`);
ALTER TABLE
    `transactions` ADD CONSTRAINT `transactions_item_id_foreign` FOREIGN KEY(`item_id`) REFERENCES `item`(`item_id`);
