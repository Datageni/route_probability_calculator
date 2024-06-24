from routes import *

main_nodes = [1,2,3,4,5,6,7,8,9,10]

class Prob_Functions():
    def __init__(self):
        self.main_nodes = main_nodes
        self.routes = routes

    def count_times(self,sequence,next_num):
        seq_count = 0
        next_num_count = 0
        seq_length = len(sequence)
        for route in self.routes:
            for i in range(len(route) - seq_length + 1):
                if route[i:i + seq_length] == sequence:
                    seq_count += 1
                    if i + seq_length < len(route) and route[i+ seq_length] == next_num:
                        next_num_count +=1
        return seq_count, next_num_count

    def prob_calculator(self,sequence):
        for node in self.main_nodes:
            seq_count, next_num_count = self.count_times(sequence,node)
            probability = next_num_count / seq_count
            print(f"The probability of moving from {sequence} to {node} is: {round(probability,2)} ")

prob_functions = Prob_Functions()