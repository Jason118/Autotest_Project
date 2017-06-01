-- schema.sql

drop database if exists interface;

create database interface;
use interface;

/* grant select, insert, update, delete on awesome.* to 'www-data'@'localhost' identified by 'www-data'; 
grant select, insert, update, delete on interface.* to 'interface_test'@'%' identified by 'interface_test'; */
grant all privileges  on *.* to 'interface_test'@'%' identified by 'interface_test';

flush privileges; 

create table interface_case(
  `model` varchar(50) not null,
  `interfaceName` varchar(50) not null,
  `interfaceID` varchar(50) not null,
  `caseID` varchar(50) not null,
  `caseName` varchar(100) not null,
  `caseLevel` varchar(50) not null,
  `reqMode` varchar(50) not null,
  `preRequisite` varchar(500),
  `caseStep` varchar(5000) not null,
  `caseData` varchar(5000) not null,
  `expResult` varchar(5000) not null,
  `testResult` varchar(5000),
  `testEnvironment` varchar(50) ,
  `autoSupport` varchar(50) not null,
  `author` varchar(50) not null,
  `remarks` varchar(500) ,
  `status` varchar(50) ,
  `createDate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  key `idx_caseLevel` (`caseLevel`),
  key `idx_autoSupport` (`autoSupport`),
  key `idx_status` (`status`),
  primary key (`caseID`)
) engine=innodb default charset=utf8;


/*caseID,caseName,interfaceID,reqMode,caseData,expResult, result, reason */
create table test_result(
  `interfaceID` varchar(50) not null,
  `caseID` varchar(50) not null,
  `caseName` varchar(100) not null,
  `reqMode` varchar(50) not null,
  `caseData` varchar(5000) not null,
  `expResult` varchar(5000) not null,
  `result` varchar(5000), 
  `reason` varchar(5000) ,
  primary key (`caseID`)
) engine=innodb default charset=utf8;

/*
create table blogs(
  `id` varchar(50) not null,
  `user_id` varchar(50) not null,
  `user_name` varchar(50) not null,
  `user_image` varchar(500) not null,
  `name` varchar(50) not null,
  `summary` varchar(200) not null,
  `content` mediumtext not null,
  `created_at` real not null,
  key `idx_create_at` (`created_at`),
  primary key (`id`)
) engine=innodb default charset=utf8;

create table comments(
  `id` varchar(50) not null,
  `blog_id` varchar(50) not null,
  `user_id` varchar(50) not null,
  `user_name` varchar(50) not null,
  `user_image` varchar(500) not null,
  `content` mediumtext not null,
  `created_at` real not null,
  key `idx_create_at` (`created_at`),
  primary key (`id`)
) engine=innodb default charset=utf8;

*/
/*-- email / password:  */
/*-- admin@example.com /password  */

