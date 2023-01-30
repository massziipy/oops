class Auth:
    def __init__(self):
        self.__username=None
        self.__password=None
        self.usertype=None
        self.loginstatus=0

    def signup(self):
        if self.loginstatus==0:
            self.__username=input('Enter Your Username for register')
            self.__password=input('Enter Your Password for register')
            self.usertype=input('Enter User Type for register')
            self.loginstatus=2

        else:
            print('User already exists')
    def login(self):
        if self.loginstatus==2:
            username=input('Enter Username for logging in')
            password=input('Enter Password for logging in')
            if self.__username==username and self.__password==password:
                self.loginstatus=1
                print('you have successfully logged in')
            else:
                print('Incorrect Usename Or Password')
        elif self.loginstatus==1:
            print('User already logged in')
        else:
            print('User Does not exist')



class School:
    def __init__(self):
        self.school_name = None
        self.school_place = None
        self.school_code = None

    def setschooldetails(self):
        print('School sign Up')
        self.school_name=input('Enter School Name')
        self.school_code=input('Enter School Code')
        self.school_place=input('Enter School Place')
    # This method displays details of the School
    def get_school_details(self):
        print(
            "School Details:"
            "\n NAME:", self.school_name,
            "\n PLACE:", self.school_place,
            "\n CODE:", self.school_code

        )
    def setstaffsalary(self,teacher):
        teacher.salary=input('Enter The Salary')


class Principal(School):
    def __init__(self):
        self.Principal_name = None
        self.PrincipalQualification = None
        self.Principal_Experience=None
        self.principal_Email=None
        self.authorize = Auth()
    def setprincipal(self):
        if self.authorize.loginstatus==0:
            print('Principal Register')
            self.authorize.signup()
            self.Principal_name=input('Enter Principal Name')
            self.PrincipalQualification=input('Enter Principal Qulaification')
            self.Principal_Experience=input('Enter Experience')
            self.principal_Email=input('Enter Email')
        else:
            print('User Already exists')


    def getprincipladetails(self):
        if self.authorize.loginstatus==1:
            print('Principal Name :',self.Principal_name,
                  '\n Principal Qualification :',self.PrincipalQualification,
                  '\n Principal Email :',self.principal_Email,
                  '\n Principal Experience',self.Principal_Experience)
        else:
            print('Un Authorized Access')


    # Method to modify teacher
    def modify_teacher(self,teacher):
        if self.authorize.loginstatus == 1:
            print('Teacher Modification')
            print('1-Update Subject \n'
              '2-Update Teacher Name \n'
              '3-Update Teacher Place \n'
              '4- Update Teacher Phone \n')
            option=input('Select an option:')
            if option=='1':
                teacher.subject = input('Enter New Subject')
            elif option=='2':
                teacher.staff_name=input('Enter The New Name')
            elif option=='3':
                teacher.place=input('Enter New Place Name')
            elif option=='4':
                teacher.phone==input('Enter New Phone Number')
            else:
                print('invaid Option')
        else:
            print('unauthorized Access')


    # Method to see details of teachers
    def see_teacher_details(self,teacher):
        if self.authorize.loginstatus == 1:
            print(
                "Teacher Details:",
                "\n NAME:", teacher.staff_name,
                "\n GENDER:", teacher.gender,
                "\n AGE:", teacher.age,
                "\n PLACE:", teacher.place,
                "\n PH_NO:", teacher.phone,
                "\nSubject:", teacher.Subject)
        else:
            print('unauthorized Access')

    # Method to see details of student
    def see_student_details(self,student):
        if self.authorize.loginstatus == 1:
            print(
                "Student Details:",
                "\n NAME:", student.s_name,
                "\n PLACE:", student.s_place,
                "\n GENDER:", student.s_gender,
                "\n AGE:", student.s_age,
                "\n STANDARD:", student.s_std,
                "\n DIVISION:", student.s_div,
                "\n BUS NO:", student.s_bus_no
            )
        else:
            print('Unauthorized Access')

    # Method to add new class
    def login(self):
        print('Principal Login')
        self.authorize.login()

    def logout(self):
        self.authorize.loginstatus=2
        print('You have logged Out Suceesfully')

    # Method to modify class
    def modify_class(self,classs):
        if self.authorize.loginstatus == 1:
            print('Class Modification')
            print('1-Update Class Name \n'
                  '2-Update Class Division \n'
                  '3-Update Class Strength \n')
            option = input('Select an option:')
            if option == '1':
                classs.std = input('Enter New Name')
            elif option == '2':
                classs.div = input('Enter The New Division')
            elif option == '3':
                classs.strength = input('Enter new Strength Value')
            else:
                print('invaid Option')
        else:
            print('unauthorized Access')

    # Method to see details of student
    def see_class_details(self,classs):
        if self.authorize.loginstatus == 1:
            print(
                "Class Details:"
            "\n STANDARD:", classs.std,
            "\n DIVISION:", classs.div,
            "\n CLASS STRENGTH:", classs.strength,
            "\n CLASS TEACHER ID:", classs.class_teacher_id
            )
        else:
            print('Unauthorized Access')

