class DataProcessing:
    # data processing module
    # includes preprocessing, postprocessing
    # also including processing labels of transcript
    def __init__(self, conf) -> None:
        # conf read from dataset class
        # already used OmegaConf create
        self.conf = conf

    # functions for processing speech and labeled data
    def preprocessing_pipeline(self):
        # convert
        pass