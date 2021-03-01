'''
################################################
#  Program: Pod_leaders.py                     #
#  Author: Baba                                #
#  Date: 2/17/2021                             #
#  Description: Program to be used by the      #
#               POD Leaders in instructing     #
#               the POD members about Object   #
#               Oriented Programming concepts  #
#  The Hidden Genius Project                   #
#  OAK8 Cohort                                 #
################################################
'''

class Pod_leaders:
  
    # Class Constructor method is called when an Object is instantiated
    def __init__(self, pod_leader, pod_member):
       self.pod_leader = {}
       self.pod_member = {}
    
    # Class method to add a leader to the pod_leader dictionary       
    def add_leader(self, name,cell):
        self.pod_leader[name] = cell
    
    
    def add_member(self, name,cell):
        self.pod_member[name] = cell
        
    # Class method to print the pod_leader and cell numbers   
    def display_leaders(self):
      print('POD Leaders')      
      for leader, number in self.pod_leader.items():
        print(leader, number)

        
    def display_member(self):
      print('POD Members')      
      for member, number in self.pod_member.items():
        print(member, number)

            
pod = Pod_leaders("POD Leaders","POD Members");
pod.add_leader("Richard","(510) 228-5623")
pod.add_leader("Jacore","(845) 200-6250")
pod.add_leader("Gabriel","(510) 326-5834")
pod.add_leader("Aris","(510) 229-6359 ")
pod.add_leader("Andrew","(925) 727-4611")
pod.display_leaders()


pod.add_member("Richard","(510) 228-5623")
pod.add_member("Jacore","(845) 200-6250")
pod.add_member("Gabriel","(510) 326-5834")
pod.add_member("Aris","(510) 229-6359 ")
pod.add_member("Andrew","(925) 727-4611")
pod.display_member()

