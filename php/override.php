<?php

class Database {
  public function getConnection()
  {
    echo "Default connection from the MySQL Database" . PHP_EOL;
  } 
}


class OracleDatabase extends Database {

  public function getConnection()
  {
    echo "Connection from the Oracle Database" . PHP_EOL;
  }
}


$db1 = new Database();
$db1->getConnection();

$db2 = new OracleDatabase();
$db2->getConnection();