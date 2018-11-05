-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Värd: localhost
-- Tid vid skapande: 05 nov 2018 kl 17:42
-- Serverversion: 5.6.41
-- PHP-version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Databas: `Halloween`
--

-- --------------------------------------------------------

--
-- Tabellstruktur `PERSON2`
--

CREATE TABLE `PERSON2` (
  `id` int(6) UNSIGNED NOT NULL,
  `firstname` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `lastname` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumpning av Data i tabell `PERSON2`
--

INSERT INTO `PERSON2` (`id`, `firstname`, `lastname`, `email`) VALUES
(14, 'Sada', 'Fessi', 'dasdas'),
(15, 'Mikael', 'Tallbo', 'dislaskdjl'),
(16, 'Sada', 'Fessehazion', 'Sddd'),
(17, 'Micke', 'Tall', 'jjkf'),
(18, 'jocke ', 'jonna', 'hello'),
(19, 'sda', 's', 'asd'),
(20, 'Sada', 's', 'd'),
(21, 'Break', 'disco', 'fast'),
(22, 'dada', 'dada', 'dada');

--
-- Index för dumpade tabeller
--

--
-- Index för tabell `PERSON2`
--
ALTER TABLE `PERSON2`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT för dumpade tabeller
--

--
-- AUTO_INCREMENT för tabell `PERSON2`
--
ALTER TABLE `PERSON2`
  MODIFY `id` int(6) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
