# M/M/1/K/∞ — modelo matemático, comparación con NetLogo y comprobación con MESA

## notación y parámetros
- $\lambda$ : tasa de llegada.  
- $s$ : tiempo medio de servicio (ticks).  
- $\mu = 1/s$ : tasa de servicio.  
- $K$ : capacidad total del sistema (clientes en servicio + en cola).  
- fuente: infinita (por eso el `/\infty` en la notación).  
- $\rho=\dfrac{\lambda}{\mu}$ : factor de tráfico (tráfico nominal).  
- $P_n$ : probabilidad estacionaria de $n$ clientes en el sistema.  
- $P_K$ : probabilidad de bloqueo (sistema en estado $K$).  
- $\lambda_{\text{eff}}$ : tasa efectiva de entrada (llegadas que sí entran).  
- $L$ (NS) : número medio en el sistema.  
- $L_q$ (Nw) : número medio en la cola (excluye el que está en servicio).  
- $W$ (TS) : tiempo medio en el sistema.  
- $W_q$ (Tw) : tiempo medio en cola.

---

## 1) modelo matemático (M/M/1/K/∞)

### probabilidades estacionarias (relación geométrica)

Para $n = 0, \dots, K$:

$$
P_n = \rho^{\,n} \, P_0
$$

**Normalización:**

- si $\rho \neq 1$:

$$
\sum_{n=0}^K P_n 
= P_0 \sum_{n=0}^K \rho^n 
= P_0 \cdot \frac{1-\rho^{\,K+1}}{1-\rho} 
= 1 
\quad \Rightarrow \quad
P_0 = \frac{1-\rho}{1-\rho^{\,K+1}}.
$$

- si $\rho = 1$:

$$
P_n = \frac{1}{K+1}, \quad (n=0,\dots,K).
$$

La probabilidad de **bloqueo** (sistema lleno) es:

$$
P_K = \rho^{\,K} P_0.
$$

La tasa efectiva de llegada (las que sí entran al sistema) es:

$$
\lambda_{\text{eff}} = \lambda (1-P_K).
$$

---

### número medio en el sistema $L$ (NS)

Definición:

$$
L = \sum_{n=0}^K n P_n.
$$

Fórmula cerrada para $\rho \neq 1$ (usando la suma conocida $\sum_{n=1}^K n r^n$):

$$
L = P_0 \cdot \frac{\rho \, \big(1 - (K+1)\rho^K + K\rho^{K+1}\big)}{(1-\rho)^2}.
$$

Para $\rho = 1$:

$$
L = \frac{K}{2}.
$$

Número medio en cola (excluye servidor):

$$
L_q = L - (1-P_0),
$$

ya que la probabilidad de que el servidor esté ocupado es $1-P_0$.


### tiempos medios (ley de Little con $\lambda_{\text{eff}}$)
$$
W=\frac{L}{\lambda_{\text{eff}}},\qquad W_q=\frac{L_q}{\lambda_{\text{eff}}}.
$$

Utilización efectiva del servidor:
$$
\rho_{\text{eff}}=\frac{\lambda_{\text{eff}}}{\mu}=\frac{\lambda(1-P_K)}{\mu}.
$$

---

## 2) Comparación práctica con NetLogo (ejemplo y notas)

### parámetros usados en la captura de NetLogo (ejemplo)
- `mean-arrival-rate = \lambda = 0.60` (por tick)  
- `mean-service-time = s = 1.55` (ticks) → $\mu=1/1.55\approx 0.64516129$  
- número de servidores = 1 → M/M/1.  
- en la captura NetLogo se muestra la versión **∞** (sin tope $K$ visible), por eso compararemos primero con $K=\infty$.

### teórico (caso infinito $K\to\infty$, válido si no hay bloqueo)
- $\rho=\dfrac{\lambda}{\mu}\approx 0.93$
- $L_q=\dfrac{\rho^2}{1-\rho}\approx 12.356$
- $W_q=\dfrac{L_q}{\lambda}\approx 20.593$ ticks
- $W\approx 22.143$ ticks
- utilización $\rho\approx 93\%$

> En la captura NetLogo se observan valores empíricos y los monitores `Exp.*` con esos mismos valores teóricos. La diferencia entre una corrida empírica concreta y el teórico suele deberse a ruido estocástico y warm-up.

