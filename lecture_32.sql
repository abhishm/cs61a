----------
-- Dogs --
----------

-- Parents
create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

-- Fur
create table dogs as
  select "abraham" as name, "long" as fur union
  select "barack"         , "short"       union
  select "clinton"        , "long"        union
  select "delano"         , "long"        union
  select "eisenhower"     , "short"       union
  select "fillmore"       , "curly"       union
  select "grover"         , "short"       union
  select "herbert"        , "curly";

-- Parents of curly dogs

select parent from parents, dogs where child = name and fur = "curly";

-- siblings

select a.child as first, b.child as second 
  from parents as a, parents as b 
  where a.parent = b.parent and a.child < b.child;

-- Grandparents

create table grandparents as
  select a.parent as grandog, b.child as granpup
    from parents as a, parents as b where 
    a.child = b.parent;

-- Grandogs with the same fur as their granpup

create table t1 as
  select grandog, granpup, fur from grandparents, dogs
  where grandog = name;

create table t2 as
  select grandog, granpup, fur from grandparents, dogs
  where granpup = name;

select t1.grandog, t1.granpup from t1, t2 
  where t1.fur = t2.fur and 
    t1.grandog = t2.grandog 
    and t1.granpup = t2.granpup;

select grandog, granpup, a.fur as grandog_fur, b.fur as granpup_fur from grandparents, dogs as a, dogs as b
  where a.name = grandog and b.name = granpup;

select grandog, granpup from grandparents, dogs as a, dogs as b
  where a.name = grandog and b.name = granpup and a.fur = b.fur;

