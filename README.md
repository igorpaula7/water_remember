# Feito em Python pra me lembrar de beber água.

## Código Fonte:
```python
from winotify import Notification, audio

toast = Notification(app_id="Beba água",
                     title="Beba água",
                     msg="Bebe água mlk",
                     duration="long",
                     icon=r"C:\Users\Igor de Paula\Desktop\Workspace\07 - Python Projects\drink_water\clean-water.png")

toast.show()
```
## Resultado:
![image](https://user-images.githubusercontent.com/105919552/204039269-ab6ee0f2-6570-44d9-879b-080f414b4803.png)

## Automação:
Configurei o Agendador de tarefas do windows pra executar de 30 em 30 minutos.
