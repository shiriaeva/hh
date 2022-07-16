# headhunter_app
Данные были получены с сайта hh.ru, с помощью функции https://github.com/shiriaeva/hh/blob/38a447654a53097cf8a5f15c9fb4ce50361d5fac/headhunter_app/hh_parser.py#L158
которая вызывалась 3 раза https://github.com/shiriaeva/hh/blob/38a447654a53097cf8a5f15c9fb4ce50361d5fac/headhunter_app/main.py#L81
https://github.com/shiriaeva/hh/blob/38a447654a53097cf8a5f15c9fb4ce50361d5fac/headhunter_app/main.py#L82
https://github.com/shiriaeva/hh/blob/38a447654a53097cf8a5f15c9fb4ce50361d5fac/headhunter_app/main.py#L83
соответственно в бд в таблице vacancy хранятся вакансии по запросам [.net framework](https://hh.ru/search/vacancy?text=.net+framework), [java](https://hh.ru/search/vacancy?text=java) и [php](https://hh.ru/search/vacancy?text=php)  

таблица statistics хранит общую информацию по каждому запросу, полученную на основе спарсенных данных (количество вакансий по данному запросу (у которых была указана з.п.), средняя и медианная зарплата (в руб.), города с наибольшим кол-вом вакансий, наиболее востребованные навыки по кол-ву упоминаний в вакансиях)  


* запрос на создание вакансии  
![image](https://user-images.githubusercontent.com/84004210/179366046-b4b9b4ad-764e-453b-9964-c035ecf6a1cc.png)   

* запрос на обновление данных о вакансии по айди  
![image](https://user-images.githubusercontent.com/84004210/179365723-920bda47-b60c-4bf4-91d3-af0788ad2a20.png)    

* запрос на удаление вакансии из бд по айди  
![image](https://user-images.githubusercontent.com/84004210/179365633-fd4d1712-1e76-43c2-9558-f5bc296e010e.png)    

![image](https://user-images.githubusercontent.com/84004210/179364999-30bb8704-dbe0-4fe4-9853-bdf01137cf15.png)    

* запрос на получение всех вакансий из бд
![image](https://user-images.githubusercontent.com/84004210/179365080-2f704b25-2308-499a-a020-a590f1ba275b.png)     

* запрос на получение определенной вакансии по айди из бд
![image](https://user-images.githubusercontent.com/84004210/179365342-24c66758-de4e-4ec9-b2d2-d8d5e58fd399.png)     

* запрос на получение статистики по вакансиям из бд
![image](https://user-images.githubusercontent.com/84004210/179365418-6020ffe7-26e3-4659-ad56-550d14c01abf.png)     

* запрос на получение статистики по определенной вакансии по поисковому запросу из бд
![image](https://user-images.githubusercontent.com/84004210/179365463-0c024bbd-093c-4b93-9108-d22e45b10f48.png)     

