# EVEREST TEST TASK

- создать каталог товара с характеристиками: цвет, вес, цена;
> URL: /admin/product/

- создать каталог адресов с фильтрами по: стране, городу, улице. Опционально: сделать адреса в виде связного списка;
> URL: /admin/address/

- создать список заказов с указанием адреса, товаров и их количества, статуса заказа;
> URL: /admin/order/

- организовать возможность добавления, удаления и изменения вышеуказанных объектов в БД MySQL/MariaDB
> URL: /admin/

- при помощи Celery отслеживать статус заказа и при его изменении записывать событие в лог в виде «Заказ %NUM% изменил статус на %STATE%». В качестве брокера для Celery использовать Redis
> Путь к логу: /evetest/server/order_status.log

- создать эндпоинт для получения информации по номеру заказа с использованием базовой авторизации и JSON-RPC.
> URL: /api/
> Данные для авторизации admin@admin.com:admin (хранится в .env)
> Тело запроса:
```
  {
    "jsonrpc": "2.0",
    "method": "order.get_order_info",
    "params": {
      "order_id": 3
    },
    "id": 1
  }
```
