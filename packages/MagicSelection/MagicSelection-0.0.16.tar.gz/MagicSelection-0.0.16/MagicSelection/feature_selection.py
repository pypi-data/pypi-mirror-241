## set up dependency(s)
import pandas as pd
import numpy as np
from numpy import vstack
from numpy import hstack
from numpy import asarray
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report
from collections import defaultdict

## plot method
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator,IndexLocator
import seaborn as sns

   
## Metices
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import KFold, StratifiedKFold
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, f1_score, balanced_accuracy_score
from sklearn.model_selection import train_test_split 
from sklearn.metrics import confusion_matrix, classification_report, precision_score, ConfusionMatrixDisplay
from sklearn.preprocessing import MinMaxScaler


# SKlearn Models
from sklearn import tree
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import CategoricalNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC

## feature ranking
from sklearn.feature_selection import SelectFromModel
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
import itertools

## regex 
import re

## resample technique
from sklearn.utils import resample

## time 
import time


def upsample(df, 
             target, 
             Flag = False, 
             ratio = 1, 
             random_state = 42, 
             replace = True):
    
    '''
    Designed for imbalanced dataset, use upsampling techniques to make target distribution 
    in some specific ratio, default ratio is 1 meaning all target values equally distributed
    after upsample
    
    Parameters
    ----------
    df : dataframe you want to make upsampling (for imbalanced dataset)
        
    target: target column for upsampling
    
    Flag: whether print the original target distribution, default is False
    
    Ratio: ratio of majority / minority, default is 1
    
    random_state: for reproducible, default is 42
    
    replace: sample with replacement or not, default is True
    ----------
    
    returns : a dataset with specific ration for target distribution
    '''
    
    if Flag:
        plt.figure(figsize=(8,4)) 
        ax = sns.countplot(x= target , data=df)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha="right")
        ax.set_title('How many counts for categorical feature: {}'.format(target))

    value_dic = df[target].value_counts()
    target_value = value_dic.keys()
    
    majority = target_value[0]
    majority_value = value_dic[majority]
    
    df_majority = df[(df[target]==majority)] 
    
    l = [df_majority]
    
    for minority in target_value[1:]:
        df_minority = df[(df[target] == minority)] 

        df_minority_upsampled = resample(df_minority, 
                                         replace=replace,    # sample with replacement
                                         n_samples= majority_value // ratio, # to match majority class
                                         random_state=random_state)  # reproducible results
        
        l.append(df_minority_upsampled)
         
    
    output = pd.concat(l)
        
    return output


def Fibe(estimator_name, 
         estimator, 
         X, 
         y, 
         score_metric, 
         feature_groups, 
         cv = 5, 
         Flag= False, 
         threshold = False):
    
    '''
    Designed for FIBE (Forward Inclusion Backward Elimination) method to find the best feature 
    combination. For more info: please check: 
    
    http://rasbt.github.io/mlxtend/user_guide/feature_selection/SequentialFeatureSelector/
    
    Parameters
    ----------
    estimator_name: the name of estimator, could be classification | regression estimator
        
    estimator: machine learning estimator
    
    X: used for model training
    
    y: used for model training
    
    score_metric: offline metric, can be either classification or regression
    
    feature_groups: group features for better explanation. The idea is group one-hot encoder features together.
                    default is None
                    
    cv: cross validation, default = 5
    
    Flag: print detail information, default = False
    
    threshold(int): set a threshold for max # number of features you want select, default = False
    
    ----------
    
    returns : a pair of ([selected features], estimator name)
    '''
    
    num_features = len(feature_groups)
    
    if threshold != None:
        if threshold > num_features:
            raise Exception('Your threshold should be smaller than the number of features')
        else:
            num_features = threshold
    
    sff_clf = SFS(estimator,
                  k_features=(1, num_features),
                  forward=True,
                  floating=True,
                  scoring= score_metric,
                  feature_groups = feature_groups,
                  cv=cv)
    
    sff_clf.fit(X, y)
    
    if Flag:
        print('best combination (%s: %.3f): %s\n' % (score_metric, sff_clf.k_score_, sff_clf.k_feature_idx_))
        print('all subsets:\n', sff_clf.subsets_)
        
    return (list(sff_clf.k_feature_names_), estimator_name)


