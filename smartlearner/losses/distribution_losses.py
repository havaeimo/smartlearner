from ..interfaces.loss import Loss

import theano.tensor as T


class BinaryCrossEntropy(Loss):
    def _get_updates(self):
        return {}  # There is no updates for BinaryCrossEntropy.

    def _compute_loss(self, model_output):
        return T.mean(T.nnet.binary_crossentropy(model_output, self.dataset.symb_targets))
