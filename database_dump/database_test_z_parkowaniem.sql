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
-- Table structure for table `z_parkowaniem`
--

DROP TABLE IF EXISTS `z_parkowaniem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `z_parkowaniem` (
  `id` int NOT NULL,
  `miejsca_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `z_parkowaniem_miejsca_fk` (`miejsca_id`),
  CONSTRAINT `z_parkowaniem_miejsca_fk` FOREIGN KEY (`miejsca_id`) REFERENCES `miejsca` (`id`),
  CONSTRAINT `z_parkowaniem_pobyt_fk` FOREIGN KEY (`id`) REFERENCES `pobyty` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `z_parkowaniem`
--

LOCK TABLES `z_parkowaniem` WRITE;
/*!40000 ALTER TABLE `z_parkowaniem` DISABLE KEYS */;
INSERT INTO `z_parkowaniem` VALUES (24,1),(39,9),(16,10),(43,11),(6,12),(4,13),(42,14),(34,16),(45,23),(20,24),(10,26),(32,29),(37,30),(29,31),(47,32),(14,47),(36,49),(17,55),(21,63),(28,72),(12,95),(1,117),(25,126),(7,135),(50,173);
/*!40000 ALTER TABLE `z_parkowaniem` ENABLE KEYS */;
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