class Marks:
    def __init__(self):
        self.sub1 = None
        self.sub2 = None
        self.sub3 = None
        self.sub4 = None

    # This method returns name of the subject
    def getmarks(self):
        print('Mark in Sub 1:',self.sub1,
              '\n Mark in Sub2:',self.sub2,
              '\n Mark in Sub 3',self.sub3,
              '\n Mark in Sub 4',self.sub4)
    def setmarks(self):
        self.sub1=input('Enter Mark')
        self.sub2=input('Enter Mark')
        self.sub3=input('Enter Mark')
        self.sub4=input('Enter Mark')

    # This method calculate and print total marks
    def total_marks(self):
           return self.sub1+ self.sub2+ self.sub3+self.sub4
class Student(School):
    def __init__(self):
        self.s_name = None
        self.s_place = None
        self.s_gender = None
        self.s_age = None
        self.s_std = None
        self.s_div = None
        self.s_bus_no = None
        self.marks=Marks()
        self.authorize=Auth()

    def setstudent(self):
        self.authorize.signup()
        self.s_name=input('Enter Student Name')
        self.s_place=input('Enter Student Place')
        self.s_gender=input('Enter Student Gender')
        self.s_age=input('Enter Student Age')
        self.s_std=input('Enter Your Std')


    # This method is to Log in
    def log_in(self):
        print('Student Login')
        self.authorize.login()


    # This method is to log out
    def log_out(self):
        self.authorize.loginstatus=2
        print('You have successfully Logged Out')

    # This method displays details of the Student
    def get_student_details(self):
        if self.authorize.loginstatus == 1:
            print(
                "Student Details:",
                "\n NAME:", self.s_name,
                "\n PLACE:", self.s_place,
                "\n GENDER:", self.s_gender,
                "\n AGE:", self.s_age,
                "\n STANDARD:", self.s_std,
                "\n DIVISION:", self.s_div,
                "\n BUS NO:", self.s_bus_no
            )
        else:
            print('Unauthorized Access')

    # This method displays reportcard of the Student
    def view_reportcard(self):
        if self.authorize.loginstatus == 1:
            print('Report Card \n',
              'Mark in Sub 1:', self.marks.sub1,
              '\n Mark in Sub2:', self.marks.sub2,
              '\n Mark in Sub 3', self.marks.sub3,
              '\n Mark in Sub 4', self.marks.sub4,
              '\n Totel Marks =',self.marks.total_marks())
        else:
            print('Unauthorized Access')

    # This method is to pay fee
    def pay_fees(self):
        if self.authorize.loginstatus == 1:
            fees=input('enter Amount To Pay')
            print('You have Successfully Paid Amount :',fees)
        else:
            print('Unauthorized Access')



class Staff(School):
    def __init__(self):
        self.staff_id = None
        self.staff_name = None
        self.salary = None
        self.age=None
        self.dept = None
        self.gender=None
        self.place=None
        self.phone=None

    # This method display details of staff
    def staff_details(self):
        print(
            "Staff Details:",
            "\n NAME:", self.staff_name,
            "\n ID:", self.staff_id,
            "\n DEPT:", self.dept,
            "\n SALARY:", self.salary)

    # This method checks whether staff is checked in or not
    def check_in(self):
        print('You have Successfully Checked in')

    # This method checks whether staff received salary or not
    def receive_salary(self):
        print('Successfully Recieved Salary Amount:',self.salary,'/-')


