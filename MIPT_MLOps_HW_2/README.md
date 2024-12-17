# MLOps Homework 2

## Описание
Проект демонстрирует использование PyTorch Lightning, Hydra, и DVC для реализации MLOps-подходов.

## Запуск
1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

2. Предварительная обработка данных:
   ```bash
   python src/preprocess.py
   ```

3. Запустите обучение:
   ```bash
   python src/train.py
   ```

4. Используйте Docker для контейнеризации:
   ```bash
   docker build -t hadamard .
   docker run hadamard
   ```

## Тесты
Запустите тесты:
```bash
pytest tests/
```

## DVC
Настройте удалённое хранилище:
```bash
dvc remote add -d storage s3://...
```

Синхронизация:
```bash
dvc push
```
