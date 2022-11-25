from winotify import Notification, audio
import time


toast = Notification(app_id="Beba água",
                     title="Beba água",
                     msg="Bebe água mlk",
                     duration="long",
                     icon=r"C:\Users\Igor de Paula\Desktop\Workspace\07 - Python Projects\drink_water\clean-water.png")

toast.show()