class Teachers(Staff, School):
    def __init__(self):
        self.staff_id = None
        self.staff_name = None
        self.salary = None
        self.dept = 'Teaching'
        self.age=None
        self.gender = None
        self.Subject=None
        self.place = None
        self.phone=None
        self.class_teacher = None
        self.authorize=Auth()
        self.classs=ClassRoom()

    def setteacherdetails(self):
        print('Teacher Register')
        self.authorize.signup()
        self.staff_id=input('Enter Staff Id')
        self.staff_name=input('Enter Staff Name')
        self.age=input('Enter Your Age')
        self.Subject=input('Enter Your Subject')
        self.place=input('Enter Your Place')
        self.gender=input('Enter Your gender')
        self.phone=input('Enter Your Phone Number')

    # This method display details of teacher
    def teacher_details(self):
        if self.authorize.loginstatus == 1:
            print(
            "Teacher Details:",
            "\n NAME:", self.staff_name,
            "\n GENDER:", self.gender,
            "\n AGE:", self.age,
            "\n PLACE:", self.place,
            "\n PH_NO:", self.phone,
            "\nSubject:", self.Subject)
        else:
            print('Unauthorized Access')

    # This method is to Log in
    def log_in(self):
        self.authorize.login()

    # This method is to log out
    def log_out(self):
        self.authorize.loginstatus=2
        print('You have Successfully Logged Out')

    # Method to see details of student
    def see_student_details(self, student):
        if self.authorize.loginstatus == 1:
            print(
                "Student Details:",
                "\n NAME:", student.s_name,
                "\n PLACE:", student.s_place,
                "\n GENDER:", student.s_gender,
                "\n AGE:", student.s_age,
                "\n STANDARD:", student.s_std,
                "\n DIVISION:", student.s_div,
                "\n BUS NO:", student.s_bus_no
            )
        else:
            print('Unauthorized Access')

    # Method to enter mark of students
    def addmarks(self,student):
        print('Add Student Marks')
        student.marks.setmarks()
        print('Marks Added Successfully')

    # This method returns the mark details
    def setclassstudents(self,student):
        print('Set Student to class')
        student.s_div=self.classs.setdivision()
    def setbusno(self,student,bus):
        print('Set student bus')
        student.s_bus_no=bus.bus_no

    # This method prepare reportcard
    def prepare_reportcard(self,student):
        print('Report card of' ,student.s_name, 'Created Successfully')


class NonTeachers(Staff, School):
    def __init__(self, n_name, n_gender, n_age,
                 n_place, n_ph_no, n_dept):
        self.n_name = n_name
        self.n_gender = n_gender
        self.n_age = n_age
        self.n_place = n_place
        self.__n_ph_no = n_ph_no
        self.n_dept = n_dept

    # This method display details of non teaching staff
    def get_details(self):
        print(
            "Details:",
            "\n NAME:", self.n_name,
            "\n GENDER:", self.n_gender,
            "\n AGE:", self.n_age,
            "\n PLACE:", self.n_place,
            "\n PH_NO:", self.__n_ph_no,
            "\n DEPT:", self.n_dept
        )


class ClassRoom(School):
    def __init__(self):
        self.name=None
        self.std = None
        self.div = None
        self.strength = None
        self.class_teacher_id = None

    def setclassroom(self):
        self.name=input('Enter Class Name')

    def setclassstd(self):
        self.std=input('Enter Standard')

    def setdivision(self):
        self.div=input('Enter The division')

    def setclassteacher(self,teacher):
        self.class_teacher_id=teacher.staff_id
        teacher.class_teacher=self.name

    def setclassroomstrength(self):
        self.strength=input('Enter The Class Strength')


    # This method display details of classroom
    def get_class_details(self):
        print(
            "Class Details:"
            "\n STANDARD:", self.std,
            "\n DIVISION:", self.div,
            "\n CLASS STRENGTH:", self.strength,
            "\n CLASS TEACHER ID:", self.class_teacher_id
        )


class ClassEquipment(ClassRoom):
    def __init__(self, bench_count, desk_count, board_count,
                 shelf_count, duster_count, light_count):
        self.bench_count = bench_count
        self.desk_count = desk_count
        self.board_count = board_count
        self.shelf_count = shelf_count
        self.duster_count = duster_count
        self.light_count = light_count

    # This method calculate and return total count of equipment
    def get_total_count(self):
        total_count = self.bench_count \
                      + self.desk_count \
                      + self.board_count \
                      + self.shelf_count \
                      + self.duster_count \
                      + self.light_count
        return total_count

    # this method displays the equipments need to purchase
    def purchase_equipment(self):
        pass


class Lab(School):
    def __init__(self):
        self.lab_name = None
        self.incharge_id = None
        self.labstatus= 0

    def setlab(self):
        self.lab_name='Enter The Lab Name'
        self.incharge_id='Enter who is incharge'

    def labcheckin(self):
        self.labstatus=1
        print('successfully checked in')
    def labcheckout(self):
        self.labstatus=0
        print('Successfully Checked Out')

    # This method display details of lab
    def lab_details(self):
        print(
            "Lab Details:",
            "\n LAB NAME:", self.lab_name,
            "\n INCHARGE ID:", self.incharge_id
        )

    # This method check whether lab is occupied or not
    def is_occupied(self):
        if self.labstatus==1:
            print('Lab is occupied')
        else:
            print('Lab is available')


