import mysql.connector

class DbHelper:

    def __init__(self):
        self.db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='employeeinfo'
            )
        self.ptr = self.db.cursor()
    def get_maximum_salary(self):
        '''
        Implement the logic to find and return maximum salary from employee table
        '''
        self.ptr.execute("Select max(salary) from employees;")
        return self.ptr.fetchone()[0]

    def get_minimum_salary(self):
        '''
        Implement the logic to find and return minimum salary from employee table
        '''
        self.ptr.execute("Select min(salary) from employees;")
        return self.ptr.fetchone()[0]

if __name__ == "__main__":
    db_helper = DbHelper()
    min_salary = db_helper.get_minimum_salary()
    max_salary = db_helper.get_maximum_salary()
    print(max_salary)
    print(min_salary)