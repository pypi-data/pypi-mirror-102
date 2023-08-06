class Student:
	def __init__(self,name):
		self.name = name
		self.exp = 0
		self.lesson = 0
		# self.AddEXP(10)

	def Hello(self):
		print('สวัสวดี ผมชื่อ {}'.format(self.name))

	def Coding(self):
		print('{} : กำลังเขียนโปรแกรม'.format(self.name))
		self.exp += 5
		self.lesson += 1

	def ShowEXP(self):
		print('-{} มี ปสก {} exp'.format(self.name,self.exp))
		print('-เรียนไป {} ครั้งแล้ว'.format(self.lesson))

	def AddEXP(self,score):
		self.exp += score
		self.lesson += 1

class SpecialStudent(Student):
	def __init__(self,name,farther):
		super().__init__(name)
		self.farther = farther
		mafia = ['Bill Gates','Thomas Edison']
		if farther in mafia:
			self.exp += 100

	def AddEXP(self,score):
		self.exp += (score*3)
		self.lesson += 1

	def AskExp(self,score=10):
		print('ครู!!! ขอคะแนนพิเศษ ผมหน่อยสิ {} Exp'.format(score))
		self.AddEXP(score)
		
if __name__ == '__main__':

	Student1 = Student('boy')
	Student1.Hello()

	student11 = SpecialStudent('Mark Zuckerberg','Bill Gates')
	student11.ShowEXP()
