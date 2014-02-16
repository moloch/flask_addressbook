drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  first_name text not null,
  last_name text not null,
  phone_number text not null
);
