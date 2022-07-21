class Solution:
    def reformatDate(self, date: str) -> str:
        months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
                  "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
                  "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        
        year = date[-4:]
        month = months[date[-8:-5]]
        day = date[:2] if date[1].isdigit() else "0" + date[0]
        
        return f"{year}-{month}-{day}"