CREATE TABLE `Metal`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` VARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Size`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carets` NUMERIC(5,2) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);


CREATE TABLE `Style`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` VARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Order`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal_id` INTEGER NOT NULL,
    `size_id` INTEGER NOT NULL,
    `style_id` INTEGER NOT NULL,
    FOREIGN KEY(`metal_id`) REFERENCES `Metal`(`id`),
    FOREIGN KEY(`size_id`) REFERENCES `Size`(`id`),
    FOREIGN KEY(`style_id`) REFERENCES `Style`(`id`)
);

INSERT INTO `Metal` VALUES (null, "Sterling Silver", 12.42);
INSERT INTO `Metal` VALUES (null, "14K Gold", 736.4);
INSERT INTO `Metal` VALUES (null, "24K Gold", 1258.9);
INSERT INTO `Metal` VALUES (null, "Platinum", 795.45);
INSERT INTO `Metal` VALUES (null, "Palladium", 1241);

INSERT INTO `Size` VALUES (null, 0.5, 405);
INSERT INTO `Size` VALUES (null, 0.75, 782);
INSERT INTO `Size` VALUES (null, 1, 1470);
INSERT INTO `Size` VALUES (null, 1.5, 1997);
INSERT INTO `Size` VALUES (null, 2, 3638);

INSERT INTO `Style` VALUES (null, "Classic", 500);
INSERT INTO `Style` VALUES (null, "Modern", 710);
INSERT INTO `Style` VALUES (null, "Vintage", 965);

INSERT INTO `Order` VALUES (null, 1, 2, 5);
INSERT INTO `Order` VALUES (null, 2, 1, 4);
INSERT INTO `Order` VALUES (null, 3, 2, 3);
INSERT INTO `Order` VALUES (null, 4, 3, 2);
INSERT INTO `Order` VALUES (null, 5, 1, 1);

DROP TABLE Metals;
DROP TABLE Order;
DROP TABLE Sizes;
DROP TABLE Styles;


SELECT
    a.id,
    a.metal_id,
    a.size_id,
    a.style_id
    -- m.metal metal_metal,
    -- m.price metal_price,
    -- z.carets size_carets,
    -- z.price size_price,
    -- y.style style_style,
    -- y.price style_price
FROM `order` a
JOIN metal m
    ON m.id = a.metal_id
JOIN size z
    ON z.id = a.size_id
JOIN style y
    ON y.id = a.style_id;






