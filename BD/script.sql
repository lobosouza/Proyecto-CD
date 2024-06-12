-- MySQL Script generated by MySQL Workbench
-- Wed Jun 12 01:40:52 2024
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `mydb` ;

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8mb3 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Proveedores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Proveedores` (
  `ID_Proveedor` INT NOT NULL AUTO_INCREMENT,
  `Nombre_Proveedor` VARCHAR(50) NOT NULL,
  `Direccion` VARCHAR(60) NOT NULL,
  `Mail` VARCHAR(55) NOT NULL,
  `Telefono` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`ID_Proveedor`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

-- -----------------------------------------------------
-- Table `mydb`.`Compras`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Compras` (
  `ID_Compra` INT NOT NULL AUTO_INCREMENT,
  `ID_Proveedor` INT NOT NULL,
  `Precio_Total` DECIMAL(10,2) NOT NULL,
  `Fecha` DATETIME NOT NULL,
  PRIMARY KEY (`ID_Compra`),
  INDEX `FK_Proveedores_idx` (`ID_Proveedor` ASC) VISIBLE,
  CONSTRAINT `ID_Proveedor`
    FOREIGN KEY (`ID_Proveedor`)
    REFERENCES `mydb`.`Proveedores` (`ID_Proveedor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

-- -----------------------------------------------------
-- Table `mydb`.`Productos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Productos` (
  `ID_Producto` INT NOT NULL AUTO_INCREMENT,
  `Nombre_Producto` VARCHAR(45) NOT NULL,
  `Precio_Venta` DECIMAL(10,2) NOT NULL,
  `Precio_Compra` DECIMAL(10,2) NOT NULL,
  `Cantidad_Stock` INT NOT NULL CHECK (`Cantidad_Stock` >= 0),
  `Descripcion` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`ID_Producto`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

-- -----------------------------------------------------
-- Table `mydb`.`Detalle_Compras`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Detalle_Compras` (
  `ID_Detalle_Compra` INT NOT NULL AUTO_INCREMENT,
  `ID_Compra` INT NOT NULL,
  `ID_Producto` INT NOT NULL,
  `Cantidad` INT NOT NULL CHECK (`Cantidad` > 0),
  PRIMARY KEY (`ID_Detalle_Compra`),
  INDEX `FK_Compras_idx` (`ID_Compra` ASC) VISIBLE,
  INDEX `FK_Productos_idx` (`ID_Producto` ASC) VISIBLE,
  CONSTRAINT `ID_Compra`
    FOREIGN KEY (`ID_Compra`)
    REFERENCES `mydb`.`Compras` (`ID_Compra`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `ID_Producto`
    FOREIGN KEY (`ID_Producto`)
    REFERENCES `mydb`.`Productos` (`ID_Producto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

-- -----------------------------------------------------
-- Table `mydb`.`Clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Clientes` (
  `ID_Cliente` INT NOT NULL AUTO_INCREMENT,
  `DNI` INT NOT NULL,
  `Apellido_Nombre` VARCHAR(50) NOT NULL,
  `Mail` VARCHAR(55) NOT NULL,
  `Telefono` VARCHAR(30) NOT NULL,
  `Direccion` VARCHAR(60) NULL DEFAULT NULL,
  `Es_Jubilado` TINYINT(1) NOT NULL,
  PRIMARY KEY (`ID_Cliente`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

-- -----------------------------------------------------
-- Table `mydb`.`Ventas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Ventas` (
  `ID_Venta` INT NOT NULL AUTO_INCREMENT,
  `ID_Cliente` INT NULL DEFAULT NULL,
  `Precio_Total` DECIMAL(10,2) NOT NULL,
  `Fecha` DATETIME NOT NULL,
  PRIMARY KEY (`ID_Venta`),
  INDEX `FK_Clientes_idx` (`ID_Cliente` ASC) VISIBLE,
  CONSTRAINT `ID_Clientes`
    FOREIGN KEY (`ID_Cliente`)
    REFERENCES `mydb`.`Clientes` (`ID_Cliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

-- -----------------------------------------------------
-- Table `mydb`.`Detalle_Ventas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Detalle_Ventas` (
  `ID_Detalle_Venta` INT NOT NULL AUTO_INCREMENT,
  `ID_Venta` INT NOT NULL,
  `ID_Producto` INT NOT NULL,
  `Cantidad` INT NOT NULL CHECK (`Cantidad` > 0),
  PRIMARY KEY (`ID_Detalle_Venta`),
  INDEX `idProducto_idx` (`ID_Producto` ASC) VISIBLE,
  INDEX `idVenta_idx` (`ID_Venta` ASC) VISIBLE,
  CONSTRAINT `ID_Producto`
    FOREIGN KEY (`ID_Producto`)
    REFERENCES `mydb`.`Productos` (`ID_Producto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `ID_Venta`
    FOREIGN KEY (`ID_Venta`)
    REFERENCES `mydb`.`Ventas` (`ID_Venta`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

DELIMITER //
CREATE PROCEDURE InsertarClienteAnonimo()
BEGIN
  DECLARE anonimoID INT;
  INSERT INTO `mydb`.`Clientes` (`DNI`, `Apellido_Nombre`, `Mail`, `Telefono`, `Es_Jubilado`)
  VALUES (0, CONCAT('Anónimo ', UUID()), 'anonimo@ejemplo.com', '0000000000', 0);
  SET anonimoID = LAST_INSERT_ID();
  SELECT anonimoID;
END //
DELIMITER ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

