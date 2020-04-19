import numpy as np
import scipy.stats
from django.db.models import QuerySet

from katago_server.runs.models import Run


def random_weighted_choice(networks):
    probability_to_be_picked = scipy.stats.expon.pdf([index for index, _ in enumerate(networks)], loc=0, scale=2)
    probability_to_be_picked /= np.sum(probability_to_be_picked)
    return np.random.choice(networks, p=probability_to_be_picked)


class NetworkQuerySet(QuerySet):
    def select_best_without_uncertainty(self, run: Run):
        self.filter(run=run).order_by("-log_gamma_lower_confidence").first()

    def select_one_of_the_best_with_uncertainty(self, run: Run):
        best_networks = self.filter(run=run).order_by("-log_gamma_upper_confidence")[:10]
        return random_weighted_choice(best_networks)

    def select_one_of_the_more_uncertain(self, run: Run):
        more_uncertain_networks = self.filter(run=run).order_by("-log_gamma_uncertainty")[:10]
        return random_weighted_choice(more_uncertain_networks)