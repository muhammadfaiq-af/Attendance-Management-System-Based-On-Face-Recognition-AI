-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: attendancesystem
-- ------------------------------------------------------
-- Server version	8.0.26

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
-- Table structure for table `student_details`
--

DROP TABLE IF EXISTS `student_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_details` (
  `Department` varchar(45) NOT NULL,
  `Course` varchar(45) NOT NULL,
  `Year` varchar(45) NOT NULL,
  `Semester` varchar(45) NOT NULL,
  `Student_ID` varchar(45) NOT NULL,
  `Name` varchar(45) NOT NULL,
  `Roll_No` varchar(45) NOT NULL,
  `Gender` varchar(45) NOT NULL,
  `Contact_No` varchar(45) NOT NULL,
  `Cnic` varchar(45) NOT NULL,
  `Address` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `PhotoSample` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Student_ID`),
  UNIQUE KEY `Cnic_UNIQUE` (`Cnic`),
  UNIQUE KEY `Roll_No_UNIQUE` (`Roll_No`),
  UNIQUE KEY `Contact_No_UNIQUE` (`Contact_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_details`
--

LOCK TABLES `student_details` WRITE;
/*!40000 ALTER TABLE `student_details` DISABLE KEYS */;
INSERT INTO `student_details` VALUES ('Computer Science','Advance Pyhton Programming','2017 -21','8','1','Faiq','171131','Male','0310-9345307','17301-4502835-5','Warsak Road','faiqqadri83@gmail.com','Yes'),('Computer Science','Advance Programming','2017 -21','6','10','Roman Khalil','171143','Male','03329138768','17301-6007742-1','Regi ','romankhan12@gmail.com','Yes'),('Chemistry','Organic Chemistry','2015 -19','5','2','Sadia Amin','177898','Female','0343-7065336','17301-8763465-8','Ramdas','sadiaamin998@gmail.com','Yes'),('Computer Science','Advance Programming','2017 -21','8','3','Umair','171014','Male','0301-1426414','17301-7740627-1','Majeed Town','umiiawan06@gmail.com','No'),('Computer Science','Advance Programming','2018 -22','8','4','Shahzad','38','Male','0346-8070408','17102-1243720-9','Charsada','shahzadkhan07@gmail.com','Yes'),('Chemistry','Organic Chemistry','2014 -18','5','5','Rabia','17233','Female','03109373763','17301-3737333-3','Dilzak Road','hagddhd','Yes'),('Computer Science','Advance Pyhton Programming','2017 -21','6','6','Ihsan Ali','171113','Male','0311-2397060','17301-2848949-3','Gulbahar','mohdahsanali2@gmail.com','Yes'),('Computer Science','Analysis of Algorithm','2012 - 16','4','7','Rashid','1316','Male','03139976372','17301-5590607-5','Dalazak Road','fiverrusd1@gmail.com','Yes'),('Computer Science','Advance Programming','2015 -19','5','8','Salman Aftab','10353','Select Gender','03099620042','17301-0305094-5','Khan mast','sallujan93@gmail.com','Yes'),('Chemistry','Organic Chemistry','2012 - 16','8','9','Qasim Qadri','11135','Male','03329974774','17301-3789864-3','Khan mast Colony','qadriqm1@gmail.com','Yes');
/*!40000 ALTER TABLE `student_details` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-16 14:46:52
