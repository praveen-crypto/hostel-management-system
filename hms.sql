-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 30, 2021 at 10:55 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hms`
--

-- --------------------------------------------------------

--
-- Table structure for table `daily_menu`
--

CREATE TABLE `daily_menu` (
  `id` varchar(100) NOT NULL,
  `breakfast` varchar(1000) NOT NULL,
  `lunch` varchar(1000) NOT NULL,
  `dinner` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `daily_menu`
--

INSERT INTO `daily_menu` (`id`, `breakfast`, `lunch`, `dinner`) VALUES
('2021-01-27', 'Dosa&&Sambar', 'Rasam&&Rice&&Sambar', 'Idly'),
('2021-01-30', 'Chapathi', 'Dosa&&Pani poori', 'Dosa');

-- --------------------------------------------------------

--
-- Table structure for table `food_items`
--

CREATE TABLE `food_items` (
  `id` int(11) NOT NULL,
  `item` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `food_items`
--

INSERT INTO `food_items` (`id`, `item`) VALUES
(1, 'Dosa'),
(2, 'Idly'),
(3, 'Sambar'),
(4, 'Vadai'),
(5, 'Poori'),
(6, 'Chapathi'),
(7, 'Rice'),
(8, 'Rasam'),
(9, 'Pani poori');

-- --------------------------------------------------------

--
-- Table structure for table `grieveance`
--

CREATE TABLE `grieveance` (
  `id` int(10) NOT NULL,
  `title` varchar(100) NOT NULL,
  `body` varchar(1000) NOT NULL,
  `user_details_email` varchar(1000) NOT NULL,
  `time` datetime NOT NULL DEFAULT current_timestamp(),
  `status` varchar(100) NOT NULL DEFAULT 'pending'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `rooms`
--

CREATE TABLE `rooms` (
  `id` varchar(15) NOT NULL,
  `capacity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rooms`
--

INSERT INTO `rooms` (`id`, `capacity`) VALUES
('A1', 1),
('A10', 1),
('A2', 1),
('A3', 1),
('A4', 1),
('A5', 1),
('A6', 1),
('A7', 1),
('A8', 1),
('A9', 1),
('B1', 2),
('B10', 2),
('B2', 2),
('B3', 2),
('B4', 2),
('B5', 2),
('B6', 2),
('B7', 2),
('B8', 2),
('B9', 2),
('C1', 3),
('C10', 3),
('C2', 3),
('C3', 3),
('C4', 3),
('C5', 3),
('C6', 3),
('C7', 3),
('C8', 3),
('C9', 3);

-- --------------------------------------------------------

--
-- Table structure for table `user_details`
--

CREATE TABLE `user_details` (
  `email` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `rollno` varchar(50) NOT NULL,
  `dept` varchar(50) NOT NULL,
  `fathers_name` varchar(100) NOT NULL,
  `Mothers_name` varchar(100) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `fees_paid` varchar(100) NOT NULL DEFAULT 'no',
  `food_type` varchar(100) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `account_type` varchar(100) NOT NULL DEFAULT 'student',
  `password` varchar(50) NOT NULL,
  `dob` varchar(100) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `access` varchar(50) NOT NULL DEFAULT 'pending',
  `rooms_id` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_details`
--

INSERT INTO `user_details` (`email`, `name`, `rollno`, `dept`, `fathers_name`, `Mothers_name`, `Address`, `fees_paid`, `food_type`, `phone`, `account_type`, `password`, `dob`, `gender`, `access`, `rooms_id`) VALUES
('admin', 'admin', 'admin', 'admin', '', '', '', '', '', '', 'admin', 'admin', '', '', 'approved', '0');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `daily_menu`
--
ALTER TABLE `daily_menu`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `food_items`
--
ALTER TABLE `food_items`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `grieveance`
--
ALTER TABLE `grieveance`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rooms`
--
ALTER TABLE `rooms`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_details`
--
ALTER TABLE `user_details`
  ADD PRIMARY KEY (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `food_items`
--
ALTER TABLE `food_items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `grieveance`
--
ALTER TABLE `grieveance`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
