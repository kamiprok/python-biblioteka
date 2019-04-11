-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 11, 2019 at 08:24 PM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `biblioteka`
--

-- --------------------------------------------------------

--
-- Table structure for table `autorzy`
--

CREATE TABLE `autorzy` (
  `id_autora` int(11) NOT NULL,
  `imie` varchar(20) COLLATE utf8_polish_ci NOT NULL,
  `nazwisko` varchar(20) COLLATE utf8_polish_ci NOT NULL,
  `narodowosc` varchar(20) COLLATE utf8_polish_ci NOT NULL,
  `liczba_dziel` int(11) NOT NULL,
  `zyciorys` text COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Dumping data for table `autorzy`
--

INSERT INTO `autorzy` (`id_autora`, `imie`, `nazwisko`, `narodowosc`, `liczba_dziel`, `zyciorys`) VALUES
(1, 'Jan', 'Kochanowski', 'polska', 0, 'Jan Kochanowski (ur. 1530 w Sycynie, zm. 22 sierpnia 1584 w Lublinie) – polski poeta epoki renesansu, tłumacz, prepozyt kapituły katedralnej poznańskiej w latach 1564–1574[3], poeta nadworny Stefana Batorego w 1579 roku[4], sekretarz królewski i wojski sandomierski w latach 1579–1584[5]. Uważany jest za jednego z najwybitniejszych twórców renesansu w Europie i poetę, który najbardziej przyczynił się do rozwoju polskiego języka literackiego.'),
(2, 'Adam', 'Mickiewicz', 'polska', 0, 'Adam Bernard Mickiewicz (ur. 24 grudnia 1798 w Zaosiu lub Nowogródku[1][2][3], zm. 26 listopada 1855 w Stambule) – polski poeta, działacz polityczny, publicysta, tłumacz, filozof, działacz religijny, mistyk, organizator i dowódca wojskowy, nauczyciel akademicki.'),
(3, 'Juliusz', 'Słowacki', 'polska', 0, 'Juliusz Słowacki herbu Leliwa (ur. 4 września 1809 w Krzemieńcu, zm. 3 kwietnia 1849 w Paryżu[1]) – polski poeta, przedstawiciel romantyzmu, dramaturg i epistolograf. Obok Mickiewicza i Krasińskiego określany jako jeden z Wieszczów Narodowych. Twórca filozofii genezyjskiej (pneumatycznej), epizodycznie związany także z mesjanizmem polskim, był też mistykiem. Obok Mickiewicza uznawany powszechnie za największego przedstawiciela polskiego romantyzmu.'),
(4, 'Henryk', 'Sienkiewicz', 'polska', 0, 'Henryk Adam Aleksander Pius Sienkiewicz herbu Oszyk, kryptonim „Litwos”, „Musagetes”, pseudonim „Juliusz Polkowski”, „K. Dobrzyński” (ur. 5 maja 1846 w Woli Okrzejskiej, zm. 15 listopada 1916 w Vevey) – polski nowelista, powieściopisarz i publicysta; laureat Nagrody Nobla w dziedzinie literatury (1905) za całokształt twórczości[1], jeden z najpopularniejszych polskich pisarzy przełomu XIX i XX w.'),
(5, 'Homer', '', 'grecka', 0, 'Homer (stgr. Ὅμηρος, Hómēros, gr. Όμηρος) (VIII wiek p.n.e.) – grecki pieśniarz wędrowny (aojda), epik, śpiewak i recytator (rapsod). Uważa się go za ojca poezji epickiej. Najstarszy znany z imienia europejski poeta, który zapewne przejął dziedzictwo długiej i bogatej tradycji ustnej poezji heroicznej. Do jego dzieł zalicza się eposy: Iliadę i Odyseję. Grecka tradycja widziała w nim również autora poematów heroikomicznych Batrachomyomachia i Margites oraz Hymnów homeryckich. Żaden poeta grecki nie przewyższył sławą Homera. Na wyspach Ios i Chios wzniesiono poświęcone mu świątynie, a w Olimpii i Delfach postawiono jego posągi. Pizystrat wprowadził recytacje homeryckich poematów na Panatenajach.'),
(6, 'Franz', 'Kafka', 'niemiecka', 0, 'Franz Kafka (ur. 3 lipca 1883 w Pradze, zm. 3 czerwca 1924 w Kierling) – niemieckojęzyczny pisarz pochodzenia żydowskiego, przez całe życie związany z Pragą. W swoich powieściach stworzył model sytuacji zwanej sytuacją kafkowską i określanej w języku niemieckim za pomocą przymiotnika „kafkaesk”, którego istotą jest konflikt zniewolonej jednostki z anonimową, nadrzędną wobec niej instancją. Deformacja groteskowa, niejednoznaczne, paraboliczne obrazy oraz poczucie zagrożenia i niepewności składają się na panoramę literackiego świata Kafki.'),
(7, 'Fiodor', 'Dostojewski', 'rosyjska', 0, 'Fiodor Michajłowicz Dostojewski (ros. Фёдор Михайлович Достоевский; ur. 30 października?/11 listopada 1821 w Moskwie, Imperium Rosyjskie, zm. 28 stycznia?/9 lutego 1881 w Petersburgu, Imperium Rosyjskie) – rosyjski pisarz i myśliciel. Jeden z najbardziej wpływowych powieściopisarzy literatury rosyjskiej i światowej.'),
(8, 'William', 'Shakespeare', 'angielska', 0, 'William Shakespeare (Szekspir) (ur. prawdopodobnie 23 kwietnia 1564, data chrztu: 26 kwietnia 1564[2], w Stratford-upon-Avon, zm. 23 kwietnia?/3 maja 1616 tamże) – angielski poeta, dramaturg, aktor. Powszechnie uważany za jednego z najwybitniejszych pisarzy literatury angielskiej oraz reformatorów teatru[3].'),
(9, 'Dante', 'Alighieri', 'włoch', 0, 'Dante Alighieri (ur. w maju lub czerwcu 1265 we Florencji, zm. 13 lub 14 września 1321 w Rawennie) – włoski poeta, filozof i polityk.\r\n\r\nJego najwybitniejszym dziełem jest poemat Boska komedia, uważany za arcydzieło literatury światowej i szczytowe osiągnięcie literatury średniowiecznej. Utwór jest w całości napisany po włosku.'),
(10, 'Geoffrey', 'Chaucer', 'angielska', 0, 'Geoffrey Chaucer (ur. ok. 1343, możliwe że w Londynie, ale dokładniejsza data i miejsce nie są znane, zm. 25 października 1400) – angielski poeta, filozof i dyplomata.');

-- --------------------------------------------------------

--
-- Table structure for table `czytelnicy`
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
-- Table structure for table `egzemplarze`
--

CREATE TABLE `egzemplarze` (
  `id_egzemplarza` int(11) NOT NULL,
  `nr_bibilioteczny` int(11) NOT NULL,
  `id_ksiazki` int(11) NOT NULL,
  `wydanie` smallint(6) NOT NULL,
  `rok_publikacji` year(4) NOT NULL,
  `dostepnosc` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `gatunki`
--

CREATE TABLE `gatunki` (
  `nazwa` varchar(30) COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Dumping data for table `gatunki`
--

INSERT INTO `gatunki` (`nazwa`) VALUES
('Dramat'),
('Epika'),
('Fantastyka'),
('Poezja'),
('Sci-Fi');

-- --------------------------------------------------------

--
-- Table structure for table `ksiazki`
--

CREATE TABLE `ksiazki` (
  `id_ksiazki` int(11) NOT NULL,
  `id_autora` int(11) NOT NULL,
  `wydawnictwo` varchar(30) COLLATE utf8_polish_ci NOT NULL,
  `gatunek` varchar(30) COLLATE utf8_polish_ci NOT NULL,
  `tytul` varchar(70) COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Dumping data for table `ksiazki`
--

INSERT INTO `ksiazki` (`id_ksiazki`, `id_autora`, `wydawnictwo`, `gatunek`, `tytul`) VALUES
(3, 1, 'Dragon', 'Poezja', 'Fraszki, pieśni, treny. Dzieła wybrane'),
(4, 1, 'Nowa Era', 'Epika', 'Odprawa posłów greckich'),
(5, 2, 'Nowa Era', 'Epika', 'Pan Tadeusz'),
(6, 2, 'Świat Książki', 'Poezja', 'Sonety krymskie'),
(7, 3, 'Świat Książki', 'Dramat', 'Balladyna'),
(8, 3, 'WSiP', 'Dramat', 'Kordian'),
(9, 4, 'WSiP', 'Epika', 'Quo Vadis'),
(10, 4, 'WSiP', 'Epika', 'Krzyżacy'),
(11, 4, 'WSiP', 'Epika', 'Ogniem i Mieczem'),
(12, 4, 'Nowa Era', 'Dramat', 'Janko Muzykant'),
(13, 5, 'Dragon', 'Dramat', 'Odyseja'),
(14, 5, 'Reader\'s Digest', 'Dramat', 'Iliada'),
(15, 6, 'Dragon', 'Epika', 'Aforyzmy z Zürau'),
(16, 6, 'Nowa Era', 'Epika', 'Ameryka'),
(17, 7, 'Reader\'s Digest', 'Epika', 'Aforyzmy'),
(18, 7, 'WSiP', 'Epika', 'Białe noce'),
(19, 8, 'Świat Książki', 'Dramat', 'Makbet'),
(20, 8, 'Świat Książki', 'Dramat', 'Hamlet'),
(21, 8, 'Świat Książki', 'Dramat', 'Romeo i Julia'),
(22, 9, 'Dragon', 'Dramat', 'Boska Komedia'),
(23, 9, 'Nowa Era', 'Dramat', 'Inferno'),
(24, 10, 'Reader\'s Digest', 'Epika', 'Opowieści kanterberyjskie'),
(25, 10, 'Reader\'s Digest', 'Epika', 'Opowieść Rycerza');

-- --------------------------------------------------------

--
-- Table structure for table `wydawnictwa`
--

CREATE TABLE `wydawnictwa` (
  `nazwa` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  `kraj` varchar(30) COLLATE utf8_polish_ci NOT NULL,
  `miasto` varchar(30) COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Dumping data for table `wydawnictwa`
--

INSERT INTO `wydawnictwa` (`nazwa`, `kraj`, `miasto`) VALUES
('Dragon', 'USA', 'Washington'),
('Nowa Era', 'Polska', 'Białystok'),
('Reader\'s Digest', 'Anglia', 'London'),
('Świat Książki', 'Polska', 'Kraków'),
('WSiP', 'Polska', 'Warszawa');

-- --------------------------------------------------------

--
-- Table structure for table `wypozyczenia`
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
-- Indexes for dumped tables
--

--
-- Indexes for table `autorzy`
--
ALTER TABLE `autorzy`
  ADD PRIMARY KEY (`id_autora`);

--
-- Indexes for table `czytelnicy`
--
ALTER TABLE `czytelnicy`
  ADD PRIMARY KEY (`id_czytelnika`);

--
-- Indexes for table `egzemplarze`
--
ALTER TABLE `egzemplarze`
  ADD PRIMARY KEY (`id_egzemplarza`),
  ADD KEY `id_ksiazki` (`id_ksiazki`);

--
-- Indexes for table `gatunki`
--
ALTER TABLE `gatunki`
  ADD PRIMARY KEY (`nazwa`);

--
-- Indexes for table `ksiazki`
--
ALTER TABLE `ksiazki`
  ADD PRIMARY KEY (`id_ksiazki`),
  ADD KEY `id_autora` (`id_autora`),
  ADD KEY `id_wydawnictwa` (`wydawnictwo`),
  ADD KEY `id_gatunku` (`gatunek`);

--
-- Indexes for table `wydawnictwa`
--
ALTER TABLE `wydawnictwa`
  ADD PRIMARY KEY (`nazwa`);

--
-- Indexes for table `wypozyczenia`
--
ALTER TABLE `wypozyczenia`
  ADD PRIMARY KEY (`id_wypozyczenia`),
  ADD KEY `id_egzemplarza` (`id_egzemplarza`),
  ADD KEY `id_czytelnika` (`id_czytelnika`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `autorzy`
--
ALTER TABLE `autorzy`
  MODIFY `id_autora` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `czytelnicy`
--
ALTER TABLE `czytelnicy`
  MODIFY `id_czytelnika` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `egzemplarze`
--
ALTER TABLE `egzemplarze`
  MODIFY `id_egzemplarza` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `ksiazki`
--
ALTER TABLE `ksiazki`
  MODIFY `id_ksiazki` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `wypozyczenia`
--
ALTER TABLE `wypozyczenia`
  MODIFY `id_wypozyczenia` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `egzemplarze`
--
ALTER TABLE `egzemplarze`
  ADD CONSTRAINT `egzemplarze_ibfk_1` FOREIGN KEY (`id_ksiazki`) REFERENCES `ksiazki` (`id_ksiazki`);

--
-- Constraints for table `ksiazki`
--
ALTER TABLE `ksiazki`
  ADD CONSTRAINT `ksiazki_ibfk_1` FOREIGN KEY (`id_autora`) REFERENCES `autorzy` (`id_autora`),
  ADD CONSTRAINT `ksiazki_ibfk_4` FOREIGN KEY (`wydawnictwo`) REFERENCES `wydawnictwa` (`nazwa`),
  ADD CONSTRAINT `ksiazki_ibfk_5` FOREIGN KEY (`gatunek`) REFERENCES `gatunki` (`nazwa`);

--
-- Constraints for table `wypozyczenia`
--
ALTER TABLE `wypozyczenia`
  ADD CONSTRAINT `wypozyczenia_ibfk_1` FOREIGN KEY (`id_egzemplarza`) REFERENCES `egzemplarze` (`id_egzemplarza`),
  ADD CONSTRAINT `wypozyczenia_ibfk_2` FOREIGN KEY (`id_czytelnika`) REFERENCES `czytelnicy` (`id_czytelnika`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
