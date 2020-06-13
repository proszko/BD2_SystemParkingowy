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
-- Table structure for table `pojemności`
--

DROP TABLE IF EXISTS `pojemności`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pojemności` (
  `miejsca` int NOT NULL DEFAULT '0',
  `miejsca_zajete` int NOT NULL DEFAULT '0',
  `strefy_id` int NOT NULL,
  `typy_pojazdów_id` int NOT NULL,
  PRIMARY KEY (`strefy_id`,`typy_pojazdów_id`),
  KEY `pojemności_typy_pojazdów_fk` (`typy_pojazdów_id`),
  CONSTRAINT `pojemności_strefy_fk` FOREIGN KEY (`strefy_id`) REFERENCES `strefy` (`id`),
  CONSTRAINT `pojemności_typy_pojazdów_fk` FOREIGN KEY (`typy_pojazdów_id`) REFERENCES `typy_pojazdów` (`id`),
  CONSTRAINT `pojemności_chk_1` CHECK ((`miejsca` >= 0)),
  CONSTRAINT `pojemności_chk_2` CHECK ((`miejsca_zajete` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pojemności`
--

LOCK TABLES `pojemności` WRITE;
/*!40000 ALTER TABLE `pojemności` DISABLE KEYS */;
INSERT INTO `pojemności` VALUES (3,0,1,1),(4,0,1,2),(5,0,1,3),(5,0,1,4),(3,0,1,5),(2,0,2,1),(2,0,2,2),(5,0,2,3),(4,0,2,4),(2,0,2,5),(3,0,3,1),(8,1,3,2),(4,2,3,3),(5,0,3,4),(3,0,3,5),(4,0,4,1),(5,0,4,2),(5,0,4,3),(3,0,4,4),(4,2,4,5),(2,1,5,1),(3,0,5,2),(4,1,5,3),(4,1,5,4),(5,0,5,5),(4,0,6,1),(8,0,6,2),(3,0,6,3),(5,0,6,4),(3,2,6,5),(5,0,7,1),(2,0,7,2),(7,1,7,3),(6,0,7,4),(4,0,7,5),(3,1,8,1),(2,0,8,2),(4,0,8,3),(8,0,8,4),(3,0,8,5),(3,0,9,1),(5,0,9,2),(3,0,9,3),(3,0,9,4),(6,0,9,5),(3,0,10,1),(3,0,10,2),(4,0,10,3),(4,0,10,4),(2,0,10,5);
/*!40000 ALTER TABLE `pojemności` ENABLE KEYS */;
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
