# magic_selection
Feature selection method with support for combined features. You can combine features like ['Feature A', 'Feature B'] so that both of them will either be chosen or not

## Installation
### Conda environment using pip

```bash
    conda create -n magic_selection python=3.9.12
    conda activate magic_selection
    conda install pip
    pip install MagicSelection
```

### Python3 virtual environment using pip

```bash
    python3 -m venv env magic_selection
    source magic_selection/bin/activate
    pip install magic_selection
```

### Conda environment from Github repository

```bash
    git clone https://github.com/dwu12/feature_selection.git
    cd magic_selection
    pip install .
```
## Usage
```bash
def magic_selection(df_train, 
                    df_test, 
                    score_metric,
                    model_dict, 
                    target,
                    cv = 5,
                    upsample_flag = False,
                    upsample_flag_show = False, 
                    ratio = 1, 
                    random_state = 42, 
                    replace = True ,
                    feature_groups = None, 
                    fibe_cv = 3,
                    fibe_flag_show = False,
                    Threshold = None):
    '''
    test your feature selection model
    
    Parameters
    ----------
    df_train: training data
    
    df_test: testing data

    score_metric: classification metrics ('accuracy', 'f1', 'balanced_accuracy')
    
    model_dict: a dictionary of model to be used
    
    target: target value
    
    cv = 5: default equal to 5 for cross-validation if df_test is None
    
    upsamle_flag: if True, use upsample method, default False 
    
    upsample_flag_show: if True, show the target distribution, default False
    
    Ratio: ratio of majority / minority, default is 1
    
    random_state: for reproducible, default is 42
    
    replace: sample with replacement or not, default is True
    
    feature_groups: group features for better explanation. The idea is group one-hot encoder features together.
                    default is None
    
    fibe_cv: cross validation with in FIBE method, default = 3
    
    fibe_flag_show: print detail information, default = False
    
    threshold: set a threshold for max # number of features you want select, default = None
    
    ----------
    
    return offline metrics for either classification or regression as a dataframe
    '''
```
## Examples

```bash
    from MagicSelection.feature_selection import magic_selection
    from MagicSelection.feature_selection import get_example_data
    df_outcome = get_example_data()
    df_train = df_outcome[df_outcome['group'] == 'A'].drop(columns=['group'])
    df_test = df_outcome[df_outcome['group'] == 'B'].drop(columns=['group'])
    
    model_dic = {
            'Decision Tree': tree.DecisionTreeClassifier(random_state = 11),
            'SVM linear classifier' : SVC(kernel = 'linear',random_state = 11),
            'SVM gaussian classifier' : SVC(random_state = 11)
        }
    
    feature_groups = [[i] for i in df_train.columns if i != 'Class']

    result = magic_selection(df_train = df_train, 
                             df_test = df_test, 
                             model_dict = model_dic, 
                             score_metric = 'accuracy',
                             target = 'Class',  
                             feature_groups = feature_groups,
                             upsample_flag = True,
                             ratio = 1,
                             cv = 5)

    display(result)
```
