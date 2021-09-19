import time
import win10toast

pop = win10toast.ToastNotifier()
pop.show_toast("Notificação", "Alerta de Teste!")

while pop.notification_active():
    time.sleep(5)
