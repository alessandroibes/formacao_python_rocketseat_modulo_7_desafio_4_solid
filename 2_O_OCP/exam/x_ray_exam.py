from .exam import Exam

# Concrete class for x-ray exam
class XRayExam(Exam):
    def check_exam_conditions(self):
        # Specific validation logic for x-ray exams
        return True

    def approve_exam_request(self):
        if self.check_exam_conditions():
            print("X-ray exam approved!")
