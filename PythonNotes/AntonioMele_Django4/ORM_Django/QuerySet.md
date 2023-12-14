```
    Встроенный в Django ORM-преобразователь основан на итерируемых наборах запросов QuerySet. 
    
    Итерируемый набор запросов QuerySet – это коллекция запросов к базе данных, предназначенных для извлечения объектов 
    из базы данных. К наборам запросов можно применять фильтры, чтобы сужать результаты запросов на основе заданных 
    параметров.
        
    Наборы запросов QuerySet в Django являются ленивыми, то есть они вычисляются только тогда, когда это приходится 
    делать. Подобное поведение придает наборам запросов QuerySet большую эффективность. Если не назначать набор 
    запросов QuerySet переменной, а вместо этого писать его непосредственно в оболочке Python, то инструкция SQL 
    набора запросов будет исполняться, потому что вы побуждаете ее генерировать результат    
```

```
    class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    class Meta:
        ordering = ["-publish"]
        indexes = [
            models.Index(fields=["-publish"]),
        ]

    def __str__(self):
        return self.title
```

#### Создание записи
```
     post = Post(title='Another post', slug='another-post', body='Post body.', author=user)
     post.save()
     
     или
     
     Post.objects.create(title='One more post', slug='one-more-post', body='Post body.', author=user)
```

#### Обновление записи
```
    post.title = 'New title'
    post.save()
```

#### Извлечение записи
```
    all_posts = Post.objects.all()
    
    Post.objects.get()
```


#### Применение метода filter()
```
    Post.objects.filter(publish__year=2022, author__username='admin')
    или то же самое
    Post.objects.filter(publish__year=2022).filter(author__username='admin')
    
    Запросы с операциями поиска в полях формируются с использованием двух знаков подчеркивания, 
    например publish__year, но те же обозначения также используются для обращения к полям ассоциированных моделей, 
    например author__username
```

### Применение метода exclude()
```
    Определенные результаты можно исключать из набора запросов QuerySet, используя метод exclude() менеджера. 
    
    Например, все посты, опубликованные в 2022 году, заголовки которых не начинаются со слова Why (Почему), можно 
    получить следующим образом:
        Post.objects.filter(publish__year=2022).exclude(title__startswith='Why')
```


### Применение метода order_by()
```
    Используя метод order_by() менеджера, можно упорядочивать результаты по разным полям. 
        Post.objects.order_by('title') Подразумевается возрастающий порядок.  
        Post.objects.order_by('-title') Подразумевается Убывающий порядок.
```

### Удаление объектов
```
    post = Post.objects.get(id=1)
    post.delete()
```

### Когда вычисляются наборы запросов QuerySet
```
    Создание набора запросов QuerySet не требует каких-либо действий с базой данных до тех пор, пока он не будет 
    вычислен. 
    
    Наборы запросов обычно возвращают еще один невычисленный набор запросов. 
    В наборе запросов можно конкатенировать столько фильтров, сколько потребуется, и база данных не будет затронута 
    до тех пор, пока набор запросов не будет вычислен. 
    При вычислении набора запросов он конвертируется в запрос на языке SQL к базе данных.
    
    Наборы запросов QuerySet вычисляются только в следующих ниже случаях:
    • при первом их прокручивании в цикле;
    • при их нарезке, например Post.objects.all()[:3];
    • при их консервации в поток байтов или кешировании;
    • при вызове на них функций repr() или len();
    • при вызове на них функции list() в явной форме;
    • при их проверке в операциях bool(), or, and или if.
```




