def check_balance(df, target):
    '''
    check a dataset has balanced distribution
    
    Parameters
    ----------
    df : dataframe you want to make upsampling (for imbalanced dataset)
        
    target: target column balance checking
    ----------
    
    returns : True if balanced distribution else false
    '''
    
    l = df[target].value_counts().tolist()
    max_val = np.max(l)
    min_val = np.min(l)
    
    return (max_val / min_val) <= 3
    

def get_feature_dic(model_dic,
                    df_train, 
                    target , 
                    score_metric,
                    cv = 5,
                    upsample_flag = False,
                    upsample_flag_show = False, 
                    ratio = 1, 
                    random_state = 42, 
                    replace = True ,
                    feature_groups = None, 
                    fibe_cv = 3,
                    fibe_flag_show = False,
                    Threshold = None
                    ):
    
    '''
    get the FIBE information for different methods
    
    Parameters
    ----------
    model_dic: a dictionary with the format key = estimator name, value = estimator
    
    df_train: dataframe for training 
    
    df_test: dataframe for testing, if df_y is None, then df_x will be split to train-test dataset using cross-validation
    
    target: target feature using on both df_x and df_y
    
    score_metric: offline metric for Fibe Method, can be either classification or regression
    
    cv = 5: default equal to 5 for cross-validation if df_test is None
    
    upsamle_flag: if True, use upsample method, default False 
    
    upsample_flag_show: if True, show the target distribution, default False
    
    Ratio: ratio of majority / minority, default is 1
    
    random_state: for reproducible, default is 42
    
    replace: sample with replacement or not, default is True
    
    feature_groups: group features for better explanation. The idea is group one-hot encoder features together.
                    default is None
    
    fibe_cv: cross validation, default = 5
    
    fibe_flag_show: print detail information, default = False
    
    threshold (int): set a threshold for max # number of features you want select, default = False
    
    
    ----------
    
    returns : A list contains [ (estimator_name, feature_selected, scoring)]
    '''
    
        
    ## check data balance: use KFold for balanced data, use StratifiedKFold for imbalanced data
    if check_balance(df_train, target): 
        kf = KFold(n_splits = cv) 
    else:
        kf = StratifiedKFold(n_splits= cv)

    X = df_train.drop(columns = [target])
    y = df_train[target]
    
    if feature_groups == None:
        feature_groups = X.columns
        
        
    result = []
    

    for train_index , test_index in kf.split(X, y):
        df_train_ = df_train.iloc[train_index]
        df_test_ = df_train.iloc[test_index]
        

        if upsample_flag:
            df_train_ = upsample(df_train_, 
                                target, 
                                Flag = upsample_flag_show, 
                                ratio = ratio, 
                                random_state = random_state, 
                                replace = replace)

        df_x = df_train_.drop(columns = [target])
        df_y = df_train_[target]
        
        df_xtest = df_test_.drop(columns = [target])
        df_ytest = df_test_[target]

        for clf_name in model_dic:
            clf = model_dic[clf_name]
            feature_list, estimator_name = Fibe(clf_name, 
                                                clf, 
                                                df_x, 
                                                df_y, 
                                                score_metric,
                                                feature_groups, 
                                                fibe_cv,
                                                fibe_flag_show,
                                                Threshold)

            
            estimator = model_dic[clf_name]
            estimator.fit( df_x[feature_list], df_y)
            y_predict = estimator.predict( df_xtest[feature_list] ) 
            
            if score_metric == 'accuracy':
                current_score = accuracy_score(df_ytest, y_predict)
            elif score_metric == 'f1':
                current_score = f1_score(df_ytest, y_predict, pos_label = 1)
            elif score_metric == 'balanced_accuracy':
                current_score = balanced_accuracy_score(df_ytest, y_predict)
                
            result.append( (clf_name, feature_list, current_score))
      

    return result

