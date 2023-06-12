/* Write your T-SQL query statement below */
;WITH emp as (
  select Max(salary) as maxSalary, departmentId from Employee
  group by
  departmentId
)
select e.name as Employee, e.salary as Salary, d.name as Department from Employee e 
inner join Department d
on d.id = e.departmentId
inner join emp
on emp.maxSalary = e.salary and emp.departmentId = d.id