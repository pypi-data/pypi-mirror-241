def plot_probability_distribution(probabilities, plot="line", ...):

    for prob in probabilities:
        if plot=='line':
            config()
            plt.plot(x, prob)
        elif plot='bar':
            config()
            plt.bar(x, prob)
        else:
            config2()
            _plot_other()

    plt.show()
