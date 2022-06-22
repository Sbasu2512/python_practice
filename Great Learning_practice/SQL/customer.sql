select * from customer;
select customer_id, customer_name, credit_limit from customer group by customer_id having max(credit_limit) ;
select * from customer order by credit_limit desc limit 5;