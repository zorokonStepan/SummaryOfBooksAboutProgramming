### Создание модельных менеджеров
```
    По умолчанию в каждой модели используется менеджер objects.     
    Этот менеджер извлекает все объекты из базы данных. 
    
    Однако имеется возможность определять конкретно-прикладные модельные менеджеры.
    
    Есть два способа добавлять или адаптировать модельные менеджеры под конкретно-прикладную задачу: 
        можно добавлять дополнительные методы менеджера в существующий менеджер 
        либо создавать новый менеджер, видоизменив изначальный набор запросов QuerySet, возвращаемый менеджером. 
        
    Первый метод предоставляет обозначение набора запросов в виде 
        Post.objects.my_manager(), 
    а второй предоставляет обозначение набора запросов в виде 
        Post.my_manager.all().
```

```
    Метод get_queryset() менеджера возвращает набор запросов QuerySet, который будет исполнен
```

### второй метод
```
    class PublishedManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status=Post.Status.PUBLISHED)
```