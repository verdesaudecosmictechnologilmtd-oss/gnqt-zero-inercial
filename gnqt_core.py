import numpy as np

class GNQT:
    def __init__(self, theta=10, decay=0.05):
        self.theta = theta
        self.decay = decay
        self.m = 0
        self.m_history = []

    def update_mass(self, signal):
        # Massa histórica com decaimento
        self.m = (self.m * (1 - self.decay)) + signal
        self.m_history.append(self.m)
        return self.m

    def detect_zi(self):
        # Detecta Zero Inercial
        return [1 if m >= self.theta else 0 for m in self.m_history]

    def detect_fz(self, window=10):
        # Detecta estabilidade (Força Zero)
        if len(self.m_history) < window:
            return False
        
        recent = self.m_history[-window:]
        variance = np.var(recent)
        
        return variance < 0.1


# Exemplo simples de uso
if __name__ == "__main__":
    gnqt = GNQT(theta=5)

    sinais = [1,1,1,2,2,3,5,5,5,5,5]

    for s in sinais:
        m = gnqt.update_mass(s)
        print(f"Massa: {m:.2f}")

    print("ZI:", gnqt.detect_zi())
    print("FZ:", gnqt.detect_fz())
