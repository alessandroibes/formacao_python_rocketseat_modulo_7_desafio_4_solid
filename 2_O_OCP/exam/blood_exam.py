from .exam import Exam

# Concrete class for blood exam
class BloodExam(Exam):
    def check_exam_conditions(self):
        # Specific validation logic for blood exams
        return True

    def approve_exam_request(self):
        if self.check_exam_conditions():
            print("Blood exam approved!")
