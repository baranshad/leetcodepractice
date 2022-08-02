CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select max(salary) from 
      employee e1 
      where 
      (select count(distinct salary) = N-1
       from employee e2 
       where e2.salary>e1.salary)
      
      
      
  );
END