from userManagement.util.ResponseUtil import ResponseEntity
from userManagement.repository.UserRepository import UserRepository
import pandas as pd
class UserController:

    @staticmethod
    def showAllUsers():

        responseBody = UserRepository.getUsersAll()
        return ResponseEntity(body=responseBody)

    @staticmethod
    def findUserByUsername(username):
        responseBody = UserRepository.getUserByUsername(username)
        return ResponseEntity(body=responseBody)

    @staticmethod
    def registerUser(user = None):
        #bool : boolean타입으로 형변환
        responseBody = bool(UserRepository.saveUser(user))
        return ResponseEntity(body=responseBody)



