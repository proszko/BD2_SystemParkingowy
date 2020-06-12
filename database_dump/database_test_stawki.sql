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
-- Table structure for table `stawki`
--

DROP TABLE IF EXISTS `stawki`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stawki` (
  `opłata_godzinowa` float NOT NULL,
  `opłata_wjazdowa` float NOT NULL,
  `strefy_id` int NOT NULL,
  `typy_pojazdów_id` int NOT NULL,
  PRIMARY KEY (`strefy_id`,`typy_pojazdów_id`),
  KEY `stawki_typy_pojazdów_fk` (`typy_pojazdów_id`),
  CONSTRAINT `stawki_strefy_fk` FOREIGN KEY (`strefy_id`) REFERENCES `strefy` (`id`),
  CONSTRAINT `stawki_typy_pojazdów_fk` FOREIGN KEY (`typy_pojazdów_id`) REFERENCES `typy_pojazdów` (`id`),
  CONSTRAINT `stawki_chk_1` CHECK ((`opłata_godzinowa` >= 0)),
  CONSTRAINT `stawki_chk_2` CHECK ((`opłata_wjazdowa` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stawki`
--

LOCK TABLES `stawki` WRITE;
/*!40000 ALTER TABLE `stawki` DISABLE KEYS */;
INSERT INTO `stawki` VALUES (1.8,1.36,1,1),(2.62,0.96,1,2),(2.17,1.76,1,3),(1.02,1.03,1,4),(1.31,1.03,1,5),(2.31,1.22,2,1),(1.79,0.91,2,2),(1.92,1.13,2,3),(2.58,1.32,2,4),(1.88,1.55,2,5),(2.81,1.49,3,1),(1.31,0.94,3,2),(1.6,1.33,3,3),(2.98,1.66,3,4),(1.85,0.87,3,5),(1.54,1.72,4,1),(2.46,0.89,4,2),(2.13,1.49,4,3),(1.19,0.92,4,4),(1.99,1.21,4,5),(1.15,1.38,5,1),(1.37,1.49,5,2),(1.62,1.4,5,3),(1.57,0.97,5,4),(2.47,1.04,5,5),(2.14,0.87,6,1),(1.72,1.62,6,2),(1.53,1.74,6,3),(2.62,1.74,6,4),(1.28,1.51,6,5),(2.88,1.39,7,1),(1.67,1.52,7,2),(1.33,1.21,7,3),(1.63,1.03,7,4),(2.86,1.63,7,5),(1.5,1.65,8,1),(1.17,1.32,8,2),(2.3,1.76,8,3),(2.72,1.61,8,4),(2.52,1.66,8,5),(1.21,1.63,9,1),(2.5,1.43,9,2),(2.07,1.79,9,3),(1.7,1.45,9,4),(2.7,1.58,9,5),(2.3,1.08,10,1),(1.27,0.82,10,2),(1.56,1,10,3),(1.1,1.14,10,4),(2.21,1.71,10,5);
/*!40000 ALTER TABLE `stawki` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-12 14:30:55