def plot(feature_map):
    '''
    Plot the feature_map information
    
    Parameters
    ----------
    feature_map: a dataframe with each cell is a precentage time that has been choosen
    ----------
    
    return Nothing but a plot
    '''
    
    fig = plt.figure(figsize=(20, 10)) 
    ax=plt.subplot()
    ax.set_xlabel('features');ax.set_ylabel('Classifier'); 
    #ax.tick_params(axis='both', which='minor', labelsize=2)

    #print (s_outcome)
    ax.yaxis.set_ticklabels(feature_map.index,fontsize=10)
    ax.xaxis.set_ticklabels(feature_map.columns,rotation=90,fontsize=10)

    img=ax.matshow(feature_map,cmap="coolwarm")
    plt.colorbar(img, ax=ax,location="bottom")
    ax.yaxis.set_major_locator(IndexLocator(base=1,offset=0.5))  # <- HERE
    ax.xaxis.set_major_locator(IndexLocator(base=1,offset=0.5))  # <- HERE

    plt.savefig("FEATURE_SELECTION.png", 
                   bbox_inches='tight', 

                   pad_inches=0) 

    plt.show()
    
def grab_info(result, df, target , cv =5 , threshold = 0.7):
    
    '''
    Grab the FIBE information 
    
    Parameters
    ----------
    result: result from model selection
    df: dataframe used for columns selections
    target: target of the task
    cv: number of cross_validation it makes
    threshold: set a threshold to get the most common features
    
    ----------
    
    return two dictionaries and a selected features: one is the best features based on score, one the most voted features
    '''
    
    dic_best = dict()
    dic_vote = dict()
    
    df = df.drop(columns = [target])
    
    dd = defaultdict(list)
    
    for (estimator_name, feature_select, score) in result:
        dd[estimator_name].append( (feature_select , score))
        
    feature_select_df = pd.DataFrame(index=dd.keys(), columns= sorted(df.columns))
    feature_select_df = feature_select_df.fillna(0)
        
    for estimator_name in dd:
        l = sorted(dd[estimator_name], key = lambda x: (x[1], -len(x[0])), reverse = True)[0]
        #print('the best selection for estimator {} is: {}, '.format(estimator_name, l[0]))
        dic_best[estimator_name] = l[0]

        for features in dd[estimator_name]:
            feature_select_df.loc[estimator_name][features[0]] += 1
        
    
    feature_select_df = feature_select_df.iloc[:,:].apply(lambda x: round(x / cv,2))
    
    for estimator_name in dd:
        A = feature_select_df.loc[estimator_name] >= threshold
        select_feature = A[A == True].index.tolist()
        #print('the most voted selection for {} , is {}'.format(estimator_name,select_feature))
        dic_vote[estimator_name] = select_feature
    
