# select * from emp limit 10;
# desc emp;
# insert into emp(empno, ename) values(8000, '장길산');
# desc emp;

# select * from emp;
# delete from emp where empno = 8000 and ename = '장길산';
# alter table emp add constraint pk_emp primary key(empno);
# alter table emp drop primary key;
# set SQL_SAFE_UPDATES = 0;  # disable safe mode
# alter table emp add constraint pk_emp primary key(empno);

desc dept;

# 외래키를 걸어주는 원본 대상 칼럼은 unique해야 한다.
# 다른 데이터 타입 간의 자동 변환은 제공되지 않는다.

# alter table emp add constraint fk_emp_dept
# foreign key(deptno) references dept(deptno);

select * from dept;
delete from dept where deptno = 10;
select * from emp;
update emp set deptno = 50 where empno = 8000;

select a.EMPNO, a.ENAME, a.DEPTNO, b.DNAME
from dept b join emp a
on b.deptno = a.deptno;

select a.EMPNO, a.ENAME, a.DEPTNO, b.DNAME
from dept b, emp a
where a.deptno = b.deptno and
a.empno in (7369, 7892, 8000, 7900, 7902);

select a.EMPNO, a.ENAME, a.DEPTNO, b.DNAME
from dept b join emp a
on a.deptno = b.deptno where
a.empno in (7369, 7892, 8000, 7900, 7902);

select a.EMPNO, a.ENAME, a.DEPTNO, b.DNAME
from dept b inner join emp a
on a.deptno = b.deptno;


select a.EMPNO, a.ENAME, b.DEPTNO, b.DNAME
from dept b left outer join emp a
on a.deptno = b.deptno;

select distinct deptno from emp;

use sakila;
select * from actor limit 10;
select * from film limit 10;


select * from film_actor limit 10;

select title, description, actor_id
from film a left join film_actor b on a.film_id = b.film_id;

select title, description, b.actor_id, concat(c.last_name, " ", c.first_name) actor_name
from film a
join film_actor b on a.film_id = b.film_id
join actor c on b.actor_id = c.actor_id;

desc film; desc category; desc film_category;

select a.*, b.*, c.* 
from film a join film_category b
on a.film_id = b.film_id
join category c
on b.category_id = c.category_id 
where c.name = 'Comedy';

# 문제1. 고객의 이름과 고객이 대여한 영화 제목을 모두 출력하자
# customer, rental, inventory, film
select distinct concat(a.first_name, ' ', a.last_name) n, d.title t
from customer a 
join rental b on b.customer_id = a.customer_id
join inventory c on b.inventory_id = c.inventory_id
join film d on d.film_id = c.film_id 
order by n, t;

# 문제2. NICK WAHLBERG 라는 배우가 출연한 영화의 제목 조회하기
select f.title
from actor a 
join film_actor fa on a.actor_id = fa.actor_id
join film f on f.film_id = fa.film_id
where a.first_name = 'NICK' and a.last_name = 'WAHLBERG';

# 문제3. 'London'의 고객 이름만 출력
select distinct concat(c.first_name, ' ', c.last_name)
from customer c 
join address a on a.address_id = c.address_id
join city ci on a.city_id = ci.city_id
where ci.city = 'London';

use mydb;

select empno, ename, deptno from emp;

select dname from dept where deptno = 10;

select (select dname from dept where dept.deptno = emp.deptno) dname, empno, ename, deptno
from emp;

use sakila;

select first_name, last_name, 
(select title from film c where b.film_id = c.film_id) title,
(select length from film c where b.film_id =  c.film_id) as length
from actor a left join film_actor b on a.actor_id = b.actor_id;

use mydb;

select a.ename, dname
from (select * from emp where deptno in (10, 20)) a
join dept b on a.deptno = b.deptno;

select * from emp where deptno = (select deptno from emp where ename = 'SMITH');

select avg(sal) from emp where deptno = (select deptno from emp where ename = 'SMITH');

select ename, sal from emp where sal > 
(select avg(sal) from emp where deptno = (select deptno from emp where ename = 'SMITH'));

select * from emp o where sal > (select avg(sal) from emp i where i.DEPTNO = o.deptno);

select max(sal) from emp;

select * from emp where mgr is not null;

# exists, any, all, in
select avg(sal) from emp where deptno = 10;
select avg(sal) from emp where deptno = 20;
select avg(sal) from emp where deptno = 30;
select avg(sal) from emp where deptno = 40;

select empno, sal, deptno from emp;

select empno, sal, deptno from emp o
where sal > (select  avg(sal) from emp i where i.DEPTNO = o.deptno);

select empno, ename, mgr from emp a
where exists (select 1 from emp b where b.empno = a.mgr);

select a.*, b.customerName, concat(c.firstName, ' ', c.lastName) from orders A
join customers b on a.customerId = b.customerId
join employees c on a.employeeid = c.employeeid;

