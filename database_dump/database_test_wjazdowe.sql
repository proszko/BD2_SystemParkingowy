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
-- Table structure for table `wjazdowe`
--

DROP TABLE IF EXISTS `wjazdowe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wjazdowe` (
  `id` int NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `wjazdowa_bramka_fk` FOREIGN KEY (`id`) REFERENCES `bramki` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wjazdowe`
--

LOCK TABLES `wjazdowe` WRITE;
/*!40000 ALTER TABLE `wjazdowe` DISABLE KEYS */;
INSERT INTO `wjazdowe` VALUES (2),(4),(5),(8),(9),(12),(13),(15),(18),(20),(21),(23),(25),(28),(30),(32),(34),(35),(37),(40),(42),(44),(46),(47),(49),(51),(54),(55),(57),(60),(61),(64),(66),(68),(69),(71),(73),(75),(77),(80),(82),(84),(86),(88),(89),(91),(93),(95),(97),(99),(101),(103),(106),(108),(109),(111),(114),(116),(117),(119),(122),(124),(126),(127),(130),(131),(133),(136),(137),(140),(141),(143),(145),(147),(149),(151),(153),(156),(158),(160),(161),(164),(165),(168),(170),(172),(174),(175),(177),(179),(181),(184),(186),(188),(190),(192),(194),(196),(198),(199),(202),(203),(206),(207),(209),(212),(214),(215),(217),(220),(222),(224),(226),(228),(229),(231),(234),(236),(237),(240),(242),(244),(246),(247),(249),(252),(254),(256),(258),(259),(261),(264),(265),(267),(270),(271),(273),(276),(277),(279),(282),(284),(285),(288),(289),(291),(293),(296),(297),(300),(301),(302),(303),(304),(305),(306),(307),(308),(309),(310),(311),(312),(313),(314),(315),(316),(317),(318),(319),(320),(321),(322),(323),(324),(325),(326),(327),(328),(329),(330),(331),(332),(333),(334),(335),(336),(337),(338),(339),(340);
/*!40000 ALTER TABLE `wjazdowe` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-14  0:29:39
