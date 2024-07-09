from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class __DbConnectionHandler:
    def __init__(self) -> None:  # No método init vamos definir a url do nosso Banco, essas credenciais não devem
        # ficar explícitas em nosso código
        db_user = 'postgres'
        db_password = '1234'
        db_host = 'localhost'
        db_port = '5432'
        db_name = 'postgres'
        
        self.__connection_string = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
        
        self.__engine = None
        self.session = None
    
    def connect_to_db(self) -> None:  # Aqui vamos criar a conexão entre o banco e nossa aplicação
        self.__engine = create_engine(self.__connection_string)
            
    def get_engine(self):
        return self.__engine
    
    def __enter__(self):  # Ao entrar no contexto with e criarmos e utilizarmos a instância da classe, será aberto uma
        # sessão
        session_maker = sessionmaker(bind=self.__engine)
        self.session = session_maker()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):  # Ao sairmos do contexto a sessão será fechada
        if self.session:
            self.session.close()


db_connection_handler = __DbConnectionHandler()
