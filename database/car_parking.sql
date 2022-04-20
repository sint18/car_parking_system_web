-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 20, 2022 at 10:05 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `car_parking`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(10) NOT NULL,
  `fullname` varchar(60) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(64) NOT NULL,
  `status` varchar(60) NOT NULL DEFAULT 'active',
  `creationDate` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `fullname`, `username`, `password`, `status`, `creationDate`) VALUES
(7, 'John Doe', 'admin', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'active', '2022-03-12 20:59:38'),
(28, 'Nilar', 'nilar', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'inactive', '2022-03-14 02:39:32'),
(49, 'Myat Hsu', 'myathsu', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'inactive', '2022-04-09 00:00:25'),
(50, 'Tone', 'tonetone', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'inactive', '2022-04-10 00:39:39');

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `id` int(10) NOT NULL,
  `category_name` varchar(60) NOT NULL,
  `description` varchar(60) NOT NULL,
  `creationDate` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`id`, `category_name`, `description`, `creationDate`) VALUES
(1, 'Visitor', 'Not a company car', '2022-03-15 01:25:44'),
(2, 'Company', 'Employees of this company', '2022-03-15 02:04:34'),
(3, 'Subscriber', 'Some idiot with horns', '2022-03-15 03:02:36'),
(4, 'Dummy', 'Lain week nay she them her she', '2022-03-15 12:21:04');

-- --------------------------------------------------------

--
-- Table structure for table `coupon`
--

