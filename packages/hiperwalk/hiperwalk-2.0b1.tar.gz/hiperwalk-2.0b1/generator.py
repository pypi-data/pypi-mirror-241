import hiperwalk as hpw

def marked_func(i):
    return {"-G": [0]}

dims = range(5, 10)

# gen = hpw.quantum_walk_generator(
#         hpw.Coined,
#         graph=hpw.Hypercube,
#         marked=marked_func,
#         func_args=dims)

gen = (hpw.Coined(
           graph=hpw.Hypercube(d),
           marked={"-G": [0]})
       for d in range(5, 10))

print(type(gen))

x = dims
y_func = hpw.QuantumWalk.max_success_probability
hpw.plot_x_by_y(gen, x, y_func)
