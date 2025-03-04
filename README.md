# Vietnamese Question and Answer

### FOLDER usage in project
```python
1. build (include train, testing and fine tune code)
2. configs (config with yaml file, config file including model conf, trainer conf, processor conf)
3. core (contains metric folder and logger for project)
4. data_manipulation (data manipulation used to handle with data like data preprocessing, 
   postprocessing, dataloader and store manifest for training)
5. model_checkpoints (saved model checkpoint folder)
6. models (model frame folder)
7. modules (others module like RNN block, CNN block, customed Conformer Encoder stored)
8. utils (...)
```

## Setup
### Window
```python
python3 -m venv venv
```

```python
pip install -m requirements.txt
```

```python
python3 my_settings.py
```

### Linux || WSL
```bash
chmod +x setup.sh
```

```bash
./setup.sh
```