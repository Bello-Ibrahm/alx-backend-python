<?php

class Employee {
    private $hours = 180;
    private $hourPrice = 10;

    // public function calculateSalary()
    // {
    //     $salary = $this->hours * $this->hourPrice;
    //     echo "Default your salary is $$salary" . PHP_EOL;   
    // }
    
    public function calculateSalary($arg1, $arg2)
    {
        $this->hours = $arg1; 
        $this->hourPrice = $arg2; 
        $salary = $arg1 * $arg2;
        echo "Your salary is $$salary" . PHP_EOL;
    }
}

class Employee1 {
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
        echo "Your default salary is $$salary" . PHP_EOL;
    }
    
    private function methodWithTwoArg($arg1, $arg2)
    {
        $this->hours = $arg1; 
        $this->hourPrice = $arg2; 
        $salary = $arg1 * $arg2;
        echo "Your modify salary is $$salary" . PHP_EOL;
    }
}

class Employee2 {
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
        echo "Default your salary is $$salary" . PHP_EOL;
    }
    
    private function methodWithTwoArg($arg1, $arg2)
    {
        $this->hours = $arg1; 
        $this->hourPrice = $arg2; 
        $salary = $arg1 * $arg2;
        echo "Your salary is $$salary" . PHP_EOL;
    }
}

$obj = new Employee();
$obj->calculateSalary();
// $obj->calculateSalary(500, 10);
// $obj->calculateSalary(500, 10, 3);
