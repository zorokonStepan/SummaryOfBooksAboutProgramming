```
        Представление является фактически сохраненным запросом к базе данных. Этот запрос получает имя, которым можно 
    воспользоваться в предложении FROM команды SELECT для получения результатов этого запроса.
    
        В отличие от таблиц, представления не содержат данных. При каждом обращении к представлению в команде SELECT 
    данные выбираются из таблиц, на основе которых это представление создано.
    
        Представления позволяют облегчить развитие и модификацию базы данных, потому что они могут позволить сохранить 
    интерфейс неизменным, но сам запрос, который лежит в основе конкретного представления, может измениться. При этом 
    для прикладного программиста представление останется неизменным, поэтому не потребуется переделывать запросы к 
    этому представлению в прикладной программе.
```

### CREATE VIEW
```
    CREATE VIEW имя-представления [ ( имя-столбца [, ...] ) ]
        AS запрос;

    CREATE VIEW seats_by_fare_cond AS
        SELECT aircraft_code,
               fare_conditions,
               count( * ) AS count
        FROM seats
        GROUP BY aircraft_code, fare_conditions
        ORDER BY aircraft_code, fare_conditions;
        
    SELECT * FROM seats_by_fare_cond;
```

### CREATE OR REPLACE VIEW
```
        Если представление уже существует, то можно его не удалять, а просто заменить новой версией.
     При создании новой версии представления (без явного удаления старой с помощью команды DROP VIEW) должны оставаться 
     неизменными имена столбцов представления. Если же вы хотите изменить имя хотя бы одного столбца, то сначала нужно 
     удалить представление с помощью команды DROP VIEW, а уже затем создать его заново.


    DROP VIEW IF EXISTS seats_by_fare_cond;
    
    CREATE OR REPLACE VIEW seats_by_fare_cond AS
        SELECT aircraft_code,
               fare_conditions,
               count( * ) AS num_seats
        FROM seats
        GROUP BY aircraft_code, fare_conditions
        ORDER BY aircraft_code, fare_conditions;
    
    *******    
      или
    *******
    
    DROP VIEW IF EXISTS seats_by_fare_cond;
    
    CREATE OR REPLACE VIEW seats_by_fare_cond ( code, fare_cond, num_seats ) AS
        SELECT aircraft_code,
               fare_conditions,
               count( * )
        FROM seats
        GROUP BY aircraft_code, fare_conditions
        ORDER BY aircraft_code, fare_conditions;
```

### CREATE MATERIALIZED VIEW
```
    CREATE MATERIALIZED VIEW [ IF NOT EXISTS ] имя-мат-представления
        [ ( имя-столбца [, ...] ) ]
        AS запрос
        [ WITH [ NO ] DATA ];
        
        В момент выполнения команды создания материализованного представления оно заполняется данными, но только если в 
    команде не было фразы WITH NO DATA.
        Если же она была включена в команду, тогда в момент своего создания представление остается пустым, а для 
    заполнения его данными нужно использовать команду REFRESH MATERIALIZED VIEW.
    
        Материализованное представление очень похоже на обычную таблицу. Однако оно отличается от таблицы тем, что не 
    только сохраняет данные, но также запоминает запрос, с помощью которого эти данные были собраны.
    
    REFRESH MATERIALIZED VIEW routes;

    DROP MATERIALIZED VIEW routes;
```