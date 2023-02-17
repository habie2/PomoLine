import json
import datetime
import csv

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
        
    def to_json(self):
        dict_report = {
            'start_date': self.start_date,
            'project_name': self.project_name,
            'duration': self.duration
        }
        return json.dumps(dict_report, indent=4)
    
    def create_new_json(self):
        file_name = self.start_date[:10]+'_'+self.start_date[11:13]+'.' \
        + self.start_date[14:16]
        with open(f'pomo_reports/{file_name}.json', 'w') as json_file:
            json_file.write(self.to_json())
        return file_name

    def to_csv(self):
        dict_report = [self.start_date, self.project_name, self.duration]
        return dict_report

    def append_row_csv(self):
        # TODO add the titles of the columns
        field_names = ['start_date', 'project_name', 'duration']
        
        with open(f'pomo_reports/global_report.csv', 'a',
        newline='') as csv_file:
            dict_object = csv.writer(csv_file)
  
            dict_object.writerow(self.to_csv())
        

report = Report('FSDB')
#report.create_new_json()
report.append_row_csv()
