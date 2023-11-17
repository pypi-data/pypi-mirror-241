# Fluxo

## Exemplo simples:

```
fluxo = Fluxo(
    name='Fluxo 1',
    interval={'minutes': 1, 'at': ':10'})


@Task('Tarefa 1', fluxo=fluxo)
async def my_func():
    print("Minha função sendo executada")
    n = 0
    for i in range(100000000):
        n += 1
```
