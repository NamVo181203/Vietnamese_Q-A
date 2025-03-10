

## MY ACCURACY ##
class MyAccuracy(Metric):
    def __init__(self):
        super(MyAccuracy, self).__init__()
        self.add_state("total", default=torch.tensor(0),
                       dist_reduce_fx="sum")
        self.add_state("correct", default=torch.tensor(0),
                       dist_reduce_fx="sum")

    def update(self, preds, target):
        preds = torch.argmax(preds, dim=1)
        assert target.shape == preds.shape
        self.correct += torch.sum(preds == target)
        self.total += target.numel()

    def compute(self):
        return self.correct.float() / self.total.float()