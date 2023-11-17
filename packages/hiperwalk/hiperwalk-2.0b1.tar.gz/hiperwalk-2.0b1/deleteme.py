import hiperwalk as hpw
g = hpw.Cycle(11)
qw = hpw.ContinuousTime(graph=g, gamma=0.35)
states = qw.simulate(time=(10, 1), initial_state=qw.ket(5))
probs = qw.probability_distribution(states)
hpw.plot_probability_distribution(probs, animate=True, show=True)
