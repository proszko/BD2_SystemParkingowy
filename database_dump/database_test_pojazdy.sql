-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: database_test
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `pojazdy`
--

DROP TABLE IF EXISTS `pojazdy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pojazdy` (
  `rejestracja` varchar(8) NOT NULL,
  `typy_pojazdów_id` int NOT NULL,
  `model` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`rejestracja`),
  KEY `pojazdy_typy_pojazdów_fk` (`typy_pojazdów_id`),
  CONSTRAINT `pojazdy_typy_pojazdów_fk` FOREIGN KEY (`typy_pojazdów_id`) REFERENCES `typy_pojazdów` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pojazdy`
--

LOCK TABLES `pojazdy` WRITE;
/*!40000 ALTER TABLE `pojazdy` DISABLE KEYS */;
INSERT INTO `pojazdy` VALUES ('ACW88EX',5,'Mitsubishi Lancer'),('AJE95HU',4,'Toyota Auris'),('BIC20XX',2,'Mercedes-Benz Viano'),('BKT36YY',4,'Fiat Panda'),('CBI92LA',1,'Fiat Ducato'),('CNF85SX',2,'Toyota Corolla'),('CVA00SS',4,'Suzuki Katana'),('CXN89BH',4,'Lamborghini Gallardo'),('DIM95DC',3,'Dodge Viper'),('FBF15XB',3,'Daewoo Leganza'),('FQP19TW',3,'Audi A4'),('GSA99GJ',3,'Chevrolet Camaro'),('HJC61FF',5,'Peugeot 2008'),('HPQ82KV',1,'Honda Civic'),('HSP83MK',4,'Kawasaki VN700'),('HUY35JF',4,'Opel Astra'),('HZW87NU',5,'Fiat 126p'),('IIH44LG',5,'Toyota Avensis'),('IJY36QQ',4,'Nissan Almera'),('IUZ87WY',3,'BMW X7'),('JIZ90GV',4,'Suzuki Ignis'),('KJA13OJ',4,'Subaru Impreza'),('MFX02EV',4,'Mercedes-Benz Citan'),('MKY72RP',2,'Subaru XT76'),('NJE60PO',1,'Fiat Punto'),('NJH35JJ',5,'Toyota Starlet'),('NWL56RH',5,'Lamborghini Espada'),('OAS70GP',4,'Volkswagen Golf'),('OAU46ZX',2,NULL),('ORH84ZW',3,'Kia K9'),('OTD32ED',1,'Mitsubishi 500'),('OWF36TR',2,'Peugeot 404'),('QRF42TM',5,'Daewoo Matiz'),('RBZ27PY',1,'Toyota Yaris'),('RSX32UZ',1,'Mercedes-Benz Actros MP4'),('RXX59MX',5,'Dodge Durango'),('SMS23EB',3,'Subaru Exiga Concept'),('SRO23YA',2,'Fiat Seicento'),('TEG17JI',3,NULL),('TKX35FP',3,'Audi A3'),('UUC97CX',4,'Kia Cerato'),('VNA71KB',5,'Suzuki Swift'),('VPB59CT',5,'Mitsubishi Colt'),('WFB31DT',5,'Volkswagen Passat'),('WGY28IG',3,'Toyota Mark x'),('XMQ55ED',4,'Opel Olympia'),('XUJ36SL',5,'Kia Sportage'),('YCU13DU',5,'Kia Cee\'d'),('YHL89NA',2,'Kawasaki VN1500'),('ZVY24IC',1,'Subaru Leone');
/*!40000 ALTER TABLE `pojazdy` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-12 14:30:56
