```
        Предложения типа from __future__ import example позволяют получить доступ к возможностям, которые планируется 
    включить в будущую версию Python. Они должны находиться в самом начале Python-файла, никакие другие предложения им 
    предшествовать не могут.
    
        В данном случае проблему составляет строчка q: queue.Queue[t.List[DataPoint]] = queue.Queue(). 
    Стандартный библиотечный объект queue.Queue в версии Python 3.8 не является обобщенным типом, поэтому не может 
    принимать определение типа содержащихся в очереди объектов. Это упущение описано как дефект 33315, причем налицо 
    обоснованное нежелание добавлять новый тип typing.Queue или модифицировать библиотечный тип. Несмотря на это, mypy 
    трактует queue.Queue как обобщенный тип, тогда как интерпретатор Python с ним не согласен. Исправить это можно двумя 
    способами: либо использовать строковую аннотацию типа, так чтобы интерпретатор Python не пытался вычислить 
    queue.Queue[...] и выдавал ошибку, встретив предложение q: "queue.Queue[t.List[DataPoint]]" = queue.Queue(),
    либо воспользоваться опцией annotations из __future__, которая активирует логику разбора аннотаций типов, 
    запланированную для включения в Python 4. Эта логика подавляет синтаксический разбор аннотаций на этапе выполнения, 
    и именно такой подход принят в примере выше.
```