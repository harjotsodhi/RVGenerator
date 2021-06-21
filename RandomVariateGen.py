import numpy as np
import matplotlib.pyplot as plt
import math



class RVGenerator:

    def __init__(self, num_vars, seed=None):

        self.num_vars = num_vars

        if seed:

            np.random.seed(seed)


    def uniform(self, plot=False):

        u = np.random.uniform(size=self.num_vars)

        if plot:

            self.__plot(u, "Uniform distribution")

        return u


    def normal(self, mu=0, sigma=1, plot=False):

        u1 = self.uniform()
        u2 = self.uniform()

        ss = -np.log(u1)

        thetas = 2*math.pi*u2

        rs = np.sqrt(2*ss)

        standard_normal = rs*np.cos(thetas)
        norm = mu + sigma * standard_normal

        if plot:

            self.__plot(norm, f"Normal distribution {mu, sigma}")

        return norm


    def exponential(self, L, plot=False):

        u = np.random.uniform(size=self.num_vars)

        expo = -(np.log(1-u)/L)

        if plot:

            self.__plot(expo, f"Exponential distribution ({L})")

        return expo


    def gamma(self, alpha=2, beta=2, plot=False):

        g = np.zeros(self.num_vars)

        for i in range(alpha):

            expo = self.exponential(beta)
            g += expo

        if plot:

            self.__plot(g, f"Gamma distribution {alpha, beta}")

        return g


    def weibull(self, alpha=2, beta=2, plot=False):

        u = np.random.uniform(size=self.num_vars)

        w = alpha*((-np.log(1-u))**(1/beta))

        if plot:

            self.__plot(w, f"Weibull distribution {alpha, beta}")

        return w

    
    def bernoulli(self, p=0.75, plot=False):

        u = np.random.uniform(size=self.num_vars)

        s = u[np.nonzero(u >= p)]
        f = u[np.nonzero(u < p)]

        if plot:

            plt.bar("Success",len(s))
            plt.bar("Failure",len(f))
            plt.ylabel('Frequency')
            plt.title(f'{self.num_vars} Bernoulli ({p}) trials')
            plt.show()

        return s


    def geometric(self, p=0.3, plot=False):
        
        u = np.random.uniform(size=self.num_vars)
        geo = np.ceil(np.log(1-u)/np.log(1-p))

        if plot:

            trials, counts = np.unique(geo, return_counts=True)
            plt.bar(trials,counts)
            plt.xlabel("Number of trials")
            plt.ylabel("Frequency")
            plt.title(f"Geometeric Distribution ({p})")
            plt.show()

        return geo


    def __plot(self, v, title):

        count, bins, ignored = plt.hist(v, 30, density=True)
        plt.ylabel("p(x)")
        plt.title(title)
        plt.show()
