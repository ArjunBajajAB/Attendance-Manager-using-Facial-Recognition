-- MySQL dump 10.13  Distrib 8.0.22, for Linux (x86_64)
--
-- Host: localhost    Database: AttendanceManager
-- ------------------------------------------------------
-- Server version	8.0.22-0ubuntu0.20.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `AI`
--

DROP TABLE IF EXISTS `AI`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AI` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AI`
--

LOCK TABLES `AI` WRITE;
/*!40000 ALTER TABLE `AI` DISABLE KEYS */;
/*!40000 ALTER TABLE `AI` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BE`
--

DROP TABLE IF EXISTS `BE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BE` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BE`
--

LOCK TABLES `BE` WRITE;
/*!40000 ALTER TABLE `BE` DISABLE KEYS */;
/*!40000 ALTER TABLE `BE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BI`
--

DROP TABLE IF EXISTS `BI`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BI` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BI`
--

LOCK TABLES `BI` WRITE;
/*!40000 ALTER TABLE `BI` DISABLE KEYS */;
/*!40000 ALTER TABLE `BI` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `C`
--

DROP TABLE IF EXISTS `C`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `C` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `C`
--

LOCK TABLES `C` WRITE;
/*!40000 ALTER TABLE `C` DISABLE KEYS */;
/*!40000 ALTER TABLE `C` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CA`
--

DROP TABLE IF EXISTS `CA`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CA` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CA`
--

LOCK TABLES `CA` WRITE;
/*!40000 ALTER TABLE `CA` DISABLE KEYS */;
/*!40000 ALTER TABLE `CA` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CG`
--

DROP TABLE IF EXISTS `CG`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CG` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CG`
--

LOCK TABLES `CG` WRITE;
/*!40000 ALTER TABLE `CG` DISABLE KEYS */;
INSERT INTO `CG` VALUES ('2020-11-26','1');
/*!40000 ALTER TABLE `CG` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CN`
--

DROP TABLE IF EXISTS `CN`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CN` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CN`
--

LOCK TABLES `CN` WRITE;
/*!40000 ALTER TABLE `CN` DISABLE KEYS */;
/*!40000 ALTER TABLE `CN` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CPP`
--

DROP TABLE IF EXISTS `CPP`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CPP` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CPP`
--

LOCK TABLES `CPP` WRITE;
/*!40000 ALTER TABLE `CPP` DISABLE KEYS */;
/*!40000 ALTER TABLE `CPP` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DBMS`
--

DROP TABLE IF EXISTS `DBMS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DBMS` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DBMS`
--

LOCK TABLES `DBMS` WRITE;
/*!40000 ALTER TABLE `DBMS` DISABLE KEYS */;
/*!40000 ALTER TABLE `DBMS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DE`
--

DROP TABLE IF EXISTS `DE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DE` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DE`
--

LOCK TABLES `DE` WRITE;
/*!40000 ALTER TABLE `DE` DISABLE KEYS */;
/*!40000 ALTER TABLE `DE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DS`
--

DROP TABLE IF EXISTS `DS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DS` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DS`
--

LOCK TABLES `DS` WRITE;
/*!40000 ALTER TABLE `DS` DISABLE KEYS */;
/*!40000 ALTER TABLE `DS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DWH_DM`
--

DROP TABLE IF EXISTS `DWH_DM`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DWH_DM` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DWH_DM`
--

LOCK TABLES `DWH_DM` WRITE;
/*!40000 ALTER TABLE `DWH_DM` DISABLE KEYS */;
/*!40000 ALTER TABLE `DWH_DM` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Ecom`
--

DROP TABLE IF EXISTS `Ecom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Ecom` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Ecom`
--

LOCK TABLES `Ecom` WRITE;
/*!40000 ALTER TABLE `Ecom` DISABLE KEYS */;
INSERT INTO `Ecom` VALUES ('2020-11-23','1'),('2020-11-24','1'),('2020-11-26','1');
/*!40000 ALTER TABLE `Ecom` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FEDT`
--

DROP TABLE IF EXISTS `FEDT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `FEDT` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FEDT`
--

LOCK TABLES `FEDT` WRITE;
/*!40000 ALTER TABLE `FEDT` DISABLE KEYS */;
/*!40000 ALTER TABLE `FEDT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ICIT`
--

DROP TABLE IF EXISTS `ICIT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ICIT` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ICIT`
--

LOCK TABLES `ICIT` WRITE;
/*!40000 ALTER TABLE `ICIT` DISABLE KEYS */;
/*!40000 ALTER TABLE `ICIT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Java`
--

DROP TABLE IF EXISTS `Java`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Java` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Java`
--

LOCK TABLES `Java` WRITE;
/*!40000 ALTER TABLE `Java` DISABLE KEYS */;
/*!40000 ALTER TABLE `Java` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Linux`
--

DROP TABLE IF EXISTS `Linux`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Linux` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Linux`
--

LOCK TABLES `Linux` WRITE;
/*!40000 ALTER TABLE `Linux` DISABLE KEYS */;
/*!40000 ALTER TABLE `Linux` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MC`
--

DROP TABLE IF EXISTS `MC`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `MC` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MC`
--

LOCK TABLES `MC` WRITE;
/*!40000 ALTER TABLE `MC` DISABLE KEYS */;
/*!40000 ALTER TABLE `MC` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Maths_1`
--

DROP TABLE IF EXISTS `Maths_1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Maths_1` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Maths_1`
--

LOCK TABLES `Maths_1` WRITE;
/*!40000 ALTER TABLE `Maths_1` DISABLE KEYS */;
/*!40000 ALTER TABLE `Maths_1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Maths_2`
--

DROP TABLE IF EXISTS `Maths_2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Maths_2` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Maths_2`
--

LOCK TABLES `Maths_2` WRITE;
/*!40000 ALTER TABLE `Maths_2` DISABLE KEYS */;
/*!40000 ALTER TABLE `Maths_2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Maths_3`
--

DROP TABLE IF EXISTS `Maths_3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Maths_3` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Maths_3`
--

LOCK TABLES `Maths_3` WRITE;
/*!40000 ALTER TABLE `Maths_3` DISABLE KEYS */;
/*!40000 ALTER TABLE `Maths_3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Maths_4`
--

DROP TABLE IF EXISTS `Maths_4`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Maths_4` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Maths_4`
--

LOCK TABLES `Maths_4` WRITE;
/*!40000 ALTER TABLE `Maths_4` DISABLE KEYS */;
/*!40000 ALTER TABLE `Maths_4` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Multimedia`
--

DROP TABLE IF EXISTS `Multimedia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Multimedia` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Multimedia`
--

LOCK TABLES `Multimedia` WRITE;
/*!40000 ALTER TABLE `Multimedia` DISABLE KEYS */;
/*!40000 ALTER TABLE `Multimedia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `NP`
--

DROP TABLE IF EXISTS `NP`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `NP` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `NP`
--

LOCK TABLES `NP` WRITE;
/*!40000 ALTER TABLE `NP` DISABLE KEYS */;
/*!40000 ALTER TABLE `NP` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `NS`
--

DROP TABLE IF EXISTS `NS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `NS` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `NS`
--

LOCK TABLES `NS` WRITE;
/*!40000 ALTER TABLE `NS` DISABLE KEYS */;
/*!40000 ALTER TABLE `NS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `OS`
--

DROP TABLE IF EXISTS `OS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `OS` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `OS`
--

LOCK TABLES `OS` WRITE;
/*!40000 ALTER TABLE `OS` DISABLE KEYS */;
INSERT INTO `OS` VALUES ('2020-11-23','1'),('2020-11-24','1'),('2020-11-26','1');
/*!40000 ALTER TABLE `OS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PHP`
--

DROP TABLE IF EXISTS `PHP`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PHP` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PHP`
--

LOCK TABLES `PHP` WRITE;
/*!40000 ALTER TABLE `PHP` DISABLE KEYS */;
INSERT INTO `PHP` VALUES ('2020-11-23','1'),('2020-11-24','1'),('2020-11-26','1');
/*!40000 ALTER TABLE `PHP` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `POA`
--

DROP TABLE IF EXISTS `POA`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `POA` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `POA`
--

LOCK TABLES `POA` WRITE;
/*!40000 ALTER TABLE `POA` DISABLE KEYS */;
/*!40000 ALTER TABLE `POA` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `POM`
--

DROP TABLE IF EXISTS `POM`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `POM` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `POM`
--

LOCK TABLES `POM` WRITE;
/*!40000 ALTER TABLE `POM` DISABLE KEYS */;
/*!40000 ALTER TABLE `POM` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Physics`
--

DROP TABLE IF EXISTS `Physics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Physics` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Physics`
--

LOCK TABLES `Physics` WRITE;
/*!40000 ALTER TABLE `Physics` DISABLE KEYS */;
/*!40000 ALTER TABLE `Physics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SE`
--

DROP TABLE IF EXISTS `SE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SE` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SE`
--

LOCK TABLES `SE` WRITE;
/*!40000 ALTER TABLE `SE` DISABLE KEYS */;
/*!40000 ALTER TABLE `SE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ST`
--

DROP TABLE IF EXISTS `ST`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ST` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ST`
--

LOCK TABLES `ST` WRITE;
/*!40000 ALTER TABLE `ST` DISABLE KEYS */;
/*!40000 ALTER TABLE `ST` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Students`
--

DROP TABLE IF EXISTS `Students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Students` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `EnrollmentNumber` bigint NOT NULL,
  `Name` varchar(255) DEFAULT NULL,
  `Course` varchar(255) DEFAULT NULL,
  `Section` varchar(255) DEFAULT NULL,
  `SubjectID` varchar(255) DEFAULT NULL,
  `ImageEncoding` blob NOT NULL,
  `Semester` int NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `EnrollmentNumber` (`EnrollmentNumber`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Students`
--

LOCK TABLES `Students` WRITE;
/*!40000 ALTER TABLE `Students` DISABLE KEYS */;
INSERT INTO `Students` VALUES (1,1514902018,'Arjun Bajaj','BCA','A','53',_binary '\Àsr=Në>aæ\Òª∑\Ì7<:√ß=\"Q%>\‚kã<r‚∑Ω?0—ºñ\÷kª/\ÿ<\÷\0=SÆ†=\ƒ\‚6º\”(>ºAºÉ<áºbƒΩ\Ù∆´ΩGy>ª)Ω∞Hº]â1=\Z&\’=\»\‡\Õ<êd±Ω`9\ΩZ-öΩi#¢<C—è=Cêx=\‰Æ>ãw-ºæ3˘=|Ωª>ï\Ì°=rh=M±#<F+Gº¯¢H=\ƒ=˘Ω∏Øº$$æÜ*òΩ¨\…=2É\»=\Z@§=\‹Tæmπ=\‡\œcΩKΩºù5=sA“ª0\Óó=\ﬂ˝\≈<Eûæó€≥=¢%€Ω\“S\‘:ò3!æ\€ø=\÷π=Aâæü˘V=¸&>\\˛\0=\„⁄†=ãP]æ¨øÀºBˇ0º[“î=\»WÂΩäèy=NÜ>+fÅ=\"å=õÇbΩR∂¶=[©=î¶x<Æ\r\Ô:æ\r©Ω\˜)/Ω\Õ\ˆ∂ªX+R=˙\Ô0Ω_µºtb\‰ªf{\">\‰\„>1\„æ:\÷!=∞L >~/•Ω3\Ï\ÁªR$Ω\‚LΩQ&´=\»<Ω\„C\Ë<qÄ°Ω\"æM˙=µ\ÌæU\–6>G∑ñΩä\ÍM<_F•ª/®Å<\Â∏\È<î\'>\Ïó:\√-\«99N<	\€\\ªTæøE\È<\Ã›Ω;=A>Ê•ì=∏ººqç4=ûÖ>±ëB:™\Ÿ=vó=\ngæ',5),(4,1114902018,'Anirudh','BCA','A','53',_binary 'NoneN',5);
/*!40000 ALTER TABLE `Students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TC`
--

DROP TABLE IF EXISTS `TC`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TC` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TC`
--

LOCK TABLES `TC` WRITE;
/*!40000 ALTER TABLE `TC` DISABLE KEYS */;
/*!40000 ALTER TABLE `TC` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `WT`
--

DROP TABLE IF EXISTS `WT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `WT` (
  `Date` date NOT NULL,
  `PresentID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `WT`
--

LOCK TABLES `WT` WRITE;
/*!40000 ALTER TABLE `WT` DISABLE KEYS */;
/*!40000 ALTER TABLE `WT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'AttendanceManager'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-30 11:53:32
