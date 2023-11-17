<!--
Here is a draft README.md for the GitHub repository of your paper:

# Multi-Class Content Ranking using Seq-to-Seq Models

This is the code repository for the paper "A High-Speed Multi-Class Content Ranking using Seq-to-Seq Models". 

## Abstract

Content Ranking is an important task in many applications, such as documents ranking, text retrieval, text summarization and other natural language processing (NLP) procedures. Existing approaches define content ranking as a binary classification boilerplate removal, in which a text is either boilerplate or main-content. While boilerplate removal provides a basic mean for text ranking, in many applications, more importance levels are required to distinguish between different parts of an HTML document. 

Based on a new dataset of segmented and labeled HTML documents, in this paper we introduce a high-speed multi-class sequence-to-sequence text classification model for determining the importance level of a text within six levels. As we use only HTML’s structural features in the training process, our model is language-agnostic and also it can be fine-tuned on a small dataset of web pages of other languages. 

The involved feature extraction uses an optimized algorithm in terms of speed, which makes the end-to-end inference on an html page in about and less than 25ms, which is a huge benefit in terms of scalability of the model. Besides, our model achieves the 83 percent score in accuracy and 74 percent score in average 6 classes f1 score, which is a prominent result.

## Requirements

- Python 3.6+
- PyTorch 1.0+
- Transformers 4.0+
- Seqeval 0.0.12
- Beautifulsoup4 4.6.0

## Dataset

The dataset used for this project can be found at [ZDA Dataset](https://www.kaggle.com/datasets/sorousham/zda-dataset-1602). It contains 1602 labeled HTML documents across 6 classes:

- Title 
- Main content
- Related parts
- Other topics
- Headers and footers
- Useless parts

## Usage

The main scripts are:

- `feature_extraction.py` - extracts features from HTML documents
- `train.py` - trains the BiLSTM-CRF model
- `predict.py` - makes predictions on new HTML documents

To extract features:

```
python feature_extraction.py --data path/to/data --output path/to/features
``` 

To train the model: 

```
python train.py --train path/to/train/features --dev path/to/dev/features 
```

To make predictions:

```
python predict.py --model path/to/model --data path/to/data --output path/to/predictions
```

Pre-trained models are provided in the `models/` directory.

## Results

Our best BiLSTM-CRF model achieves 83% accuracy and 74% average F1 score on the test set. See the paper for more details on the results.

### Confusion Matrix

The confusion matrix for our best model BiLSTM-CRF 6 is shown below:

![Confusion Matrix](figures/confusion_matrix.png)

We see that the model confuses each class with its adjacent classes more than its non-adjacent classes.

## Citation

If you use this code for your research, please cite our paper:

```
@article{ashourisefat2021highspeed,
  title={A High-Speed Multi-Class Content Ranking using Seq-to-Seq Models},
  author={AshouriSefat, Soroush and Kazemi, Reza and Alikhany, Morteza and Raziei, Mohammad and Amini, Arash},
  journal={IEEE Access},
  volume={9},
  pages={XXXXX--XXXXX}, 
  year={2021},
  publisher={IEEE}
}
```

## Contact

For any questions, feel free to open an issue or contact me at soroush_ashourisefat@ee.sharif.edu.

-->

# Multi-Class Content Ranking using Seq-to-Seq Models

This repository contains code for a multi-class HTML content ranking model using BiLSTM-CRF, as described in the paper "A High-Speed Multi-Class Content Ranking using Seq-to-Seq Models".

## Overview

The model classifies HTML content into 6 classes indicating importance:

- Title
- Main content  
- Related parts
- Other topics
- Headers and footers
- Useless parts

The model uses only structural HTML features and is language agnostic. 

![Model Architecture](docs/readme/figures/model-architecture.png)

## Abstract

Content Ranking is an important task in many applications, such as documents ranking, text retrieval, text summarization and other natural language processing (NLP) procedures. Existing approaches define content ranking as a binary classification boilerplate removal, in which a text is either boilerplate or main-content. While boilerplate removal provides a basic mean for text ranking, in many applications, more importance levels are required to distinguish between different parts of an HTML document. 

Based on a new dataset of segmented and labeled HTML documents, in this paper we introduce a high-speed multi-class sequence-to-sequence text classification model for determining the importance level of a text within six levels. As we use only HTML’s structural features in the training process, our model is language-agnostic and also it can be fine-tuned on a small dataset of web pages of other languages. 

The involved feature extraction uses an optimized algorithm in terms of speed, which makes the end-to-end inference on an html page in about and less than 25ms, which is a huge benefit in terms of scalability of the model. Besides, our model achieves the 83 percent score in accuracy and 74 percent score in average 6 classes f1 score, which is a prominent result.



## Dataset

The dataset used for this project can be found at [ZDA Dataset](https://www.kaggle.com/datasets/sorousham/zda-dataset-1602). It contains 1602 labeled HTML documents across 6 classes:

- Title 
- Main content
- Related parts
- Other topics
- Headers and footers
- Useless parts


## Results

The model achieves 83% accuracy and 74% average F1 score on the test set.

### Confusion Matrix

The confusion matrix shows the model confuses classes with adjacent importance levels:

![Confusion Matrix](docs/readme/figures/confusion-matrix.png) 

### Example Output

The model generalizes well to new HTML pages:

![Example English Output 1](docs/readme/figures/example-english-page-1.png)

![Example English Output 2](docs/readme/figures/example-english-page-2.png)

![Example Persian Output](docs/readme/figures/example-persian-page-1.png)

## Usage

See the [examples](examples/) for scripts showing end-to-end usage.

Basic usage:

```python
from content_ranker import predict

model = predict.load_model("path/to/model.pt") 

html_string = load_html(...)

features = extract_features(html_string) 

tags = model.predict(features)
```

## Repository Structure

```
.
├── Dockerfile
├── examples/               - Example scripts showing usage
├── main.py                 - Main entry point  
├── pyproject.toml          - pypi config
├── README.md
├── requirements.txt        - Python requirements
├── src/                    - Source code
│   └── content_ranker/     - Package containing model code
│       ├── features/       - Feature extraction  
│       ├── models/         - PyTorch model definitions
│       ├── resources/      - Resources like pretrained models
│       └── utils/          - Utility functions
└── tests/                  - Tests
```

## Citation

Please cite the paper if you use this repository:

```
@article{ashourisefat-raziei-2023-content-ranker,
  title={A High-Speed Multi-Class Content Ranking using Seq-to-Seq Models},
  author={AshouriSefat, Soroush and Kazemi, Reza and Alikhany, Morteza and Raziei, Mohammad and Amini, Arash},
  journal={IEEE Access},
  volume={9},
  pages={XXXXX--XXXXX},
  year={2023},
  publisher={IEEE}
}
```

## Contact

For any questions, feel free to open an issue or contact us at 
[soroush_ashourisefat@ee.sharif.edu](mailto:soroush_ashourisefat@ee.sharif.edu)
or 
[mohammadraziei1375@gmail.com](mailto:mohammadraziei1375@gmail.com)
.
