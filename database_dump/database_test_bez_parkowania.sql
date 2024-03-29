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
-- Table structure for table `bez_parkowania`
--

DROP TABLE IF EXISTS `bez_parkowania`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bez_parkowania` (
  `id` int NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `bez_parkowania_pobyt_fk` FOREIGN KEY (`id`) REFERENCES `pobyty` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bez_parkowania`
--

LOCK TABLES `bez_parkowania` WRITE;
/*!40000 ALTER TABLE `bez_parkowania` DISABLE KEYS */;
INSERT INTO `bez_parkowania` VALUES (1),(4),(6),(7),(10),(12),(13),(15),(18),(19),(22),(23),(25),(27),(29),(32),(34),(36),(37),(40),(41),(44),(45),(48),(49),(52),(54),(55),(58),(59),(61),(63),(65),(67),(70),(72),(74),(76),(78),(80),(82),(83),(86),(87),(90),(91),(93),(95),(97),(100),(101),(104),(105),(108),(110),(111),(113),(116),(118),(120),(121),(123),(125),(127),(129),(131),(134),(136),(138),(140),(142),(144),(146),(148),(149),(151),(154),(156),(157),(160),(162),(164),(166),(167),(169),(171),(173),(175),(177),(180),(182),(183),(186),(187),(189),(192),(194),(196),(198),(200),(202),(204),(205),(208),(210),(212),(213),(215),(218),(219),(222),(224),(225),(228),(230),(231),(233),(235),(238),(240),(242),(243),(246),(247),(249),(252),(254),(256),(257),(259),(262),(264),(266),(267),(270),(272),(274),(276),(278),(279),(281),(284),(285),(288),(290),(291),(293),(296),(297),(299),(302),(304),(305),(307),(310),(311),(313),(315),(317),(319),(321),(324),(325),(327),(330),(332),(333),(336),(337),(340),(341),(344),(345),(347),(349),(351),(354),(355),(358),(359),(361),(363),(365),(367),(369),(372),(374),(375),(378),(379),(382),(384),(386),(388),(389),(392),(393),(396),(398),(400),(401),(403),(406),(407),(410),(412),(413),(415),(418),(420),(422),(423),(425),(427),(429),(432),(433),(436),(438),(440),(441),(443),(446),(448),(450),(451),(453),(455),(457),(460),(461),(463),(466),(468),(469),(471),(474),(475),(477),(480),(481),(484),(485),(487),(490),(492),(493),(496),(498),(500),(502),(504),(505),(508),(509),(512),(514),(516),(518),(519),(522),(523),(526),(528),(530),(532),(533),(535),(537),(540),(542),(544),(545),(547),(550),(552),(554),(556),(557),(559),(561),(564),(565),(568),(570),(572),(573),(575),(578),(579),(582),(584),(585),(587),(590),(591),(593),(596),(597),(600),(601),(604),(605),(607),(610),(611),(614),(615),(618),(620),(621),(624),(625),(628),(629),(631),(634),(635),(637),(640),(642),(643),(646),(647),(649),(651),(654),(655),(657),(660),(662),(664),(665),(667),(670),(672),(673),(676),(678),(679),(682),(683),(686),(688),(690),(692),(693),(696),(698),(700),(702),(703),(705),(707),(709),(712),(714),(715),(718),(720),(722),(724),(726),(727),(730),(732),(734),(736),(738),(739),(742),(743),(745),(748),(750),(751),(754),(755),(758),(759),(762),(764),(766),(767),(770),(771),(774),(776),(777),(780),(782),(784),(785),(788),(790),(791),(793),(796),(798),(800),(802),(803),(806),(807),(809),(811),(813),(815),(818),(820),(822),(823),(826),(828),(829),(832),(833),(836),(838),(840),(841),(844),(846),(848),(849),(852),(854),(856),(857),(859),(861),(863),(866),(868),(869),(872),(874),(876),(878),(880),(881),(884),(886),(887),(890),(891),(894),(896),(897),(900),(901),(904),(905),(908),(909),(911),(913),(915),(918),(919),(922),(923),(926),(927),(929),(932),(934),(935),(937),(940),(942),(943),(946),(947),(950),(952),(953),(956),(958),(960),(961),(964),(966),(968),(969),(971),(973),(976),(977),(979),(982),(983),(985),(988),(990),(991),(994),(996),(997),(1000),(1001),(1003),(1005),(1007),(1010),(1011),(1014),(1015),(1017),(1020),(1022),(1023),(1025),(1028),(1030),(1032),(1034),(1036),(1037),(1040),(1041),(1044),(1045),(1047),(1049),(1052),(1054),(1055),(1058),(1060),(1061),(1063),(1066),(1068),(1069),(1071),(1074),(1075),(1077),(1079),(1082),(1084),(1085),(1088),(1090),(1092),(1093),(1095),(1098),(1099),(1102),(1104),(1106),(1108),(1109),(1111),(1114),(1116),(1117),(1120),(1121),(1123),(1125),(1127),(1130),(1131),(1134),(1135),(1137),(1139),(1141),(1144),(1146),(1147),(1149),(1151),(1154),(1156),(1157),(1160),(1162),(1164),(1165),(1168),(1169),(1172),(1174),(1176),(1178),(1179),(1181),(1183),(1186),(1188),(1189),(1192),(1193),(1196),(1197),(1199),(1201),(1203),(1206),(1207),(1209),(1211),(1214),(1215),(1217),(1219),(1221),(1223),(1226),(1228),(1230),(1232),(1233),(1235),(1238),(1240),(1241),(1243),(1245),(1247),(1250),(1252),(1253),(1256),(1257),(1260),(1261),(1264),(1266),(1268),(1269),(1271),(1274),(1276),(1277),(1280),(1282),(1283),(1286),(1288),(1289),(1291),(1293),(1295),(1297),(1300),(1301),(1303),(1306),(1307),(1310),(1312),(1313),(1316),(1317),(1320),(1321),(1324),(1325),(1328),(1329),(1331),(1333),(1336),(1338),(1339),(1341),(1344),(1346),(1348),(1350),(1351),(1353),(1356),(1357),(1359),(1361),(1363),(1366),(1367),(1369),(1372),(1374),(1375),(1377),(1380),(1381),(1384),(1385),(1388),(1390),(1391),(1393),(1395),(1397),(1400),(1402),(1404),(1405),(1407),(1409),(1411),(1413),(1415),(1417),(1419),(1422),(1424),(1425),(1427),(1429),(1432),(1434),(1435),(1438),(1439),(1442),(1444),(1446),(1447),(1450),(1451),(1453),(1455),(1458),(1460),(1462),(1463),(1465),(1468),(1469),(1472),(1474),(1476),(1477),(1479),(1482),(1483),(1486),(1487),(1490),(1492),(1494),(1496),(1498),(1500),(1501),(1504),(1506),(1508),(1510),(1511),(1514),(1516),(1518),(1520),(1521),(1524),(1525),(1528),(1530),(1531),(1533),(1536),(1537),(1540),(1542),(1543),(1546),(1547),(1549),(1552),(1554),(1556),(1557),(1560),(1562),(1564),(1565),(1568),(1569),(1571),(1574),(1576),(1578),(1580),(1581),(1584),(1586),(1587),(1589),(1592),(1593),(1596),(1597),(1600),(1601),(1604),(1606),(1608),(1609),(1611),(1614),(1616),(1617),(1620),(1622),(1624),(1626),(1628),(1629),(1631),(1634),(1636),(1638),(1639),(1642),(1643),(1645),(1647),(1650),(1652),(1654),(1656),(1658),(1660),(1661),(1663),(1665),(1667),(1669),(1672),(1674),(1675),(1677),(1680),(1681),(1684),(1686),(1687),(1689),(1692),(1694),(1696),(1697),(1700),(1702),(1704),(1705),(1708),(1709),(1711),(1714),(1715),(1718),(1719),(1721),(1723),(1725),(1727),(1730),(1732),(1733),(1736),(1738),(1739),(1741),(1743),(1745),(1748),(1750),(1751),(1754),(1756),(1758),(1760),(1761),(1763),(1765),(1768),(1769),(1771),(1773),(1776),(1778),(1780),(1782),(1783),(1785),(1787),(1790),(1791),(1794),(1796),(1798),(1800),(1801),(1804),(1805),(1808),(1809),(1812),(1813),(1815),(1817),(1820),(1822),(1823),(1826),(1828),(1830),(1832),(1833),(1836),(1838),(1840),(1841),(1844),(1845),(1848),(1850),(1852),(1854),(1855),(1857),(1859),(1861),(1863),(1866),(1868),(1870),(1872),(1874),(1875),(1878),(1879),(1881),(1884),(1885),(1887),(1890),(1891),(1893),(1896),(1898),(1900),(1902),(1903),(1906),(1907),(1910),(1911),(1914),(1915),(1917),(1919),(1922),(1923),(1926),(1927),(1929),(1931),(1933),(1936),(1937),(1940),(1941),(1943),(1946),(1947),(1949),(1952),(1954),(1956),(1958),(1959),(1961),(1963),(1966),(1967),(1970),(1971),(1974),(1975),(1977),(1979),(1981),(1983),(1985),(1988),(1990),(1992),(1993),(1995),(1998),(1999),(2001),(2003),(2005),(2008),(2010),(2011),(2013),(2016),(2017),(2019),(2022),(2024),(2025),(2027),(2030),(2031),(2033),(2036),(2037),(2040),(2041),(2044),(2046),(2048),(2049),(2051),(2054),(2056),(2058),(2060),(2062),(2064),(2065),(2068),(2069),(2072),(2073),(2076),(2077),(2079),(2081),(2083),(2085),(2087),(2090),(2092),(2093),(2095),(2098),(2100),(2102),(2103),(2105),(2107),(2109),(2112),(2114),(2116),(2118),(2120),(2121),(2124),(2126),(2128),(2129),(2131),(2134),(2136),(2138),(2140),(2141),(2144),(2146),(2147),(2150),(2152),(2154),(2155),(2158),(2159),(2161),(2164),(2166),(2168),(2170),(2171),(2173),(2175),(2178),(2179),(2181),(2184),(2185),(2187),(2190),(2192),(2194),(2196),(2198),(2199);
/*!40000 ALTER TABLE `bez_parkowania` ENABLE KEYS */;
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
