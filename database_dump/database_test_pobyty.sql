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
-- Table structure for table `pobyty`
--

DROP TABLE IF EXISTS `pobyty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pobyty` (
  `id` int NOT NULL AUTO_INCREMENT,
  `godzina_rozpoczecia` datetime NOT NULL,
  `godzina_zakonczenia` datetime DEFAULT NULL,
  `należność` float DEFAULT NULL,
  `konta_id` int DEFAULT NULL,
  `wjazdowe_bramki_id` int NOT NULL,
  `wyjazdowe_bramki_id` int DEFAULT NULL,
  `selektor` char(15) NOT NULL,
  `pojazdy_rejestracja` varchar(8) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pobyty_konta_fk` (`konta_id`),
  KEY `pobyty_pojazdy_fk` (`pojazdy_rejestracja`),
  KEY `pobyty_wjazdowe_fk` (`wjazdowe_bramki_id`),
  KEY `pobyty_wyjazdowe_fk` (`wyjazdowe_bramki_id`),
  CONSTRAINT `pobyty_konta_fk` FOREIGN KEY (`konta_id`) REFERENCES `konta` (`id`),
  CONSTRAINT `pobyty_pojazdy_fk` FOREIGN KEY (`pojazdy_rejestracja`) REFERENCES `pojazdy` (`rejestracja`),
  CONSTRAINT `pobyty_wjazdowe_fk` FOREIGN KEY (`wjazdowe_bramki_id`) REFERENCES `wjazdowe` (`id`),
  CONSTRAINT `pobyty_wyjazdowe_fk` FOREIGN KEY (`wyjazdowe_bramki_id`) REFERENCES `wyjazdowe` (`id`),
  CONSTRAINT `pobyty_chk_1` CHECK ((`należność` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pobyty`
--

LOCK TABLES `pobyty` WRITE;
/*!40000 ALTER TABLE `pobyty` DISABLE KEYS */;
INSERT INTO `pobyty` VALUES (1,'2020-04-10 08:04:53','2020-04-10 08:39:49',2.11,NULL,9,13,'z_parkowaniem','BKT36YY'),(2,'2020-02-07 22:45:54','2020-02-07 22:52:34',1.33,22,37,29,'bez_parkowania','TKX35FP'),(3,'2020-03-10 13:18:32','2020-03-10 13:34:04',2.54,NULL,27,12,'bez_parkowania','MFX02EV'),(4,'2020-01-01 00:00:03',NULL,NULL,6,9,NULL,'z_parkowaniem','HZW87NU'),(5,'2020-01-28 17:01:04',NULL,NULL,2,9,NULL,'bez_parkowania','RSX32UZ'),(6,'2020-04-15 16:33:53',NULL,NULL,48,36,NULL,'z_parkowaniem','RBZ27PY'),(7,'2020-03-18 03:45:24','2020-03-18 03:55:24',3.15,15,30,21,'z_parkowaniem','BKT36YY'),(8,'2020-03-27 08:01:53',NULL,NULL,15,47,NULL,'bez_parkowania','CNF85SX'),(9,'2020-05-09 01:15:53','2020-05-09 01:15:53',1.66,1,1,29,'bez_parkowania','CVA00SS'),(10,'2020-04-04 16:39:53','2020-04-04 18:18:04',5.75,41,43,13,'z_parkowaniem','DIM95DC'),(11,'2020-01-21 11:48:03','2020-01-21 11:48:14',1.74,25,8,20,'bez_parkowania','HSP83MK'),(12,'2020-02-08 02:59:02','2020-02-08 06:01:36',6.97,25,47,18,'z_parkowaniem','CNF85SX'),(13,'2020-04-11 02:43:07','2020-04-11 04:42:07',4.57,5,16,2,'bez_parkowania','XUJ36SL'),(14,'2020-01-04 05:52:06',NULL,NULL,2,47,NULL,'z_parkowaniem','TKX35FP'),(15,'2020-02-18 20:42:31','2020-02-18 23:24:45',9.68,42,33,21,'bez_parkowania','ACW88EX'),(16,'2020-03-11 20:30:57',NULL,NULL,23,1,NULL,'z_parkowaniem','SMS23EB'),(17,'2020-04-17 05:41:27',NULL,NULL,39,6,NULL,'z_parkowaniem','NJE60PO'),(18,'2020-01-22 09:11:15',NULL,NULL,2,30,NULL,'bez_parkowania','MFX02EV'),(19,'2020-02-24 21:46:15','2020-02-24 23:16:52',7.62,25,37,2,'bez_parkowania','CVA00SS'),(20,'2020-01-01 01:37:15','2020-01-01 04:11:34',8.66,29,6,44,'z_parkowaniem','SMS23EB'),(21,'2020-03-29 09:25:23','2020-03-29 09:29:19',2.79,42,8,34,'z_parkowaniem','ACW88EX'),(22,'2020-02-25 15:55:31','2020-02-25 18:58:27',7.24,13,19,28,'bez_parkowania','ORH84ZW'),(23,'2020-03-26 14:48:25',NULL,NULL,38,8,NULL,'bez_parkowania','YHL89NA'),(24,'2020-01-01 00:00:04',NULL,NULL,8,1,NULL,'z_parkowaniem','YHL89NA'),(25,'2020-01-01 00:05:48','2020-01-01 01:43:27',3.3,22,40,17,'z_parkowaniem','KJA13OJ'),(26,'2020-01-07 23:43:49',NULL,NULL,NULL,22,NULL,'bez_parkowania','JIZ90GV'),(27,'2020-03-30 19:08:36','2020-03-30 21:10:55',9.22,45,6,44,'bez_parkowania','NJH35JJ'),(28,'2020-01-01 00:01:12',NULL,NULL,45,8,NULL,'z_parkowaniem','NWL56RH'),(29,'2020-02-29 23:09:32','2020-03-01 01:35:04',10.6,NULL,37,2,'z_parkowaniem','MFX02EV'),(30,'2020-01-04 23:59:59','2020-01-05 01:01:02',7.11,46,16,29,'bez_parkowania','RSX32UZ'),(31,'2020-01-01 00:00:11','2020-01-01 00:32:17',4.64,42,1,2,'bez_parkowania','KJA13OJ'),(32,'2020-03-17 09:47:25','2020-03-17 10:49:24',7.11,39,1,29,'z_parkowaniem','OTD32ED'),(33,'2020-02-19 05:42:38','2020-02-19 08:30:45',10.03,9,3,23,'bez_parkowania','HPQ82KV'),(34,'2020-04-23 17:12:06','2020-04-23 17:28:06',2.72,39,37,2,'z_parkowaniem','NWL56RH'),(35,'2020-01-01 00:10:48',NULL,NULL,26,24,NULL,'bez_parkowania','SRO23YA'),(36,'2020-01-01 00:00:05','2020-01-01 00:41:37',3.43,39,49,5,'z_parkowaniem','YCU13DU'),(37,'2020-03-17 12:56:33','2020-03-17 15:30:36',9.68,49,33,21,'z_parkowaniem','YCU13DU'),(38,'2020-01-17 09:00:23','2020-01-17 11:48:49',8.27,40,41,13,'bez_parkowania','CNF85SX'),(39,'2020-03-18 11:01:28','2020-03-18 11:02:28',3.35,46,26,13,'z_parkowaniem','YHL89NA'),(40,'2020-01-01 00:00:26','2020-01-01 01:33:23',4.97,42,49,5,'bez_parkowania','DIM95DC'),(41,'2020-03-11 07:15:46','2020-03-11 08:44:43',7.62,49,14,29,'bez_parkowania','XMQ55ED'),(42,'2020-01-01 00:24:42',NULL,NULL,41,31,NULL,'z_parkowaniem','FBF15XB'),(43,'2020-03-08 23:50:18',NULL,NULL,36,27,NULL,'z_parkowaniem','MFX02EV'),(44,'2020-01-01 00:01:28',NULL,NULL,24,6,NULL,'bez_parkowania','RBZ27PY'),(45,'2020-03-10 13:12:45',NULL,NULL,34,3,NULL,'z_parkowaniem','SMS23EB'),(46,'2020-01-23 05:54:56',NULL,NULL,16,24,NULL,'bez_parkowania','ACW88EX'),(47,'2020-03-23 06:53:55',NULL,NULL,15,40,NULL,'z_parkowaniem','QRF42TM'),(48,'2020-03-22 01:57:05',NULL,NULL,NULL,1,NULL,'bez_parkowania','IUZ87WY'),(49,'2020-01-27 09:22:38',NULL,NULL,NULL,47,NULL,'bez_parkowania','KJA13OJ'),(50,'2020-05-09 12:58:10',NULL,NULL,NULL,8,NULL,'z_parkowaniem','YCU13DU');
/*!40000 ALTER TABLE `pobyty` ENABLE KEYS */;
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