select *
, (select customername from customers b where b.customerid = a.customerid)
, (select concat(c.firstname, ' ', c.lastname) from employees c where a.employeeid = c.employeeid)
from orders a;

use mydb;

select ename, sal, (select avg(sal) from emp) avg_sal
from emp;

select deptno, avg(sal) from emp group by deptno;

select ename, deptno, (select avg(sal) from emp b where a.deptno = b.deptno) dept_sal
from emp a;

select ename, a.deptno, dept_sal, sum_sal, max_sal, min_sal
from emp a
left join(select deptno, avg(sal) dept_sal, sum(sal) sum_sal, max(sal) max_sal, min(sal) min_sal
from emp group by deptno) b
on a.deptno = b.deptno;

use w3schools;

# 고객별 주문 수 내림차순
select customername, count(*) cnt 
from customers group by customerid order by cnt desc, customername;

-- 오늘의 과제 --
use w3schools;
# 과제1. 주문이 한번도 없는 고객의 이름을 조회하기
	select * from customers 
    where customerid not in (select customerid from orders);
# 과제2. 가장 주문건수가 많은 판매자 이름구하기
	select e.firstName, e.lastName
	from employees e
	where employeeid = (select employeeid 
		from orders 
		group by employeeid 
		order by count(*) desc limit 1);
-- 과제3. 판매건수가 5건 이상인 판매자 인원수 구하기
select count(*) cnt 
	from (select employeeid 
		from orders 
		group by employeeid 
		having count(*) >= 5) a;
        
# 10258 	10263 	10351 	10368 	10382	10390	10402	10403	10430	10042
use w3schools;
desc orderdetails;

select a.productid, quantity, productname
from orderdetails a
join products b on a.productid = b.productid
where orderid in (
	select orderid from customers a join orders b on a.customerid = b.customerid
	where customername like '%Handel%'
);

select a.customerid, b.orderid
from customers a, orders b;

use mydb;

with recursive cte as (
	select a.empno, a.ename, a.job, a.mgr, a.sal, a.comm, a.deptno, a.gender, 1 lv
    from emp a where MGR is null
    union all
    select b.empno, b.ename, b.job, b.mgr, b.sal, b.comm, b.deptno, b.gender, cte.lv + 1 lv
    from emp b
    join cte on b.mgr = cte.empno
)
select * from cte;

use w3schools;
select a.lastname, b.orderid, d.customername, c.shippername, g.productname
from employees a
join orders b on a.employeeid = b.employeeid
join orderdetails f on f.orderid = b.orderid
join products g on g.productid = f.productid
join customers d on d.customerid = b.customerid
join shippers c on b.shipperid = c.shipperid
join products e where a.lastname like '%King%';

use mydb;
select empno, ename from emp
union all
select deptno, dname from dept;

use w3schools;
select aa.*
from (
	select shippername, count(*) cnt, a.shipperid
    from orders a
    join shippers b on a.shipperid = b.shipperid
    group by shippername
) aa
join orders b on b.shipperid = aa.shipperid;

select shippername, count(*) cnt, a.shipperid
    from orders a
    join shippers b on a.shipperid = b.shipperid
    group by shipperid
    order by count(*) desc
    limit 2;
    
select orderid, b.shipperid, cnt from orders a
	join (
	select a.shipperid, count(*) cnt
	from orders a
	join shippers b 
	on a.shipperid = b.shipperid
	group by shipperid
	order by count(*) desc
limit 2) b 
on a.shipperid = b.shipperid;

select suppliername
from suppliers a
where exists (
	select 1 from products b
    where b.supplierid = a.supplierid and price < 20
);

select ceil(25.55);
select floor(25.55);

select adddate('2017-06-15', interval 10 day);
select adddate('2017-06-15', interval -77 day);
select adddate('2017-06-15', interval 15 minute);

select datediff('2017-01-01', '2017-02-01');

use mydb;
desc dept;
select * from dept;

insert into dept(deptno, dname) value(60, 'lgbt');
select * from dept;

desc emp;
insert into emp(empno) values(9000);
insert into emp(empno, ename, sal) values(8000, '홍길동', '3000');

insert into emp(empno, ename, sal)
values(8001, '둘리', '3200'),
	(8002, '도우너', '3200'),
	(8003, '길동이', '3200');

select * from emp;

insert into emp(empno, ename, sal) values(8004, 'tmp', '3200'), (8005, '''jane''', '7500');

select * from emp;

create table emp2 as select * from emp;
create table emp3 as select * from emp where 1 = 0;
CREATE TABLE emp4 LIKE emp3;

USE W3SCHOOLS;
-- 문제1. customers 테이블의 구조를 복사한 후 customers2로 
-- 만들고 고객 아이디중에 3,23,21,45,67,89,54 복사하기 

CREATE TABLE CUSTOMERS2 LIKE CUSTOMERS;
INSERT INTO CUSTOMERS2 SELECT * FROM CUSTOMERS WHERE CUSTOMERID IN (3, 23, 21, 45, 67, 89, 54);

