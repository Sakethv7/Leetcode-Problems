# Write your MySQL query statement below
# find the prices of all products on a specific date, 
# resultant table should  be product_id, price
# if a product's price was changed after 16th then assume its price on 16th or before that was 10 

SELECT product_id, 
       COALESCE( 
           (SELECT new_price 
            FROM products p2 
            WHERE p1.product_id = p2.product_id 
              AND p2.change_date <= '2019-08-16' 
            ORDER BY p2.change_date DESC 
            LIMIT 1), 
           10) AS price  # coalesce helps replacing missing values
FROM products p1
GROUP BY product_id;