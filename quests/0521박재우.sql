use sakila;
# 1. 모든 배우(actor) 정보를 조회하세요. 다음처럼 출력이 나오게 하세요
select concat(first_name, ' ', last_name) from actor;
/*
+----------------------+
| 배우이름             |
+----------------------+
| GUINESS PENELOPE     |
| WAHLBERG NICK        |
| CHASE ED             |
| DAVIS JENNIFER       |
| LOLLOBRIGIDA JOHNNY  |
| NICHOLSON BETTE      |
| MOSTEL GRACE         |
| JOHANSSON MATTHEW    |
| SWANK JOE            |
| GABLE CHRISTIAN      |
| CAGE ZERO            |
| BERRY KARL           |
| WOOD UMA             |
| BERGEN VIVIEN        |
.........................  이하생략 
*/

# 2. 성(last_name)이 'BERRY', 'HOFFMAN', 'DENCH' 인 배우를 조회하세요.  or연산자로 한번 in 연산자로 한번 두번 작성해보세요 
select * from actor where last_name in ('BERRY', 'HOFFMAN', 'DENCH');
select * from actor where last_name = 'BERRY' or last_name = 'HOFFMAN' or last_name = 'DENCH';
# 3. 이름이 'SCARLETT'인 배우의 actor_id를 조회하세요.
select actor_id from actor where first_name = 'SCARLETT';
# 4. actor_id가 2,18,34,56,77,88,120, 199, 192, 191 인 배우의 정보를 조회하시오 출력방식은 1번 참조입니다.
select concat(first_name, ' ', last_name) from actor where actor_id in (2,18,34,56,77,88,120, 199, 192, 191);
# 5.고객(customer) 테이블에서 이메일이 'KATHLEEN.ADAMS@sakilacustomer.org'인 고객의 전체 정보를 조회하세요.
select * from customer where email = 'KATHLEEN.ADAMS@sakilacustomer.org';
# 6. 고객 중에서 store_id가 1이고 last_name이 'MILLER'인 사람을 조회하세요.
select * from customer where store_id = 1 and last_name = 'MILLER';
# 7. 카테고리(category) 이름이 'Comedy'인 카테고리의 ID를 찾으세요.
select category_id from category where name = 'Comedy';
# 8. 7일 이상 대여된(rental_duration > 7) 영화 정보를 조회하세요.
select * from film where rental_duration > 7;
# 9. replacement_cost가 20 이상 25 이하인 영화 목록을 조회하세요.
select * from film where replacement_cost >= 20 and replacement_cost <= 25;
# 10. title에 'ACADEMY'라는 단어가 포함된 영화 제목만 검색하세요.
select title from film where title like '%ACADEMY%';
# 11. 가장 최근에 등록된 고객 5명의 이름과 이메일을 조회하세요.
select first_name, last_name, email from customer order by create_date desc limit 5;
# 12. 'Comedy' 카테고리에 속한 모든 영화 제목을 조회하세요.
select title from film where film_id in (select film_id from film_category where category_id in (select category_id from category where name = 'Comedy'));
# 13. 고객과 대여(rental)를 조인하여 고객 이름과 대여 일자를 10건만 조회하세요.
select concat(first_name, ' ', last_name), rental_date from customer a join rental b on a.customer_id = b.customer_id limit 10;
# 14. 'Action' 장르의 영화를 빌린 고객 이름과 영화 제목을 조회하세요.
select concat(first_name, ' ', last_name), title from customer a
join rental b on a.customer_id = b.customer_id
join inventory c on c.inventory_id = b.inventory_id
join film_category d on d.film_id = c.film_id
join film f on f.film_id = d.film_id
join category e on e.category_id = d.category_id
where e.name = 'Action';
# 15. 'Alberta'에 사는 고객의 이름과 이메일을 조회하세요.
select first_name, last_name, email from customer where address_id in (select address_id from address where address like '%Alberta%' or address2 like '%Alberta%');
# 16. 배우 이름과 그 배우가 출연한 영화 제목을 전체에서 10건만 조회하세요.
select first_name, last_name, title from actor a join film_actor b on a.actor_id = b.actor_id join film c on b.film_id = c.film_id;
# 17. 각 고객이 대여한 총 횟수를 고객 이름과 함께 조회하세요
select first_name, last_name, count(*) cnt from customer a join rental b on a.customer_id = b.rental_id group by a.customer_id;
# 18. 각 배우가 출연한 영화 수를 조회하고, 가장 많이 출연한 배우 상위 5명을 조회하세요.
select concat(first_name, ' ', last_name), count(*) cnt from actor a join film_actor b on a.actor_id = b.actor_id group by a.actor_id;
select concat(first_name, ' ', last_name), count(*) cnt from actor a join film_actor b on a.actor_id = b.actor_id group by a.actor_id order by cnt desc limit 5;
# 19. 각 스토어별로 총 매출을 조회하세요.
select a.store_id, sum(amount) from store a join staff b on a.store_id = b.store_id join payment c on c.staff_id = b.staff_id group by a.store_id;
# 20. 월별 대여 건수를 조회하세요 (예: 2005-06, 2005-07 등).
select date_format(rental_date, '%Y-%m') m, count(*) cnt from rental group by m;


