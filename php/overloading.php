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
$emp2->calculateSalary(165, 20); // Output => Your salary is $3300
