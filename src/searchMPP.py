from searchGeneric import AStarSearcher, visualize
from searchProblem import Path

class SearcherMPP(AStarSearcher):
    """returns a searcher for a problem.
    Paths can be found by repeatedly calling search().
    """
    def __init__(self, problem):
        super().__init__(problem)
        self.explored = set()
        self.solution = None
        self.actions = []
        self.states = []
    @visualize
    def search(self):
        """returns next path from an element of problem's start nodes
        to a goal node. 
        Returns None if no path exists.
        """
        while not self.empty_frontier():
                        
            path = self.frontier.pop()
            
            if path.end() not in self.explored:
                self.display(2, "Expanding:",path,"(cost:",path.cost,")")
                self.explored.add(path.end())
                self.num_expanded += 1
                #if path.arc is not None and path.arc.action not in self.actions:
                #    self.actions.append(path.arc.action)
               
                if self.problem.is_goal(path.end()):
                    self.display(1, self.num_expanded, "paths have been expanded and",
                           len(self.frontier), "paths remain in the frontier")
                    self.solution = path   # store the solution found
                    #print(path)
                    
                    self.actions = (path.get_acts())
                    self.states = path.nodes()
                    return path, self.actions, self.states
                else:
                    neighs = self.problem.neighbors(path.end())
                    self.display(3,"Neighbors are", neighs)
                    for arc in neighs:
                        self.add_to_frontier(Path(path,arc))
                    self.display(3,"Frontier:",self.frontier)    
        self.display(1,"No (more) solutions. Total of",
                     self.num_expanded,"paths expanded.")
            
#from stripsProblem import problem0
#searcherMPPcdp = SearcherMPP(problem0)
#print(searcherMPPcdp.search())  # find first path

