import cplex as cp
from cplex.exceptions import CplexError

from inputdata import read_dat_file

class cplexModel:
      
    def __init__(self, filename):
        self.procced(filename)
       

    def procced(self, filename):
       data = Data(filename)
       model = cp.Cplex()
       handle = self.defineProblem(model, data)
       model.solve()
       model.write("model.lp")
       print(model.solution.get_objective_value())
    
    def defineProblem(self,n_model, data):
        n_model.objective.set_sense(n_model.objective.sense.minimize)
        vars = ['x' + str(i) for i in range(1,len(data.k)+1)]
        n_model.variables.add(names = vars, obj = [1,1,4])
        coef = [1]*len(data.k)
        n_model.linear_constraints.add(lin_expr= [cp.SparsePair(ind = vars, val = coef)], senses=["L"], rhs=data.budget)      
     
        
    def getValue(self):
        return self.model.solution.get_objective_value()


class Data:
    p= []    
    def __init__(self, filename):

        # read the data
        (self.budget, self.k )= read_dat_file(filename)
        for n in range(len(self.k)):
                self.p.append(1/((self.k[n]-1)*5/4+1))

if __name__ == "__main__":
    c = cplexModel()


        
        

        

        
