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
-- Table structure for table `bramki`
--

DROP TABLE IF EXISTS `bramki`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bramki` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nazwa` varchar(40) NOT NULL,
  `strefy_id` int NOT NULL,
  `selektor` char(9) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `bramki_strefy_fk` (`strefy_id`),
  CONSTRAINT `bramki_strefy_fk` FOREIGN KEY (`strefy_id`) REFERENCES `strefy` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bramki`
--

LOCK TABLES `bramki` WRITE;
/*!40000 ALTER TABLE `bramki` DISABLE KEYS */;
INSERT INTO `bramki` VALUES (1,'Krzysztofa Arciszewskiego',3,'wjazdowe'),(2,'Czerwińska',3,'wyjazdowe'),(3,'Eskimoska',7,'wjazdowe'),(4,'1 Maja',7,'wyjazdowe'),(5,'Czerwona Droga',2,'wyjazdowe'),(6,'Batalionu AK \"Karpaty\"',8,'wjazdowe'),(7,'Teodora Duracza',6,'wyjazdowe'),(8,'Eskulapów',6,'wjazdowe'),(9,'Czerwonego Krzyża',4,'wjazdowe'),(10,'Goździków',1,'wyjazdowe'),(11,'Objazdowa',5,'wjazdowe'),(12,'1 Praskiego Pułku',5,'wyjazdowe'),(13,'Kępna',4,'wyjazdowe'),(14,'Batalionu AK \"Olza\"',3,'wjazdowe'),(15,'Janczarów',5,'wyjazdowe'),(16,'Teofila Jaśkiewicza',3,'wjazdowe'),(17,'Esperanto',4,'wyjazdowe'),(18,'Czerwonych Beretów',5,'wyjazdowe'),(19,'1 Praskiego Pułku (Wesoła)',10,'wjazdowe'),(20,'Batalionu AK \"Pięść\"',6,'wyjazdowe'),(21,'1 Sierpnia',9,'wyjazdowe'),(22,'Oboźna',8,'wjazdowe'),(23,'Grabalówki',7,'wyjazdowe'),(24,'Janinówka',8,'wjazdowe'),(25,'Tomasza Edisona',1,'wyjazdowe'),(26,'Obozowa',4,'wjazdowe'),(27,'Krzysztofa Kamila Baczyńskiego',5,'wjazdowe'),(28,'Ketlinga',10,'wyjazdowe'),(29,'Krzysztofa Kiersnowskiego',3,'wyjazdowe'),(30,'Topazowa',9,'wjazdowe'),(31,'Odolańska',3,'wjazdowe'),(32,'Kibiców',1,'wyjazdowe'),(33,'Grabowska',9,'wjazdowe'),(34,'Janiszowska',6,'wyjazdowe'),(35,'Topiel',9,'wyjazdowe'),(36,'Odrębna',5,'wjazdowe'),(37,'Topolowa',3,'wjazdowe'),(38,'Estońska',7,'wyjazdowe'),(39,'Krzysztofa Kieślowskiego',6,'wyjazdowe'),(40,'Kiejstuta',4,'wjazdowe'),(41,'Ogrodowa',4,'wjazdowe'),(42,'Czerwonych Maków',1,'wyjazdowe'),(43,'Estrady',4,'wjazdowe'),(44,'Czerwonych Wierchów',8,'wyjazdowe'),(45,'Torfowa',1,'wjazdowe'),(46,'Etiudy Rewolucyjnej',10,'wyjazdowe'),(47,'Czeska',5,'wjazdowe'),(48,'Batalionu AK \"Ryś\"',7,'wyjazdowe'),(49,'Eugeniusza Bodo',2,'wjazdowe'),(50,'Okopowa',8,'wyjazdowe');
/*!40000 ALTER TABLE `bramki` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-12 14:30:54
