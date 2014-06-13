/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50524
Source Host           : localhost:3306
Source Database       : pythonacl

Target Server Type    : MYSQL
Target Server Version : 50524
File Encoding         : 65001

Date: 2014-06-13 18:19:37
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for `system_rbac_catelog`
-- ----------------------------
DROP TABLE IF EXISTS `system_rbac_catelog`;
CREATE TABLE `system_rbac_catelog` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `fid` int(11) unsigned NOT NULL DEFAULT '0',
  `title` varchar(100) NOT NULL,
  `sort` int(11) NOT NULL DEFAULT '0',
  `site_id` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fid` (`fid`),
  KEY `sort` (`sort`),
  KEY `catelog_site_id` (`site_id`),
  CONSTRAINT `catelog_site_id` FOREIGN KEY (`site_id`) REFERENCES `system_rbac_sites` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of system_rbac_catelog
-- ----------------------------
INSERT INTO `system_rbac_catelog` VALUES ('1', '0', 'Admin', '0', '1');

-- ----------------------------
-- Table structure for `system_rbac_controllers`
-- ----------------------------
DROP TABLE IF EXISTS `system_rbac_controllers`;
CREATE TABLE `system_rbac_controllers` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `controller` varchar(255) NOT NULL,
  `catelog_id` int(11) unsigned NOT NULL DEFAULT '0',
  `site_id` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `controller` (`controller`) USING BTREE,
  KEY `catelog_id` (`catelog_id`),
  KEY `controller_site_id` (`site_id`),
  CONSTRAINT `catelog_id` FOREIGN KEY (`catelog_id`) REFERENCES `system_rbac_catelog` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `controller_site_id` FOREIGN KEY (`site_id`) REFERENCES `system_rbac_sites` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of system_rbac_controllers
-- ----------------------------
INSERT INTO `system_rbac_controllers` VALUES ('1', '管理', 'Admin', '1', '1');

-- ----------------------------
-- Table structure for `system_rbac_role_controller`
-- ----------------------------
DROP TABLE IF EXISTS `system_rbac_role_controller`;
CREATE TABLE `system_rbac_role_controller` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_role_id` int(11) unsigned NOT NULL,
  `controller_id` int(11) unsigned NOT NULL DEFAULT '0',
  `site_id` int(11) unsigned NOT NULL,
  `permission` tinyint(3) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `controller_id` (`controller_id`),
  KEY `user_role_id_4_controller` (`user_role_id`),
  KEY `role_controller_site_id` (`site_id`),
  CONSTRAINT `controller_id` FOREIGN KEY (`controller_id`) REFERENCES `system_rbac_controllers` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `role_controller_site_id` FOREIGN KEY (`site_id`) REFERENCES `system_rbac_sites` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `user_role_id_4_controller` FOREIGN KEY (`user_role_id`) REFERENCES `system_rbac_roles` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of system_rbac_role_controller
-- ----------------------------
INSERT INTO `system_rbac_role_controller` VALUES ('1', '1', '1', '1', '1');

-- ----------------------------
-- Table structure for `system_rbac_roles`
-- ----------------------------
DROP TABLE IF EXISTS `system_rbac_roles`;
CREATE TABLE `system_rbac_roles` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `role_name` varchar(30) NOT NULL,
  `site_id` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `roles_site_id` (`site_id`),
  CONSTRAINT `roles_site_id` FOREIGN KEY (`site_id`) REFERENCES `system_rbac_sites` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of system_rbac_roles
-- ----------------------------
INSERT INTO `system_rbac_roles` VALUES ('1', 'Admin', '0');

-- ----------------------------
-- Table structure for `system_rbac_sessions`
-- ----------------------------
DROP TABLE IF EXISTS `system_rbac_sessions`;
CREATE TABLE `system_rbac_sessions` (
  `session_id` char(128) NOT NULL,
  `atime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `data` text,
  UNIQUE KEY `session_id` (`session_id`),
  KEY `atime` (`atime`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of system_rbac_sessions
-- ----------------------------
INSERT INTO `system_rbac_sessions` VALUES ('e345ba323426724476d7606fa0d4a1b0b5488eb6', '2014-06-13 18:17:16', 'KGRwMQpTJ2NvdW50JwpwMgpJMApzUydpcCcKcDMKVjEyNy4wLjAuMQpwNApzUydzZXNzaW9uX2lk\nJwpwNQpTJ2UzNDViYTMyMzQyNjcyNDQ3NmQ3NjA2ZmEwZDRhMWIwYjU0ODhlYjYnCnA2CnMu\n');

-- ----------------------------
-- Table structure for `system_rbac_sites`
-- ----------------------------
DROP TABLE IF EXISTS `system_rbac_sites`;
CREATE TABLE `system_rbac_sites` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `domain` varchar(50) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `domain` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of system_rbac_sites
-- ----------------------------
INSERT INTO `system_rbac_sites` VALUES ('1', '', 'Admin');

-- ----------------------------
-- Table structure for `system_rbac_users`
-- ----------------------------
DROP TABLE IF EXISTS `system_rbac_users`;
CREATE TABLE `system_rbac_users` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `site_id` int(11) unsigned NOT NULL,
  `login` varchar(30) NOT NULL,
  `passwd` char(32) NOT NULL,
  `salt` char(10) NOT NULL,
  `user_role_id` int(11) unsigned NOT NULL DEFAULT '0',
  `last_login` datetime DEFAULT '0000-00-00 00:00:00',
  `last_login_ip` varchar(64) DEFAULT NULL,
  `status` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `account` (`login`),
  KEY `status` (`status`),
  KEY `user_role_id_4_user` (`user_role_id`),
  KEY `users_site_id` (`site_id`),
  CONSTRAINT `users_site_id` FOREIGN KEY (`site_id`) REFERENCES `system_rbac_sites` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `user_role_id_4_user` FOREIGN KEY (`user_role_id`) REFERENCES `system_rbac_roles` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of system_rbac_users
-- ----------------------------
INSERT INTO `system_rbac_users` VALUES ('1', '1', 'ison', '2f92ebbd3dd167504e629086cc695071', '1X6cDd7Y29', '1', '2012-03-24 02:52:51', '0', '1');
