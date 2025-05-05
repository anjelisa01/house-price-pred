import numpy as np
import pandas as pd
def transform_to_model_ready_data(data):
    """
    Transforms raw input data to the model-ready data format (88 features).
    """
    # ubah data ke dataframe bisa bisa diproses
    columns_name=['Id', 'MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea', 'Street',
       'Alley', 'LotShape', 'LandContour', 'Utilities', 'LotConfig',
       'LandSlope', 'Neighborhood', 'Condition1', 'Condition2', 'BldgType',
       'HouseStyle', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd',
       'RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType',
       'MasVnrArea', 'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual',
       'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinSF1',
       'BsmtFinType2', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'Heating',
       'HeatingQC', 'CentralAir', 'Electrical', '1stFlrSF', '2ndFlrSF',
       'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath',
       'HalfBath', 'BedroomAbvGr', 'KitchenAbvGr', 'KitchenQual',
       'TotRmsAbvGrd', 'Functional', 'Fireplaces', 'FireplaceQu', 'GarageType',
       'GarageYrBlt', 'GarageFinish', 'GarageCars', 'GarageArea', 'GarageQual',
       'GarageCond', 'PavedDrive', 'WoodDeckSF', 'OpenPorchSF',
       'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'PoolQC',
       'Fence', 'MiscFeature', 'MiscVal', 'MoSold', 'YrSold', 'SaleType',
       'SaleCondition']
    data=pd.DataFrame(data,columns=columns_name)
    try:
        # Apply your transformation logic here (e.g., scaling, encoding)
        if isinstance(data,pd.DataFrame)==True:
            X_transformed = data.copy()
            X_transformed['HouseAge'] = X_transformed['YrSold']-X_transformed['YearBuilt']
            X_transformed['BuildingSF']=X_transformed['TotalBsmtSF']+X_transformed['GrLivArea']+X_transformed['GarageArea']+X_transformed['WoodDeckSF']+X_transformed['OpenPorchSF']+ X_transformed['EnclosedPorch']	+X_transformed['3SsnPorch']	+ X_transformed['ScreenPorch']+X_transformed['PoolArea']
            bins=[0,10,20,50,100,float('inf')]
            labels=['New','Recent','Middle-aged','Old','Historic']
            X_transformed['HouseBin']=pd.cut(X_transformed['HouseAge'],bins=bins,labels=labels)
            X_transformed['RemodYrSold']=X_transformed['YrSold']-X_transformed['YearRemodAdd']
            X_transformed['QualGrLiv']=X_transformed['GrLivArea']*X_transformed['OverallQual']
            X_transformed['RatioBedroom']=X_transformed['BedroomAbvGr']/X_transformed['TotRmsAbvGrd']
            X_transformed['Neighborhood_HouseStyle']=X_transformed['Neighborhood']+'_'+X_transformed['HouseStyle']
            X_transformed=X_transformed.drop(['Id','YearBuilt','YrSold','HouseAge','YearRemodAdd'],axis=1)
            print("feature engineering output:",X_transformed)
            return X_transformed
        else:
            print(0)
    except Exception as e:
        print("error in feature engineering:",str(e))
        return None
