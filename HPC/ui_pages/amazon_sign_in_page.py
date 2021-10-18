import uiautomator2 as u2
import status
from devices_info import DevicesInfo

class amazon_page:
    def amazon_sign(self,d: u2.Device):
        d.press("home")
        if d(text="MOVIES").exists(timeout=10):
           d(text="MOVIES").click_exists(10)
           d(resourceId="com.ff.iai.paxlauncher:id/titleTextView").click()
        if d(text="Email or mobile phone number").exists(timeout=5):
           d(resourceId="ap_email").set_text(DevicesInfo.Amazon_account)
           d(text="Continue").click()
        if d(text="Password").exists(timeout=5):
           d(resourceId="ap_password").set_text(DevicesInfo.Amazon_password)
           d(resourceId="signInSubmit").click()
        if d(text="Prime Video").exists(timeout=5):
            print("Amazon login successful")
            d.press("home")







if __name__ == '__main__':
    ap = amazon_page()
    d = u2.connect(DevicesInfo.HPC_SERIALNO)
    ap.amazon_sign(d)









