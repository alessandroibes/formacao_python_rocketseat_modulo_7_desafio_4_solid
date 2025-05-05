from exam.blood_exam import BloodExam
from exam.exam_approver import ExamApprover
from exam.x_ray_exam import XRayExam

blood_exam = BloodExam()
x_ray_exam = XRayExam()

blood_exam_approver = ExamApprover(blood_exam)
x_ray_exam_approver = ExamApprover(x_ray_exam)

blood_exam_approver.approve_exam()
x_ray_exam_approver.approve_exam()
