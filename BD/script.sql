-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8mb3 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`clientes` (
  `idClientes` INT NOT NULL,
  PRIMARY KEY (`idClientes`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`productos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`productos` (
  `idProductos` INT NOT NULL,
  `Nombre_Producto` VARCHAR(45) NOT NULL,
  `Precio_Venta` DECIMAL(10,0) NOT NULL,
  `Precio_Compra` DECIMAL(10,0) NOT NULL,
  PRIMARY KEY (`idProductos`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`proveedores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`proveedores` (
  `idProveedores` INT NOT NULL,
  PRIMARY KEY (`idProveedores`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
