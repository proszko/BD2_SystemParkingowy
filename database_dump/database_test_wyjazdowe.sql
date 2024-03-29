CREATE DATABASE  IF NOT EXISTS `database_test` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `database_test`;
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
INSERT INTO `wyjazdowe` VALUES (1,49,45,26,28,4,27,1,15,7),(3,14,46,39,2,4,14,17,1,10),(6,9,46,3,16,17,7,11,0,5),(7,40,48,19,0,29,23,19,11,13),(10,32,34,22,5,17,8,15,19,8),(11,42,28,13,21,21,12,18,7,0),(14,10,45,45,24,11,12,19,11,14),(16,6,38,22,27,5,6,9,16,9),(17,36,37,26,12,16,14,14,5,3),(19,9,16,2,9,10,24,0,14,9),(22,41,15,4,14,5,13,14,5,2),(24,5,48,27,24,13,22,9,2,2),(26,24,47,11,9,28,23,2,3,7),(27,6,3,48,18,7,9,15,1,14),(29,35,31,47,27,19,18,0,8,13),(31,6,4,2,29,20,16,12,8,6),(33,33,9,44,26,21,28,11,0,6),(36,49,34,26,15,2,25,0,9,6),(38,28,31,23,13,24,22,5,2,11),(39,29,30,11,11,4,20,18,10,11),(41,20,35,15,12,2,8,2,14,4),(43,19,48,36,22,14,5,8,12,11),(45,46,21,18,15,15,2,16,15,7),(48,12,33,31,4,26,26,15,5,1),(50,26,19,19,23,22,10,11,17,8),(52,15,39,1,21,18,24,5,17,8),(53,17,46,29,4,1,21,9,2,4),(56,3,21,0,21,15,15,19,4,5),(58,4,15,17,23,25,26,17,16,7),(59,1,29,45,23,5,18,10,15,2),(62,32,36,35,9,12,3,7,8,0),(63,49,41,6,5,14,25,15,7,6),(65,6,17,18,22,20,5,17,15,4),(67,7,44,48,5,1,18,19,18,11),(70,48,29,3,16,15,28,5,9,7),(72,12,30,16,25,6,15,18,1,8),(74,33,30,4,18,23,0,16,0,11),(76,29,36,44,7,19,13,5,0,5),(78,38,35,10,27,1,12,17,4,7),(79,40,26,13,21,23,20,3,16,9),(81,29,2,26,14,26,26,15,4,11),(83,2,2,4,7,2,17,13,13,6),(85,47,24,32,23,0,19,5,7,2),(87,30,28,1,14,7,23,3,10,3),(90,19,16,22,8,0,9,9,8,9),(92,1,10,45,28,2,14,3,8,9),(94,39,3,0,25,5,11,7,14,6),(96,7,19,24,9,2,15,4,13,10),(98,21,4,5,7,0,8,7,1,3),(100,49,8,44,29,8,10,0,0,0),(102,4,19,32,2,12,24,16,12,9),(104,20,4,9,22,4,13,16,16,9),(105,36,34,12,5,6,14,14,4,14),(107,11,7,5,2,2,4,9,18,3),(110,22,27,16,1,7,3,17,19,3),(112,17,48,39,2,28,17,1,10,5),(113,13,13,29,3,25,24,11,9,8),(115,21,24,6,4,13,23,9,2,2),(118,20,29,34,20,12,29,14,12,14),(120,1,7,36,4,17,15,16,12,8),(121,1,18,41,29,13,10,8,0,14),(123,27,45,44,22,0,25,5,14,11),(125,42,42,34,27,13,16,7,4,1),(128,35,15,20,4,13,25,19,3,14),(129,19,49,40,1,26,5,4,13,9),(132,13,17,49,25,9,29,18,14,12),(134,6,3,49,21,17,25,9,16,9),(135,39,49,29,28,0,5,17,16,7),(138,48,20,7,16,7,17,3,3,4),(139,47,42,20,16,13,17,11,2,13),(142,13,26,42,19,19,10,15,18,2),(144,0,29,45,23,5,16,4,10,14),(146,9,5,45,8,18,9,14,14,5),(148,38,35,11,1,16,19,11,18,12),(150,28,13,29,4,0,16,16,6,3),(152,4,39,35,6,25,21,19,14,9),(154,7,38,19,19,3,19,18,12,4),(155,37,39,36,7,0,9,10,15,4),(157,7,42,39,11,18,25,9,15,7),(159,9,22,35,3,15,6,10,0,8),(162,34,39,45,4,0,18,0,4,1),(163,46,14,31,7,13,12,16,16,9),(166,39,49,29,28,1,12,18,5,9),(167,19,49,39,28,12,8,3,0,7),(169,21,32,49,0,3,16,6,0,3),(171,45,48,3,14,5,12,11,13,9),(173,12,13,28,1,14,9,3,19,5),(176,48,31,13,14,18,18,3,2,0),(178,39,41,39,13,26,3,16,18,1),(180,39,28,24,22,9,8,8,6,3),(182,18,5,22,27,7,13,11,8,5),(183,27,33,37,21,11,21,9,5,13),(185,38,5,9,18,17,28,2,12,13),(187,32,25,28,11,3,14,0,15,9),(189,1,9,42,21,29,21,13,4,1),(191,36,21,48,16,25,17,8,5,2),(193,45,4,37,12,27,7,11,2,12),(195,42,36,7,14,0,19,4,3,1),(197,2,45,20,8,7,11,3,15,6),(200,32,49,49,1,6,0,7,15,11),(201,21,47,23,14,1,23,15,11,6),(204,26,17,5,14,3,3,4,16,4),(205,9,49,19,29,20,15,9,18,2),(208,47,16,39,29,13,12,13,1,6),(210,47,21,16,10,23,26,19,6,9),(211,7,46,8,0,19,5,19,8,0),(213,3,6,22,27,4,29,8,5,2),(216,47,12,17,1,5,21,1,4,11),(218,18,23,9,18,13,14,19,9,6),(219,38,24,8,12,14,6,12,9,7),(221,48,23,18,15,12,14,4,13,9),(223,9,2,33,5,28,4,19,7,12),(225,11,27,5,26,3,29,9,9,0),(227,32,9,0,13,4,14,0,11,11),(230,3,4,11,26,20,22,13,4,0),(232,27,31,26,21,0,29,15,0,9),(233,14,24,30,15,23,10,6,13,6),(235,2,47,31,8,16,26,14,18,8),(238,1,23,9,18,12,10,7,18,7),(239,41,28,19,5,22,6,15,4,13),(241,32,31,11,8,20,16,15,1,3),(243,40,17,19,25,2,24,18,4,2),(245,17,8,38,11,19,3,11,12,4),(248,35,28,38,3,9,6,3,4,10),(250,32,9,48,10,23,26,1,14,5),(251,29,44,35,27,11,3,10,5,12),(253,16,5,30,19,14,15,1,15,9),(255,47,38,2,28,18,8,9,10,2),(257,14,47,43,15,0,13,3,12,8),(260,41,28,15,26,13,18,13,10,10),(262,43,11,28,4,29,14,9,18,3),(263,13,36,39,24,21,4,12,13,6),(266,8,25,5,29,18,3,14,5,2),(268,47,14,32,10,23,28,6,16,1),(269,47,27,42,19,21,16,11,6,12),(272,5,4,7,14,0,18,19,1,6),(274,45,13,32,12,3,11,11,14,12),(275,48,20,7,15,4,4,5,0,4),(278,19,3,7,17,12,10,9,5,1),(280,23,5,6,10,10,21,10,7,5),(281,36,26,24,25,21,2,4,15,5),(283,23,9,30,13,13,26,1,16,11),(286,21,42,46,3,25,26,15,7,6),(287,1,45,21,12,23,20,0,4,13),(290,39,17,15,16,22,5,11,8,6),(292,45,8,5,1,26,7,13,9,7),(294,3,42,2,20,7,8,11,0,6),(295,48,31,13,12,8,5,0,13,5),(298,30,49,8,26,24,15,3,6,0),(299,6,30,33,14,14,29,7,18,9),(341,15,31,11,9,23,2,0,18,7),(342,40,23,45,5,5,11,8,17,0),(343,33,10,3,21,11,20,6,10,8),(344,22,23,49,16,21,28,12,5,8),(345,48,6,36,8,8,13,9,18,4),(346,38,44,5,28,9,24,2,5,13),(347,31,26,37,4,13,26,1,15,7),(348,16,4,24,4,7,25,8,12,12),(349,10,29,17,28,22,27,6,17,6),(350,27,19,14,9,23,25,19,4,4),(351,44,23,34,1,4,19,15,19,6),(352,20,34,12,3,25,25,13,17,5),(353,6,28,23,18,22,24,18,0,6),(354,4,5,16,7,10,28,13,11,11),(355,4,9,34,25,7,17,5,11,0),(356,26,27,4,25,29,10,16,2,0),(357,35,26,24,26,26,26,13,16,1),(358,0,35,26,15,1,20,4,2,12),(359,42,36,4,8,2,18,16,7,5),(360,34,18,36,17,20,22,12,16,3),(361,34,38,37,13,1,26,4,8,9),(362,34,30,0,6,1,16,12,8,4),(363,14,25,32,21,20,7,3,0,10),(364,23,11,35,26,9,28,14,15,12),(365,32,42,13,24,9,5,16,13,14),(366,35,34,15,14,15,4,2,2,4),(367,5,31,43,14,22,8,2,18,1),(368,42,46,2,14,7,25,9,17,14),(369,2,23,8,14,25,25,13,16,2),(370,13,42,23,23,17,15,16,13,11),(371,48,23,23,26,0,12,2,4,12),(372,22,37,19,20,9,13,8,12,13),(373,30,17,48,22,25,28,5,10,12),(374,29,20,15,9,21,15,9,17,14),(375,3,25,16,4,24,16,6,1,4),(376,19,49,37,24,22,10,11,13,12),(377,0,28,42,15,29,13,4,17,10),(378,40,49,24,15,4,5,8,12,13),(379,32,23,21,20,5,26,16,8,11),(380,28,25,42,21,1,0,19,16,2);
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

-- Dump completed on 2020-06-14  0:29:38