#     display(feature_select_df)
    plot(feature_select_df)
    
    return dic_best, dic_vote, feature_select_df


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
    
    fibe_cv: cross validation, default = 5
    
    fibe_flag_show: print detail information, default = False
    
    threshold: set a threshold for max # number of features you want select, default = False
    
    ----------
    
    return offline metrics for either classification or regression 
    '''
    
    if df_test is None:
  
        kf = StratifiedKFold(n_splits= cv)
            
        X = df_train.drop(columns = [target])
        y = df_train[target]
        
        
        eval_best = defaultdict(list)
        eval_vote = defaultdict(list) 
            
        for train_index , test_index in kf.split(X, y):
            df_train_ = df_train.iloc[train_index]
            df_test_ = df_train.iloc[test_index]
            
            data = get_feature_dic(model_dict,
                               df_train_, 
                               target , 
                               score_metric,
                               cv,
                               upsample_flag,
                               upsample_flag_show, 
                               ratio, 
                               random_state, 
                               replace ,
                               feature_groups, 
                               fibe_cv,
                               fibe_flag_show,
                               Threshold)
        
        
            dic_best, dic_vote, feature_select_df = grab_info(data, df_train_, target , cv =5 , threshold = 0.2)

            for estimator_name in model_dict:
                estimator = model_dict[estimator_name]

                best_feature = dic_best[estimator_name]
                vote_feature = dic_vote[estimator_name]

                df_x = df_train_.drop(columns = [target])
                df_y = df_train_[target]

                df_xtest = df_test_.drop(columns = [target])
                df_ytest = df_test_[target]

                #---------best feature--------#
                estimator.fit( df_x[best_feature], df_y)
                y_predict = estimator.predict( df_xtest[best_feature])

                if score_metric == 'accuracy':
                    current_score = accuracy_score(df_ytest, y_predict)
                elif score_metric == 'f1':
                    current_score = f1_score(df_ytest, y_predict, pos_label = 1)
                elif score_metric == 'balanced_accuracy':
                    current_score = balanced_accuracy_score(df_ytest, y_predict)

                eval_best[estimator_name].append([current_score,best_feature])

                #--------voted feature--------#
                estimator.fit( df_x[vote_feature], df_y)
                y_predict = estimator.predict( df_xtest[vote_feature])
                
                if score_metric == 'accuracy':
                    current_score = accuracy_score(df_ytest, y_predict)
                elif score_metric == 'f1':
                    current_score = f1_score(df_ytest, y_predict, pos_label = 1)
                elif score_metric == 'balanced_accuracy':
                    current_score = balanced_accuracy_score(df_ytest, y_predict)

                eval_vote[estimator_name].append([current_score,vote_feature])

    
    else:
        data = get_feature_dic(model_dict,
                               df_train, 
                               target , 
                               score_metric,
                               cv,
                               upsample_flag,
                               upsample_flag_show, 
                               ratio, 
                               random_state, 
                               replace ,
                               feature_groups, 
                               fibe_cv,
                               fibe_flag_show,
                               Threshold)
        
        
        dic_best, dic_vote, feature_select_df = grab_info(data, df_train, target , cv , threshold = 0.5)
        
        eval_best = defaultdict(list)
        eval_vote = defaultdict(list) 
             
        
        for estimator_name in model_dict:
            estimator = model_dict[estimator_name]

            best_feature = dic_best[estimator_name]
            vote_feature = dic_vote[estimator_name]

            df_x = df_train.drop(columns = [target])
            df_y = df_train[target]

            df_xtest = df_test.drop(columns = [target])
            df_ytest = df_test[target]

            
            #---------best feature--------#
            estimator.fit( df_x[best_feature], df_y)
            y_predict = estimator.predict( df_xtest[best_feature])
            
            sensitivity = None
            specificity = None
            
            if score_metric == 'accuracy':
                current_score = accuracy_score(df_ytest, y_predict)
            elif score_metric == 'f1':
                current_score = f1_score(df_ytest, y_predict, pos_label = 1)
            elif score_metric == 'balanced_accuracy':
                current_score = balanced_accuracy_score(df_ytest, y_predict)             
                
            eval_best[estimator_name].append([current_score,best_feature])

            #--------voted feature--------#
            estimator.fit( df_x[vote_feature], df_y)
            y_predict = estimator.predict( df_xtest[vote_feature])
            
            sensitivity = None
            specificity = None
            
            if score_metric == 'accuracy':
                current_score = accuracy_score(df_ytest, y_predict)
            elif score_metric == 'f1':
                current_score = f1_score(df_ytest, y_predict, pos_label = 1)
            elif score_metric == 'balanced_accuracy':
                current_score = balanced_accuracy_score(df_ytest, y_predict)   
                
            eval_vote[estimator_name].append([current_score,vote_feature])
                
       
    if score_metric == 'balanced_accuracy':
        result_df = pd.DataFrame(columns= ['Model','BSF', 'BSF-score','MVF', 'MVF-score'])
        for estimator_name in eval_vote:
            best_score , best_feature = max(eval_best[estimator_name], key = lambda x: (x[0], -len(x[1])))
            vote_score , vote_feature = max(eval_vote[estimator_name], key = lambda x: (x[0], -len(x[1])))

            result_df.loc[len(result_df.index)] = [estimator_name, ','.join(best_feature), best_score, ','.join(vote_feature), vote_score]

    
    else:
        result_df = pd.DataFrame(columns= ['Model','BSF', 'BSF-Score','MVF','MVF-Score'])
        for estimator_name in eval_vote:
            best_score , best_feature = max(eval_best[estimator_name], key = lambda x: (x[0], -len(x[1])))
            vote_score , vote_feature  = max(eval_vote[estimator_name], key = lambda x: (x[0], -len(x[1])))

            result_df.loc[len(result_df.index)] = [estimator_name, ','.join(best_feature), best_score, ','.join(vote_feature), vote_score]

    return result_df
    
    

    


