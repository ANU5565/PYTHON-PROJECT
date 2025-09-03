class Student:
    def _init_(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.subject_marks = {}
        self._percentage = 0.0
        self._grade = None

    def record_marks(self, subject, score):
        if not (0 <= score <= 100):
            raise ValueError("Marks must be between 0 and 100")
        self.subject_marks[subject] = score

    def get_percentage(self):
        if self.subject_marks:
            total = sum(self.subject_marks.values())
            self._percentage = total / len(self.subject_marks)
        return self._percentage

    def assign_grade(self):
        percent = self.get_percentage()
        if percent >= 90:
            self._grade = "A+"
        elif percent >= 80:
            self._grade = "A"
        elif percent >= 70:
            self._grade = "B"
        elif percent >= 60:
            self._grade = "C"
        elif percent >= 50:
            self._grade = "D"
        else:
            self._grade = "F"
        return self._grade

    def show_report(self):
        print("\n--- Student Report ---")
        print(f"Name       : {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print("\nMarks Obtained:")
        for sub, score in self.subject_marks.items():
            print(f"  {sub:<12} : {score}")
        print("-" * 25)
        print(f"Percentage : {self._percentage:.2f}%")
        print(f"Grade      : {self._grade}")


def run():
    # Input details
    s_name = input("Enter student name: ")
    s_roll = input("Enter roll number: ")

    learner = Student(s_name, s_roll)

    subject_count = int(input("How many subjects? "))

    for idx in range(1, subject_count + 1):
        subject = input(f"Enter name of subject {idx}: ")
        while True:
            try:
                score = float(input(f"Enter marks in {subject}: "))
                learner.record_marks(subject, score)
                break
            except ValueError as err:
                print(err)

    learner.assign_grade()
    learner.show_report()


if __name__ == "_main_":
    try:
        run()
    except Exception as problem:
        print("Something went wrong:", problem)