-- 문제2. 고객아이디중에 4,5,11,33,42,43,56,57,58번을 이동하기 
--        customers -> customers2 로 옮기기 
INSERT INTO CUSTOMERS2 SELECT * FROM CUSTOMERS WHERE CUSTOMERID IN (4, 5, 11, 33, 42, 43, 56, 57, 58);

ALTER TABLE ORDERS DROP foreign key ORDERS_IBFK_1; 

-- alter table customers add primary key(customerid);

-- ALTER TABLE ORDERS ADD 
-- CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`customerID`) REFERENCES `CUSTOMERS` (`customerID`)
-- ON UPDATE CASCADE ON DELETE CASCADE;

DELETE FROM CUSTOMERS WHERE CUSTOMERID IN (4,5,11,33,42,43,56,57,58);

-- 문제3. 제품가격이 100$를 넘는 제품을 구매한 고객 리스트 
SELECT * FROM CUSTOMERS
WHERE CUSTOMERID in (
	SELECT CUSTOMERID FROM ORDERS 
    GROUP BY ORDERID IN(
		SELECT ORDERID FROM ORDERDETAILS WHERE PRODUCTID IN (
			SELECT PRODUCTID FROM PRODUCTS WHERE PRICE >= 100)
		)
	);

-- 문제4. orderdetails테이블의 quantity가 제품을 구매한 수량이고 product테이블의 있는 
--       price 가 단가이다. 구매한 고객이름과, 제품명, 제품전체가액을 구하시오 
--      예) 홍길동    가구     quiantity 와 price 가 곱해져야 한다. 
SELECT A.CUSTOMERNAME, D.PRODUCTNAME, C.QUANTITY * D.PRICE
FROM CUSTOMERS A
JOIN ORDERS B ON A.CUSTOMERID = B.CUSTOMERID
JOIN ORDERDETAILS C ON C.ORDERID = B.ORDERID
JOIN PRODUCTS D ON C.PRODUCTID = D.PRODUCTID;

-- 문제5. 핀란드에 있는 공급자 리스트 가져오기 
SELECT * FROM SUPPLIERS WHERE COUNTRY = 'Finland';

-- 문제6. 카테고리 제품이 seafood 인 제품의 구매자 리스트를 조회하시오 
SELECT * FROM CUSTOMERS A
JOIN ORDERS B ON A.CUSTOMERID = B.CUSTOMERID
JOIN ORDERDETAILS C ON B.ORDERID = C.ORDERID
JOIN PRODUCTS D ON C.PRODUCTID = D.PRODUCTID
JOIN CATEGORIES E ON D.CATEGORYID = E.CATEGORYID
WHERE LOWER(CATEGORYNAME) = 'Seafood';

# 오늘의 과제
use w3schools;
# 문제1. Customers 테이블에서 나라가 Geramany인 나라의 정보 전체
select * from customers where lower(country) = 'Germany';

# 문제2. customers 테이블에서 나라가 Austria, USA, Poland, Denmark에 사는 고객리스트
select * from customers where lower(country) in ('Austria', 'USA', 'Poland', 'Denmark');

# 문제3. 각자 나라별로 고객이 몇명씩 있는지 확인
select country, count(*) cnt from customers group by country;

# 문제4. 나라별로 고객이 5명 이상인 나라 목록만 조회
select country, count(*) cnt from customers group by country having count(*) >= 5;

# 문제5. 나라이름이 B로 시작하는 나라들의 고객 전체 합
select a.country, sum(d.price * c.quantity)
from customers a
JOIN ORDERS B ON A.CUSTOMERID = B.CUSTOMERID
JOIN ORDERDETAILS C ON B.ORDERID = C.ORDERID
JOIN PRODUCTS D ON C.PRODUCTID = D.PRODUCTID
group by a.country having lower(a.country) like 'B%';

# 문제6. 나라는 UK 도시명은 London에 있는 고객들 이름 목록
select customername from customers where lower(country) = 'UK' and lower(city) = 'London';

# 문제7. 주문날짜가 '1996-07-01'~'1996-09-30' 일까지의 주문아이디와 고객이름
select a.customerid, a.customername
from customers a
join orders b on a.customerid = b.customerid
where b.orderdate >= '1996-07-01' and b.orderdate <= '1996-09-30';

# 문제8. 위의 7번 문제를 고객이름 오름차순으로 정렬하여 출력하기
select a.customerid, a.customername
from customers a
join orders b
on a.customerid = b.customerid
where b.orderdate >= '1996-07-01' and b.orderdate <= '1996-09-30'
order by customername;

# 문제9. 배달자가 Federal Shipping인 경우의 상품명, 가격, 수량만 출력
select productname, price, c.quantity
from orders b
join shippers a on a.shipperid = b.shipperid
JOIN ORDERDETAILS C ON B.ORDERID = C.ORDERID
JOIN PRODUCTS D ON C.PRODUCTID = D.PRODUCTID
where lower(a.shippername) = 'Federal Shipping';