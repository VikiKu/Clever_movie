# Clever_movie
В данном проекте будет осуществляться подбор фильмов по настроению.
## Идея:
Каждый человек сталкивается с проблемой выбора фильма для просмотра. Часто мы спрашиваем совет у друзей, но не всегда их выбор совпадает с нашим настроением. Мой проект является по сути рекомендательной системой: пользователь пишет боту чего он ожидает от фильма, какие эмоции хочет получить от просмотра и т.п., программа на основе списка отзывов на различные фильмы подбирает фильм.
## План:
1. Парсинг данных. (10 часов)
3. Модель, которая по запросу пользователя подбирает самые подходящие фильмы. (10 часов)
### Телеграм-бот
Для удобства взаимодействия пользователя с программой создан телеграм-бот. Именно через сообщения с ним осуществляется выбор фильма.
https://t.me/Movie_Master_super_bot
### Подготовка данных
Для того, чтобы обучить модель, надо иметь данные.
![image](https://github.com/VikiKu/Clever_movie/assets/148389982/15b16aa9-ee56-4de2-951e-5ded6832e9cb)

Необходимо найти сайт с отзывами на фильмы, для последующей работы с этими данными. 
Как это должно вообще выглядеть? В итоге должен получиться датасет с колонками:
1. название фильма
2. возрастное ограничение
3. год выпуска
4. список актеров
5. режиссер
6. отзывы на фильм в каком-то удобном формате...возможно просто запихнуть все отзывы в одну ячейку
7. оценка фильма
