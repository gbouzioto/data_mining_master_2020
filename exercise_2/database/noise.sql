
--noise No1
insert into funding (scientist_id,funder,budget,start_date,end_date)(select scientist_id,funder,budget,start_date,end_date from funding where funding_id=1);
insert into funding (scientist_id,funder,budget,start_date,end_date)(select scientist_id,funder,budget,start_date,end_date from funding where funding_id=1);
insert into funding (scientist_id,funder,budget,start_date,end_date)(select scientist_id,funder,budget,start_date,end_date from funding where funding_id=2);
insert into funding (scientist_id,funder,budget,start_date,end_date)(select scientist_id,funder,budget,start_date,end_date from funding where funding_id=3);

--noise No2
insert into conference (faculty_id,address_id,start_date,end_date,title,fee)(select faculty_id,address_id,start_date,end_date,title,fee from conference where conference_id=1);
insert into conference (faculty_id,address_id,start_date,end_date,title,fee)(select faculty_id,address_id,start_date,end_date,title,fee from conference where conference_id=1);
insert into conference (faculty_id,address_id,start_date,end_date,title,fee)(select faculty_id,address_id,start_date,end_date,title,fee from conference where conference_id=2);

--noise No3

--insert into scientist_works_at_faculty(scientist_id)(select scientist_id from scientist_works_at_faculty where scientist_id=1);

insert into scientist_works_at_faculty(faculty_id,scientist_id)(select 2,scientist_id from scientist_works_at_faculty where scientist_id=1);
insert into scientist_works_at_faculty(faculty_id,scientist_id)(select 2,scientist_id from scientist_works_at_faculty where scientist_id=2);
insert into scientist_works_at_faculty(faculty_id,scientist_id)(select 2,scientist_id from scientist_works_at_faculty where scientist_id=3);
insert into scientist_works_at_faculty(faculty_id,scientist_id)(select 2,scientist_id from scientist_works_at_faculty where scientist_id=4);

--noise No4

update scientist set name='Βαγγ' where scientist_id in (select scientist_id from phd where phd_id=1);
update scientist set name='Παν' where scientist_id in (select scientist_id from phd where phd_id=2);
update scientist set name='Γ' where scientist_id in (select scientist_id from phd where phd_id=3);
update scientist set name='Δ' where scientist_id in (select scientist_id from phd where phd_id=4);
update scientist set name='Ε' where scientist_id in (select scientist_id from phd where phd_id=5);
update scientist set name='Ζ' where scientist_id in (select scientist_id from phd where phd_id=6);
update scientist set name='Η' where scientist_id in (select scientist_id from phd where phd_id=7);
update scientist set name='Θ' where scientist_id in (select scientist_id from phd where phd_id=8);
update scientist set name='Ι' where scientist_id in (select scientist_id from phd where phd_id=9);
update scientist set name='Κ' where scientist_id in (select scientist_id from phd where phd_id=10);
update scientist set name='Λ' where scientist_id in (select scientist_id from phd where phd_id=11);
update scientist set name='Μ' where scientist_id in (select scientist_id from phd where phd_id=12);
update scientist set name='Ν' where scientist_id in (select scientist_id from phd where phd_id=13);
update scientist set name='Ξ' where scientist_id in (select scientist_id from phd where phd_id=14);
update scientist set name='Ο' where scientist_id in (select scientist_id from phd where phd_id=15);
update scientist set name='Π' where scientist_id in (select scientist_id from phd where phd_id=16);
update scientist set name='Ρ' where scientist_id in (select scientist_id from phd where phd_id=17);
update scientist set name='Σ' where scientist_id in (select scientist_id from phd where phd_id=18);
update scientist set name='Τ' where scientist_id in (select scientist_id from phd where phd_id=19);
update scientist set name='Υ' where scientist_id in (select scientist_id from phd where phd_id=20);
update scientist set name='Φ' where scientist_id in (select scientist_id from phd where phd_id=21);
update scientist set name='Χ' where scientist_id in (select scientist_id from phd where phd_id=22);
update scientist set name='Ψ' where scientist_id in (select scientist_id from phd where phd_id=23);
update scientist set name='Ω' where scientist_id in (select scientist_id from phd where phd_id=24);
update scientist set name='ΑΑ' where scientist_id in (select scientist_id from phd where phd_id=25);
update scientist set name='ΒΒ' where scientist_id in (select scientist_id from phd where phd_id=26);
update scientist set name='ΓΓ' where scientist_id in (select scientist_id from phd where phd_id=27);
update scientist set name='ΔΔ' where scientist_id in (select scientist_id from phd where phd_id=28);
update scientist set name='ΕΕ' where scientist_id in (select scientist_id from phd where phd_id=29);
update scientist set name='ΖΖ' where scientist_id in (select scientist_id from phd where phd_id=30);
update scientist set name='ΗΗ' where scientist_id in (select scientist_id from phd where phd_id=31);
update scientist set name='ΘΘ' where scientist_id in (select scientist_id from phd where phd_id=32);
update scientist set name='ΙΙ' where scientist_id in (select scientist_id from phd where phd_id=33);
update scientist set name='ΚΚ' where scientist_id in (select scientist_id from phd where phd_id=34);
update scientist set name='ΛΛ' where scientist_id in (select scientist_id from phd where phd_id=35);
update scientist set name='ΜΜ' where scientist_id in (select scientist_id from phd where phd_id=36);
update scientist set name='ΝΝ' where scientist_id in (select scientist_id from phd where phd_id=37);
update scientist set name='ΞΞ' where scientist_id in (select scientist_id from phd where phd_id=38);
update scientist set name='ΟΟ' where scientist_id in (select scientist_id from phd where phd_id=39);
update scientist set name='ΠΠ' where scientist_id in (select scientist_id from phd where phd_id=40);


--noise No5

update phd set date_received='1-1-900' where scientist_id=7;
update phd set date_received='1-1-900' where scientist_id=6;
update phd set date_received='1-1-900' where scientist_id=3;
update phd set date_received='1-1-900' where scientist_id=1;
update phd set date_received='1-1-900' where scientist_id=8;
update phd set date_received='1-1-900' where scientist_id=9;
update phd set date_received='1-1-900' where scientist_id=11;
update phd set date_received='1-1-900' where scientist_id=12;
update phd set date_received='1-1-3000' where scientist_id=13;
update phd set date_received='1-1-3000' where scientist_id=14;
update phd set date_received='1-1-3000' where scientist_id=15;
update phd set date_received='1-1-3000' where scientist_id=16;
update phd set date_received='1-1-3000' where scientist_id=17;
update phd set date_received='1-1-3000' where scientist_id=21;

--noise No6

update funding set funder='' where scientist_id=1;
update funding set funder='' where scientist_id=2;
update funding set funder='' where scientist_id=3;
update funding set funder='' where scientist_id=4;
update funding set funder='' where scientist_id=5;
update funding set funder='' where scientist_id=6;
update funding set funder='' where scientist_id=7;
update funding set funder='' where scientist_id=8;

--noise No9

update publication set title='' where publication_id=1;
update publication set title='' where publication_id=2;
update publication set title='' where publication_id=3;
update publication set title='' where publication_id=4;
update publication set title='' where publication_id=5;
update publication set title='' where publication_id=6;
update publication set title='' where publication_id=7;
