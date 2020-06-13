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
-- Table structure for table `strefy`
--

DROP TABLE IF EXISTS `strefy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `strefy` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nazwa` varchar(40) NOT NULL,
  `kod` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `strefy`
--

LOCK TABLES `strefy` WRITE;
/*!40000 ALTER TABLE `strefy` DISABLE KEYS */;
INSERT INTO `strefy` VALUES (1,'Warszawa Zachodnia WKD','TR-460'),(2,'Warszawa Radość','VF-099'),(3,'Warszawa Stadion','QK-302'),(4,'Warszawa Żerań','RF-623'),(5,'Warszawa Aleje Jerozolimskie','CP-022'),(6,'Warszawa Gdańska','QF-685'),(7,'Warszawa Ursus-Niedźwiadek','KR-996'),(8,'Warszawa Włochy (przystanek kolejowy)','JQ-587'),(9,'Warszawa Ochota (przystanek kolejowy)','EX-167'),(10,'Warszawa Koło','RJ-847'),(11,'Warszawa Ursus Północny','NE-158'),(12,'Warszawa Rakowiec','[Y-293'),(13,'Warszawa Okęcie','UZ-210'),(14,'Warszawa Lotnisko Chopina','JB-861'),(15,'Warszawa Wola (przystanek kolejowy)','LL-928'),(16,'Warszawa Zacisze Wilno','MQ-516'),(17,'Warszawa Wawer (stacja kolejowa)','QY-118'),(18,'Warszawa Targówek','BY-708'),(19,'Warszawa Żwirki i Wigury','NV-823'),(20,'Warszawa Raków','PF-683'),(21,'Warszawa Anin','DP-219'),(22,'Warszawa Śródmieście','LW-347'),(23,'Warszawa Wola Grzybowska','YK-310'),(24,'Warszawa Zoo','PJ-337'),(25,'Warszawa Główna Towarowa','KU-229'),(26,'Warszawa Olszynka Grochowska','QY-604'),(27,'Warszawa Reduta Ordona','MG-630'),(28,'Warszawa Wesoła (przystanek kolejowy)','NA-858'),(29,'Warszawa Miedzeszyn','BP-627'),(30,'Warszawa Śródmieście WKD','ZO-121'),(31,'Warszawa Rembertów (stacja kolejowa)','DT-508'),(32,'Warszawa Toruńska','KB-629'),(33,'Warszawa Centralna','[O-938'),(34,'Warszawa Gocławek','FZ-183'),(35,'Warszawa Choszczówka','CU-031'),(36,'Warszawa Płudy','OR-138'),(37,'Warszawa Salomea','DE-250'),(38,'Warszawa Międzylesie','ZL-292'),(39,'Warszawa Wschodnia','BU-762'),(40,'Warszawa Ursus (przystanek kolejowy)','JD-568');
/*!40000 ALTER TABLE `strefy` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-14  0:29:36
