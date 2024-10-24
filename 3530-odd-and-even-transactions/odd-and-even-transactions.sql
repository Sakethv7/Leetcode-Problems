SELECT 
    transaction_date,
    SUM(CASE WHEN CAST(amount AS SIGNED) % 2 = 1 THEN CAST(amount AS SIGNED) ELSE 0 END) AS odd_sum,
    SUM(CASE WHEN CAST(amount AS SIGNED) % 2 = 0 THEN CAST(amount AS SIGNED) ELSE 0 END) AS even_sum
FROM 
    transactions
GROUP BY 
    transaction_date
ORDER BY 
    transaction_date ASC;
