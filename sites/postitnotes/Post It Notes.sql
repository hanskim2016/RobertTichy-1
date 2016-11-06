CREATE DATABASE  IF NOT EXISTS `ajaxnotes2` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `ajaxnotes2`;
-- MySQL dump 10.13  Distrib 5.7.12, for osx10.9 (x86_64)
--
-- Host: localhost    Database: ajaxnotes2
-- ------------------------------------------------------
-- Server version	5.6.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `notes`
--

LOCK TABLES `notes` WRITE;
/*!40000 ALTER TABLE `notes` DISABLE KEYS */;
INSERT INTO `notes` VALUES (44,'Real notes to self()','Remember to clean up the print messages out of the python server as well as the console.logging in the Javascript','2016-11-05 16:18:51','2016-11-05 21:09:53'),(48,'Header info','This is another note being updated.','2016-11-05 16:18:59','2016-11-05 20:37:43'),(60,'Next Notes','And more....','2016-11-05 21:09:30','2016-11-05 21:36:40'),(61,'The fifth note will be a real doozy','Why?\r\n\r\nWhy?','2016-11-05 21:12:14','2016-11-05 21:13:13'),(62,'Post-It Notes by 3M','Minnesota Mining and Manufacturing','2016-11-05 21:21:11','2016-11-05 21:21:38'),(63,'Buy milk and Paper Towels','shopping list\r\n','2016-11-05 21:23:17','2016-11-05 21:35:19');
/*!40000 ALTER TABLE `notes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-11-05 21:40:51
