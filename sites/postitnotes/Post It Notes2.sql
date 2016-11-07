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
-- Table structure for table `notes`
--

DROP TABLE IF EXISTS `notes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `notes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subject` varchar(45) DEFAULT NULL,
  `note` varchar(250) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notes`
--

LOCK TABLES `notes` WRITE;
/*!40000 ALTER TABLE `notes` DISABLE KEYS */;
INSERT INTO `notes` VALUES (44,'Real notes to self()','Remember to clean up the print messages out of the python server as well as the console.logging in the Javascript','2016-11-05 16:18:51','2016-11-05 21:09:53'),(48,'Header info','This is another note being updated.','2016-11-05 16:18:59','2016-11-05 20:37:43'),(60,'Next Notes plus x2x','And more.... and more','2016-11-05 21:09:30','2016-11-05 21:55:02'),(61,'The 5th note will be a real doozy','Why?\r\nx\r\nWhy?','2016-11-05 21:12:14','2016-11-05 22:06:04'),(62,'Post-It Notes by 3M','Minnesota Mining and Manufacturing','2016-11-05 21:21:11','2016-11-05 21:21:38'),(63,'Buy milk and Paper Towels','shopping list xyz\r\nwhat is the deal?','2016-11-05 21:23:17','2016-11-05 21:55:08'),(64,'Buy soda for party','get Izzy Black Cherry soda and Coca-Cola in glass bottles\r\n','2016-11-05 21:55:59','2016-11-05 21:56:32'),(65,'Get chips for party','','2016-11-05 22:00:52','2016-11-05 22:05:32'),(66,'Take car to the dealer for oil change','Monday 11/7/2016...','2016-11-05 22:02:00','2016-11-05 22:06:28'),(67,'9th Note?','This might be the 9th note, creating a page right function possibility...\r\n','2016-11-06 10:43:42','2016-11-06 10:44:06');
/*!40000 ALTER TABLE `notes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'ajaxnotes2'
--

--
-- Dumping routines for database 'ajaxnotes2'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-11-07 13:46:34
