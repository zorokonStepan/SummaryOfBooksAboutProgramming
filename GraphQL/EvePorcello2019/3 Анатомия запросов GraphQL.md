```
    Запросы — это простые строки, которые отправляются в теле запросов POST в конечную точку GraphQL.
    
    Запрос описывает данные, которые вы хотите получить от сервера GraphQL.
    Когда вы отправляете запрос, вы запрашиваете единицы данных по полям.
```

### GraphQL-запрос
```
    query {
        allLifts {
            name
            status
        }
    }
    
    query - операция для запроса данных из API.
    allLifts - запрос
    name, status - поля запроса
    
    query — это тип GraphQL. Мы называем его корневым типом, потому что это тип, который сопоставляется с операцией, 
            а операции представляют собой корни нашего документа запроса
            
    Поля, доступные для запроса в API GraphQL, определены в данной схеме API.
    В документации указывается, какие поля доступны для выбора в типе query.
    
    Когда мы пишем запросы, мы выбираем поля, которые нам нужны, заключая их в фигурные скобки. 
    Эти блоки называются выборками.
```

### Псевдонимы
```
    query liftsAndTrails {
        open: liftCount(status: OPEN)
        chairlifts: allLifts {
            liftName: name
            status
        }
        skiSlopes: allTrails {
            name
            difficulty
        }
    }
    
    Ниже приводится ответ:
    
    {
        "data": {
            "open": 5,
            "chairlifts": [
                {
                    "liftName": "Astra Express",
                    "status": "open"
                }
            ],
            "skiSlopes": [
                {
                    "name": "Ditch of Doom",
                    "difficulty": "intermediate"
                }
             ]
        }
    }
```