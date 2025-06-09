use mydb2;

show tables;

desc team;

select count(*) from team;
select * from team;

desc team;
desc player;

# 1. team_id = K01인 선수들의 명단을 확인하고 싶다
select * from player where team_id = 'K01';

# 2. K01 팀의 등번호, 입단년, 이름 각각 오름차순
select back_no, ifnull(join_yyyy, 2025) join_yyyy, player_name 
from player where team_id = 'K01'
order by join_yyyy, player_name;

select aa.* from (select back_no, join_yyyy, player_name 
from player where team_id = 'K01' and join_yyyy is null
order by join_yyyy, player_name) aa
union all 
(select back_no, join_yyyy, player_name 
	from player where team_id = 'K01' and join_yyyy is not null
	order by player_name, join_yyyy);

# 울산 지역에 있는 모든 팀과 각 팀에 속한 선수이름과 우편번호로 주소를 출력하자
select player_name, b.team_name, region_name, concat(b.zip_code1, '-', b.zip_code2), c.address, stadium_name
from player a
join team b on a.team_id = b.team_id
join stadium c on b.stadium_id = c.stadium_id
where region_name = '울산';

select b.team_name, a.player_name, b.address
from player a
join team b on a.team_id = b.team_id
where a.team_id in ('K01', 'K03');

select a.player_name,
(select team_name from team where team_id = a.team_id) team_name,
(select address from team where team_id = a.team_id) address,
(select concat(zip_code1, '-', zip_code2)
from team where team_id = a.team_id) zipcode
from player a
where a.team_id in ('K01', 'K03');

select team_name from team where team_id = 'K01';

select team_id from team;

select player_name, team_name, stadium_name
from player a
join team b on a.team_id = b.team_id
join stadium c on b.stadium_id = c.stadium_id
where a.team_id in ('K05', 'K07', 'K12')
order by team_name, back_no;

select a.player_name,
(select team_name from team where team_id = a.team_id) team_name,
(select address from team where team_id = a.team_id) address,
(select concat(zip_code1, '-', zip_code2)
from team where team_id = a.team_id) zipcode
from player a
where a.team_id in (select team_id from team where region_name = '울산');

create table test
(
	id bigint,
    title varchar(50)
);

insert into test(id, title) values(1, '제목1');
select * from test;

insert into test(id, title) select
max(id) + 1, concat(title, 2) from test;

desc player;

select player_name, 
	case posit 
		when 'GF' then '골키퍼'
        when 'DF' then '수비수'
        when 'FW' then '공격수'
        when 'MF' then '미드필더'
		else '없음'
	end as position
from player where team_id = 'K01';

# K03팀 190초과 a 180초과 b 나머지 c 
select height, a.player_id, player_name, case 
	 when (height > 190) then 'a' 
	 when (height > 180) then 'b' 
	 else 'c'
	 end grade
from player a
join team b on a.team_id = b.team_id
where a.team_id = 'K03';

select count(*) cnt from team a
join player b on a.team_id = b.team_id
where b.height >= 180
group by a.team_id;

select team_id, count(*) cnt,
	(select team_name from team where team_id = player.team_id) team_name
from player
where height >= 180
group by team_id;

select team_name
from team b join (
	select team_id, count(*) cnt
	from player
	where height >= 180
	group by team_id
) as a
on a.team_id = b.team_id;

# FC서울 전체 일정(원정 포함)
select a.team_name, i.hometeam_id , i.awayteam_id, stadium_name, sche_date
from schedule i
join team a
on i.hometeam_id = a.team_id or i.awayteam_id = a.team_id
join stadium o
on o.stadium_id = i.stadium_id
where a.team_name = 'FC서울'
order by sche_date;

select sche_date, b.team_id, b.team_name, 'home' as home
from schedule a join team b 
on a.hometeam_id = b.team_id or a.awayteam_id = b.team_id
where team_name = 'FC서울'
union all
select sche_date, b.team_id, b.team_name, 'away' as away
from schedule a join team b
on a.hometeam_id = b.team_id or a.awayteam_id = b.team_id
where team_name = 'FC서울';

# 2012년 10월 19일 C06스타디움 C05스타디움 경기하는 선수들의 이름과 팀명
select player_name, team_name
from player a
join team b on a.team_id = b.team_id
join schedule c on c.hometeam_id = b.team_id or c.awayteam_id = b.team_id
join stadium d on c.stadium_id = d.stadium_id
where c.sche_date = '20121019' and d.stadium_id in ('C06', 'C05');

# DCL : 통제, 권한을 주고 받는 등의 쿼리
# DML : insert, update, delte | select 
# DDL : 데이터 구조 정의어, create, drop, alter

CREATE TABLE `tb_member` (
  `member_id` bigint NOT NULL,
  `user_id` varchar(45) NOT NULL,
  `password` varchar(2000) NOT NULL,
  `member_name` varchar(45) NOT NULL,
  `member_phone` varchar(45) NOT NULL,
  `member_email` varchar(45) NOT NULL,
  `member_ip` varchar(45) NOT NULL,
  `reg_date` datetime DEFAULT NULL,
  `tb_membercol` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='			';

insert into tb_member(member_id, user_id, password, member_name, member_phone, member_email, member_ip, reg_date)
values (5, 'user01', '1234', '홍길동', '010-0000-1111', 'hong@gmail.com', '0.0.0.0', now());

use mydb2;

select stadium_id, sche_date, 
	case 
	when home_score = away_score then '비김' 
    when home_score > away_score then '홈팀승' 
    when home_score < away_score then '원정팀승'
    end result, 
	case 
    when home_score > away_score then hometeam_id
    when home_score < away_score then awayteam_id
    else 'None'
    end result
from schedule where gubun = 'Y';

create table tb_guestbook(
id bigint auto_increment unique,
title varchar(1000) not null,
contents text,
writer bigint,
regdate datetime);

show tables;

alter table tb_guestbook
add constraint fk_guestbook_member
foreign key(writer)
references tb_member(member_id);

use information_schema;
show tables;
select * from tables;

select table_name from tables where table_schema = 'sakila';
select * from key_column_usage where table_schema = 'mydb2';

use mydb;
alter table tb_guestbook
add constraint fk_guestbook_member
foreign key(writer)
references tb_member(member_id);

use mysql;
select * from user;

select * from tb_guestbook;

insert into tb_guestbook(title, writer, contents, regdate)
values('제목1', 1, '내용1', now());

insert into tb_guestbook(title, writer, contents, regdate)
values('제목2', 2, '내용2', now());


