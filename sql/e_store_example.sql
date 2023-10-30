-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Oct 30, 2023 at 07:09 AM
-- Server version: 8.0.31
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `e_store_example`
--

-- --------------------------------------------------------

--
-- Table structure for table `boat`
--

DROP TABLE IF EXISTS `boat`;
CREATE TABLE IF NOT EXISTS `boat` (
  `product_id` int NOT NULL,
  `width_cm` float NOT NULL,
  `length_cm` float NOT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
CREATE TABLE IF NOT EXISTS `category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
CREATE TABLE IF NOT EXISTS `customer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`id`, `first_name`, `last_name`) VALUES
(3, 'graphql', 'taalta tullaan');

-- --------------------------------------------------------

--
-- Table structure for table `hat`
--

DROP TABLE IF EXISTS `hat`;
CREATE TABLE IF NOT EXISTS `hat` (
  `product_id` int NOT NULL,
  `color` varchar(45) NOT NULL,
  `size` varchar(45) NOT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
CREATE TABLE IF NOT EXISTS `order` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date_created` datetime NOT NULL,
  `order_state_id` int NOT NULL,
  `customer_id` int NOT NULL,
  `handler_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_order_order_state1_idx` (`order_state_id`),
  KEY `fk_order_customer1_idx` (`customer_id`),
  KEY `fk_order_user1_idx` (`handler_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `order_has_product`
--

DROP TABLE IF EXISTS `order_has_product`;
CREATE TABLE IF NOT EXISTS `order_has_product` (
  `order_id` int NOT NULL,
  `product_id` int NOT NULL,
  `product_count` int NOT NULL,
  PRIMARY KEY (`order_id`,`product_id`),
  KEY `fk_order_has_product_product1_idx` (`product_id`),
  KEY `fk_order_has_product_order1_idx` (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `order_state`
--

DROP TABLE IF EXISTS `order_state`;
CREATE TABLE IF NOT EXISTS `order_state` (
  `id` int NOT NULL AUTO_INCREMENT,
  `state` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `state_UNIQUE` (`state`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
CREATE TABLE IF NOT EXISTS `product` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `price` float NOT NULL,
  `category_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_product_category_idx` (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `shoe`
--

DROP TABLE IF EXISTS `shoe`;
CREATE TABLE IF NOT EXISTS `shoe` (
  `product_id` int NOT NULL,
  `size` varchar(45) NOT NULL,
  `color` varchar(45) NOT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `boat`
--
ALTER TABLE `boat`
  ADD CONSTRAINT `fk_boat_product1` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`);

--
-- Constraints for table `hat`
--
ALTER TABLE `hat`
  ADD CONSTRAINT `fk_hat_product1` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`);

--
-- Constraints for table `order`
--
ALTER TABLE `order`
  ADD CONSTRAINT `fk_order_customer1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`),
  ADD CONSTRAINT `fk_order_order_state1` FOREIGN KEY (`order_state_id`) REFERENCES `order_state` (`id`),
  ADD CONSTRAINT `fk_order_user1` FOREIGN KEY (`handler_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `order_has_product`
--
ALTER TABLE `order_has_product`
  ADD CONSTRAINT `fk_order_has_product_order1` FOREIGN KEY (`order_id`) REFERENCES `order` (`id`),
  ADD CONSTRAINT `fk_order_has_product_product1` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`);

--
-- Constraints for table `product`
--
ALTER TABLE `product`
  ADD CONSTRAINT `fk_product_category` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`);

--
-- Constraints for table `shoe`
--
ALTER TABLE `shoe`
  ADD CONSTRAINT `fk_shoe_product1` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