class LabEquipment:
    def __init__(self, equipment_name, equipment_count):
        self.equipment_name = equipment_name
        self.equipment_count = equipment_count

    # This method display details of equipments
    def equipment_details(self):
        print(
            "Equipment Details:",
            "\n NAME:", self.equipment_name,
            "\n COUNT:", self.equipment_count
        )

    # this method displays the equipments need to purchase
    def purchase_equipment(self):
        print('Equipmnet Purchased')


class SchoolBus(School):
    def __init__(self):
        self.bus_no = None
        self.driver_id = None
        self.capacity = None


    def busdetails(self):
        self.bus_no=input('Enter Bus No')
        self.driver_id=input('Driver ID')
        self.capacity=input('Enter Capacity')

    # This method display details of
    def get_bus_details(self):
        print(
            "Bus Details:",
            "\n BUS NO:", self.bus_no,
            "\n DRIVER ID:", self.driver_id,
            "\n CAPACITY:", self.capacity
        )

    def show_seats(self):
        print('Showing Seats')


class PlayGround(School):
    def __init__(self):
        self.length = 0
        self.width = 0
        self.status=0
    def setplayground(self):
        self.length=input('Enter Length of the Ground')
        self.width=input('Enter Width of the ground')

    def startplaying(self):
        self.status=1

    def stopplaying(self):
        self.status=0


    # This method calculate and return area of the ground
    def get_area(self):
        area = self.length * self.width
        return area

    # This method check whether lab is occupied or not
    def is_occupied(self):
        if self.status==1:
            print('Ground is Occuppied')
        else:
            print('Not Occuppied')


class Auditorium:
    def __init__(self, total_seat, event_name,
                 event_date, event_time):
        self.total_seat = total_seat
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time

    def book_auditorium(self):
        name='enter Your Name'
        date='date of event'
        print('Mr',name,',','Well Contact you back after Checking The availablity')

    def get_event_details(self):
        print(
            "Event Details:",
            "\n Event Name:", self.event_name,
            "\n Event Date:", self.event_date,
            "\n Event Time:", self.event_time
        )

    def display_seats(self):
        print('Displaying Seats')


school1=School()
school1.setschooldetails()
princi=Principal()
teacher=Teachers()
student=Student()
classs=ClassRoom()
bus=SchoolBus()
lab=Lab()
# labeq=LabEquipment()
play=PlayGround()
princi.setprincipal()
classs.setclassroom()
teacher.setteacherdetails()
student.setstudent()
lab.setlab()
play.setplayground()
classs.setclassteacher(teacher)

princi.getprincipladetails()
princi.see_teacher_details(teacher)
princi.see_student_details(student)
princi.see_class_details(classs)
princi.modify_teacher(teacher)
princi.modify_class(classs)
classs.setclassteacher(teacher)
teacher.log_in()
teacher.see_student_details(student)
teacher.setclassstudents(student)
teacher.addmarks(student)
teacher.setbusno(student,bus)
teacher.prepare_reportcard(student)
teacher.teacher_details()
teacher.see_student_details(student)
teacher.log_out()



# school = School("GIHSS", "Garhoud", "GI-77")
# school.get_school_details()
# student = Student("username", "password", "Arun", "Kochi", "Male", 15, "10th", "A", 3)
# student.get_student_details()
# mark1 = Marks("Science", 28, 25, 22)
# mark1.get_subject()
# print(mark1.get_subject())
# mark1.total_marks()
# staff = Staff("Ani", "TS-77", "Teaching", 20000)
# staff.staff_details()
# teacher = Teachers("username", "password", "Manju", 35, "Female", "Wayanad", 9876895678, "10th B")
# teacher.teacher_details()
# non_teachers = NonTeachers("Mani", "Male", 37, "Kottayam", 9087467859, "Maintenance")
# non_teachers.get_details()
# classroom = ClassRoom("8th", "C", 45, "RH-38")
# classroom.get_class_details()
# class_equipment = ClassEquipment(10, 10, 2, 3, 2, 2)
# class_equipment.get_total_count()
# print(class_equipment.get_total_count())
# lab = Lab("Zoology", "ZY-04")
# lab.lab_details()
# lab_equipment = LabEquipment("Funnel", 10)
# lab_equipment.equipment_details()
# bus = SchoolBus(5, "SB-5", 40)
# bus.get_bus_details()
# auditorium = Auditorium(500, "OZORA", "3-2-2023", "2:00 PM")
# auditorium.get_event_details()
