from imagesearch import *

class AutoTempest:
	def __init__(self):
		pyautogui.FAILSAFE = False
		self.ongoing = False

	def start(self): 
		pos = imagesearch("stage.png")
		if pos[0] != -1:
			print("STAGE FOUND")
			pyautogui.click(pos[0], pos[1])
			time.sleep(1)
			self.fight_large()
			self.check_restore()
			self.ongoing = True

	def check_restore(self): 
		pos = imagesearch("restore.png")
		if pos[0] != -1:
			print("RESTORE FOUND")
			pyautogui.click(pos[0], pos[1])
			time.sleep(1)
			self.close()

	def auto(self):
		pos = imagesearch("auto.png")
		if pos[0] != -1:
			print("AUTO FOUND")
			pyautogui.click(pos[0], pos[1])
			time.sleep(1)
			pos = imagesearch("autoconfirm.png")
			if pos[0] != -1:
				pyautogui.click(pos[0], pos[1])
				time.sleep(1)

	def fight_large(self):
		pos = imagesearch("fightlarge.png")
		if pos[0] != -1:
			print("FIGHT LARGE FOUND")
			pyautogui.click(pos[0], pos[1])
			time.sleep(1)

	def fight_small(self):
		pos = imagesearch("fightsmall.png")
		if pos[0] != -1:
			print("FIGHT SMALL FOUND")
			pyautogui.click(pos[0], pos[1])
			time.sleep(1)
			self.fight_large()

	def ok(self): 
		pos = imagesearch("ok.png")
		if pos[0] != -1:
			print("OK FOUND")
			pyautogui.click(pos[0], pos[1])
			self.ongoing = False

	def close(self): 
		pos = imagesearch("close.png")
		if pos[0] != -1:
			print("CLOSE FOUND")
			pyautogui.click(pos[0], pos[1])
			time.sleep(1)

	def main(self):
		try:
			while True:
				if self.ongoing == False:
					self.start()
				else:
					self.auto()
					self.fight_small()
					self.ok()
					self.close()
		except KeyboardInterrupt:
			pass

if __name__ == "__main__":
	tempest = AutoTempest()
	tempest.main()