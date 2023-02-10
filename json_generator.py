import json
import datetime

class Report():
    def __init__(self, project_name:str(), duration:int = 50, 
    start_date = datetime.datetime.now()):
        '''
        Parameters:
            project_name (str): Name of the project
            duration (int): Duration of the pomodoro in minutes
            start_date (datetime): Date of the pomodoro
            '''
        self.project_name = project_name
        self.start_date = str(start_date)
        self.duration = duration
        
    def to_json(self) -> json:
        dict_report = {
            'start_date': self.start_date,
            'project_name': self.project_name,
            'duration': self.duration
        }
        return json.dumps(dict_report, indent=4)
    
    def create_new_json(self):
        print(self.start_date)
        file_name = self.start_date[:10]+'_'+self.start_date[11:13]+'.' \
        + self.start_date[14:16]
        with open(f'json_reports/{file_name}.json', 'w') as file:
            file.write(self.to_json())
        return file_name
        

report = Report('FSDB')
print(report.create_new_json())

