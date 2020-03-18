from datetime import date
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        day_name = datetime.date(year,month,day)

        return day_name.strftime("%A")
        
