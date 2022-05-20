select * from product;
select * from customer;

select c.customer_id, c.customer_name, c.credit_limit, p.price, p.product_name, p.product_id from customer c 
left outer join product p 
on c.credit_limit 
where c.credit_limit > p.price
order by c.customer_name ;