-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 08 Kwi 2019, 21:44
-- Wersja serwera: 10.1.35-MariaDB
-- Wersja PHP: 7.2.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `biblioteka`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `autorzy`
--

CREATE TABLE `autorzy` (
  `id_autora` int(11) NOT NULL,
  `imie` varchar(20) COLLATE utf8_polish_ci NOT NULL,
  `nazwisko` varchar(20) COLLATE utf8_polish_ci NOT NULL,
  `narodowosc` varchar(20) COLLATE utf8_polish_ci NOT NULL,
  `liczba_dziel` int(11) NOT NULL,
  `zyciorys` text COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `czytelnicy`
--

CREATE TABLE `czytelnicy` (
  `id_czytelnika` int(11) NOT NULL,
  `imie` varchar(30) COLLATE utf8_polish_ci NOT NULL,
  `nazwisko` varchar(30) COLLATE utf8_polish_ci NOT NULL,
  `miasto` varchar(30) COLLATE utf8_polish_ci NOT NULL,
  `ulica` varchar(30) COLLATE utf8_polish_ci NOT NULL,
  `liczba_ksiazek` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `egzemplarze`
--

CREATE TABLE `egzemplarze` (
  `id_egzemplarza` int(11) NOT NULL,
  `nr_bibilioteczny` int(11) NOT NULL,
  `id_ksiazki` int(11) NOT NULL,
  `wydanie` smallint(6) NOT NULL,
  `rok_publikacji` int(11) NOT NULL,
  `dostepnosc` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `gatunki`
--

CREATE TABLE `gatunki` (
  `id_gatunku` int(11) NOT NULL,
  `nazwa` varchar(30) COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `ksiazki`
--

CREATE TABLE `ksiazki` (
  `id_ksiazki` int(11) NOT NULL,
  `id_autora` int(11) NOT NULL,
  `id_wydawnictwa` int(11) NOT NULL,
  `id_gatunku` int(11) NOT NULL,
  `tytul` varchar(70) COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `wydawnictwa`
--

CREATE TABLE `wydawnictwa` (
  `id_wydawnictwa` int(11) NOT NULL,
  `nazwa` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `kraj` varchar(30) COLLATE utf8_polish_ci NOT NULL,
  `miasto` varchar(30) COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `wypozyczenia`
--

CREATE TABLE `wypozyczenia` (
  `id_wypozyczenia` int(11) NOT NULL,
  `id_czytelnika` int(11) NOT NULL,
  `id_egzemplarza` int(11) NOT NULL,
  `data_zamowienia` date NOT NULL,
  `data_wypozyczenia` date NOT NULL,
  `data_zwrotu` date NOT NULL,
  `status` varchar(30) COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `autorzy`
--
ALTER TABLE `autorzy`
  ADD PRIMARY KEY (`id_autora`);

--
-- Indeksy dla tabeli `czytelnicy`
--
ALTER TABLE `czytelnicy`
  ADD PRIMARY KEY (`id_czytelnika`);

--
-- Indeksy dla tabeli `egzemplarze`
--
ALTER TABLE `egzemplarze`
  ADD PRIMARY KEY (`id_egzemplarza`),
  ADD KEY `id_ksiazki` (`id_ksiazki`);

--
-- Indeksy dla tabeli `gatunki`
--
ALTER TABLE `gatunki`
  ADD PRIMARY KEY (`id_gatunku`);

--
-- Indeksy dla tabeli `ksiazki`
--
ALTER TABLE `ksiazki`
  ADD PRIMARY KEY (`id_ksiazki`),
  ADD KEY `id_autora` (`id_autora`),
  ADD KEY `id_wydawnictwa` (`id_wydawnictwa`),
  ADD KEY `id_gatunku` (`id_gatunku`);

--
-- Indeksy dla tabeli `wydawnictwa`
--
ALTER TABLE `wydawnictwa`
  ADD PRIMARY KEY (`id_wydawnictwa`);

--
-- Indeksy dla tabeli `wypozyczenia`
--
ALTER TABLE `wypozyczenia`
  ADD PRIMARY KEY (`id_wypozyczenia`),
  ADD KEY `id_egzemplarza` (`id_egzemplarza`),
  ADD KEY `id_czytelnika` (`id_czytelnika`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT dla tabeli `autorzy`
--
ALTER TABLE `autorzy`
  MODIFY `id_autora` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `czytelnicy`
--
ALTER TABLE `czytelnicy`
  MODIFY `id_czytelnika` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `egzemplarze`
--
ALTER TABLE `egzemplarze`
  MODIFY `id_egzemplarza` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `gatunki`
--
ALTER TABLE `gatunki`
  MODIFY `id_gatunku` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `ksiazki`
--
ALTER TABLE `ksiazki`
  MODIFY `id_ksiazki` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `wydawnictwa`
--
ALTER TABLE `wydawnictwa`
  MODIFY `id_wydawnictwa` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `wypozyczenia`
--
ALTER TABLE `wypozyczenia`
  MODIFY `id_wypozyczenia` int(11) NOT NULL AUTO_INCREMENT;

--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `egzemplarze`
--
ALTER TABLE `egzemplarze`
  ADD CONSTRAINT `egzemplarze_ibfk_1` FOREIGN KEY (`id_ksiazki`) REFERENCES `ksiazki` (`id_ksiazki`);

--
-- Ograniczenia dla tabeli `ksiazki`
--
ALTER TABLE `ksiazki`
  ADD CONSTRAINT `ksiazki_ibfk_1` FOREIGN KEY (`id_autora`) REFERENCES `autorzy` (`id_autora`),
  ADD CONSTRAINT `ksiazki_ibfk_2` FOREIGN KEY (`id_wydawnictwa`) REFERENCES `wydawnictwa` (`id_wydawnictwa`),
  ADD CONSTRAINT `ksiazki_ibfk_3` FOREIGN KEY (`id_gatunku`) REFERENCES `gatunki` (`id_gatunku`);

--
-- Ograniczenia dla tabeli `wypozyczenia`
--
ALTER TABLE `wypozyczenia`
  ADD CONSTRAINT `wypozyczenia_ibfk_1` FOREIGN KEY (`id_egzemplarza`) REFERENCES `egzemplarze` (`id_egzemplarza`),
  ADD CONSTRAINT `wypozyczenia_ibfk_2` FOREIGN KEY (`id_czytelnika`) REFERENCES `czytelnicy` (`id_czytelnika`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
