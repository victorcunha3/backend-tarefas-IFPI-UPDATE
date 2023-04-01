from pydantic import BaseModel

class Tarefa(BaseModel):
    id: str | None
    descricao: str
    responsavel: str| None
    nivel: int
    situacao: str| None
    prioridade: int

    class Config:
        orm_mode = True

    @classmethod
    def fromDict(cls, tarefa):
        usuario_ = Tarefa(id=str(tarefa['_id']), descricao=tarefa['descricao'], 
                          responsavel=tarefa['responsavel'], nivel=tarefa['nivel'],
                           situacao=tarefa['situacao'], prioridade=tarefa['prioridade'])
        
        return usuario_
    
    def toDict(self):
        return {
            "descricao": self.descricao,
            "responsavel": self.responsavel,
            "nivel": self.nivel,
            "situacao": self.situacao,
            "prioridade": self.prioridade,
        }