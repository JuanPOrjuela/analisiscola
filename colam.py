from mesa import Model, Agent
from mesa.time import RandomActivation
import random

class Cliente(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

class Servidor(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.ocupado = False

    def step(self):
        # si está ocupado, chance de liberar
        if self.ocupado and random.random() < self.model.mu:
            self.ocupado = False
        # si está libre y hay clientes en la cola, atiende
        if not self.ocupado and len(self.model.cola) > 0:
            self.model.cola.pop(0)
            self.ocupado = True

class SistemaColas(Model):
    def __init__(self, lambda_, mu, K, pasos):
        self.schedule = RandomActivation(self)
        self.lambda_ = lambda_
        self.mu = mu
        self.K = K
        self.pasos = pasos
        self.servidor = Servidor(0, self)
        self.schedule.add(self.servidor)
        self.cola = []
        self.rechazados = 0
        self.atendidos = 0

    def step(self):
        # llegada de cliente
        if random.random() < self.lambda_:
            if len(self.cola) < self.K:
                cliente = Cliente(self.random.randrange(1, 10000), self)
                self.cola.append(cliente)
            else:
                self.rechazados += 1
        # servidor atiende
        clientes_prev = len(self.cola)
        self.schedule.step()
        if clientes_prev > len(self.cola):
            self.atendidos += 1

    def run(self):
        for _ in range(self.pasos):
            self.step()
        return {
            "rechazados": self.rechazados,
            "atendidos": self.atendidos,
            "prob_bloqueo": self.rechazados / (self.rechazados + self.atendidos)
        }

# ejemplo de corrida
if __name__ == "__main__":
    modelo = SistemaColas(lambda_=0.4, mu=0.5, K=5, pasos=1000)
    resultados = modelo.run()
    print(resultados)
