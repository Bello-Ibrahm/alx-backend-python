# Overriding versus Overloading in PHP Object Oriented Programming (OOP)

In this article, I'll delve into the concepts of method overriding and overloading in PHP object-oriented programming (OOP), elucidating their significance with examples.

Before we proceed, I'll assume a basic understanding of OOP principles. However, if you're new to the concept, fret not! I'll guide you through with detailed explanations.

Method overriding and overloading are fundamental concepts in PHP OOP, each serving unique purposes and exhibiting distinct behaviors. Let's explore them in depth:

# Overriding Image here

**Overriding:**
Overriding refers to providing a new implementation for a method in a Derived class(subclass) that is already defined in its Base class (superclass). The method in the subclass has the same name, parameters, and return type as the method in the superclass.

The purpose of overriding is to allow a subclass to provide its own implementation of a method inherited from its superclass. This enables customization and specialization of behavior in subclasses while maintaining a common interface defined by the superclass.
*Example:*
I will use a Database and Oracle Database class as an example.
*Overridding Code* 
```
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

```


# Overloading Image here

**Overloading:**
Overloading allows the definition of multiple methods with the same name but different parameters or parameter types within a single class. While PHP does not directly support true method overloading like languages such as Java or C++, alternatives exist. I'll demonstrate how to achieve method overloading in PHP using magic methods like __call() and manual techniques.

The purpose of overloading is to allow a class to define multiple methods with the same name but different parameter lists. This enables flexibility in method invocation and can be used to provide alternative ways to interact with objects of the class.
*Example:*
I will use an Employee class to demostrate method overloading example.

*Overloading Code*
```
<?php

class Employee {
    private $hours = 180;
    private $hourPrice = 10;

    public function calculateSalary()
    {
        $salary = $this->hours * $this->hourPrice;
        echo "Default, your salary is $$salary" . PHP_EOL;   
    }
    
    public function calculateSalary($arg1, $arg2)
    {
        $this->hours = $arg1; 
        $this->hourPrice = $arg2; 
        $salary = $arg1 * $arg2;
        echo "Your salary is $$salary" . PHP_EOL;
    }
}
```
Running the code above result in error: 
*Image here*

**Using the magic __call() method:**
```
<?php

class Employee {
    public $hours = 180;
    public $hourPrice = 10;

    public function __call($name, $args) {
        if ($name === 'calculateSalary') {
            $argCount = count($args);
            switch ($argCount) {
                case 0:
                    $this->methodWithNoArg();
                    break;
                case 2:
                    $this->methodWithTwoArg($args[0], $args[1]);
                    break;
                default:
                    echo "Invalid arguments" . PHP_EOL;
                    break;
            }
        }
    }

    private function methodWithNoArg()
    {
        $salary = $this->hours * $this->hourPrice;
        echo "Default, your salary is $$salary" . PHP_EOL;
    }
    
    private function methodWithTwoArg($arg1, $arg2)
    {
        $this->hours = $arg1; 
        $this->hourPrice = $arg2; 
        $salary = $arg1 * $arg2;
        echo "Your salary is $$salary" . PHP_EOL;
    }
}
$emp1 = new Employee();
$emp1->calculateSalary(); // Output => Default, your salary is $1800

$emp2 = new Employee();
$emp2->calculateSalary(190, 15); // Output => Your salary is $2850
```

**Using the variadic function (variable-length) method:**
```
<?php

class Employee {
    public $hours = 180;
    public $hourPrice = 10;

    public function calculateSalary(...$args)
    {
        $argCount = count($args);
        switch ($argCount) {
            case 0:
                $this->methodWithNoArg();
                break;
            case 2:
                $this->methodWithTwoArg($args[0], $args[1]);
                break;
            default:
                echo "Invalid arguments" . PHP_EOL;
                break;
        }
    }

    private function methodWithNoArg()
    {
        $salary = $this->hours * $this->hourPrice;
        echo "Default, your salary is $$salary" . PHP_EOL;
    }
    
    private function methodWithTwoArg($arg1, $arg2)
    {
        $this->hours = $arg1; 
        $this->hourPrice = $arg2; 
        $salary = $arg1 * $arg2;
        echo "Your salary is $$salary" . PHP_EOL;
    }
}

$emp1 = new Employee();
$emp1->calculateSalary(); // Output => Default, your salary is $1800

$emp2 = new Employee();
$emp2->calculateSalary(190, 15); // Output => Your salary is $2850
```

**Conclusion**
Both overriding and overloading are essential concepts in PHP object-oriented programming, each serving distinct purposes:

**Overriding:** Allows a subclass to provide its own implementation for a method inherited from its superclass, enabling customization and specialization of behavior while maintaining a common interface.

**Overloading:** offers flexibility by enabling a class to define multiple methods with identical names but varying parameter lists. Although PHP doesn't natively support true method overloading as in some other languages, it provides mechanisms such as magic methods to emulate this behavior. As demonstrated earlier, I've showcased manual techniques alongside the utilization of magic methods to achieve overloading functionality in PHP.

Both concepts contribute to the flexibility, extensibility, and maintainability of object-oriented code in PHP, enabling developers to create more modular, reusable, and adaptable software systems. Understanding when and how to use overriding and overloading effectively can lead to well-structured, efficient, and scalable PHP applications.

If you have any other effective manual techniques for implementing method overloading in PHP OOP, feel free to share them in the comments below. Additionally, if you found this article insightful and helpful, please consider liking and sharing it with others. Your support is greatly appreciated!