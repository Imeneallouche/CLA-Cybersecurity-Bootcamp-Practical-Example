# 1. Encapsulation

```yaml
Example: BankAccount class
```

### Explanation:

- Encapsulation refers to bundling the data (attributes) and methods that operate on the data into a single unit or class.

- In the BankAccount class, the attributes (balance) and methods (deposit, withdraw) are encapsulated within the class.

- This encapsulation hides the internal state of the object and restricts direct access to it from outside the class

- Why? To ensure data integrity and security.

<br><br>

# 2. Abstraction

```yaml
Example: Shape and its subclasses (Rectangle, Circle)
```

### Explanation:

- Abstraction involves hiding the complex implementation details and exposing only the essential features of an object.

- In the Shape class, the area method is declared as an abstract method, indicating that every subclass must implement

- Subclasses like Rectangle and Circle provide concrete implementations of the area method, while the Shape class itself remains abstract, providing a blueprint for creating shape objects.

- This abstraction allows users to work with shapes without needing to know the specific implementation details of each shape.

<br><br>

# 3. Inheritance

```yaml
Example: Animal class and its subclasses (Dog, Cat)
```

### Explanation:

- Inheritance is a mechanism in which a new class (subclass) is created based on an existing class (superclass), inheriting its attributes and methods.

- The subclass can then extend or modify the behavior of the superclass.

- In the example, We have a base class Employee with attributes name and salary, and a method calculate_pay to calculate the salary

- We have two subclasses: Developer and Manager, representing different types of employees.

- Each subclass inherits from the Employee class and adds its own attributes and methods.

- The Developer subclass adds a programming_language attribute and a write_code method, while the Manager subclass adds a department attribute and a manage_team method.

<br><br>

# 4. Polymorphism

```yaml
Example: Shape class and its subclasses (Rectangle, Circle, Triangle)
```

Explanation:

- Polymorphism allows objects of different classes to be treated as objects of a common superclass.

- It enables the same method to behave differently based on the object it is called on.

- In the example, When we create objects of each subclass (Rectangle, Circle, Triangle) and call the area method on them, polymorphism allows the behavior of the area method to vary depending on the type of shape.

- Despite calling the same method (area), each object invokes its own implementation of the method specific to its class.

- This showcases polymorphic behavior, where objects of different classes are treated uniformly while exhibiting different behaviors based on their types.