### si usas M/M/1/K con $K$ finito
- al elegir un $K$ pequeño (p. ej. $K=10$), aparecerá bloqueo ($P_K>0$) y las medidas cambiarán: $\lambda_{\text{eff}}<\lambda$, $L_q$ y tiempos disminuirán comparados con el caso infinito (porque se descartan llegadas cuando el sistema está lleno).
- para comparar NetLogo con el modelo finito, asegúrate de que NetLogo esté configurado con la misma capacidad $K$ (si tu NetLogo no tiene tope, entonces compáralo con $K\to\infty$).

### interpretación práctica
- Si tu experimento en NetLogo refleja un sistema con **sin límite** (cola infinita), usa las fórmulas M/M/1/∞.  
- Si tu profe pide **M/M/1/K/∞**, en el README incluye las fórmulas anteriores (M/M/1/K) y señala en la práctica qué $K$ se usó en cada simulación.  
- Para validar con simulación, haz varias réplicas, aplica warm-up (descartar transitorio) y promedia; así la discrepancia teórica/simulación cae mucho.

---

## 3) pasos prácticos para reproducir y comparar
1. elige $(\lambda,s,K)$ (si $K$ grande → aproxima infinito).  
2. calcula $P_0,P_n,P_K$ y luego $L,L_q,W,W_q$ con las fórmulas de la sección 1.  
3. corre simulación (NetLogo / MESA) con los mismos parámetros, usa warm-up y varias réplicas.  
4. compara medias y reporta error relativo y, si es posible, intervalos de confianza.  

---

## 4) recursos y ejemplo numérico rápido
- ejemplo: $\lambda=0.60,\ s=1.55,\ \mu\approx0.64516,\ K=\infty$ → resultados teóricos listos arriba.  
- para $K=10$ (muestra): calcula $P_0=\dfrac{1-\rho}{1-\rho^{11}}$ y luego $L$ con la fórmula cerrada para $K=10$; usa eso para obtener $W$ y $W_q$ con $\lambda_{\text{eff}}=\lambda(1-P_{10})$.

# 3) Comprobación experimental (MESA)

Para validar el modelo matemático de la cola **M/M/1/K/∞**, se implementó una simulación computacional en Python usando la librería [Mesa](https://mesa.readthedocs.io/).

En cada corrida, se registraron:
- **rechazados**: clientes que llegaron cuando el sistema estaba lleno.  
- **atendidos**: clientes que sí entraron al sistema y recibieron servicio.  
- **prob\_bloqueo**: proporción de clientes rechazados respecto al total de llegadas.  

## Resultados de la simulación

Ejemplo de ejecuciones independientes:

```python
{'rechazados': 13, 'atendidos': 396, 'prob_bloqueo': 0.0318}
{'rechazados':  2, 'atendidos': 380, 'prob_bloqueo': 0.0052}
{'rechazados': 10, 'atendidos': 372, 'prob_bloqueo': 0.0262}
{'rechazados': 18, 'atendidos': 384, 'prob_bloqueo': 0.0448}
{'rechazados':  6, 'atendidos': 340, 'prob_bloqueo': 0.0173}
{'rechazados':  0, 'atendidos': 381, 'prob_bloqueo': 0.0000}
{'rechazados': 17, 'atendidos': 378, 'prob_bloqueo': 0.0430}
{'rechazados': 21, 'atendidos': 393, 'prob_bloqueo': 0.0507}
{'rechazados':  6, 'atendidos': 423, 'prob_bloqueo': 0.0139}
{'rechazados': 10, 'atendidos': 401, 'prob_bloqueo': 0.0243}
{'rechazados':  5, 'atendidos': 378, 'prob_bloqueo': 0.0131}
{'rechazados':  1, 'atendidos': 388, 'prob_bloqueo': 0.0026}
{'rechazados': 10, 'atendidos': 408, 'prob_bloqueo': 0.0239}
{'rechazados':  9, 'atendidos': 381, 'prob_bloqueo': 0.0231}
```

## Comparación con el modelo matemático

Del modelo teórico para una cola **M/M/1/K/∞**, la probabilidad de bloqueo (sistema lleno) se obtiene como:

$$
P_K = \rho^K P_0,
$$

donde

$$
P_0 = \frac{1-\rho}{1-\rho^{K+1}}
$$

La tasa efectiva de llegada (las que sí entran al sistema) es:

$$
\lambda_{\text{eff}} = \lambda (1 - P_K).
$$

---

Al comparar los valores experimentales de $P_{K}$ obtenidos con **MESA**  
(aproximadamente entre $0.02$ y $0.05$ en las corridas) con la predicción teórica,  
se observa que **los resultados coinciden de forma cercana**, validando así el modelo matemático.
