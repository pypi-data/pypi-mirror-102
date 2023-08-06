pip install git+http://git2.uriit.local/CIAS/dirba.git@master#egg=dirba  
pip install git+http://192.168.212.128/CIAS/dirba.git@master#egg=dirba  
Мини библиотечка для уменьшения рутины связанной с моделями.

Возможности:
 - [x] базовые классы для моделей
 - [x] запуск моделей в kafka
 - [x] запуск моделей в rest api
 - [x] валидация
 
Пример использования валидации 
```python
from dirba.models.dambo import DamboModel
from dirba.runners import APIRunner
from dirba.validation import ProhibitedTexValidationDataset
from dirba.validation import PrecisionMetric
from dirba.validation import Validator

if __name__ == '__main__':
    dataset = ProhibitedTexValidationDataset()
    model = DamboModel()

    validator = Validator(dataset,model, [PrecisionMetric])
    validator.describe()

```