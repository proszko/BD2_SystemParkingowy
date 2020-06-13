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
-- Table structure for table `wyjazdowe`
--

DROP TABLE IF EXISTS `wyjazdowe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wyjazdowe` (
  `id` int NOT NULL,
  `count_1gr` int NOT NULL DEFAULT '0',
  `count_2gr` int NOT NULL DEFAULT '0',
  `count_5gr` int NOT NULL DEFAULT '0',
  `count_10gr` int NOT NULL DEFAULT '0',
  `count_20gr` int NOT NULL DEFAULT '0',
  `count_50gr` int NOT NULL DEFAULT '0',
  `count_1zl` int NOT NULL DEFAULT '0',
  `count_2zl` int NOT NULL DEFAULT '0',
  `count_5zl` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  CONSTRAINT `wyjazdowa_bramka_fk` FOREIGN KEY (`id`) REFERENCES `bramki` (`id`),
  CONSTRAINT `wyjazdowe_chk_1` CHECK ((`count_1gr` >= 0)),
  CONSTRAINT `wyjazdowe_chk_2` CHECK ((`count_2gr` >= 0)),
  CONSTRAINT `wyjazdowe_chk_3` CHECK ((`count_5gr` >= 0)),
  CONSTRAINT `wyjazdowe_chk_4` CHECK ((`count_10gr` >= 0)),
  CONSTRAINT `wyjazdowe_chk_5` CHECK ((`count_20gr` >= 0)),
  CONSTRAINT `wyjazdowe_chk_6` CHECK ((`count_50gr` >= 0)),
  CONSTRAINT `wyjazdowe_chk_7` CHECK ((`count_1zl` >= 0)),
  CONSTRAINT `wyjazdowe_chk_8` CHECK ((`count_2zl` >= 0)),
  CONSTRAINT `wyjazdowe_chk_9` CHECK ((`count_5zl` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wyjazdowe`
--

LOCK TABLES `wyjazdowe` WRITE;
/*!40000 ALTER TABLE `wyjazdowe` DISABLE KEYS */;
INSERT INTO `wyjazdowe` VALUES (2,2,6,27,8,25,12,10,8,8),(4,26,48,14,13,14,28,7,18,9),(5,19,1,46,17,4,1,14,11,10),(7,30,1,18,21,14,6,13,15,12),(10,42,36,5,9,9,17,19,1,8),(12,28,6,48,13,10,12,18,10,11),(13,20,33,3,10,18,28,19,1,4),(15,23,18,23,5,17,9,15,19,8),(17,48,6,35,4,20,26,6,1,5),(18,30,46,41,10,8,12,3,12,7),(20,40,25,3,25,2,23,14,5,2),(21,45,8,2,24,26,28,1,9,3),(23,31,27,43,19,21,19,19,1,6),(25,43,4,40,22,11,20,3,19,3),(28,15,43,17,5,27,27,18,17,8),(29,4,40,41,20,29,25,5,17,8),(32,9,10,25,26,25,20,15,17,1),(34,37,25,13,25,12,18,14,16,13),(35,6,43,0,12,3,9,3,17,14),(38,13,17,49,25,10,3,10,5,13),(39,31,20,10,23,7,26,13,15,13),(42,0,22,9,19,17,1,8,0,11),(44,45,7,1,22,18,26,10,0,6),(46,10,34,40,29,14,13,15,11,8),(48,3,31,47,27,20,19,3,19,6),(50,8,26,8,7,20,23,14,8,12);
/*!40000 ALTER TABLE `wyjazdowe` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-12 14:30:57
