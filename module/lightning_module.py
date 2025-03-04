from torch import optim, nn
from torch.optim.lr_scheduler import ExponentialLR
import pytorch_lightning as pl
import torchmetrics


class Light_Neural(pl.LightningModule):
    def __init__(self, conf, neural_net):
        super().__init__()
        # models
        self.conf = conf
        self.model = neural_net

        # loss function
        self.loss_fc = nn.CrossEntropyLoss()

        # Log hyper params
        self.save_hyperparameters()

        # Metrics
        self.accuracy = torchmetrics.Accuracy(task="multiclass",
                                              num_classes=self.conf.hyperparam.num_classes)
        self.f1_score = torchmetrics.F1Score(task="multiclass",
                                             num_classes=self.conf.hyperparam.num_classes)

        # train, val, test, output
        self.train_step_outputs = []
        self.val_step_outputs = []
        self.test_step_outputs = []

    def configure_optimizers(self):
        """
        - Lightning calls ``.backward()`` and ``.step()`` automatically in case of automatic optimization.
        - If a learning rate scheduler is specified in ``configure_optimizers()`` with key
          ``"interval"`` (default "epoch") in the scheduler configuration, Lightning will call
          the scheduler's ``.step()`` method automatically in case of automatic optimization.
        """
        # optimizer
        optimizer = optim.AdamW(self.model.parameters(),
                                lr=self.conf.hyperparam.learning_rate,
                                weight_decay=self.conf.hyperparam.weight_decay)
        # scheduler
        scheduler = ExponentialLR(optimizer=optimizer,
                                  gamma=self.conf.hyperparam.gamma)

        return [optimizer], [{"scheduler": scheduler, "interval": "epoch"}]

    # Step common for all training, dev, testing steps
    def _common_step(self, batch, batch_idx):

        return

    ## TRAIN STEP ##
    def training_step(self, batch, batch_idx):

        return

    ## VAL/DEV STEP ##
    def validation_step(self, batch, batch_idx):

        return

    ## TEST STEP ##
    def test_step(self, batch, batch_idx):

        return