CREATE TABLE `coupon` (
  `coupon_id` int(11) NOT NULL,
  `coupon_code` varchar(60) NOT NULL,
  `discount` int(11) NOT NULL,
  `creation_date` datetime NOT NULL DEFAULT current_timestamp(),
  `status` varchar(60) NOT NULL DEFAULT 'active'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `coupon`
--

INSERT INTO `coupon` (`coupon_id`, `coupon_code`, `discount`, `creation_date`, `status`) VALUES
(1, 'INVOICE15', 15, '2022-04-15 19:02:02', 'active'),
(2, 'INV150', 20, '2022-04-16 01:44:34', 'expired');

-- --------------------------------------------------------

--
-- Table structure for table `log`
--

CREATE TABLE `log` (
  `id` int(11) NOT NULL,
  `admin_id` int(11) NOT NULL,
  `datetime` datetime NOT NULL DEFAULT current_timestamp(),
  `msg` varchar(120) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `log`
--

INSERT INTO `log` (`id`, `admin_id`, `datetime`, `msg`) VALUES
(121, 7, '2022-04-17 21:10:14', 'admin deleted the coupon with the id \'3\''),
(122, 7, '2022-04-17 21:10:18', 'admin activated the coupon with the id \'1\''),
(123, 7, '2022-04-18 00:13:08', 'admin logged in successfully'),
(124, 7, '2022-04-18 00:31:08', 'admin created a new coupon \'TESTCOUPON\''),
(125, 7, '2022-04-18 00:31:13', 'admin deleted the coupon with the id \'7\''),
(126, 7, '2022-04-18 00:34:03', 'admin created a new coupon \'COUPON100\''),
(127, 7, '2022-04-18 00:34:14', 'admin deleted the coupon with the id \'8\''),
(128, 7, '2022-04-18 00:39:40', 'admin logged in successfully'),
(129, 7, '2022-04-18 00:47:10', 'admin added a new admin with the username \'testguy\''),
(130, 7, '2022-04-18 00:47:18', 'admin deactivated the user with the id \'51\''),
(131, 7, '2022-04-18 00:47:20', 'admin activated the user with the id \'51\''),
(132, 7, '2022-04-18 00:47:40', 'admin added a new admin with the username \'1245\''),
(133, 7, '2022-04-18 00:49:12', 'admin deleted the user with the id \'52\''),
(134, 7, '2022-04-18 00:49:18', 'admin deleted the user with the id \'51\''),
(135, 7, '2022-04-18 00:49:28', 'admin added a new admin with the username \'testguy\''),
(136, 7, '2022-04-18 00:49:32', 'admin deactivated the user with the id \'53\''),
(137, 7, '2022-04-18 00:49:35', 'admin deleted the user with the id \'53\''),
(138, 7, '2022-04-18 00:55:42', 'admin added a new category with the name \'Stupid\''),
(139, 7, '2022-04-18 00:55:55', 'admin deleted the category with the id \'15\''),
(140, 7, '2022-04-18 01:04:29', 'admin added a tier id \'2\' membership for the reg no. \'0B-3421\''),
(141, 7, '2022-04-18 01:06:14', 'admin terminated membership with the membership id \'10\'');

-- --------------------------------------------------------

--
-- Table structure for table `members`
--

CREATE TABLE `members` (
  `member_id` int(11) NOT NULL,
  `plate_number` varchar(60) NOT NULL,
  `status` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `members`
--

INSERT INTO `members` (`member_id`, `plate_number`, `status`) VALUES
(1, 'Test Car', 'inactive'),
(3, 'Tesla car num', 'inactive'),
(4, 'Test Car 1', 'active'),
(5, '1K-3323', 'active'),
(6, '5G-9983', 'active'),
(7, 'Test Car 5', 'active'),
(8, '0B-3421', 'inactive');

-- --------------------------------------------------------

--
-- Table structure for table `membership`
--

CREATE TABLE `membership` (
  `id` int(11) NOT NULL,
  `member_id` int(11) NOT NULL,
  `tier_id` int(11) NOT NULL,
  `start_date` date NOT NULL,
  `valid_until` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `membership`
--

INSERT INTO `membership` (`id`, `member_id`, `tier_id`, `start_date`, `valid_until`) VALUES
(1, 1, 1, '2022-04-12', '2022-04-13'),
(3, 1, 1, '2022-04-12', '2022-04-13'),
(5, 5, 1, '2022-04-13', '2022-05-13'),
(6, 6, 1, '2022-04-13', '2022-05-13'),
(7, 3, 1, '2022-02-01', '2022-03-01'),
(8, 4, 1, '2022-04-01', '2022-05-01'),
(9, 7, 2, '2022-04-16', '2022-05-16'),
(10, 8, 2, '2022-04-18', '2022-04-18');

-- --------------------------------------------------------

--
-- Table structure for table `membership_tier`
--

CREATE TABLE `membership_tier` (
  `id` int(11) NOT NULL,
  `tier` varchar(60) NOT NULL,
  `cost` int(11) NOT NULL,
  `discount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `membership_tier`
--

INSERT INTO `membership_tier` (`id`, `tier`, `cost`, `discount`) VALUES
(1, 'Bronze', 25000, 10),
(2, 'Silver', 30000, 15);

-- --------------------------------------------------------

--
-- Table structure for table `rate`
--

CREATE TABLE `rate` (
  `id` int(11) NOT NULL,
  `rate_1` int(10) NOT NULL,
  `rate_2` int(10) NOT NULL,
  `modifiedDate` datetime DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rate`
--

INSERT INTO `rate` (`id`, `rate_1`, `rate_2`, `modifiedDate`) VALUES
(1, 1000, 500, '2022-03-24 22:07:55');

-- --------------------------------------------------------

--
-- Table structure for table `vehicle_info`
--

CREATE TABLE `vehicle_info` (
  `id` int(11) NOT NULL,
  `category_id` int(11) NOT NULL,
  `plate_number` varchar(30) NOT NULL,
  `in_time` datetime NOT NULL,
  `out_time` datetime DEFAULT NULL,
  `fees` int(11) DEFAULT NULL,
  `total_hours` varchar(60) DEFAULT NULL,
  `fined` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vehicle_info`
--

INSERT INTO `vehicle_info` (`id`, `category_id`, `plate_number`, `in_time`, `out_time`, `fees`, `total_hours`, `fined`) VALUES
(1, 4, '4X-4545', '2022-03-23 00:22:38', NULL, NULL, NULL, NULL),
(2, 3, '2K-8658', '2022-01-08 08:59:38', NULL, NULL, NULL, NULL),
(3, 4, '6B-7798', '2022-03-04 00:44:06', '2022-01-12 14:59:02', 4, '-1209.75', NULL),
(4, 1, '2Q-8089', '2022-03-25 20:16:02', '2022-01-19 20:41:02', 50, '-1559.58', NULL),
(5, 3, '3K-3773', '2022-01-03 03:44:38', NULL, NULL, NULL, NULL),
(6, 2, '0K-6518', '2022-01-30 10:01:44', NULL, NULL, NULL, NULL),
(7, 1, '7O-1138', '2022-03-19 11:10:00', NULL, NULL, NULL, NULL),
(8, 3, '3S-2860', '2022-02-12 16:00:53', '2022-02-26 20:02:32', 48, '340.03', NULL),
(9, 4, '1D-9885', '2022-01-13 10:55:36', '2022-01-02 21:19:20', 96, '-253.60', NULL),
(10, 2, '2Y-9219', '2022-03-17 09:09:42', NULL, NULL, NULL, NULL),
(11, 3, '3Z-3478', '2022-01-23 22:53:13', NULL, NULL, NULL, NULL),
(12, 4, '9U-6512', '2022-03-06 09:38:05', NULL, NULL, NULL, NULL),
(13, 1, '8X-6893', '2022-03-04 11:47:23', NULL, NULL, NULL, NULL),
(14, 2, '8W-0909', '2022-03-22 23:13:08', NULL, NULL, NULL, NULL),
(15, 1, '1U-1233', '2022-01-04 05:50:25', NULL, NULL, NULL, NULL),
(16, 4, '7Y-8082', '2022-03-01 00:31:37', '2022-03-12 14:20:52', 76, '277.82', NULL),
(17, 1, '1I-3825', '2022-03-24 06:42:53', NULL, NULL, NULL, NULL),
(18, 2, '2W-1992', '2022-03-15 10:25:38', NULL, NULL, NULL, NULL),
(19, 1, '9U-8276', '2022-03-03 02:48:40', NULL, NULL, NULL, NULL),
(20, 1, '5S-0111', '2022-02-23 13:21:20', '2022-03-17 14:46:49', 92, '529.42', NULL),
(21, 2, '6B-2645', '2022-02-17 06:56:15', NULL, NULL, NULL, NULL),
(22, 2, '1C-3745', '2022-03-05 23:37:14', NULL, NULL, NULL, NULL),
(23, 2, '9Q-0302', '2022-02-20 04:57:53', '2022-03-09 15:53:45', 35, '418.93', NULL),
(24, 1, '6J-5309', '2022-02-08 12:36:30', NULL, NULL, NULL, NULL),
(25, 2, '6K-9509', '2022-02-12 03:30:34', NULL, NULL, NULL, NULL),
(26, 4, '8K-5766', '2022-02-18 01:35:24', NULL, NULL, NULL, NULL),
(27, 2, '1H-0091', '2022-01-22 18:19:20', NULL, NULL, NULL, NULL),
(28, 2, '3P-4001', '2022-01-24 11:50:14', NULL, NULL, NULL, NULL),
(29, 3, '0E-9290', '2022-02-19 12:32:17', NULL, NULL, NULL, NULL),
(30, 3, '3W-5369', '2022-01-14 20:22:23', '2022-03-27 23:24:37', 866500, '1731.04', NULL),
(31, 2, '4I-1491', '2022-01-02 10:03:21', '2022-01-02 04:00:00', 10000, '-06:03:21', '4000'),
(32, 1, '2K-3873', '2022-01-06 15:01:04', NULL, NULL, NULL, NULL),
(33, 4, '5M-0445', '2022-03-02 10:36:11', NULL, NULL, NULL, NULL),
(34, 2, '8Q-5856', '2022-01-28 03:24:52', '2022-03-12 07:16:02', 16, '1035.85', NULL),
(35, 2, '7K-7400', '2022-02-18 20:12:45', NULL, NULL, NULL, NULL),
(36, 2, '9B-6075', '2022-01-12 14:22:03', NULL, NULL, NULL, NULL),
(37, 3, '7H-7071', '2022-03-01 21:14:52', NULL, NULL, NULL, NULL),
(38, 4, '2D-9592', '2022-03-01 05:52:52', '2022-01-27 17:48:37', 39, '-780.07', NULL),
(39, 3, '3N-7824', '2022-02-21 10:13:59', NULL, NULL, NULL, NULL),
(40, 2, '0A-8649', '2022-02-23 01:09:40', NULL, NULL, NULL, NULL),
(41, 1, '1S-9784', '2022-01-04 09:48:39', NULL, NULL, NULL, NULL),
(42, 4, '2G-3384', '2022-02-13 17:26:21', NULL, NULL, NULL, NULL),
(43, 2, '0B-3421', '2022-02-15 16:37:22', NULL, NULL, NULL, NULL),
(44, 3, '0V-9729', '2022-01-03 23:19:46', '2022-02-14 16:45:38', 62, '1001.43', NULL),
(45, 3, '5S-3339', '2022-02-18 09:25:31', NULL, NULL, NULL, NULL),
(46, 2, '1P-9888', '2022-03-13 01:49:58', NULL, NULL, NULL, NULL),
(47, 4, '6K-4714', '2022-02-05 02:37:54', NULL, NULL, NULL, NULL),
(48, 1, '1W-9985', '2022-01-24 09:05:32', NULL, NULL, NULL, NULL),
(49, 4, '9I-1916', '2022-01-16 02:19:37', NULL, NULL, NULL, NULL),
(50, 4, '5L-7353', '2022-03-09 12:44:39', '2022-01-26 18:46:39', 29, '-1001.97', NULL),
(51, 3, '0J-9468', '2022-01-19 18:21:54', NULL, NULL, NULL, NULL),
(52, 1, '0E-0048', '2022-01-20 12:24:58', NULL, NULL, NULL, NULL),
(53, 1, '8F-1535', '2022-02-04 19:35:36', NULL, NULL, NULL, NULL),
(54, 2, '9L-5276', '2022-01-13 12:10:24', '2022-03-24 18:54:21', 70, '1686.73', NULL),
(55, 3, '2G-7059', '2022-02-01 06:14:07', NULL, NULL, NULL, NULL),
(56, 3, '6M-6685', '2022-01-06 16:51:50', NULL, NULL, NULL, NULL),
(57, 4, '4R-2439', '2022-01-24 13:49:51', NULL, NULL, NULL, NULL),
(58, 2, '3M-6998', '2022-02-03 16:41:33', NULL, NULL, NULL, NULL),
(59, 4, '2M-4132', '2022-02-27 19:12:01', NULL, NULL, NULL, NULL),
(60, 4, '7F-4664', '2022-01-24 13:17:41', NULL, NULL, NULL, NULL),
(61, 1, '7O-4503', '2022-02-20 17:30:02', NULL, NULL, NULL, NULL),
(62, 3, '2U-6137', '2022-03-01 12:14:18', NULL, NULL, NULL, NULL),
(63, 2, '5N-6645', '2022-01-29 17:18:12', NULL, NULL, NULL, NULL),
(64, 4, '8B-2473', '2022-02-03 16:23:22', NULL, NULL, NULL, NULL),
(65, 1, '1E-2456', '2022-01-20 17:33:35', NULL, NULL, NULL, NULL),
(66, 1, '4O-1837', '2022-03-20 20:52:54', NULL, NULL, NULL, NULL),
(67, 2, '2A-3258', '2022-03-23 21:25:51', NULL, NULL, NULL, NULL),
(68, 2, '1U-2475', '2022-02-26 12:51:50', '2022-01-24 08:12:20', 56, '-796.66', NULL),
(69, 3, '4I-2218', '2022-03-14 15:07:16', NULL, NULL, NULL, NULL),
(70, 2, '3K-7739', '2022-02-07 18:33:32', NULL, NULL, NULL, NULL),
(71, 2, '9I-6750', '2022-03-18 12:03:01', '2022-03-19 06:03:51', 93, '18.01', NULL),
(72, 1, '8R-8779', '2022-01-03 03:05:50', NULL, NULL, NULL, NULL),
(73, 4, '6G-3436', '2022-03-12 12:51:55', NULL, NULL, NULL, NULL),
(74, 1, '5X-6531', '2022-01-07 18:21:57', NULL, NULL, NULL, NULL),
(75, 2, '4U-1555', '2022-01-22 08:28:55', NULL, NULL, NULL, NULL),
(76, 4, '2E-9028', '2022-02-20 06:11:24', '2022-02-26 00:33:50', 30, '138.37', NULL),
(77, 1, '1Q-6140', '2022-03-11 01:26:09', '2022-03-29 21:00:52', 226500, '451.58', NULL),
(78, 3, '3O-9762', '2022-01-23 03:13:33', NULL, NULL, NULL, NULL),
(79, 1, '5E-9890', '2022-01-28 05:38:51', NULL, NULL, NULL, NULL),
(80, 2, '1L-7520', '2022-01-19 18:24:40', NULL, NULL, NULL, NULL),
(81, 4, '1F-7232', '2022-03-05 07:16:18', '2022-02-03 01:14:55', 55, '-726.02', NULL),
(82, 2, '9N-0021', '2022-02-17 08:43:00', NULL, NULL, NULL, NULL),
(83, 1, '5X-8236', '2022-03-01 18:21:02', NULL, NULL, NULL, NULL),
(84, 3, '4J-0209', '2022-02-27 04:43:45', NULL, NULL, NULL, NULL),
(85, 2, '7O-1982', '2022-01-01 13:59:49', '2022-03-22 18:02:41', 63, '1924.05', NULL),
(86, 3, '4I-6074', '2022-01-12 15:00:53', '2022-01-26 11:57:57', 71, '332.95', NULL),
(87, 1, '8E-8317', '2022-03-23 03:17:09', NULL, NULL, NULL, NULL),
(88, 1, '5R-1425', '2022-02-03 06:24:43', NULL, NULL, NULL, NULL),
(89, 3, '7I-0204', '2022-01-30 06:59:07', '2022-03-31 00:59:29', 718000, '1434.01', NULL),
(90, 3, '5A-1271', '2022-01-02 14:17:35', NULL, NULL, NULL, NULL),
(91, 2, '1H-0339', '2022-02-12 10:55:48', NULL, NULL, NULL, NULL),
(92, 2, '1H-9114', '2022-01-13 03:13:03', NULL, NULL, NULL, NULL),
(93, 4, '3T-0028', '2022-02-21 19:23:41', '2022-02-14 16:38:26', 71, '-170.75', NULL),
(94, 1, '6T-6813', '2022-02-12 06:36:24', NULL, NULL, NULL, NULL),
(95, 2, '5J-3431', '2022-01-26 17:02:40', '2022-02-27 07:09:35', 92, '758.12', NULL),
(96, 1, '0B-2271', '2022-03-12 10:04:34', NULL, NULL, NULL, NULL),
(97, 4, '3R-7531', '2022-02-23 13:30:11', '2022-02-25 22:57:53', 3, '57.46', NULL),
(98, 3, '4J-5259', '2022-01-04 15:31:16', '2022-03-06 19:36:54', 74, '1468.09', NULL),
(99, 1, '4O-6708', '2022-02-26 15:29:14', '2022-03-28 00:37:30', 353500, '705.14', NULL),
(100, 1, '7Y-3559', '2022-03-21 06:13:22', '2022-03-27 23:12:51', 81, '160.99', NULL),
(105, 3, '5G-9982', '2022-03-27 23:26:45', '2022-03-29 20:56:36', 23500, '45.5', NULL),
(106, 1, '5H-5678', '2022-03-29 20:41:23', NULL, NULL, NULL, NULL),
(107, 2, '6G-8765', '2022-03-29 20:42:29', NULL, NULL, NULL, NULL),
(108, 2, '6G-8765', '2022-03-29 20:43:19', '2022-04-16 18:44:54', 186500, '17 days, 22:01:35', '100000'),
(109, 1, '1G-5545', '2022-03-29 20:47:01', NULL, NULL, NULL, NULL),
(110, 1, '9I-9998', '2022-03-29 20:50:34', NULL, NULL, NULL, NULL),
(111, 2, '8A-5592', '2022-03-29 20:55:09', NULL, NULL, NULL, NULL),
(112, 2, '4G-5545', '2022-03-31 01:21:41', '2022-04-12 20:26:23', 161900, '12 days, 19:04:42', '100000'),
(113, 1, '7J-6656', '2022-03-31 01:21:55', '2022-04-12 20:17:46', 161700, '306:55:51', '100'),
(114, 1, '1K-3323', '2022-04-10 00:45:54', '2022-04-12 20:09:21', 113900, '2 days, 19:23:27', '100000'),
(115, 2, '5G-9983', '2022-04-12 01:50:26', '2022-04-12 22:11:50', 4500, '20:21:24', '0'),
(116, 2, 'Test Car', '2022-04-12 20:13:53', '2022-04-17 18:07:18', 109560, '4 days, 21:53:25', '100000|TESTCP'),
(117, 1, 'Test Car 1', '2022-04-12 20:14:01', '2022-04-14 19:07:19', 108730, '1 day, 22:53:18', '100000'),
(118, 2, 'Test car 2', '2022-04-12 20:14:06', NULL, NULL, NULL, NULL),
(119, 1, 'Test Car 4', '2022-04-13 23:50:15', NULL, NULL, NULL, NULL),
(120, 3, '5G-9983', '2022-04-14 01:00:39', '2022-04-15 18:27:48', 107830, '1 day, 17:27:09', '100000'),
(121, 3, '1K-3323', '2022-04-14 01:13:27', '2022-04-16 02:05:23', 109090, '2 days, 0:51:56', '100000'),
(122, 1, '9A-1234', '2022-04-14 19:06:41', '2022-04-16 02:01:00', 106500, '1 day, 6:54:19', '100000'),
(123, 3, 'Test Car 1', '2022-04-14 19:07:29', '2022-04-15 18:23:08', 4590, '23:15:39', '0'),
(124, 1, 'ရိုးရိုးကား', '2022-04-16 02:02:05', '2022-04-16 02:09:20', 500, '0:07:15', '0'),
(125, 3, '8B-8888', '2022-04-16 02:10:04', '2022-04-16 18:42:46', 3700, '16:32:42', '0'),
(126, 3, 'Test Car 5', '2022-04-16 18:28:47', '2022-04-16 18:42:21', 425, '0:13:34', '0'),
(127, 3, 'Test Car 5', '2022-04-16 19:05:26', '2022-04-17 16:53:46', -235705, '21:48:20', 'None|TESTCP'),
(129, 1, 'Paul Car', '2022-04-17 18:23:12', '2022-04-17 18:23:23', 500, '0:00:11', 'None|None');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `coupon`
--
ALTER TABLE `coupon`
  ADD PRIMARY KEY (`coupon_id`),
  ADD UNIQUE KEY `coupon_code` (`coupon_code`);

--
-- Indexes for table `log`
--
ALTER TABLE `log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `admin_id` (`admin_id`);

--
-- Indexes for table `members`
--
ALTER TABLE `members`
  ADD PRIMARY KEY (`member_id`),
  ADD UNIQUE KEY `plate_number` (`plate_number`);

--
-- Indexes for table `membership`
--
ALTER TABLE `membership`
  ADD PRIMARY KEY (`id`),
  ADD KEY `member_id` (`member_id`),
  ADD KEY `tier_id` (`tier_id`);

--
-- Indexes for table `membership_tier`
--
ALTER TABLE `membership_tier`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rate`
--
ALTER TABLE `rate`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `vehicle_info`
--
ALTER TABLE `vehicle_info`
  ADD PRIMARY KEY (`id`),
  ADD KEY `category_id` (`category_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `coupon`
--
ALTER TABLE `coupon`
  MODIFY `coupon_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `log`
--
ALTER TABLE `log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=142;

--
-- AUTO_INCREMENT for table `members`
--
ALTER TABLE `members`
  MODIFY `member_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `membership`
--
ALTER TABLE `membership`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `membership_tier`
--
ALTER TABLE `membership_tier`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `rate`
--
ALTER TABLE `rate`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `vehicle_info`
--
ALTER TABLE `vehicle_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=130;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `log`
--
ALTER TABLE `log`
  ADD CONSTRAINT `log_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `membership`
--
ALTER TABLE `membership`
  ADD CONSTRAINT `membership_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `members` (`member_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `membership_ibfk_2` FOREIGN KEY (`tier_id`) REFERENCES `membership_tier` (`id`) ON UPDATE CASCADE;

--
-- Constraints for table `vehicle_info`
--
ALTER TABLE `vehicle_info`
  ADD CONSTRAINT `vehicle_info_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
