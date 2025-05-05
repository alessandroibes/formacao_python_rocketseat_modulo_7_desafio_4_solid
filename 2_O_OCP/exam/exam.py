from abc import ABC, abstractmethod

# Abstract base class that defines the contract for all exam types
class Exam(ABC):

    @abstractmethod
    def check_exam_conditions(self):
        pass

    @abstractmethod
    def approve_exam_request(self):
        pass
