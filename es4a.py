class CSVFile:
    
    def __init__ (self, file_name):
        self.name = file_name
        self.can_read = True
    def get_data(self):
        file_reader = open('file_vuoto.txt','r') #apro il file in modalità lettura
        if file_reader.readline():
            print("file presente")
        else:
            print("Errore")
        list=[]
        
        for line in file_reader:
            elements = line.split(',')
            list.append(elements)
        
        return list
csv_file = CSVFile('file_vuoto.txt')
list = csv_file.get_data()
