from abc import ABC, abstractmethod

# ABSTRACTION: Define contract
class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def execute_query(self, query):
        pass

# INHERITANCE: Child classes inherit from parent
class MySQLConnection(DatabaseConnection):
    def __init__(self, host):
        self.__host = host  # ENCAPSULATION: Private
    
    def connect(self):
        return f"Connected to MySQL at {self.__host}"
    
    def execute_query(self, query):
        return f"MySQL: {query}"

class PostgreSQLConnection(DatabaseConnection):
    def __init__(self, host):
        self.__host = host  # ENCAPSULATION: Private
    
    def connect(self):
        return f"Connected to PostgreSQL at {self.__host}"
    
    def execute_query(self, query):
        return f"PostgreSQL: {query}"

# POLYMORPHISM: Same method, different behavior
databases = [
    MySQLConnection("localhost"),
    PostgreSQLConnection("remote.server")
]

for db in databases:
    print(db.connect())
    print(db.execute_query("SELECT * FROM users"))
