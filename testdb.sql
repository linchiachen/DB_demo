-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2022-04-27 09:52:00
-- 伺服器版本： 10.4.24-MariaDB
-- PHP 版本： 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫: `testdb`
--

-- --------------------------------------------------------

--
-- 資料表結構 `course`
--

CREATE TABLE `course` (
  `cou_id` int(11) NOT NULL,
  `cou_name` varchar(10) DEFAULT NULL,
  `cou_dept` varchar(10) DEFAULT NULL,
  `cou_credit` int(11) DEFAULT NULL,
  `cou_necessary` varchar(10) DEFAULT NULL,
  `cou_maximum_people` int(11) DEFAULT NULL,
  `cou_time1` int(11) DEFAULT NULL,
  `cou_time2` int(11) DEFAULT NULL,
  `t_id` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `course`
--

INSERT INTO `course` (`cou_id`, `cou_name`, `cou_dept`, `cou_credit`, `cou_necessary`, `cou_maximum_people`, `cou_time1`, `cou_time2`,`t_id`) VALUES
(1, '班級活動', '資工系', 3, '是', 4, 1, 2, 'T001'),
(2, '體育(一)', '資工系', 1, '是', 4, 3, 4, 'T001'),
(3, '程式設計(一)', '資工系', 2, '是', 4, 9, 10, 'T001'),
(4, '程式設計(二)', '資工系', 2, '是', 4, 11, 12, 'T001'),
(5, '普通物理', '資工系', 3, '是', 4, 17, 18, 'T001'),
(6, '程式設計(三)', '資工系', 2, '是', 4, 5, 6, 'T001'),
(7, '程式設計(四)', '資工系', 2, '是', 4, 7, 8, 'T001'),
(8, '微積分(一)', '資工系', 2, '是', 4, 5, 6, 'T002'),
(9, '微積分(二)', '資工系', 2, '是', 4, 7, 8, 'T002'),
(10, '日文(一)', '外語系', 2, '是', 4, 5, 6, 'T003'),
(11, '日文(二)', '外語系', 2, '是', 4, 7, 8, 'T003'),
(12, '日文(三)', '外語系', 2, '是', 4, 5, 6, 'T003'),
(13, '日文(四)', '外語系', 2, '是', 4, 7, 8, 'T003'),
(14, '法文(一)', '外語系', 2, '否', 4, 19, 20, 'T004'),
(15, '法文(二)', '外語系', 2, '否', 4, 21, 22, 'T004'),
(16, '英文(一)', '外語系', 2, '是', 4, 13, 14, 'T004'),
(17, '英文(二)', '外語系', 2, '是', 4, 15, 16, 'T004'),
(18, '班級活動', '外語系', 3, '是', 4, 21, 22, 'T004'),
(19, '密碼學', '資工系', 3, '否', 4, 25, 26, 'T004'),
(20, '物件導向', '資工系', 3, '否', 4, 27, 28, 'T004'),
(21, '組合數學', '資工系', 3, '否', 4, 25, 26, 'T004'),
(22, '線性代數', '資工系', 3, '否', 4, 27, 28, 'T004'),
(23, '法文(三)', '外語系', 2, '否', 4, 19, 20, 'T001'),
(24, '法文(四)', '外語系', 2, '是', 4, 21, 22, 'T001'),
(25, '韓文(一)', '外語系', 2, '是', 4, 29, 30, 'T001'),
(26, '韓文(二)', '外語系', 2, '是', 4, 31, 32, 'T001'),
(27, '西語(一)', '外語系', 2, '否', 4, 25, 26, 'T001'),
(28, '西語(二)', '外語系', 2, '否', 4, 27, 28, 'T001'),
(29, '西語(三)', '外語系', 2, '否', 4, 25, 26, 'T001'),
(30, '西語(四)', '外語系', 2, '否', 4, 27, 28, 'T001'),
(31, '韓文(三)', '外語系', 2, '是', 4, 29, 30, 'T001'),
(32, '韓文(四)', '外語系', 2, '是', 4, 31, 32, 'T001'),
(33, 'python基礎', '資工系', 2, '否', 4, 19, 20, 'T001'),
(34, '網頁設計', '資工系', 2, '否', 4, 19, 20, 'T001'),
(35, 'unix', '資工系', 2, '否', 4, 5, 6, 'T001'),
(36, '數位設計', '資工系', 2, '否', 4, 7, 8, 'T001');


-- --------------------------------------------------------

--
-- 資料表結構 `curriculum`
--

CREATE TABLE `curriculum` (
  `stu_id` varchar(10) NOT NULL,
  `cou_id` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `curriculum`
--

INSERT INTO `curriculum` (`stu_id`, `cou_id`) VALUES
('D002', '1'),
('D001', '3'),
('D001', '5'),
('D002', '2'),
('D002', '3'),
('D002', '4'),
('D002', '5'),
('D003', '10'),
('D003', '11'),
('D003', '16'),
('D003', '17'),
('D003', '18'),
('D004', '10'),
('D004', '11'),
('D004', '16'),
('D004', '17'),
('D004', '18'),
('D001', '4'),
('D001', '1'),
('D001', '2'),
('D001', '10');

-- --------------------------------------------------------

--
-- 資料表結構 `dep`
--

CREATE TABLE `dep` (
  `dep_name` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `dep`
--

INSERT INTO `dep` (`dep_name`) VALUES
('資工系'),
('外語系'),
('電子系'),
('電機系');

-- --------------------------------------------------------

--
-- 資料表結構 `student`
--

CREATE TABLE `student` (
  `stu_id` varchar(10) NOT NULL,
  `stu_name` varchar(10) DEFAULT NULL,
  `stu_gender` varchar(10) DEFAULT NULL,
  `stu_dept` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `student`
--

INSERT INTO `student` (`stu_id`, `stu_name`, `stu_gender`, `stu_dept`) VALUES
('D001', '王大明', '男', '資工系'),
('D002', '王忠明', '男', '資工系'),
('D003', '王曉明', '男', '外語系'),
('D004', '邱閔鴻', '女', '外語系');

-- --------------------------------------------------------

--
-- 資料表結構 `teacher`
--

CREATE TABLE `teacher` (
  `t_id` varchar(10) NOT NULL,
  `t_name` varchar(10) DEFAULT NULL,
  `t_dept` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `teacher`
--

INSERT INTO `teacher` (`t_id`, `t_name`, `t_dept`) VALUES
('T001', '林老師', '資工系'),
('T002', '周老師', '資工系'),
('T003', '陳老師', '外語系'),
('T004', '徐老師', '外語系');

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`cou_id`);

--
-- 資料表索引 `dep`
--
ALTER TABLE `dep`
  ADD PRIMARY KEY (`dep_name`);

--
-- 資料表索引 `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`stu_id`);

--
-- 資料表索引 `teacher`
--
ALTER TABLE `teacher`
  ADD PRIMARY KEY (`t_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
