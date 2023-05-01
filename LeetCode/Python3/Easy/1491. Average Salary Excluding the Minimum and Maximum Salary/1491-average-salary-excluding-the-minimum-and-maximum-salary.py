class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = min(salary)
        max_salary = max(salary)
        total_sum = sum(salary)
        adjusted_sum = total_sum - min_salary - max_salary
        n = len(salary) - 2
        avg_salary = adjusted_sum / n
        return round(avg_salary, 5)