-- MySQL Workbench Synchronization
-- Generated: 2024-06-11 20:42
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: Uvita

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

ALTER TABLE `mydb`.`productos` 
DROP FOREIGN KEY `Provisión`;

ALTER TABLE `mydb`.`Ventas` 
DROP FOREIGN KEY `cliente`;

ALTER TABLE `mydb`.`Ventas` 
CHARACTER SET = utf8 , COLLATE = utf8_spanish_ci ;

CREATE TABLE IF NOT EXISTS `mydb`.`Detalle_Venta` (
  `idDetalle_Venta` INT(11) NOT NULL AUTO_INCREMENT,
  `fecha` DATETIME NOT NULL,
  `Productos` INT(11) NOT NULL,
  `Precio_Unitario` DECIMAL(10) NOT NULL,
  PRIMARY KEY (`idDetalle_Venta`),
  INDEX `idProductos_idx` (`Productos` ASC) VISIBLE,
  CONSTRAINT `idProductos`
    FOREIGN KEY (`Productos`)
    REFERENCES `mydb`.`Productos` (`idProductos`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE,
  CONSTRAINT `idVenta`
    FOREIGN KEY (`idDetalle_Venta`)
    REFERENCES `mydb`.`Ventas` (`IdVenta`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

ALTER TABLE `mydb`.`productos` 
ADD CONSTRAINT `Provisión`
  FOREIGN KEY (`idProductos`)
  REFERENCES `mydb`.`Proveedores` (`idProveedores`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `mydb`.`Ventas` 
DROP FOREIGN KEY `venta`;

ALTER TABLE `mydb`.`Ventas` ADD CONSTRAINT `venta`
  FOREIGN KEY (`IdVenta`)
  REFERENCES `mydb`.`Productos` (`idProductos`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `cliente`
  FOREIGN KEY (`IdVenta`)
  REFERENCES `mydb`.`Clientes` (`DNI`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
