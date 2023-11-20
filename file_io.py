class FileIO:
    
     #decorator in Python,used to define a static method,
    #You can call it using the class name directly, without creating an instance of the class.
    #used for utility functions that don't depend on the state of a particular instance of the class.
    @staticmethod
    def read_line_by_line(file_name: str)->list[list[str]]:
        #parameter type : str :  expects a string argument representing the name or path of a file.
        #indicates that the function is expected to return a list of lists of strings,Each inner list represents a line from the file
        result = []
        
        # reads the specified file line by line and processes each line to create a list of lists.
        with open(file_name, 'r') as map_file:
            for row in map_file:
                result.append(row.split())
            return result      
        