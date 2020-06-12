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
-- Table structure for table `konta`
--

DROP TABLE IF EXISTS `konta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `konta` (
  `id` int NOT NULL AUTO_INCREMENT,
  `imię` varchar(30) NOT NULL,
  `nazwisko` varchar(50) NOT NULL,
  `pesel` varchar(11) NOT NULL,
  `saldo` float NOT NULL DEFAULT '0',
  `telefon` varchar(15) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `ulgi_id` int DEFAULT NULL,
  `kod_karty` varchar(10) DEFAULT NULL,
  `aktywne` char(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `konta_ulgi_fk` (`ulgi_id`),
  CONSTRAINT `konta_ulgi_fk` FOREIGN KEY (`ulgi_id`) REFERENCES `ulgi` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `konta`
--

LOCK TABLES `konta` WRITE;
/*!40000 ALTER TABLE `konta` DISABLE KEYS */;
INSERT INTO `konta` VALUES (1,'Jodok','Hughes','31172770595',168.48,'968211283',NULL,1,'EX25127','0'),(2,'Linux','Rand','74142542126',164.96,NULL,'Edmonds73@example.com',2,'PS09656','1'),(3,'Rijana','Longo','12071323831',71.72,'191981273','Laurice.Abernathy9@nowhere.com',4,'DI36791','1'),(4,'Juniper','Moses','27062226420',181.1,'811593811','Espinal@example.com',1,NULL,'1'),(5,'Eberhard','Hughey','14130772825',20.81,'427274389','Westbrook@example.com',3,'VU56357','1'),(6,'Egidius','Randall','87022873274',150.2,'891867589','Metcalf214@example.com',1,'RD75530','1'),(7,'Gerbrand','Weaver','71183846063',198.32,'606762531','JoleneAnders44@nowhere.com',4,'LC46990','1'),(8,'Helias','Bain','87100837288',-48.42,'675243486','Higgs1@example.com',3,'JC32988','0'),(9,'Hellfried','Longoria','10001386608',196.97,'854870878',NULL,3,'IP10405','0'),(10,'Cesar','Cade','50163346213',71.63,'096951915','Shelby@nowhere.com',3,'ON12370','1'),(11,'Fawini','Gilchrist','63050221489',133.44,'136552663','nmme1925@example.com',3,'JC67228','0'),(12,'Wedigo','Baines','51080957040',113.68,'739794967','StewartGrimm44@example.com',2,'AD06272','1'),(13,'Corbinian','Dobson','58150103587',71.17,NULL,'Nunes@example.com',4,NULL,'0'),(14,'Brendalie','Hull','69032920401',-47.79,'322638914',NULL,1,'OL23980','0'),(15,'Otfried','Solomon','07031576640',136.93,'271179649','Sheffield@nowhere.com',3,'HK33083','0'),(16,'Gerarda','Loomis','81102686345',132.88,NULL,NULL,5,'QK02806','1'),(17,'Liebhard','Webber','04191565830',-10.91,NULL,'Autry4@example.com',2,'LY16433','0'),(18,'Waldefried','Giles','75092549843',229.06,'252740789','DonnY_Early35@example.com',3,'MM24211','1'),(19,'Kunibert','Hulsey','73111835002',71.11,'185392568','BeliaWofford@example.com',5,NULL,'0'),(20,'Fey','Mosher','56010051870',178.54,'659342353','Thibodeaux@nowhere.com',1,'ON60205','0'),(21,'Abeline ','Cagle','99112041172',-43.01,NULL,'Chamberlin6@example.com',4,'FS69752','0'),(22,'Alruna','Bair','14142901115',-18.71,'909929490','swtsmqwl_cchxo@example.com',1,'JV49233','1'),(23,'Dorle','Cahill','15070974984',58.9,'313978253',NULL,2,'ZQ90570','1'),(24,'Odovacar','Randle','17180223397',-11.9,'178488511','Laverne_Scherer@example.com',5,'WQ73560','1'),(25,'Sivana','Dockery','53190785534',147.74,'848669351',NULL,5,'VQ35986','0'),(26,'Saiga','Looney','94061176201',-30.65,'614693787','KatzY78@example.com',5,'FN58473','1'),(27,'Eliah','Humes','36133355767',-45.79,'380270878','Luigi.Bradley31@example.com',3,'YP47801','0'),(28,'Kordula','Somers','37042102092',195.9,'290317999','Luckett21@example.com',3,'HS78690','0'),(29,'Clemens','Mosier','34120547767',148.51,'830730865','FaustoATenney682@example.com',1,'BN67649','0'),(30,'Vajessa','Baird','18170426687',20.7,'798012641','Adolfo_Pearson@nowhere.com',5,'EG46932','1'),(31,'Praxedis','Loper','17181703030',7.7,'976951255','Wolfe@example.com',1,'KK85817','0'),(32,'Rayko','Hummel','84080325106',150.09,'465154194','Rudy.Otoole695@example.com',4,'ZO60239','1'),(33,'Adelisa ','Lopes','85062914576',69.5,'508393709','Schmitz558@example.com',1,'NC34919','0'),(34,'Swena','Cain','22093881694',215.23,'293611273',NULL,5,'OK07801','0'),(35,'Jolissa','Randolph','93141617805',44.51,'822517694',NULL,4,'SC75343','0'),(36,'Vitalis','Baker','39013720865',21.66,'805164183','rhogaxya_cwfvk@example.com',2,'WE82967','1'),(37,'Dietger','Mosley','02173061182',191.19,'240312618','dhkukgf56@nowhere.com',4,'NZ24422','0'),(38,'Bartel ','Raney','92131505044',-40.65,'731439645','CarmonClement237@example.com',4,NULL,'0'),(39,'Huldrich','Weber','00113788140',12.36,'905000728',NULL,1,'LN64742','0'),(40,'Nestor','Humphrey','69170264835',105.61,NULL,'Crabtree37@example.com',1,'EX74849','1'),(41,'Natanael','Calabrese','41081532738',189.44,'667462539','kyyf1@example.com',1,'LH76456','1'),(42,'Reginbert','Gill','73051156055',81.75,'196718380','Braswell293@nowhere.com',3,'ZD43690','0'),(43,'Gordian','Balderas','56161507605',112.45,'476550182','DemetriaI.Hutcherson@example.c',3,'YF88320','1'),(44,'Ingold','Moss','53153762285',188.68,'958817875','Musser956@example.com',5,'MX25887','0'),(45,'Rubertus','Sommer','08101402850',107.87,'687168274','Cameron_DCook569@example.com',4,'ME04488','1'),(46,'Godot','Webster','44081073899',156.61,'328802623','Brogan@example.com',3,'RY68612','0'),(47,'Gertraud','Rangel','05082406918',25.98,NULL,'AbneyE7@nowhere.com',4,'WW85888','1'),(48,'Elieser','Dodd','54190445165',221.91,NULL,NULL,5,'YP60789','0'),(49,'Romi','Gillen','90031103999',216.1,NULL,NULL,5,'QI85337','0'),(50,'Clovis','Sommers','20153310438',30.01,NULL,NULL,1,NULL,'0');
/*!40000 ALTER TABLE `konta` ENABLE KEYS */;
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
