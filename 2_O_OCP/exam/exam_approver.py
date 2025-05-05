from .exam import Exam


class ExamApprover:
    def __init__(self, exam_type: Exam):
        self.exam_type = exam_type

    def approve_exam(self):
        self.exam_type.approve_exam_request()
