import cplex as cp
from cplex.exceptions import CplexError
import data as Data


class cplexModel:
    
    def __init__(self, dane):
        self.data = dane
        self.procced()
##    def __init__(self, filename):
##        self.procced(filename)

    
##    def procced(self, filename):
##       data = Data(filename)
##       model = cp.Cplex()
##       handle = self.defineProblem(model, data)
##       model.solve()
##       model.write("model.lp")
##       print(model.solution.get_objective_value())
       
    def procced(self):
       self.model = cp.Cplex()
       if(self.data.riskOrGain == 0):
           handle = self.defineProblem(self.model, self.data)
       else:
           handle = self.defineProblem2(self.model, self.data)
       
       self.model.solve()
       self.model.write("model.lp")
       print(self.model.solution.get_objective_value())
    
    def defineProblem(self,n_model, data):
        n_model.objective.set_sense(n_model.objective.sense.minimize)
        vars = ['x' + str(i) for i in range(1,len(data.k)+1)]
        n_model.variables.add(names = vars, obj = data.pk)
        coef = [1]*len(data.k)
        print(vars)
        print(coef)
        budget = [float(data.budget)]
        n_model.linear_constraints.add(lin_expr= [cp.SparsePair(ind = vars, val = coef)], senses=["L"], rhs=budget)      

    def defineProblem2(self,n_model, data):
        n_model.objective.set_sense(n_model.objective.sense.maximize)
        vars = ['x' + str(i) for i in range(1,len(data.k)+1)]
        n_model.variables.add(names = vars, obj = [1,1,4])
        coef = [1]*len(data.k)
        n_model.linear_constraints.add(lin_expr= [cp.SparsePair(ind = vars, val = coef)], senses=["L"], rhs=data.budget)
        
    def getValue(self):
        return self.model.solution.get_objective_value()

##
##class Data:
##    p= []    
##    def __init__(self, filename):
##
##        # read the data
##        (self.budget, self.k )= read_dat_file(filename)
##        for n in range(len(self.k)):
##                self.p.append(1/((self.k[n]-1)*5/4+1))

##if __name__ == "__main__":
##    c = cplexModel(Data.Data())


        
        

        

        
